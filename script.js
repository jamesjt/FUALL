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

let contentElements = {}; // Global object to store preloaded content
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

            // Preload and store all content
            const contentBody = document.querySelector('.content-body');
            if (unifiedData.length === 0) {
                contentBody.textContent = '';
                contentBody.appendChild(createErrorP('No data found.'));
            } else {
                const loadPromises = [];
                unifiedData.forEach(row => {
                    const title = row['Title']?.trim();
                    const link = row['Link']?.trim();
                    const type = row['Type']?.trim().toLowerCase();
                    const tag = row['Tag']?.trim(); // Optional, e.g., for articles
                    const parent = row['Parent']?.trim(); // Optional, e.g., for articles
                    if (title && link && type) {
                        contentElements[title] = document.createElement('div');
                        contentElements[title].className = 'doc-content';
                        contentElements[title].dataset.tag = tag || '';
                        contentElements[title].dataset.parent = parent || '';
                        contentElements[title].dataset.type = type || '';
                        loadPromises.push(loadAndDisplayContent(link, type, title, contentElements[title]));
                    }
                });

                Promise.all(loadPromises).then(() => {
                    // Remove loading indicator
                    const loadingEl = document.getElementById('loading-indicator');
                    if (loadingEl) loadingEl.remove();

                    // Handle deep link from URL params if present
                    const params = new URLSearchParams(window.location.search);
                    const deepType = params.get('type');
                    const deepContent = params.get('content');
                    if (deepType && deepContent && contentElements[deepContent]) {
                        showContent(deepType, deepContent, params); // Pass params for row/tab handling
                    } else {
                        // Show the first item if available (default behavior)
                        if (articlesData.length > 0) {
                            showContent('article', articlesData[0]['Title']);
                        } else if (booksData.length > 0) {
                            showContent('book', booksData[0]['Title']);
                        } else if (breakdownsData.length > 0) {
                            showContent('breakdown', breakdownsData[0]['Title']);
                        }
                    }

                    // Populate sidebars
                    populateSidebarList('.articles-list', articlesData, 'Title', 'article');
                    populateSidebarList('.books-list', booksData, 'Title', 'book');
                    populateSidebarList('.breakdowns-list', breakdownsData, 'Title', 'breakdown');

                    // Add MutationObserver to reapply tooltips on DOM changes
                    const observer = new MutationObserver(() => {
                        observer.disconnect(); // Prevent loop from own modifications
                        highlightReferences(contentBody, tooltips);
                        initializeTippy(contentBody);
                        observer.observe(contentBody, { childList: true, subtree: true }); // Re-observe
                    });
                    observer.observe(contentBody, { childList: true, subtree: true });
                });
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

// Function to build wisdom map with phi-shaped layout
function buildWisdomMap(data) {
    const container = document.getElementById('wisdom-map');
    container.style.position = 'relative';
    const nodes = new vis.DataSet();
    const edges = new vis.DataSet();

    // Group styles — Wisdom is the stem (deep gold), branches are leaves
    const groups = {
        'Wisdom':  { color: { background: '#b8862f', border: '#93681e' }, shape: 'dot', size: 20, font: { color: '#e0e0e0', size: 12 } },
        'Reality': { color: { background: '#d29a38', border: '#b8862f' }, shape: 'dot', size: 18, font: { color: '#e0e0e0', size: 12 } },
        'Reason':  { color: { background: '#4a90d9', border: '#3570b0' }, shape: 'dot', size: 18, font: { color: '#e0e0e0', size: 12 } },
        'Right':   { color: { background: '#c0392b', border: '#962d22' }, shape: 'dot', size: 18, font: { color: '#e0e0e0', size: 12 } },
        'Musings': { color: { background: '#6f42c1', border: '#5a32a3' }, shape: 'star', size: 12, font: { color: '#e0e0e0', size: 10 } },
        'Root':    { color: { background: '#b8862f', border: '#93681e' }, shape: 'diamond', size: 25, font: { color: '#e0e0e0', size: 14 } }
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

    // --- Phi layout coordinates ---
    // Bottom: root circle (phi loop). Stem: Wisdom rises upward. Three leaves branch from top.
    const centerX = 0;
    const bottomY = 500;       // Root circle center
    const circleRadius = 120;  // Phi loop radius
    const stemTopY = -100;     // Where Wisdom stem meets branching point
    const branchSpread = 350;  // Horizontal spread of leaf branches

    // Branch anchor positions (seeding locations for each group)
    const branchAnchors = {
        'Wisdom':   { x: centerX,                y: (bottomY + stemTopY) / 2 },  // Along the stem
        'Reality':  { x: centerX - branchSpread,  y: stemTopY - 150 },            // Left leaf
        'Reason':   { x: centerX,                 y: stemTopY - 250 },            // Center leaf (tallest)
        'Right':    { x: centerX + branchSpread,   y: stemTopY - 150 },            // Right leaf
        'Musings':  { x: centerX - branchSpread * 1.2, y: bottomY + 50 },         // Lower-left cluster
        'Other':    { x: centerX + branchSpread * 0.5, y: bottomY + 100 }         // Fallback
    };

    // --- Position root nodes in a circle at the bottom (phi loop) ---
    const rootCount = classified.Root.length || 1;
    classified.Root.forEach((entry, i) => {
        const angle = (2 * Math.PI * i) / rootCount - Math.PI / 2; // Start from top of circle
        nodes.add({
            id: entry.title,
            label: entry.title,
            group: 'Root',
            x: centerX + circleRadius * Math.cos(angle),
            y: bottomY + circleRadius * Math.sin(angle),
            fixed: { x: true, y: true },
            data: { parent: entry.parent, type: entry.type }
        });
    });

    // --- Add branch nodes seeded near their anchor positions ---
    function addBranchNodes(entries, anchor, groupName) {
        entries.forEach((entry, i) => {
            // Spread nodes around anchor with deterministic offsets
            const angle = (2 * Math.PI * i) / (entries.length || 1);
            const spread = Math.min(entries.length * 15, 150);
            const nodeConfig = {
                id: entry.title,
                label: entry.title,
                group: entry.tag || groupName,
                x: anchor.x + spread * Math.cos(angle),
                y: anchor.y + spread * Math.sin(angle),
                data: { parent: entry.parent, type: entry.type }
            };

            // Visual differentiation by content type
            if (entry.type === 'book') {
                nodeConfig.shape = 'box';
                nodeConfig.borderWidth = 2;
            } else if (entry.type === 'breakdown') {
                nodeConfig.shape = 'triangle';
            }

            nodes.add(nodeConfig);

            // Create edge to parent (skip Root, Musing, self-reference)
            if (entry.parent && entry.parent !== 'Root' && entry.parent !== 'Musing' && entry.parent !== entry.title) {
                edges.add({ from: entry.title, to: entry.parent });
            }
        });
    }

    addBranchNodes(classified.Wisdom, branchAnchors['Wisdom'], 'Wisdom');
    addBranchNodes(classified.Reality, branchAnchors['Reality'], 'Reality');
    addBranchNodes(classified.Reason, branchAnchors['Reason'], 'Reason');
    addBranchNodes(classified.Right, branchAnchors['Right'], 'Right');
    addBranchNodes(classified.Musings, branchAnchors['Musings'], 'Musings');
    addBranchNodes(classified.Other, branchAnchors['Other'], 'Wisdom');

    // --- Network options: physics-based settling then freeze ---
    const options = {
        layout: { hierarchical: { enabled: false } },
        physics: {
            enabled: true,
            solver: 'barnesHut',
            barnesHut: {
                gravitationalConstant: -3000,
                centralGravity: 0.1,
                springLength: 120,
                springConstant: 0.04,
                damping: 0.09
            },
            stabilization: {
                enabled: true,
                iterations: 200,
                updateInterval: 25
            }
        },
        groups: groups,
        edges: {
            arrows: { to: { enabled: true, scaleFactor: 0.5 } },
            color: { color: '#555', highlight: '#d29a38' },
            smooth: { type: 'cubicBezier', roundness: 0.4 }
        },
        interaction: { hover: true, zoomView: true, dragView: true }
    };

    network = new vis.Network(container, { nodes, edges }, options);

    // Freeze physics after stabilization to prevent drift
    network.on('stabilized', () => {
        network.setOptions({ physics: { enabled: false } });
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
        preview.style.left = (params.pointer.DOM.x + 10) + 'px';
        preview.style.top = (params.pointer.DOM.y + 10) + 'px';
        preview.style.display = 'block';
    });

    network.on('blurNode', () => {
        document.getElementById('hover-preview').style.display = 'none';
    });

    // --- Click event: open content in main area ---
    network.on('click', (params) => {
        if (params.nodes.length > 0) {
            const nodeId = params.nodes[0];
            const nodeData = nodes.get(nodeId);
            if (nodeData && nodeData.data) {
                showContent(nodeData.data.type || 'article', nodeId);
                // Switch from map view to content view
                document.getElementById('wisdom-map').style.display = 'none';
                document.querySelector('.content').style.display = 'flex';
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
function showContent(type, title, deepParams = null) {
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
window.addEventListener('popstate', (event) => {
    if (event.state && event.state.type && event.state.title) {
        isPopstateNavigation = true;
        showContent(event.state.type, event.state.title);
        isPopstateNavigation = false;
    }
});

// Function to load and display content
async function loadAndDisplayContent(link, type, title, targetContentBody = null) {
    const contentBody = targetContentBody || document.querySelector('.content-body');
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
                        setTextWithBreaks(p, row[singleCol]);
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
                        setTextWithBreaks(p, row[singleCol]);
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
                            tab.addEventListener('click', (event) => {
                                const currentTab = event.target;
                                const tabs = currentTab.parentNode.querySelectorAll('.tab');
                                tabs.forEach(t => t.classList.remove('active'));
                                currentTab.classList.add('active');

                                const container = currentTab.closest('.row-container');
                                const rowContent = container.querySelector('.row-content');
                                rowContent.textContent = '';
                                const p = document.createElement('p');
                                setTextWithBreaks(p, row[col]);
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
                            setTextWithBreaks(initP, row[initialCol]);
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