// Helper: safely set text content with newlines as <br> elements
function setTextWithBreaks(element, text) {
    element.textContent = '';
    (text || '').split('\n').forEach((line, i) => {
        if (i > 0) element.appendChild(document.createElement('br'));
        element.appendChild(document.createTextNode(line));
    });
}

// Helper: create an error paragraph safely (no innerHTML)
function createErrorP(message) {
    const p = document.createElement('p');
    p.className = 'error';
    p.textContent = message;
    return p;
}

// Helper: safely render HTML content (CSV data with formatting) via DOMPurify
function setSanitizedHTML(element, html) {
    element.innerHTML = DOMPurify.sanitize(
        (html || '').replace(/\n/g, '<br>'),
        { ALLOWED_TAGS: ['b', 'i', 'strong', 'em', 'a', 'br', 'span', 'u', 'sub', 'sup'],
          ALLOWED_ATTR: ['href', 'target', 'class', 'rel'] }
    );
}

// Make all links open in new tab
DOMPurify.addHook('afterSanitizeAttributes', function(node) {
    if (node.tagName === 'A' && node.getAttribute('href')) {
        node.setAttribute('target', '_blank');
        node.setAttribute('rel', 'noopener noreferrer');
    }
});

let contentElements = {}; // Global object to store preloaded content
let contentMeta = {}; // Metadata for lazy loading: { title: { link, type, loaded } }
let tooltips = {}; // Global tooltips object to store refs data
let currentBookRows = [];    // raw CSV row objects for current book
let currentBookColumns = []; // D: column names
let activeColumnCount = 1;   // number of visible content columns
let network = null; // vis.js network instance
let mapInitialized = false; // Flag for lazy init
let unifiedData, articlesData, booksData, breakdownsData, phiShapeData;

document.addEventListener('DOMContentLoaded', () => {
    // Unified content sheet URL (Articles sheet with Type column)
    const unifiedSheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?gid=464648636&output=csv';
    // Internal refs URL (separate)
    const refsSheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?gid=1749170252&single=true&output=csv';
    // Phi shape points URL — spreadsheet tab with Part, Order, X, Y columns
    // defining the outline of each phi shape section (stem, left-loop, right-loop, etc.)
    const phiShapeUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?gid=849779106&single=true&output=csv';

    // Fetch unified content, refs, and phi shape points
    Promise.all([
        fetchGoogleSheetData(unifiedSheetUrl),
        fetchGoogleSheetData(refsSheetUrl),
        fetchGoogleSheetData(phiShapeUrl).catch(() => [])  // Optional — don't fail if missing
    ])
        .then(([unified, refs, phiShapePoints]) => {
            // Process tooltips data (separate)
            tooltips = refs.reduce((acc, row) => {
                if (row.References && row.Data) {
                    acc[row.References.trim()] = row.Data.trim();
                }
                return acc;
            }, {});

            // Store and filter unified data
            unifiedData = unified || [];
            phiShapeData = phiShapePoints || [];
            articlesData = unifiedData.filter(row => row.Type?.trim().toLowerCase() === 'article');
            booksData = unifiedData.filter(row => row.Type?.trim().toLowerCase() === 'book');
            breakdownsData = unifiedData.filter(row => row.Type?.trim().toLowerCase() === 'breakdown');

            // Register content metadata for lazy loading (don't fetch yet)
            const contentBody = document.querySelector('.content-body');
            if (unifiedData.length === 0) {
                contentBody.textContent = '';
                contentBody.appendChild(createErrorP('No data found.'));
            } else {
                unifiedData.forEach(row => {
                    const title = row['Title']?.trim();
                    const link = row['Link']?.trim();
                    const type = row['Type']?.trim().toLowerCase();
                    const tag = row['Tag']?.trim();
                    const parent = row['Parent']?.trim();
                    if (title && link && type) {
                        contentElements[title] = document.createElement('div');
                        contentElements[title].className = 'doc-content';
                        contentElements[title].dataset.tag = tag || '';
                        contentElements[title].dataset.parent = parent || '';
                        contentElements[title].dataset.type = type || '';
                        contentMeta[title] = { link, type, loaded: false };
                    }
                });

                // Remove loading indicator immediately — sidebar is ready
                const loadingEl = document.getElementById('loading-indicator');
                if (loadingEl) loadingEl.remove();

                // Populate sidebars right away
                populateSidebarList('.articles-list', articlesData, 'Title', 'article');
                populateSidebarList('.books-list', booksData, 'Title', 'book');
                populateSidebarList('.breakdowns-list', breakdownsData, 'Title', 'breakdown');

                // Handle deep link from URL params if present
                const params = new URLSearchParams(window.location.search);
                const deepType = params.get('type');
                const deepContent = params.get('content');
                if (deepType && deepContent && contentElements[deepContent]) {
                    showContent(deepType, deepContent, params);
                } else {
                    // Show the first item if available (lazy load triggered inside showContent)
                    if (articlesData.length > 0) {
                        showContent('article', articlesData[0]['Title']);
                    } else if (booksData.length > 0) {
                        showContent('book', booksData[0]['Title']);
                    } else if (breakdownsData.length > 0) {
                        showContent('breakdown', breakdownsData[0]['Title']);
                    }
                }

                // Add MutationObserver to reapply tooltips on DOM changes (debounced)
                let mutationTimeout = null;
                const observer = new MutationObserver(() => {
                    if (mutationTimeout) clearTimeout(mutationTimeout);
                    mutationTimeout = setTimeout(() => {
                        observer.disconnect();
                        highlightReferences(contentBody, tooltips);
                        initializeTooltips(contentBody);
                        observer.observe(contentBody, { childList: true, subtree: true });
                    }, 100);
                });
                observer.observe(contentBody, { childList: true, subtree: true });
            }
        })
        .catch(error => {
            console.error('Data fetch error:', error);
            const contentBody = document.querySelector('.content-body');
            if (contentBody) {
                contentBody.appendChild(createErrorP('Failed to load data: ' + error.message));
            }
        });

    // Toggle wisdom map on button click
    document.getElementById('wisdom-map-btn').addEventListener('click', () => {
        const mapDiv = document.getElementById('wisdom-map');
        const contentDiv = document.querySelector('.content');
        if (mapDiv.style.display === 'block') {
            mapDiv.style.display = 'none';
            contentDiv.style.display = 'flex';
        } else {
            mapDiv.style.display = 'block';
            contentDiv.style.display = 'none';
            if (!mapInitialized) {
                // Wait for icon fonts to load before building map
                document.fonts.ready.then(() => {
                    buildWisdomMap(unifiedData, phiShapeData);
                    mapInitialized = true;
                });
            }
            if (network) network.stabilize();
        }
    });

    // Popover close
    document.getElementById('popover-close').addEventListener('click', () => {
        document.getElementById('popover').style.display = 'none';
    });

    // Mobile sidebar toggle
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');
    const sidebarOverlay = document.getElementById('sidebar-overlay');
    if (sidebarToggle && sidebar) {
        const closeSidebar = () => {
            sidebar.classList.remove('open');
            if (sidebarOverlay) sidebarOverlay.classList.remove('active');
        };
        sidebarToggle.addEventListener('click', () => {
            const isOpen = sidebar.classList.toggle('open');
            if (sidebarOverlay) sidebarOverlay.classList.toggle('active', isOpen);
        });
        if (sidebarOverlay) {
            sidebarOverlay.addEventListener('click', closeSidebar);
        }
    }

    // ── Mobile: hide nav/toolbar on scroll down, show on scroll up ──
    (() => {
        const mq = window.matchMedia('(max-width: 768px)');
        let lastY = 0;
        const threshold = 8;

        const onScroll = (scrollEl) => {
            if (!mq.matches) return;
            const y = scrollEl.scrollTop;
            const nav = document.querySelector('.nav-bar');
            const toolbar = document.querySelector('.book-toolbar');
            if (y > lastY + threshold) {
                if (nav) nav.classList.add('hide-on-scroll');
                if (toolbar) toolbar.classList.add('hide-on-scroll');
            } else if (y < lastY - threshold) {
                if (nav) nav.classList.remove('hide-on-scroll');
                if (toolbar) toolbar.classList.remove('hide-on-scroll');
            }
            lastY = y;
        };

        // .content-body is the scrolling container
        const contentBody = document.querySelector('.content-body');
        if (contentBody) {
            contentBody.addEventListener('scroll', () => onScroll(contentBody), { passive: true });
        }
        // Fallback for window scroll
        window.addEventListener('scroll', () => onScroll(document.documentElement), { passive: true });
    })();

    // Font switcher
    const fontSwitcher = document.querySelector('.font-switcher');
    if (fontSwitcher) {
        // Load saved preference
        const savedFont = localStorage.getItem('preferredFont') || 'serif';
        applyFont(savedFont);

        // Update active button
        fontSwitcher.querySelectorAll('.font-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.font === savedFont);
        });

        // Handle clicks
        fontSwitcher.addEventListener('click', (e) => {
            const btn = e.target.closest('.font-btn');
            if (!btn) return;

            const font = btn.dataset.font;
            applyFont(font);
            localStorage.setItem('preferredFont', font);

            // Update active state
            fontSwitcher.querySelectorAll('.font-btn').forEach(b => {
                b.classList.toggle('active', b === btn);
            });
        });
    }

    // Theme switcher
    const themeSwitcher = document.querySelector('.theme-switcher');
    if (themeSwitcher) {
        const savedTheme = localStorage.getItem('preferredTheme') || 'dark';
        applyTheme(savedTheme);

        themeSwitcher.querySelectorAll('.theme-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.theme === savedTheme);
        });

        themeSwitcher.addEventListener('click', (e) => {
            const btn = e.target.closest('.theme-btn');
            if (!btn) return;

            const theme = btn.dataset.theme;
            applyTheme(theme);
            localStorage.setItem('preferredTheme', theme);

            themeSwitcher.querySelectorAll('.theme-btn').forEach(b => {
                b.classList.toggle('active', b === btn);
            });
        });
    }

    // Section toggle (collapsible sidebar sections)
    document.querySelectorAll('.section-toggle').forEach(toggle => {
        toggle.addEventListener('click', () => {
            const content = toggle.nextElementSibling;
            if (content) {
                content.classList.toggle('collapsed');
                const isCollapsed = content.classList.contains('collapsed');
                toggle.textContent = toggle.textContent.replace(/[▸▾]/, isCollapsed ? '▸' : '▾');
                toggle.setAttribute('aria-expanded', !isCollapsed);
            }
        });
    });
});

