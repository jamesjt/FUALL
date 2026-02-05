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
          ALLOWED_ATTR: ['href', 'target', 'class'] }
    );
}

let contentElements = {}; // Global object to store preloaded content
let contentMeta = {}; // Metadata for lazy loading: { title: { link, type, loaded } }
let tooltips = {}; // Global tooltips object to store refs data
let network = null; // vis.js network instance
let mapInitialized = false; // Flag for lazy init
let unifiedData, articlesData, booksData, breakdownsData;

document.addEventListener('DOMContentLoaded', () => {
    // Unified content sheet URL (Articles sheet with Type column)
    const unifiedSheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?gid=464648636&output=csv';
    // Internal refs URL (separate)
    const refsSheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?gid=1749170252&single=true&output=csv';

    // Fetch unified content and refs
    Promise.all([
        fetchGoogleSheetData(unifiedSheetUrl),
        fetchGoogleSheetData(refsSheetUrl)
    ])
        .then(([unified, refs]) => {
            // Process tooltips data (separate)
            tooltips = refs.reduce((acc, row) => {
                if (row.References && row.Data) {
                    acc[row.References.trim()] = row.Data.trim();
                }
                return acc;
            }, {});

            // Store and filter unified data
            unifiedData = unified || [];
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

                // Add MutationObserver to reapply tooltips on DOM changes
                const observer = new MutationObserver(() => {
                    observer.disconnect();
                    highlightReferences(contentBody, tooltips);
                    initializeTippy(contentBody);
                    observer.observe(contentBody, { childList: true, subtree: true });
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
                buildWisdomMap(unifiedData);
                mapInitialized = true;
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
});

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
            buttonElement.addEventListener('click', () => showContent(type, item));
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
function buildWisdomMap(data) {
    const container = document.getElementById('wisdom-map');
    container.style.position = 'relative';
    const nodes = new vis.DataSet();
    const edges = new vis.DataSet();

    // Group styles — muted fills with darker borders (colors only, shapes set by content type)
    const groups = {
        'Wisdom':  { color: { background: 'rgba(212, 175, 55, 0.5)', border: '#d4af37' }, size: 20, font: { color: '#ffffff', size: 12, vadjust: 30 } },
        'Reality': { color: { background: 'rgba(122, 138, 154, 0.5)', border: '#7a8a9a' }, size: 18, font: { color: '#ffffff', size: 12, vadjust: 28 } },
        'Reason':  { color: { background: 'rgba(212, 175, 55, 0.5)', border: '#d4af37' }, size: 18, font: { color: '#ffffff', size: 12, vadjust: 28 } },
        'Right':   { color: { background: 'rgba(176, 128, 128, 0.5)', border: '#b08080' }, size: 18, font: { color: '#ffffff', size: 12, vadjust: 28 } },
        'Musings': { color: { background: 'rgba(144, 128, 160, 0.5)', border: '#9080a0' }, size: 12, font: { color: '#ffffff', size: 10, vadjust: 22 } },
        'Root':    { color: { background: 'rgba(212, 175, 55, 0.5)', border: '#d4af37' }, size: 25, font: { color: '#ffffff', size: 14, vadjust: 35 } }
    };

    // --- Classify nodes by Tag and Parent ---
    const classified = { Root: [], Wisdom: [], Reality: [], Reason: [], Right: [], Musings: [], Other: [] };

    data.forEach(row => {
        const title = row['Title']?.trim();
        const tag = row['Tag']?.trim();
        const parent = row['Parent']?.trim();
        const type = row['Type']?.trim().toLowerCase();
        if (!title) return;

        const entry = { title, tag, parent, type, row };
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

    // --- Helper: get shape by content type ---
    function getShape(type) {
        if (type === 'article') return 'diamond';
        if (type === 'book') return 'square';
        if (type === 'breakdown') return 'triangle';
        return 'dot';
    }

    // --- Add all nodes (hierarchical layout will position them) ---
    function addNode(entry, groupName) {
        const nodeConfig = {
            id: entry.title,
            label: entry.title,
            group: entry.tag || groupName,
            shape: getShape(entry.type),
            data: { parent: entry.parent, type: entry.type }
        };
        if (entry.type === 'book') {
            nodeConfig.borderWidth = 2;
        }
        nodes.add(nodeConfig);

        // Create edge from parent to child (arrow points to child)
        if (entry.parent && entry.parent !== 'Root' && entry.parent !== 'Musing' && entry.parent !== entry.title) {
            edges.add({ from: entry.parent, to: entry.title });
        }
    }

    // Add all classified nodes
    classified.Root.forEach(entry => addNode(entry, 'Root'));
    classified.Wisdom.forEach(entry => addNode(entry, 'Wisdom'));
    classified.Reality.forEach(entry => addNode(entry, 'Reality'));
    classified.Reason.forEach(entry => addNode(entry, 'Reason'));
    classified.Right.forEach(entry => addNode(entry, 'Right'));
    classified.Musings.forEach(entry => addNode(entry, 'Musings'));
    classified.Other.forEach(entry => addNode(entry, 'Wisdom'));

    // --- Network options: hierarchical layout (upward flow, no dragging) ---
    const options = {
        layout: {
            hierarchical: {
                enabled: true,
                direction: 'DU',           // Down-to-Up (root at bottom, leaves at top)
                sortMethod: 'directed',    // Follow edge directions
                levelSeparation: 120,      // Vertical spacing between levels
                nodeSpacing: 180,          // Horizontal spacing between nodes
                treeSpacing: 250,          // Spacing between disconnected trees
                shakeTowards: 'roots'      // Minimize edge crossings toward roots
            }
        },
        physics: {
            enabled: false  // Static layout, no physics
        },
        groups: groups,
        edges: {
            arrows: { to: { enabled: true, scaleFactor: 0.5 } },
            color: { color: '#555', highlight: '#d29a38' },
            smooth: { type: 'cubicBezier', roundness: 0.4 }
        },
        interaction: {
            hover: true,
            zoomView: true,
            dragView: true,
            dragNodes: false  // Prevent node dragging
        }
    };

    network = new vis.Network(container, { nodes, edges }, options);

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
        preview.style.left = (params.pointer.DOM.x + 10) + 'px';
        preview.style.top = (params.pointer.DOM.y + 10) + 'px';
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

    container.appendChild(controlsDiv);
}

// Function to show specific content (simplified toggle, now accepts optional params for deep linking)
// Lazy-load content for a title if not yet fetched
async function ensureContentLoaded(title) {
    const meta = contentMeta[title];
    if (!meta || meta.loaded) return;
    meta.loaded = true;
    const el = contentElements[title];
    // Show inline spinner while loading
    el.innerHTML = '<div class="inline-loading"><div class="spinner"></div><p>Loading...</p></div>';
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
            const rowContainers = docContent.querySelectorAll('.row-container');
            const targetRow = rowContainers[rowIndex];
            if (targetRow) {
                // Select tab if specified
                if (!isNaN(tabIndex)) {
                    const tabs = targetRow.querySelectorAll('.tab');
                    const targetTab = Array.from(tabs).find(tab => parseInt(tab.textContent, 10) === tabIndex);
                    if (targetTab) {
                        targetTab.click(); // Simulate click to activate
                    }
                }
                // Scroll to row
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

            docContent.innerHTML = '';
            let currentChapter = null;
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

                if (columns.length === 1) {
                    const singleCol = columns[0];
                    if (row[singleCol] && row[singleCol].trim() !== '') {
                        const p = document.createElement('p');
                        setSanitizedHTML(p, row[singleCol]);
                        docContent.appendChild(p);
                        highlightReferences(p, tooltips);
                        initializeTippy(p);
                    }
                } else {
                    const nonEmptyCols = [];
                    columns.forEach(col => {
                        if (row[col] && row[col].trim() !== '') {
                            nonEmptyCols.push(col);
                        }
                    });

                    if (nonEmptyCols.length === 0) return;

                    if (nonEmptyCols.length === 1) {
                        // Render as simple p without tabs
                        const singleCol = nonEmptyCols[0];
                        const p = document.createElement('p');
                        setSanitizedHTML(p, row[singleCol]);
                        docContent.appendChild(p);
                        highlightReferences(p, tooltips);
                        initializeTippy(p);
                    } else {
                        // Multi: render tabs/container
                        const rowContainer = document.createElement('div');
                        rowContainer.className = 'row-container';
                        rowContainer.id = `row-${rowIndex}`; // Add ID for deep linking

                        const rowTabs = document.createElement('div');
                        rowTabs.className = 'row-tabs';

                        nonEmptyCols.forEach((col, adjustedIndex) => {
                            const colIndex = columns.indexOf(col); // Original index for textContent
                            const tab = document.createElement('div');
                            tab.className = 'tab';
                            tab.textContent = colIndex + 1;
                            const tooltipContent = col.replace('D:', '').trim(); // Tooltip without 'D:'
                            tab.dataset.column = col;
                            tab.dataset.rowIndex = rowIndex;
                            tab.dataset.tabIndex = colIndex + 1; // Add for deep linking (1-based)
                            tab.dataset.rowData = JSON.stringify(row); // Store row data for popup cloning
                            tab.addEventListener('click', (event) => {
                                const currentTab = event.target;
                                const tabs = currentTab.parentNode.querySelectorAll('.tab');
                                tabs.forEach(t => t.classList.remove('active'));
                                currentTab.classList.add('active');

                                const container = currentTab.closest('.row-container');
                                const rowContent = container.querySelector('.row-content');
                                rowContent.innerHTML = '';
                                const p = document.createElement('p');
                                setSanitizedHTML(p, row[col]);
                                rowContent.appendChild(p);
                                highlightReferences(rowContent, tooltips);
                                initializeTippy(rowContent);

                                // Update URL with row/tab for deep linking
                                const url = new URL(window.location);
                                url.searchParams.set('row', rowIndex + 1);
                                url.searchParams.set('tab', colIndex + 1);
                                history.replaceState(null, '', url);
                            });
                            tippy(tab, {
                                content: tooltipContent,
                                allowHTML: false,
                                theme: 'custom',
                                placement: 'top',
                                arrow: true,
                                interactive: false,
                            });
                            rowTabs.appendChild(tab);
                        });

                        rowContainer.appendChild(rowTabs);

                        const rowContent = document.createElement('div');
                        rowContent.className = 'row-content';

                        // Set initial content to the first non-empty column
                        const initialCol = nonEmptyCols[0];
                        if (initialCol) {
                            const initP = document.createElement('p');
                            setSanitizedHTML(initP, row[initialCol]);
                            rowContent.appendChild(initP);
                        }

                        rowContainer.appendChild(rowContent);

                        docContent.appendChild(rowContainer);

                        // Set first tab active
                        const firstTab = rowTabs.querySelector('.tab');
                        if (firstTab) {
                            firstTab.classList.add('active');
                        }

                        highlightReferences(rowContent, tooltips);
                        initializeTippy(rowContent);
                    }
                }
            });
        }
        highlightReferences(docContent, tooltips);
        initializeTippy(docContent);
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

function initializeTippy(container) {
    const refs = container.querySelectorAll('.ref');
    refs.forEach(ref => {
        const keyPhrase = ref.textContent.trim();
        if (tooltips[keyPhrase]) {
            tippy(ref, {
                content: tooltips[keyPhrase],
                allowHTML: true,
                theme: 'custom',
                placement: 'top',
                arrow: true,
                interactive: true,
            });
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