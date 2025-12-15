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
                contentBody.innerHTML = '<p class="error">No data found.</p>';
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
                        if (type === 'article') {
                            contentElements[title].dataset.tag = tag || '';
                            contentElements[title].dataset.parent = parent || '';
                        }
                        loadPromises.push(loadAndDisplayContent(link, type, title, contentElements[title]));
                    }
                });

                Promise.all(loadPromises).then(() => {
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
                contentBody.innerHTML += '<p class="error">Failed to load data: ' + error.message + '</p>';
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
                buildWisdomMap(articlesData); // articlesData needs to be in scope; assume hoisted or adjust
                mapInitialized = true;
            }
            if (network) network.stabilize();
        }
    });

    // Popover close
    document.getElementById('popover-close').addEventListener('click', () => {
        document.getElementById('popover').style.display = 'none';
    });
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

// Function to build wisdom map
function buildWisdomMap(articlesData) {
    const container = document.getElementById('wisdom-map');
    const nodes = new vis.DataSet();
    const edges = new vis.DataSet();

    // Group styles (made up colors)
    const groups = {
        'Wisdom': {color: '#007bff', shape: 'ellipse'},
        'Reality': {color: '#28a745', shape: 'box'},
        'Reason': {color: '#ffc107', shape: 'diamond'},
        'Right': {color: '#dc3545', shape: 'circle'},
        'Musings': {color: '#6f42c1', shape: 'star'}
    };

    // Add nodes and edges
    articlesData.forEach(row => {
        const title = row['Title']?.trim();
        const tag = row['Tag']?.trim();
        const parent = row['Parent']?.trim();
        if (title) {
            nodes.add({
                id: title,
                label: title,
                group: tag,
                data: {parent: parent, content: contentElements[title] ? contentElements[title].innerHTML : 'Content not loaded'}
            });
            if (parent && parent !== 'Root' && parent !== 'Musing' && parent !== title) { // Avoid self-loops
                edges.add({from: title, to: parent});
            }
        }
    });

    // Network options
    const options = {
        layout: {
            hierarchical: {
                enabled: true,
                direction: 'UD', // Default top-down
                sortMethod: 'directed',
                nodeSpacing: 150,
                levelSeparation: 150
            }
        },
        physics: {enabled: false}, // Disable for hierarchical
        groups: groups,
        edges: {arrows: 'to'},
        interaction: {hover: true}
    };

    network = new vis.Network(container, {nodes, edges}, options);

    // Cluster Musings
    network.cluster({
        joinCondition: (nodeOptions) => nodeOptions.data.parent === 'Musing',
        clusterNodeProperties: {id: 'musingsCluster', label: 'Musings Bucket', shape: 'database', color: '#6f42c1'}
    });

    // Simple zoom clustering (for scale)
    network.on('zoom', (params) => {
        if (params.scale < 0.5 && !network.getClusters().length) {
            // Cluster loose nodes (simplified: cluster all non-root)
            network.clusterByConnection('Foundations'); // Example, cluster around a root
        } else if (params.scale >= 0.5) {
            network.openCluster(network.getClusters()[0]); // Open if clustered
        }
    });

    // Hover event
    network.on('hoverNode', (params) => {
        const preview = document.getElementById('hover-preview');
        preview.innerHTML = network.body.nodes[params.node].options.data.content || 'No content';
        preview.style.left = `${params.pointer.DOM.x + 10}px`;
        preview.style.top = `${params.pointer.DOM.y + 10}px`;
        preview.style.display = 'block';
    });

    network.on('blurNode', () => {
        document.getElementById('hover-preview').style.display = 'none';
    });

    // Click event
    network.on('click', (params) => {
        if (params.nodes.length > 0) {
            const popover = document.getElementById('popover');
            const contentDiv = document.getElementById('popover-content');
            contentDiv.innerHTML = network.body.nodes[params.nodes[0]].options.data.content || 'No content';
            popover.style.display = 'block';
        }
    });

    // Add layout buttons
    const buttonsDiv = document.createElement('div');
    buttonsDiv.className = 'layout-buttons';
    ['UD', 'DU', 'LR'].forEach(dir => { // No RL button
        const btn = document.createElement('button');
        btn.textContent = dir === 'UD' ? 'Top-Down' : dir === 'DU' ? 'Bottom-Top' : 'Left-Right';
        btn.addEventListener('click', () => {
            buttonsDiv.querySelectorAll('button').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            network.setOptions({layout: {hierarchical: {direction: dir}}});
            network.redraw();
        });
        if (dir === 'UD') btn.classList.add('active');
        buttonsDiv.appendChild(btn);
    });
    document.body.appendChild(buttonsDiv);
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
    } else {
        contentBody.innerHTML = `<h2>${type.charAt(0).toUpperCase() + type.slice(1)}: ${title} (Content not loaded)</h2><div class="doc-content"></div>`;
    }
}

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
                const bannersDiv = bodyContent.querySelector('#banners');
                if (bannersDiv) bannersDiv.remove();
                const elements = bodyContent.querySelectorAll('p, div, span, footer, header');
                elements.forEach(element => {
                    const text = element.textContent.toLowerCase();
                    if (
                        text.includes('published by google') ||
                        text.includes(title.toLowerCase()) ||
                        text.includes('google docs') ||
                        text.includes('share') ||
                        text.includes('document') ||
                        element.className.includes('docs') ||
                        element.tagName.toLowerCase() === 'footer' ||
                        element.tagName.toLowerCase() === 'header'
                    ) {
                        element.remove();
                    }
                });
                const children = Array.from(bodyContent.children);
                if (children.length > 0) {
                    if (children[0].tagName.toLowerCase() === 'div' || children[0].tagName.toLowerCase() === 'p') {
                        if (children[0].textContent.trim().length < 50) children[0].remove();
                    }
                    if (children.length > 0 && (children[children.length - 1].tagName.toLowerCase() === 'div' || children[children.length - 1].tagName.toLowerCase() === 'p')) {
                        if (children[children.length - 1].textContent.trim().length < 50) children[children.length - 1].remove();
                    }
                }
                docContent.innerHTML = bodyContent.innerHTML;
            } else {
                const fallbackDiv = document.createElement('div');
                fallbackDiv.innerHTML = htmlText;
                fallbackDiv.querySelectorAll('style').forEach(style => style.remove());
                fallbackDiv.querySelectorAll('#banners').forEach(banner => banner.remove());
                docContent.innerHTML = fallbackDiv.innerHTML;
            }
        } else if (link.includes('spreadsheets')) {
            const csvLink = link.replace('/edit', '/pub?output=csv');
            const data = await fetchGoogleSheetData(csvLink);
            if (!data || data.length === 0) {
                docContent.innerHTML = '<p class="error">No data found for ' + title + '.</p>';
                return;
            }

            const columns = Object.keys(data[0] || {}).filter(key => key.startsWith('D:'));
            if (columns.length === 0) {
                docContent.innerHTML = '<p class="error">No columns with "D:" found for ' + title + '.</p>';
                return;
            }

            docContent.innerHTML = '';
            data.forEach((row, rowIndex) => {
                if (columns.length === 1) {
                    const singleCol = columns[0];
                    if (row[singleCol] && row[singleCol].trim() !== '') {
                        docContent.innerHTML += `<p>${(row[singleCol] || '').replace(/\n/g, '<br/>')}</p>`;
                    }
                } else {
                    const rowContainer = document.createElement('div');
                    rowContainer.className = 'row-container';
                    rowContainer.id = `row-${rowIndex}`; // Add ID for deep linking

                    const rowTabs = document.createElement('div');
                    rowTabs.className = 'row-tabs';

                    columns.forEach((col, colIndex) => {
                        if (row[col] && row[col].trim() !== '') {
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
                                rowContent.innerHTML = `<p>${(row[col] || '').replace(/\n/g, '<br/>')}</p>`;
                                highlightReferences(rowContent, tooltips);
                                initializeTippy(rowContent);
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
                        }
                    });

                    if (rowTabs.children.length > 0) {
                        rowContainer.appendChild(rowTabs);

                        const rowContent = document.createElement('div');
                        rowContent.className = 'row-content';

                        // Set initial content to the first non-empty column
                        const initialCol = columns.find(col => row[col] && row[col].trim() !== '');
                        if (initialCol) {
                            rowContent.innerHTML = `<p>${(row[initialCol] || '').replace(/\n/g, '<br/>')}</p>`;
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
        docContent.innerHTML = '<p class="error">Failed to load data for ' + title + '. Please try again later.</p>';
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