// Apply font class to body
function applyFont(fontKey) {
    // Remove all font classes
    document.body.classList.remove('font-inter', 'font-open-sans', 'font-lato');
    // Add new font class (serif is default, no class needed)
    if (fontKey !== 'serif') {
        document.body.classList.add('font-' + fontKey);
    }
}

// Apply theme class to body
function applyTheme(themeKey) {
    document.body.classList.toggle('light-theme', themeKey === 'light');
}

// Function to populate a sidebar list
function populateSidebarList(listSelector, data, itemKey, type) {
    const list = document.querySelector(listSelector);
    list.innerHTML = '';
    data.forEach(row => {
        const item = row[itemKey]?.trim();
        if (item && contentElements[item]) {
            const listItem = document.createElement('li');
            const buttonElement = document.createElement('button');
            buttonElement.textContent = item;
            buttonElement.dataset.title = item; // For identifying active item
            buttonElement.classList.add('book-button');
            buttonElement.addEventListener('click', () => {
                if (buttonElement.classList.contains('active-item')) {
                    const subList = buttonElement.parentElement.querySelector('.sub-list');
                    if (subList) subList.classList.toggle('collapsed');
                    return;
                }
                showContent(type, item);
            });
            listItem.appendChild(buttonElement);
            list.appendChild(listItem);
        }
    });
    if (list.children.length === 0) {
        list.innerHTML = `<li>No valid ${type}/link pairs found</li>`;
    }
}

// --- Map Popup System ---
// Creates draggable, resizable popups on the wisdom map
async function createMapPopup(nodeId, nodeData, clickX, clickY, container) {
    // Check if popup already exists for this node
    const existingPopup = document.getElementById(`map-popup-${CSS.escape(nodeId)}`);
    if (existingPopup) {
        // Bring to front and focus
        existingPopup.style.zIndex = getNextPopupZ();
        return;
    }

    // Ensure content is loaded
    await ensureContentLoaded(nodeId);

    // Create popup element
    const popup = document.createElement('div');
    popup.className = 'map-popup';
    popup.id = `map-popup-${CSS.escape(nodeId)}`;
    popup.style.left = `${Math.max(10, clickX - 175)}px`;
    popup.style.top = `${Math.max(10, clickY - 150)}px`;
    popup.style.zIndex = getNextPopupZ();

    // Header (draggable)
    const header = document.createElement('div');
    header.className = 'map-popup-header';

    const title = document.createElement('span');
    title.className = 'map-popup-title';
    title.textContent = nodeId;
    header.appendChild(title);

    const typeLabel = document.createElement('button');
    typeLabel.className = 'map-popup-type';
    typeLabel.innerHTML = `${(nodeData?.data?.type || 'content').toUpperCase()} <span class="goto-arrow">→</span>`;
    typeLabel.addEventListener('click', (e) => {
        e.stopPropagation(); // Prevent drag from starting
        showContent(nodeData?.data?.type || 'article', nodeId);
        document.getElementById('wisdom-map').style.display = 'none';
        document.querySelector('.content').style.display = 'flex';
    });
    header.appendChild(typeLabel);

    const closeBtn = document.createElement('button');
    closeBtn.className = 'map-popup-close';
    closeBtn.innerHTML = '&times;';
    closeBtn.addEventListener('click', () => popup.remove());
    header.appendChild(closeBtn);

    popup.appendChild(header);

    // Body (content)
    const body = document.createElement('div');
    body.className = 'map-popup-body';

    // Clone the content
    const content = contentElements[nodeId];
    if (content) {
        const clonedContent = content.cloneNode(true);
        clonedContent.classList.add('active');
        body.appendChild(clonedContent);

        // Re-wire tab click handlers for cloned content
        clonedContent.querySelectorAll('.tab').forEach(tab => {
            tab.addEventListener('click', function() {
                const container = this.closest('.row-container');
                const rowContent = container.querySelector('.row-content');
                const col = this.dataset.column; // Use 'column' not 'col'
                const rowData = JSON.parse(this.dataset.rowData || '{}'); // Use 'rowData' not 'row'

                // Update active tab
                container.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                this.classList.add('active');

                // Update content
                if (rowData[col]) {
                    rowContent.innerHTML = '';
                    const p = document.createElement('p');
                    p.innerHTML = DOMPurify.sanitize(
                        (rowData[col] || '').replace(/\n/g, '<br>'),
                        { ALLOWED_TAGS: ['b', 'i', 'strong', 'em', 'a', 'br', 'span', 'u', 'sub', 'sup'],
                          ALLOWED_ATTR: ['href', 'target', 'class'] }
                    );
                    rowContent.appendChild(p);
                }
            });
        });
    } else {
        body.innerHTML = '<p class="loading">Loading content...</p>';
    }

    popup.appendChild(body);

    // Add to container
    container.appendChild(popup);

    // Make draggable
    makePopupDraggable(popup, header);

    // Bring to front on click
    popup.addEventListener('mousedown', () => {
        popup.style.zIndex = getNextPopupZ();
    });
}

// Z-index counter for popup stacking
let popupZIndex = 100;
function getNextPopupZ() {
    return ++popupZIndex;
}

// Make popup draggable by its header
function makePopupDraggable(popup, handle) {
    let isDragging = false;
    let offsetX = 0;
    let offsetY = 0;

    handle.addEventListener('mousedown', (e) => {
        if (e.target.classList.contains('map-popup-close') ||
            e.target.classList.contains('map-popup-type') ||
            e.target.classList.contains('goto-arrow')) return;
        isDragging = true;
        offsetX = e.clientX - popup.offsetLeft;
        offsetY = e.clientY - popup.offsetTop;
        popup.style.zIndex = getNextPopupZ();
        e.preventDefault();
    });

    document.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        popup.style.left = `${e.clientX - offsetX}px`;
        popup.style.top = `${e.clientY - offsetY}px`;
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
    });
}

// Function to build wisdom map with phi-shaped layout
function buildWisdomMap(data, shapePoints) {
    if (!data || !Array.isArray(data)) return;
    const container = document.getElementById('wisdom-map');
    container.style.position = 'relative';
    const nodes = new vis.DataSet();
    const edges = new vis.DataSet();

    // Hardcoded node positions from user layout
    const hardcodedPositions = {
        "Foundations": { x: 102, y: 227 },
        "Nicomachaen Ethics": { x: 50, y: -90 },  // Moved right into Right leaf (Ethics topic)
        "Metaphysics": { x: -2, y: -34 },
        "Republic": { x: 119, y: 169 },
        "Synposium": { x: 96, y: 99 },
        "Phaedo": { x: -99, y: 103 },
        "Apology": { x: -117, y: 200 },
        "Physics": { x: -91, y: -145 },
        "Civil Discourse: 3D's of Discourse": { x: -5, y: -170 },
        "Critique of Pure Reason": { x: 3, y: -290 },
        "The Organon": { x: 0, y: -130 },  // Moved up into center leaf (Logic topic)
        "Rhetoric": { x: -5, y: -189 },
        "Poetics": { x: -5, y: -236 },
        "Power": { x: 67, y: -115 },
        "Left and Right": { x: 107, y: -155 },
        "On Liberty": { x: 127, y: -181 },
        "Philosophy of Right": { x: 56, y: -162 },
        "De Anima": { x: -63, y: -127 },
        "Politics": { x: 181, y: -251 },
        "Sneaky Candy": { x: -200, y: 220 },
        "Test Breakdown": { x: 321, y: 154 }
    };

    // Group styles — small grey nodes with subtle borders
    const groups = {
        'Wisdom':  { color: { background: 'rgba(160, 160, 170, 0.5)', border: '#888890' }, size: 8, font: { color: '#ffffff', size: 6, vadjust: 1 } },
        'Reality': { color: { background: 'rgba(140, 150, 165, 0.5)', border: '#7a8a9a' }, size: 8, font: { color: '#ffffff', size: 6, vadjust: 1 } },
        'Reason':  { color: { background: 'rgba(160, 160, 170, 0.5)', border: '#888890' }, size: 8, font: { color: '#ffffff', size: 6, vadjust: 1 } },
        'Right':   { color: { background: 'rgba(155, 145, 155, 0.5)', border: '#888890' }, size: 8, font: { color: '#ffffff', size: 6, vadjust: 1 } },
        'Musings': { color: { background: 'rgba(140, 140, 150, 0.5)', border: '#808088' }, size: 6, font: { color: '#eeeeee', size: 5, vadjust: 0 } },
        'Root':    { color: { background: 'rgba(170, 170, 180, 0.5)', border: '#999' }, size: 10, font: { color: '#ffffff', size: 7, vadjust: 2 } }
    };

    // --- Phi shape coordinates (matching widephi.png proportions) ---
    // The phi image is roughly 500x600, centered at origin
    const phi = {
        // Image dimensions for background
        width: 500,
        height: 600,
        // Loop (bottom) - the circular part of phi
        loop: {
            centerX: 0,
            centerY: 220,
            radius: 80
        },
        // Stem - vertical line from loop to branch point
        stem: {
            x: 0,
            bottomY: 140,    // Just above loop top
            topY: -100       // Branch point where leaves start
        },
        // Leaves - curved paths for Reality (left), Reason (center), Right (right)
        leaves: {
            // Left leaf curves outward and up
            reality: { tipX: -200, tipY: -280, ctrlX: -140, ctrlY: -180 },
            // Center leaf goes straight up
            reason:  { tipX: 0, tipY: -320, ctrlX: 0, ctrlY: -210 },
            // Right leaf curves outward and up
            right:   { tipX: 200, tipY: -280, ctrlX: 140, ctrlY: -180 }
        }
    };

    // --- Classify nodes by Tag and Parent ---
    // Also extract manual X/Y coordinates if provided in spreadsheet
    const classified = { Root: [], Wisdom: [], Reality: [], Reason: [], Right: [], Musings: [], Other: [] };

    data.forEach(row => {
        const title = row['Title']?.trim();
        const tag = row['Tag']?.trim();
        const parent = row['Parent']?.trim();
        const type = row['Type']?.trim().toLowerCase();
        if (!title) return;

        // Read manual X/Y coordinates (if columns exist and have values)
        const manualX = row['X'] !== undefined && row['X'] !== '' ? parseFloat(row['X']) : null;
        const manualY = row['Y'] !== undefined && row['Y'] !== '' ? parseFloat(row['Y']) : null;
        const hasManualPos = manualX !== null && manualY !== null && !isNaN(manualX) && !isNaN(manualY);

        const entry = { title, tag, parent, type, row, manualX, manualY, hasManualPos };
        if (parent === 'Root') {
            classified.Root.push(entry);
        } else if (parent === 'Musing' || tag === 'Musings') {
            classified.Musings.push(entry);
        } else if (tag === 'Wisdom') {
            classified.Wisdom.push(entry);
        } else if (tag === 'Reality') {
            classified.Reality.push(entry);
        } else if (tag === 'Reason') {
            classified.Reason.push(entry);
        } else if (tag === 'Right') {
            classified.Right.push(entry);
        } else {
            classified.Other.push(entry);
        }
    });

    // --- Helper: get shape/icon by content type ---
    // Uses Font Awesome 4 icons via vis.js icon shape
    function getNodeAppearance(type) {
        if (type === 'article') return { shape: 'icon', icon: { face: 'FontAwesome', code: '\uf15c', size: 10, color: '#ffffff' } };
        if (type === 'book')    return { shape: 'icon', icon: { face: 'FontAwesome', code: '\uf02d', size: 10, color: '#ffffff' } };
        if (type === 'breakdown') return { shape: 'icon', icon: { face: 'FontAwesome', code: '\uf0e8', size: 10, color: '#ffffff' } };
        return { shape: 'dot' };
    }

    // --- Helper: add edge from parent to child ---
    function addEdge(entry) {
        if (entry.parent && entry.parent !== 'Root' && entry.parent !== 'Musing' && entry.parent !== entry.title) {
            edges.add({ from: entry.parent, to: entry.title });
        }
    }

    // --- Helper: quadratic bezier point at t ---
    function bezierPoint(t, p0, p1, p2) {
        const mt = 1 - t;
        return {
            x: mt * mt * p0.x + 2 * mt * t * p1.x + t * t * p2.x,
            y: mt * mt * p0.y + 2 * mt * t * p1.y + t * t * p2.y
        };
    }

    // --- Helper: create node with manual or auto position ---
    function addNodeWithPosition(entry, groupName, autoX, autoY) {
        // Priority: hardcoded > manual spreadsheet > auto
        const hardcoded = hardcodedPositions[entry.title];
        const x = hardcoded ? hardcoded.x : (entry.hasManualPos ? entry.manualX : autoX);
        const y = hardcoded ? hardcoded.y : (entry.hasManualPos ? entry.manualY : autoY);
        const appearance = getNodeAppearance(entry.type);
        const nodeData = {
            id: entry.title,
            label: entry.title,
            group: groupName,
            shape: appearance.shape,
            x: x,
            y: y,
            fixed: { x: true, y: true },
            data: { parent: entry.parent, type: entry.type }
        };
        if (appearance.icon) nodeData.icon = appearance.icon;
        if (appearance.image) nodeData.image = appearance.image;
        if (appearance.size) nodeData.size = appearance.size;
        nodes.add(nodeData);
        addEdge(entry);
        return { x, y };  // Return position for leaf curve calculations
    }

    // Track node positions for dynamic leaf curves
    const nodePositions = { Reality: [], Reason: [], Right: [], Wisdom: [], Root: [] };

    // --- 1. Root nodes positioned in the phi loop area (bottom) ---
    const rootCount = classified.Root.length;
    classified.Root.forEach((entry, i) => {
        // Spread horizontally across the loop center, vertically at loop center
        const spread = rootCount > 1 ? (i - (rootCount - 1) / 2) * 60 : 0;
        const autoX = phi.loop.centerX + spread;
        const autoY = phi.loop.centerY;
        const pos = addNodeWithPosition(entry, 'Root', autoX, autoY);
        nodePositions.Root.push(pos);
    });

    // --- Parse phi shape points from spreadsheet (if available) ---
    // Expected columns: Part, Order, X, Y, Width (optional)
    const shapeParts = {};
    if (shapePoints && shapePoints.length > 0) {
        shapePoints.forEach(row => {
            const part = row['Part']?.trim();
            const order = parseFloat(row['Order']);
            const x = parseFloat(row['X']);
            const y = parseFloat(row['Y']);
            const width = row['Width'] !== undefined && row['Width'] !== '' ? parseFloat(row['Width']) : null;
            if (part && !isNaN(order) && !isNaN(x) && !isNaN(y)) {
                if (!shapeParts[part]) shapeParts[part] = [];
                shapeParts[part].push({ order, x, y, width });
            }
        });
        // Sort each part's points by order
        Object.values(shapeParts).forEach(pts => pts.sort((a, b) => a.order - b.order));
    }
    const hasShapeData = Object.keys(shapeParts).length > 0;

    // --- 2. Wisdom nodes along ribbon centerline ---
    const wisdomCount = classified.Wisdom.length;

    // Get centerline points from shape data (if available)
    const seedPts = shapeParts['seed'] || [];

    if (seedPts.length >= 2 && wisdomCount > 0) {
        // Calculate cumulative distances along centerline
        const distances = [0];
        for (let i = 1; i < seedPts.length; i++) {
            const dx = seedPts[i].x - seedPts[i-1].x;
            const dy = seedPts[i].y - seedPts[i-1].y;
            distances.push(distances[i-1] + Math.sqrt(dx*dx + dy*dy));
        }
        const totalLength = distances[distances.length - 1];

        // Distribute Wisdom nodes evenly along path
        classified.Wisdom.forEach((entry, i) => {
            // Target distance along path (evenly spaced)
            const targetDist = (i / (wisdomCount - 1 || 1)) * totalLength;

            // Find which segment this falls on
            let segIdx = 0;
            while (segIdx < distances.length - 1 && distances[segIdx + 1] < targetDist) {
                segIdx++;
            }

            // Interpolate within segment
            const segStart = distances[segIdx];
            const segEnd = distances[segIdx + 1] || segStart;
            const segLen = segEnd - segStart;
            const t = segLen > 0 ? (targetDist - segStart) / segLen : 0;

            const p0 = seedPts[segIdx];
            const p1 = seedPts[segIdx + 1] || p0;
            const autoX = p0.x + t * (p1.x - p0.x);
            const autoY = p0.y + t * (p1.y - p0.y);

            const pos = addNodeWithPosition(entry, 'Wisdom', autoX, autoY);
            nodePositions.Wisdom.push(pos);
        });
    } else {
        // Fallback: center of loop if no shape data
        classified.Wisdom.forEach((entry) => {
            const pos = addNodeWithPosition(entry, 'Wisdom', phi.loop.centerX, phi.loop.centerY);
            nodePositions.Wisdom.push(pos);
        });
    }

    // --- 3. Reality nodes along left leaf curve ---
    const realityCount = classified.Reality.length;
    const realityStart = { x: phi.stem.x - 20, y: phi.stem.topY };
    const realityCtrl = { x: phi.leaves.reality.ctrlX, y: phi.leaves.reality.ctrlY };
    const realityTip = { x: phi.leaves.reality.tipX, y: phi.leaves.reality.tipY };
    classified.Reality.forEach((entry, i) => {
        const t = (i + 1) / (realityCount + 1);  // Spread along curve
        const autoPos = bezierPoint(t, realityStart, realityCtrl, realityTip);
        const pos = addNodeWithPosition(entry, 'Reality', autoPos.x, autoPos.y);
        nodePositions.Reality.push(pos);
    });

    // --- 4. Reason nodes along center leaf (straight up) ---
    const reasonCount = classified.Reason.length;
    const reasonStart = { x: phi.stem.x, y: phi.stem.topY };
    const reasonCtrl = { x: phi.leaves.reason.ctrlX, y: phi.leaves.reason.ctrlY };
    const reasonTip = { x: phi.leaves.reason.tipX, y: phi.leaves.reason.tipY };
    classified.Reason.forEach((entry, i) => {
        const t = (i + 1) / (reasonCount + 1);
        const autoPos = bezierPoint(t, reasonStart, reasonCtrl, reasonTip);
        const pos = addNodeWithPosition(entry, 'Reason', autoPos.x, autoPos.y);
        nodePositions.Reason.push(pos);
    });

    // --- 5. Right nodes along right leaf curve ---
    const rightCount = classified.Right.length;
    const rightStart = { x: phi.stem.x + 20, y: phi.stem.topY };
    const rightCtrl = { x: phi.leaves.right.ctrlX, y: phi.leaves.right.ctrlY };
    const rightTip = { x: phi.leaves.right.tipX, y: phi.leaves.right.tipY };
    classified.Right.forEach((entry, i) => {
        const t = (i + 1) / (rightCount + 1);
        const autoPos = bezierPoint(t, rightStart, rightCtrl, rightTip);
        const pos = addNodeWithPosition(entry, 'Right', autoPos.x, autoPos.y);
        nodePositions.Right.push(pos);
    });

    // --- 6. Musings nodes positioned off to the side ---
    classified.Musings.forEach((entry, i) => {
        const autoX = -200 + (i % 3) * 50;
        const autoY = 220 + Math.floor(i / 3) * 50;
        addNodeWithPosition(entry, 'Musings', autoX, autoY);
    });

    // --- 7. Other nodes along stem extension ---
    classified.Other.forEach((entry, i) => {
        const autoX = 30 + (i % 2) * 40;
        const autoY = phi.stem.bottomY + 20 + Math.floor(i / 2) * 40;
        addNodeWithPosition(entry, 'Wisdom', autoX, autoY);
    });

    // --- Network options: no physics, all fixed positions ---
    const options = {
        layout: {
            hierarchical: { enabled: false }
        },
        physics: {
            enabled: false  // All nodes are fixed, no physics needed
        },
        groups: groups,
        edges: {
            arrows: { to: { enabled: true, scaleFactor: 0.3 } },  // Smaller arrows
            color: { color: 'rgba(180, 160, 120, 0.4)', highlight: '#d29a38' },  // Elegant warm gold
            width: 1,  // Thinner edges
            smooth: { type: 'continuous', roundness: 0.2 }  // Gentler curves
        },
        interaction: {
            hover: true,
            zoomView: true,
            dragView: true,
            dragNodes: false  // Positions are hardcoded; use Edit Nodes button to enable dragging
        }
    };

    network = new vis.Network(container, { nodes, edges }, options);

    // Force redraw after short delay to ensure icon fonts are rendered
    setTimeout(() => { if (network) network.redraw(); }, 500);

    // --- Helper: calculate bounding box with padding for a set of positions ---
    function getLeafBounds(positions, padding = 30) {
        if (positions.length === 0) return null;
        let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
        positions.forEach(p => {
            minX = Math.min(minX, p.x);
            maxX = Math.max(maxX, p.x);
            minY = Math.min(minY, p.y);
            maxY = Math.max(maxY, p.y);
        });
        return {
            minX: minX - padding,
            maxX: maxX + padding,
            minY: minY - padding,
            maxY: maxY + padding,
            centerX: (minX + maxX) / 2,
            centerY: (minY + maxY) / 2
        };
    }

    // --- Draw phi shape on canvas ---
    network.on('beforeDrawing', (ctx) => {
        ctx.save();

        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';

        if (hasShapeData) {
            // ==========================================================
            // SPREADSHEET-DRIVEN: Draw each part as a filled ribbon
            // Points define the centerline, Width defines ribbon thickness
            // Code computes outer/inner edges, traces them as a filled polygon
            // ==========================================================

            Object.keys(shapeParts).forEach(partName => {
                const pts = shapeParts[partName];
                if (pts.length < 2) return;

                const defaultW = 38;
                const getW = (i) => (pts[i].width !== null && !isNaN(pts[i].width)) ? pts[i].width : defaultW;

                // Compute perpendicular normal at each point
                const leftEdge = [];
                const rightEdge = [];

                for (let i = 0; i < pts.length; i++) {
                    let dx, dy;
                    if (i === 0) {
                        dx = pts[1].x - pts[0].x;
                        dy = pts[1].y - pts[0].y;
                    } else if (i === pts.length - 1) {
                        dx = pts[i].x - pts[i - 1].x;
                        dy = pts[i].y - pts[i - 1].y;
                    } else {
                        dx = pts[i + 1].x - pts[i - 1].x;
                        dy = pts[i + 1].y - pts[i - 1].y;
                    }

                    const len = Math.sqrt(dx * dx + dy * dy) || 1;
                    const nx = -dy / len;
                    const ny = dx / len;
                    const halfW = getW(i) / 2;

                    leftEdge.push({ x: pts[i].x + nx * halfW, y: pts[i].y + ny * halfW });
                    rightEdge.push({ x: pts[i].x - nx * halfW, y: pts[i].y - ny * halfW });
                }

                // Build closed polygon: left edge forward, right edge backward
                ctx.beginPath();
                ctx.moveTo(leftEdge[0].x, leftEdge[0].y);

                // Smooth curve along left edge (forward)
                if (leftEdge.length > 2) {
                    for (let i = 1; i < leftEdge.length - 1; i++) {
                        const midX = (leftEdge[i].x + leftEdge[i + 1].x) / 2;
                        const midY = (leftEdge[i].y + leftEdge[i + 1].y) / 2;
                        ctx.quadraticCurveTo(leftEdge[i].x, leftEdge[i].y, midX, midY);
                    }
                }
                ctx.lineTo(leftEdge[leftEdge.length - 1].x, leftEdge[leftEdge.length - 1].y);

                // Connect to right edge at the end
                ctx.lineTo(rightEdge[rightEdge.length - 1].x, rightEdge[rightEdge.length - 1].y);

                // Smooth curve along right edge (backward)
                if (rightEdge.length > 2) {
                    for (let i = rightEdge.length - 2; i > 0; i--) {
                        const midX = (rightEdge[i].x + rightEdge[i - 1].x) / 2;
                        const midY = (rightEdge[i].y + rightEdge[i - 1].y) / 2;
                        ctx.quadraticCurveTo(rightEdge[i].x, rightEdge[i].y, midX, midY);
                    }
                }
                ctx.lineTo(rightEdge[0].x, rightEdge[0].y);

                ctx.closePath();

                // Fill at 50% opacity
                ctx.fillStyle = 'rgba(212, 175, 55, 0.5)';
                ctx.fill();

                // Border at same color
                ctx.strokeStyle = 'rgba(212, 175, 55, 0.5)';
                ctx.lineWidth = 2;
                ctx.stroke();
            });

            // Draw three filled leaf shapes at their respective node locations
            // Leaves are almond/eye shaped - wide in middle, pointed at both ends
            ctx.fillStyle = 'rgba(212, 175, 55, 0.5)';
            ctx.strokeStyle = 'rgba(212, 175, 55, 0.5)';
            ctx.lineWidth = 2;

            // Helper to draw a filled leaf shape with customizable width
            function drawLeaf(startX, startY, tipX, tipY, width) {
                const dx = tipX - startX;
                const dy = tipY - startY;
                const len = Math.sqrt(dx * dx + dy * dy);
                const nx = -dy / len; // perpendicular
                const ny = dx / len;
                const midX = (startX + tipX) / 2;
                const midY = (startY + tipY) / 2;
                const bulge = width / 2;

                ctx.beginPath();
                ctx.moveTo(startX, startY); // base point
                // Left curve to tip
                ctx.quadraticCurveTo(midX + nx * bulge, midY + ny * bulge, tipX, tipY);
                // Right curve back to base
                ctx.quadraticCurveTo(midX - nx * bulge, midY - ny * bulge, startX, startY);
                ctx.closePath();
                ctx.fill();
                ctx.stroke();
            }

            // Left leaf - starts at y=-34 (Metaphysics area), angles toward Reality nodes
            // Reality nodes: Physics (-91, -145), De Anima (-63, -127)
            drawLeaf(0, -34, -130, -170, 70);

            // Right leaf - starts at y=-87 (Nicomachaen Ethics area), angles toward Right nodes
            // Right nodes: Power (67, -115), Left and Right (107, -155), On Liberty (127, -181)
            drawLeaf(0, -87, 160, -200, 70);

            // Center leaf - starts at y=-90 (just above stem end at -100), points straight up
            // Reason nodes: Rhetoric (-5, -189), Poetics (-5, -236), Critique (3, -290)
            drawLeaf(0, -90, 0, -320, 70);

        } else {
            // ==========================================================
            // FALLBACK: Programmatic phi shape (when no spreadsheet tab)
            // ==========================================================
            const loopCX = phi.loop.centerX;
            const loopCY = phi.loop.centerY;
            const loopR = phi.loop.radius;

            // Get dynamic leaf bounds
            const realityBounds = getLeafBounds(nodePositions.Reality, 40);
            const reasonBounds = getLeafBounds(nodePositions.Reason, 30);
            const rightBounds = getLeafBounds(nodePositions.Right, 40);

            // Stem
            ctx.beginPath();
            ctx.moveTo(loopCX, loopCY - loopR * 0.4);
            ctx.lineTo(loopCX, phi.stem.topY);
            ctx.stroke();

            // Left leaf
            if (realityBounds) {
                ctx.beginPath();
                ctx.moveTo(loopCX, phi.stem.topY);
                ctx.quadraticCurveTo(
                    realityBounds.minX - 10, realityBounds.centerY + 10,
                    realityBounds.centerX, realityBounds.minY - 15
                );
                ctx.stroke();
            }

            // Center leaf
            if (reasonBounds) {
                ctx.beginPath();
                ctx.moveTo(loopCX, phi.stem.topY);
                ctx.quadraticCurveTo(
                    loopCX, reasonBounds.centerY,
                    reasonBounds.centerX, reasonBounds.minY - 25
                );
                ctx.stroke();
            }

            // Right leaf
            if (rightBounds) {
                ctx.beginPath();
                ctx.moveTo(loopCX, phi.stem.topY);
                ctx.quadraticCurveTo(
                    rightBounds.maxX + 10, rightBounds.centerY + 10,
                    rightBounds.centerX, rightBounds.minY - 15
                );
                ctx.stroke();
            }

            // Left loop
            const loopW = loopR * 1.3;
            const loopH = loopR * 1.2;
            const crossSpread = loopR * 0.45;

            ctx.beginPath();
            ctx.moveTo(loopCX, loopCY - loopR * 0.4);
            ctx.bezierCurveTo(
                loopCX - loopW * 1.8, loopCY - loopR * 0.4,
                loopCX - loopW * 1.8, loopCY + loopH * 1.8,
                loopCX + crossSpread, loopCY + loopH * 1.4
            );
            ctx.stroke();

            // Right loop
            ctx.beginPath();
            ctx.moveTo(loopCX, loopCY - loopR * 0.4);
            ctx.bezierCurveTo(
                loopCX + loopW * 1.8, loopCY - loopR * 0.4,
                loopCX + loopW * 1.8, loopCY + loopH * 1.8,
                loopCX - crossSpread, loopCY + loopH * 1.4
            );
            ctx.stroke();
        }

        ctx.restore();
    });

    // --- Hover event (safe: textContent only) ---
    network.on('hoverNode', (params) => {
        const nodeData = nodes.get(params.node);
        if (!nodeData) return;
        const preview = document.getElementById('hover-preview');
        preview.textContent = '';
        const titleEl = document.createElement('strong');
        titleEl.textContent = nodeData.label;
        preview.appendChild(titleEl);
        if (nodeData.group) {
            const tagEl = document.createElement('span');
            tagEl.textContent = ' — ' + nodeData.group;
            tagEl.style.color = '#999';
            preview.appendChild(tagEl);
        }
        const containerRect = container.getBoundingClientRect();
        preview.style.left = (containerRect.left + params.pointer.DOM.x + 15) + 'px';
        preview.style.top = (containerRect.top + params.pointer.DOM.y + 15) + 'px';
        preview.style.display = 'block';
    });

    network.on('blurNode', () => {
        document.getElementById('hover-preview').style.display = 'none';
    });

    // --- Click event: open popup on map ---
    network.on('click', (params) => {
        if (params.nodes.length > 0) {
            const nodeId = params.nodes[0];
            const nodeData = nodes.get(nodeId);
            if (nodeData && nodeData.data) {
                createMapPopup(nodeId, nodeData, params.pointer.DOM.x, params.pointer.DOM.y, container);
            }
        }
    });

    // --- Map controls (inside container, not document.body) ---
    const controlsDiv = document.createElement('div');
    controlsDiv.className = 'map-controls';

    const resetBtn = document.createElement('button');
    resetBtn.textContent = 'Reset View';
    resetBtn.addEventListener('click', () => network.fit({ animation: true }));
    controlsDiv.appendChild(resetBtn);

    const labelsBtn = document.createElement('button');
    labelsBtn.textContent = 'Toggle Labels';
    let labelsVisible = true;
    labelsBtn.addEventListener('click', () => {
        labelsVisible = !labelsVisible;
        const updates = [];
        nodes.forEach(node => {
            updates.push({ id: node.id, font: { size: labelsVisible ? 12 : 0 } });
        });
        nodes.update(updates);
        labelsBtn.classList.toggle('active', !labelsVisible);
    });
    controlsDiv.appendChild(labelsBtn);

    const physicsBtn = document.createElement('button');
    physicsBtn.textContent = 'Reflow';
    physicsBtn.addEventListener('click', () => {
        network.setOptions({ physics: { enabled: true, stabilization: { iterations: 100 } } });
        network.stabilize();
    });
    controlsDiv.appendChild(physicsBtn);

    // Edit Nodes toggle - enables/disables dragging
    const editBtn = document.createElement('button');
    editBtn.textContent = 'Edit Nodes';
    let editMode = false;
    editBtn.addEventListener('click', () => {
        editMode = !editMode;
        // Enable dragNodes interaction
        network.setOptions({ interaction: { dragNodes: editMode } });

        if (editMode) {
            // Get current positions and update nodes to allow dragging while keeping position
            const positions = network.getPositions();
            const updates = [];
            nodes.forEach(node => {
                const pos = positions[node.id];
                if (pos) {
                    updates.push({
                        id: node.id,
                        x: pos.x,
                        y: pos.y,
                        fixed: false  // Allow dragging
                    });
                }
            });
            nodes.update(updates);
        } else {
            // Lock nodes in their current positions
            const positions = network.getPositions();
            const updates = [];
            nodes.forEach(node => {
                const pos = positions[node.id];
                if (pos) {
                    updates.push({
                        id: node.id,
                        x: pos.x,
                        y: pos.y,
                        fixed: { x: true, y: true }  // Lock in place
                    });
                }
            });
            nodes.update(updates);
        }

        editBtn.classList.toggle('active', editMode);
        editBtn.textContent = editMode ? 'Edit Nodes (ON)' : 'Edit Nodes';
    });
    controlsDiv.appendChild(editBtn);

    // Export Positions - outputs JSON of all node positions
    const exportBtn = document.createElement('button');
    exportBtn.textContent = 'Export Positions';
    exportBtn.addEventListener('click', () => {
        const positions = network.getPositions();
        const exportData = [];
        nodes.forEach(node => {
            const pos = positions[node.id];
            if (pos) {
                exportData.push({
                    Title: node.id,
                    X: Math.round(pos.x),
                    Y: Math.round(pos.y)
                });
            }
        });
        // Format as table for easy copying
        let output = 'Title\tX\tY\n';
        exportData.forEach(row => {
            output += `${row.Title}\t${row.X}\t${row.Y}\n`;
        });
        console.log('=== EXPORTED NODE POSITIONS ===');
        console.log(output);
        console.log('=== JSON FORMAT ===');
        console.log(JSON.stringify(exportData, null, 2));
        alert('Node positions exported to browser console (F12 to view).\n\nCopy the tab-separated table or JSON from there.');
    });
    controlsDiv.appendChild(exportBtn);

    container.appendChild(controlsDiv);

    // --- Search/Filter Controls (top-left) ---
    const filterDiv = document.createElement('div');
    filterDiv.className = 'map-filter-controls';

    // Search input
    const searchInput = document.createElement('input');
    searchInput.type = 'text';
    searchInput.placeholder = 'Search nodes...';
    searchInput.className = 'map-search-input';
    filterDiv.appendChild(searchInput);

    // Tag filter buttons
    const tagFilters = document.createElement('div');
    tagFilters.className = 'map-tag-filters';

    const tags = ['All', 'Reality', 'Reason', 'Right', 'Root', 'Wisdom'];
    const activeFilters = new Set(['All']);

    tags.forEach(tag => {
        const btn = document.createElement('button');
        btn.textContent = tag;
        btn.className = 'map-filter-btn' + (tag === 'All' ? ' active' : '');
        btn.dataset.tag = tag;
        tagFilters.appendChild(btn);
    });
    filterDiv.appendChild(tagFilters);
    container.appendChild(filterDiv);

    // Store original node appearance for restoration
    const originalNodeAppearance = {};
    nodes.forEach(node => {
        originalNodeAppearance[node.id] = {
            icon: node.icon ? { ...node.icon } : null,
            color: node.color,
            font: node.font ? { ...node.font } : null
        };
    });

    // Helper: dim a node (non-matching)
    function dimNode(nodeId) {
        const node = nodes.get(nodeId);
        if (!node) return;
        const update = { id: nodeId };
        if (node.icon) {
            update.icon = { ...node.icon, color: 'rgba(80, 80, 80, 0.3)' };
        } else {
            update.color = { background: 'rgba(80, 80, 80, 0.3)', border: '#444' };
        }
        update.font = { color: 'rgba(100, 100, 100, 0.4)', size: 8 };
        nodes.update(update);
    }

    // Helper: restore a node to original appearance
    function restoreNode(nodeId) {
        const original = originalNodeAppearance[nodeId];
        if (!original) return;
        const update = { id: nodeId };
        if (original.icon) {
            update.icon = { ...original.icon };
        }
        if (original.color) {
            update.color = original.color;
        }
        if (original.font) {
            update.font = { ...original.font };
        }
        nodes.update(update);
    }

    // Helper: emphasize a node (click-to-focus)
    function emphasizeNode(nodeId) {
        const node = nodes.get(nodeId);
        if (!node) return;
        const update = { id: nodeId };
        if (node.icon) {
            update.icon = { ...node.icon, color: '#d29a38' };
        } else {
            update.color = { background: '#d29a38', border: '#fff' };
        }
        update.font = { color: '#fff', size: 12 };
        nodes.update(update);
    }

    // Track focused node for click-to-focus
    let focusedNodeId = null;

    // Apply search + tag filters
    function applyFilters() {
        const searchText = searchInput.value.toLowerCase().trim();
        const showAll = activeFilters.has('All');

        nodes.forEach(node => {
            const matchesSearch = !searchText || node.label.toLowerCase().includes(searchText);
            const matchesTag = showAll || activeFilters.has(node.group);

            if (matchesSearch && matchesTag) {
                restoreNode(node.id);
            } else {
                dimNode(node.id);
            }
        });

        // Clear focus when filtering
        focusedNodeId = null;
    }

    // Search input handler
    searchInput.addEventListener('input', applyFilters);

    // Tag button click handlers
    tagFilters.querySelectorAll('.map-filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const tag = btn.dataset.tag;

            if (tag === 'All') {
                // Reset all filters
                activeFilters.clear();
                activeFilters.add('All');
                tagFilters.querySelectorAll('.map-filter-btn').forEach(b => {
                    b.classList.toggle('active', b.dataset.tag === 'All');
                });
            } else {
                // Toggle this tag
                activeFilters.delete('All');
                tagFilters.querySelector('[data-tag="All"]').classList.remove('active');

                if (activeFilters.has(tag)) {
                    activeFilters.delete(tag);
                    btn.classList.remove('active');
                } else {
                    activeFilters.add(tag);
                    btn.classList.add('active');
                }

                // If no tags selected, default to All
                if (activeFilters.size === 0) {
                    activeFilters.add('All');
                    tagFilters.querySelector('[data-tag="All"]').classList.add('active');
                }
            }

            applyFilters();
        });
    });

    // Click-to-focus: clicking a node highlights it and its connections
    network.on('click', (params) => {
        if (params.nodes.length > 0) {
            const clickedId = params.nodes[0];

            // Toggle focus
            if (focusedNodeId === clickedId) {
                // Unfocus - restore to filter state
                focusedNodeId = null;
                applyFilters();
            } else {
                // Focus on this node and connections
                focusedNodeId = clickedId;
                const connectedNodes = network.getConnectedNodes(clickedId);
                const relevantNodes = new Set([clickedId, ...connectedNodes]);

                nodes.forEach(node => {
                    if (relevantNodes.has(node.id)) {
                        if (node.id === clickedId) {
                            emphasizeNode(node.id);
                        } else {
                            restoreNode(node.id);
                        }
                    } else {
                        dimNode(node.id);
                    }
                });
            }
        } else {
            // Clicked empty space - clear focus, restore filter state
            if (focusedNodeId) {
                focusedNodeId = null;
                applyFilters();
            }
        }
    });
}

// Mobile notes overlay — singleton, created once
function getNotesOverlay() {
    let overlay = document.getElementById('notes-overlay');
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.id = 'notes-overlay';
        overlay.className = 'notes-overlay';
        const content = document.createElement('div');
        content.className = 'notes-overlay-content';
        overlay.appendChild(content);
        overlay.addEventListener('click', () => {
            overlay.classList.remove('active');
        });
        document.body.appendChild(overlay);
    }
    return overlay;
}

function showMobileNotes(rowGroup) {
    const notesDiv = rowGroup.querySelector('.row-notes');
    if (!notesDiv) return;
    const overlay = getNotesOverlay();
    const content = overlay.querySelector('.notes-overlay-content');
    content.innerHTML = notesDiv.innerHTML;
    overlay.classList.add('active');
}

// Create a per-row notes checkbox toggle
function createRowNotesToggle() {
    const label = document.createElement('label');
    label.className = 'row-notes-toggle';
    label.title = 'Show notes';
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.addEventListener('change', (e) => {
        const rowGroup = label.closest('.row-group');
        if (!rowGroup) return;
        if (window.matchMedia('(max-width: 768px)').matches) {
            e.preventDefault();
            checkbox.checked = false;
            showMobileNotes(rowGroup);
        } else {
            rowGroup.classList.toggle('show-row-notes', checkbox.checked);
        }
    });
    label.appendChild(checkbox);
    label.appendChild(document.createTextNode(' N'));
    return label;
}

// Create a single row-container for a given column index
function createRowContainer(rowData, allColumns, colIndex, defaultTab, dataRowIndex) {
    const nonEmptyCols = allColumns.filter(col => rowData[col] && rowData[col].trim() !== '');
    if (nonEmptyCols.length === 0) return null;

    const rowContainer = document.createElement('div');
    rowContainer.className = 'row-container';
    rowContainer.dataset.col = colIndex;

    const hasNotes = colIndex === 0 && rowData['Notes']?.trim() && rowData['Index']?.trim();

    if (nonEmptyCols.length === 1) {
        if (hasNotes) {
            const rowTabs = document.createElement('div');
            rowTabs.className = 'row-tabs';
            rowTabs.appendChild(createRowNotesToggle());
            rowContainer.appendChild(rowTabs);
        }
        const rowContent = document.createElement('div');
        rowContent.className = 'row-content active';
        const p = document.createElement('p');
        setSanitizedHTML(p, rowData[nonEmptyCols[0]]);
        rowContent.appendChild(p);
        rowContainer.appendChild(rowContent);
        highlightReferences(rowContent, tooltips);
        initializeTooltips(rowContent);
    } else {
        const rowTabs = document.createElement('div');
        rowTabs.className = 'row-tabs';
        if (hasNotes) {
            rowTabs.appendChild(createRowNotesToggle());
        }
        let activeCol = null;

        nonEmptyCols.forEach(col => {
            const origColIdx = allColumns.indexOf(col);
            const tabIdx = origColIdx + 1;
            const tab = document.createElement('div');
            tab.className = 'tab';
            tab.textContent = tabIdx;
            tab.dataset.column = col;
            tab.dataset.tabIndex = tabIdx;
            tab.dataset.rowData = JSON.stringify(rowData);
            tab.title = col.replace('D:', '').trim();

            if (tabIdx === defaultTab) {
                tab.classList.add('active');
                activeCol = col;
            }

            tab.addEventListener('click', (event) => {
                const currentTab = event.target;
                const tabs = currentTab.parentNode.querySelectorAll('.tab');
                tabs.forEach(t => t.classList.remove('active'));
                currentTab.classList.add('active');

                const container = currentTab.closest('.row-container');
                const rowContent = container.querySelector('.row-content');
                rowContent.innerHTML = '';
                const p = document.createElement('p');
                setSanitizedHTML(p, rowData[col]);
                rowContent.appendChild(p);
                highlightReferences(rowContent, tooltips);
                initializeTooltips(rowContent);

                const url = new URL(window.location);
                url.searchParams.set('row', dataRowIndex + 1);
                url.searchParams.set('tab', tabIdx);
                history.replaceState(null, '', url);
            });

            rowTabs.appendChild(tab);
        });

        rowContainer.appendChild(rowTabs);

        const rowContent = document.createElement('div');
        rowContent.className = 'row-content';
        const initialCol = activeCol || nonEmptyCols[0];
        const initP = document.createElement('p');
        setSanitizedHTML(initP, rowData[initialCol]);
        rowContent.appendChild(initP);

        if (!activeCol) {
            const firstTab = rowTabs.querySelector('.tab');
            if (firstTab) firstTab.classList.add('active');
        }

        rowContainer.appendChild(rowContent);
        highlightReferences(rowContent, tooltips);
        initializeTooltips(rowContent);
    }

    return rowContainer;
}

// Create a column header with version dropdown
function createColumnHeader(colIndex, columns) {
    const header = document.createElement('div');
    header.className = 'column-header';
    header.dataset.col = colIndex;

    const select = document.createElement('select');
    select.className = 'column-select';
    select.setAttribute('aria-label', 'Column ' + (colIndex + 1) + ' version');

    columns.forEach((col, i) => {
        const option = document.createElement('option');
        option.value = i + 1;
        option.textContent = (i + 1) + ': ' + col.replace('D:', '').trim();
        select.appendChild(option);
    });

    select.value = Math.min(colIndex + 1, columns.length);

    select.addEventListener('change', () => {
        switchColumnTabs(colIndex, parseInt(select.value, 10));
    });

    header.appendChild(select);
    return header;
}

// Switch all tabs in a specific column
function switchColumnTabs(colIndex, tabIndex) {
    const contentBody = document.querySelector('.content-body');
    const containers = contentBody.querySelectorAll('.row-container[data-col="' + colIndex + '"]');
    containers.forEach(container => {
        const tabs = container.querySelectorAll('.row-tabs .tab');
        if (tabs.length === 0) return;
        const targetTab = Array.from(tabs).find(t => t.dataset.tabIndex === String(tabIndex));
        if (targetTab && !targetTab.classList.contains('active')) {
            targetTab.click();
        }
    });
}

// Add a comparison column
function addColumn() {
    if (currentBookColumns.length <= 1) return;

    activeColumnCount++;
    const defaultTab = ((activeColumnCount - 1) % currentBookColumns.length) + 1;

    const columnHeaders = document.querySelector('.content-body .column-headers');
    if (columnHeaders) {
        const header = createColumnHeader(activeColumnCount - 1, currentBookColumns);
        columnHeaders.appendChild(header);
    }

    document.querySelectorAll('.content-body .row-group').forEach(rowGroup => {
        const dataIndex = parseInt(rowGroup.dataset.dataIndex, 10);
        const row = currentBookRows[dataIndex];
        if (!row) return;

        const rowContainer = createRowContainer(row, currentBookColumns, activeColumnCount - 1, defaultTab, dataIndex);
        if (rowContainer) {
            const notesDiv = rowGroup.querySelector('.row-notes');
            if (notesDiv) {
                rowGroup.insertBefore(rowContainer, notesDiv);
            } else {
                rowGroup.appendChild(rowContainer);
            }
        }
    });


    document.getElementById('remove-column-btn').style.display = '';
}

// Remove the last comparison column
function removeColumn() {
    if (activeColumnCount <= 1) return;

    const lastCol = activeColumnCount - 1;

    const columnHeaders = document.querySelector('.content-body .column-headers');
    if (columnHeaders) {
        const lastHeader = columnHeaders.querySelector('.column-header[data-col="' + lastCol + '"]');
        if (lastHeader) lastHeader.remove();
    }

    document.querySelectorAll('.content-body .row-container[data-col="' + lastCol + '"]').forEach(c => c.remove());

    activeColumnCount--;


    if (activeColumnCount <= 1) {
        document.getElementById('remove-column-btn').style.display = 'none';
    }
}

// Reset all added columns back to 1
function resetColumns() {
    for (let i = activeColumnCount - 1; i > 0; i--) {
        document.querySelectorAll('.content-body .row-container[data-col="' + i + '"]').forEach(c => c.remove());
    }
    const columnHeaders = document.querySelector('.content-body .column-headers');
    if (columnHeaders) {
        const headers = columnHeaders.querySelectorAll('.column-header');
        headers.forEach((h, i) => { if (i > 0) h.remove(); });
        const firstSelect = columnHeaders.querySelector('.column-select');
        if (firstSelect) firstSelect.value = '1';
    }
    activeColumnCount = 1;

    const removeBtn = document.getElementById('remove-column-btn');
    if (removeBtn) removeBtn.style.display = 'none';
}


// Reset book toolbar state when switching content
function resetBookToolbarState() {
    const contentBody = document.querySelector('.content-body');
    // Reset per-row notes toggles
    contentBody.querySelectorAll('.row-group.show-row-notes').forEach(rg => rg.classList.remove('show-row-notes'));
    contentBody.querySelectorAll('.row-notes-toggle input').forEach(cb => cb.checked = false);
    const removeBtn = document.getElementById('remove-column-btn');
    if (removeBtn) removeBtn.style.display = 'none';
}

// Function to show specific content (simplified toggle, now accepts optional params for deep linking)
// Lazy-load content for a title if not yet fetched
async function ensureContentLoaded(title) {
    const meta = contentMeta[title];
    if (!meta || meta.loaded) return;
    meta.loaded = true;
    const el = contentElements[title];
    // Show inline phi image while loading
    el.innerHTML = '<div class="inline-loading"><img src="images/phi.png" class="loading-phi" alt="Loading"></div>';
    await loadAndDisplayContent(meta.link, meta.type, title, el);
}

async function showContent(type, title, deepParams = null) {
    const contentBody = document.querySelector('.content-body');
    const mapDiv = document.getElementById('wisdom-map');
    const contentDiv = document.querySelector('.content');

    // If map is visible, toggle it off and show content
    if (mapDiv.style.display === 'block') {
        mapDiv.style.display = 'none';
        contentDiv.style.display = 'flex';
    }

    // Reset previous content's per-row notes state before switching
    contentBody.querySelectorAll('.row-group.show-row-notes').forEach(rg => rg.classList.remove('show-row-notes'));
    contentBody.querySelectorAll('.row-notes-toggle input').forEach(cb => cb.checked = false);

    // Clean up previous content's extra columns before switching
    if (activeColumnCount > 1) {
        const prevDoc = contentBody.querySelector('.doc-content');
        if (prevDoc) {
            for (let i = activeColumnCount - 1; i > 0; i--) {
                prevDoc.querySelectorAll('.row-container[data-col="' + i + '"]').forEach(c => c.remove());
            }
            const prevHeaders = prevDoc.querySelector('.column-headers');
            if (prevHeaders) {
                prevHeaders.querySelectorAll('.column-header').forEach((h, idx) => {
                    if (idx > 0) h.remove();
                });
                const firstSelect = prevHeaders.querySelector('.column-select');
                if (firstSelect) firstSelect.value = '1';
            }
        }
        activeColumnCount = 1;
    }
    contentBody.innerHTML = ''; // Clear previous content

    // Update active sidebar item
    document.querySelectorAll('.sidebar button.active-item').forEach(btn => btn.classList.remove('active-item'));
    document.querySelectorAll('.sidebar .sub-list').forEach(sl => sl.remove());
    const activeBtn = document.querySelector(`.sidebar button[data-title="${CSS.escape(title)}"]`);
    if (activeBtn) {
        activeBtn.classList.add('active-item');
        activeBtn.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    // Lazy-load content if not yet fetched
    await ensureContentLoaded(title);

    const docContent = contentElements[title];
    if (docContent) {
        docContent.classList.add('active');
        contentBody.appendChild(docContent);

        // Handle deep link to row and tab if params provided (or fallback to URL params)
        const params = deepParams || new URLSearchParams(window.location.search);
        const rowIndex = parseInt(params.get('row'), 10) - 1; // 1-based to 0-based
        const tabIndex = parseInt(params.get('tab'), 10); // 1-based
        if (!isNaN(rowIndex)) {
            const targetRow = docContent.querySelector('#row-' + rowIndex);
            if (targetRow) {
                // Select tab if specified (in the first column)
                if (!isNaN(tabIndex)) {
                    const firstCol = targetRow.querySelector('.row-container[data-col="0"]');
                    if (firstCol) {
                        const tabs = firstCol.querySelectorAll('.tab');
                        const targetTab = Array.from(tabs).find(tab => parseInt(tab.textContent, 10) === tabIndex);
                        if (targetTab) {
                            targetTab.click();
                        }
                    }
                }
                targetRow.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }

        // Add chapter sub-list to sidebar
        const chapters = Array.from(docContent.querySelectorAll('.chapter-head')).map(head => ({
            id: head.id,
            text: head.textContent.trim()
        }));
        if (chapters.length > 0) {
            // Find the active sidebar item
            const activeButton = document.querySelector(`.sidebar button[data-title="${title}"]`);
            if (activeButton) {
                const listItem = activeButton.parentElement;
                // Clear existing sub-list if any
                const existingSubList = listItem.querySelector('.sub-list');
                if (existingSubList) existingSubList.remove();
                // Create new sub-list
                const subList = document.createElement('ul');
                subList.className = 'sub-list';
                chapters.forEach(chapter => {
                    const subItem = document.createElement('li');
                    const chapterButton = document.createElement('button');
                    chapterButton.className = 'chapter-button';
                    chapterButton.textContent = chapter.text;
                    chapterButton.addEventListener('click', () => {
                        const heading = document.getElementById(chapter.id);
                        if (heading) heading.scrollIntoView({ behavior: 'smooth' });
                    });
                    subItem.appendChild(chapterButton);
                    subList.appendChild(subItem);
                });
                listItem.appendChild(subList);
            }
        }
    } else {
        const heading = document.createElement('h2');
        heading.textContent = type.charAt(0).toUpperCase() + type.slice(1) + ': ' + title + ' (Content not loaded)';
        contentBody.appendChild(heading);
        const emptyDoc = document.createElement('div');
        emptyDoc.className = 'doc-content';
        contentBody.appendChild(emptyDoc);
    }

    // Reset toolbar state for fresh content
    resetBookToolbarState();

    // Update URL state for bookmarkability (skip during initial deep link load and popstate)
    if (!deepParams && !isPopstateNavigation) {
        const url = new URL(window.location);
        url.searchParams.set('type', type);
        url.searchParams.set('content', title);
        url.searchParams.delete('row');
        url.searchParams.delete('tab');
        history.pushState({ type, title }, '', url);
    }
}

// Handle browser back/forward navigation
let isPopstateNavigation = false;
window.addEventListener('popstate', async (event) => {
    if (event.state && event.state.type && event.state.title) {
        isPopstateNavigation = true;
        await showContent(event.state.type, event.state.title);
        isPopstateNavigation = false;
    }
});

// Function to load and display content
async function loadAndDisplayContent(link, type, title, targetContentBody = null) {
    const contentBody = targetContentBody || document.querySelector('.content-body');
    // Clear any loading spinner or prior content
    contentBody.innerHTML = '';
    let docContent = contentBody.querySelector('.doc-content');
    if (!docContent) {
        docContent = document.createElement('div');
        docContent.className = 'doc-content';
        contentBody.appendChild(docContent);
    }

    try {
        if (link.includes('document')) {
            const response = await fetch(link);
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const htmlText = await response.text();
            const parser = new DOMParser();
            const doc = parser.parseFromString(htmlText, 'text/html');
            const bodyContent = doc.querySelector('body');

            if (bodyContent) {
                // Remove known Google Docs UI containers
                const bannersDiv = bodyContent.querySelector('#banners');
                if (bannersDiv) bannersDiv.remove();
                bodyContent.querySelectorAll('footer, header').forEach(el => el.remove());
                bodyContent.querySelectorAll('[class*="docs-"], [id*="docs-"]').forEach(el => el.remove());

                // Remove only exact-match Google UI strings (not broad substring matching)
                bodyContent.querySelectorAll('div, p, span').forEach(el => {
                    const text = el.textContent.toLowerCase().trim();
                    if (
                        text === 'published by google sheets' ||
                        text === 'published by google docs' ||
                        text === 'published by google' ||
                        (el.querySelector('a[href*="docs.google.com"]') && text.length < 100)
                    ) {
                        el.remove();
                    }
                });

                // Remove first child if it exactly matches the document title
                const firstChild = bodyContent.firstElementChild;
                if (firstChild && firstChild.textContent.trim().toLowerCase() === title.toLowerCase()) {
                    firstChild.remove();
                }

                docContent.innerHTML = DOMPurify.sanitize(bodyContent.innerHTML);
            } else {
                const fallbackDiv = document.createElement('div');
                fallbackDiv.innerHTML = DOMPurify.sanitize(htmlText);
                fallbackDiv.querySelectorAll('style').forEach(style => style.remove());
                fallbackDiv.querySelectorAll('#banners').forEach(banner => banner.remove());
                docContent.innerHTML = DOMPurify.sanitize(fallbackDiv.innerHTML);
            }
        } else if (link.includes('spreadsheets')) {
            const csvLink = link.replace('/edit', '/pub?output=csv');
            const data = await fetchGoogleSheetData(csvLink);
            if (!data || data.length === 0) {
                docContent.textContent = '';
                docContent.appendChild(createErrorP('No data found for ' + title + '.'));
                return;
            }

            const columns = Object.keys(data[0] || {}).filter(key => key.startsWith('D:'));
            if (columns.length === 0) {
                docContent.textContent = '';
                docContent.appendChild(createErrorP('No columns with "D:" found for ' + title + '.'));
                return;
            }

            // Store for column management
            currentBookColumns = columns;
            currentBookRows = data;
            activeColumnCount = 1;

            docContent.innerHTML = '';
            let currentChapter = null;

            // Create book toolbar (column headers aligned to content columns)
            if (columns.length > 1) {
                const toolbar = document.createElement('div');
                toolbar.className = 'book-toolbar';

                const columnHeaders = document.createElement('div');
                columnHeaders.className = 'column-headers';

                // First column header: title + select + add/remove buttons
                const header = createColumnHeader(0, columns);

                const titleSpan = document.createElement('span');
                titleSpan.className = 'book-title';
                titleSpan.textContent = title;
                header.insertBefore(titleSpan, header.firstChild);

                const addBtn = document.createElement('button');
                addBtn.className = 'column-btn column-btn-add';
                addBtn.id = 'add-column-btn';
                addBtn.textContent = '+';
                addBtn.title = 'Add column';
                addBtn.addEventListener('click', addColumn);
                header.appendChild(addBtn);

                const removeBtn = document.createElement('button');
                removeBtn.className = 'column-btn column-btn-remove';
                removeBtn.id = 'remove-column-btn';
                removeBtn.textContent = '\u2212';
                removeBtn.title = 'Remove column';
                removeBtn.style.display = 'none';
                removeBtn.addEventListener('click', removeColumn);
                header.appendChild(removeBtn);

                columnHeaders.appendChild(header);

                toolbar.appendChild(columnHeaders);
                docContent.appendChild(toolbar);
            }

            data.forEach((row, rowIndex) => {
                const chapter = row['Chapter']?.trim() || null;
                if (chapter && chapter !== currentChapter) {
                    const chapterHeading = document.createElement('div');
                    chapterHeading.className = 'chapter-head';
                    chapterHeading.id = `chapter-${chapter}`;
                    chapterHeading.textContent = `Chapter ${chapter}`;
                    docContent.appendChild(chapterHeading);
                    currentChapter = chapter;
                }

                // Check for non-empty D: columns
                const nonEmptyCols = columns.filter(col => row[col] && row[col].trim() !== '');
                if (nonEmptyCols.length === 0) return;

                // Create row-group wrapper
                const rowGroup = document.createElement('div');
                rowGroup.className = 'row-group';
                rowGroup.id = `row-${rowIndex}`;
                rowGroup.dataset.dataIndex = rowIndex;

                // Create initial row-container (column 0)
                const rowContainer = createRowContainer(row, columns, 0, 1, rowIndex);
                if (rowContainer) {
                    rowGroup.appendChild(rowContainer);
                }

                // Create per-row notes div
                const rowNotes = document.createElement('div');
                rowNotes.className = 'row-notes';
                const notesVal = row['Notes']?.trim();
                const rowIdx = row['Index']?.trim();
                if (notesVal && rowIdx) {
                    const noteIdx = document.createElement('span');
                    noteIdx.className = 'note-index';
                    noteIdx.textContent = rowIdx;
                    rowNotes.appendChild(noteIdx);
                    const noteText = document.createElement('span');
                    setSanitizedHTML(noteText, notesVal);
                    rowNotes.appendChild(noteText);
                }
                rowGroup.appendChild(rowNotes);

                docContent.appendChild(rowGroup);
            });
        }
        highlightReferences(docContent, tooltips);
        initializeTooltips(docContent);
    } catch (error) {
        docContent.textContent = '';
        docContent.appendChild(createErrorP('Failed to load data for ' + title + '. Please try again later.'));
    }
}

function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function highlightReferences(container, tooltips) {
    const terms = Object.keys(tooltips).sort((a, b) => b.length - a.length);
    const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
        const node = walker.currentNode;
        if (node.parentElement.tagName === 'SCRIPT' || node.parentElement.tagName === 'STYLE' || node.parentElement.classList.contains('ref')) continue;
        let text = node.nodeValue;
        let replaced = false;
        terms.forEach(term => {
            const regex = new RegExp(`\\b${escapeRegExp(term)}\\b`, 'g');
            if (regex.test(text)) {
                text = text.replace(regex, '<span class="ref">$&</span>');
                replaced = true;
            }
        });
        if (replaced) {
            const temp = document.createElement('div');
            // Safe: text originates from text node nodeValue, only <span class="ref"> wrappers injected via regex
            temp.innerHTML = text;
            const fragment = document.createDocumentFragment();
            while (temp.firstChild) {
                fragment.appendChild(temp.firstChild);
            }
            node.parentNode.replaceChild(fragment, node);
        }
    }
}

// Custom tooltip element and state
const customTooltip = document.getElementById('custom-tooltip');
let tooltipTimeout = null;

function showTooltip(refElement, content) {
    // Clear any pending hide
    if (tooltipTimeout) {
        clearTimeout(tooltipTimeout);
        tooltipTimeout = null;
    }

    // Sanitize and set content
    customTooltip.innerHTML = DOMPurify.sanitize(content, {
        ALLOWED_TAGS: ['b', 'i', 'strong', 'em', 'a', 'br', 'span', 'u', 'sub', 'sup'],
        ALLOWED_ATTR: ['href', 'target', 'class', 'rel']
    });

    // Position tooltip above the element
    const rect = refElement.getBoundingClientRect();
    customTooltip.style.left = rect.left + 'px';
    customTooltip.style.top = (rect.top - 10) + 'px';
    customTooltip.style.transform = 'translateY(-100%)';
    customTooltip.classList.add('visible');

    // Adjust if tooltip goes off screen (check after making visible)
    requestAnimationFrame(() => {
        const tooltipRect = customTooltip.getBoundingClientRect();
        if (tooltipRect.top < 0) {
            // Show below instead
            customTooltip.style.top = (rect.bottom + 10) + 'px';
            customTooltip.style.transform = 'translateY(0)';
        }
        if (tooltipRect.right > window.innerWidth) {
            customTooltip.style.left = (window.innerWidth - tooltipRect.width - 10) + 'px';
        }
        if (tooltipRect.left < 0) {
            customTooltip.style.left = '10px';
        }
    });
}

function hideTooltip() {
    tooltipTimeout = setTimeout(() => {
        customTooltip.classList.remove('visible');
    }, 150); // Small delay to allow moving to tooltip for clicking links
}

// Allow hovering over tooltip content (for clicking links)
if (customTooltip) {
    customTooltip.addEventListener('mouseenter', () => {
        if (tooltipTimeout) {
            clearTimeout(tooltipTimeout);
            tooltipTimeout = null;
        }
    });
    customTooltip.addEventListener('mouseleave', hideTooltip);
}

function initializeTooltips(container) {
    const refs = container.querySelectorAll('.ref');
    refs.forEach(ref => {
        // Skip if already initialized
        if (ref.dataset.tooltipInit) return;
        ref.dataset.tooltipInit = 'true';

        const keyPhrase = ref.textContent.trim();
        if (tooltips[keyPhrase]) {
            ref.addEventListener('mouseenter', () => {
                showTooltip(ref, tooltips[keyPhrase]);
            });
            ref.addEventListener('mouseleave', hideTooltip);
        }
    });
}

// Function to fetch and parse CSV data from a Google Sheet
function fetchGoogleSheetData(url) {
    return fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(csvText => {
            return new Promise((resolve, reject) => {
                Papa.parse(csvText, {
                    header: true,
                    complete: function(results) {
                        resolve(results.data);
                    },
                    error: function(error) {
                        reject(error);
                    }
                });
            });
        })
        .catch(error => {
            throw error;
        });
}