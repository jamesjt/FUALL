let contentElements = {}; // Global object to store preloaded content
let tooltips = {}; // Global tooltips object to store refs data
let network = null; // vis.js network instance
let mapInitialized = false; // Flag for lazy init

document.addEventListener('DOMContentLoaded', () => {
    // Articles sheet URL
    const articlesSheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?gid=464648636&output=csv';
    // Books sheet URL
    const booksSheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?output=csv';
    // Internal refs URL
    const refsSheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?gid=1749170252&single=true&output=csv';

    let articlesData = [];
    let booksData = [];

    // Fetch all data simultaneously
    Promise.all([
        fetchGoogleSheetData(articlesSheetUrl),
        fetchGoogleSheetData(booksSheetUrl),
        fetchGoogleSheetData(refsSheetUrl)
    ])
        .then(([articles, books, refs]) => {
            // Process tooltips data
            tooltips = refs.reduce((acc, row) => {
                if (row.References && row.Data) {
                    acc[row.References.trim()] = row.Data.trim();
                }
                return acc;
            }, {});

            // Store articles and books data
            articlesData = articles || [];
            booksData = books || [];

            // Preload and store all content (extend for articles with Tag/Parent)
            const contentBody = document.querySelector('.content-body');
            if (articlesData.length === 0) {
                contentBody.innerHTML = '<p class="error">No articles data found.</p>';
            } else {
                articlesData.forEach(row => {
                    const article = row['Articles']?.trim();
                    const link = row['Link']?.trim();
                    const tag = row['Tag']?.trim();
                    const parent = row['Parent']?.trim();
                    if (article && link) {
                        contentElements[article] = document.createElement('div');
                        contentElements[article].className = 'doc-content';
                        contentElements[article].dataset.tag = tag || '';
                        contentElements[article].dataset.parent = parent || '';
                        loadAndDisplayContent(link, 'article', article, contentElements[article]);
                    }
                });
            }

            if (booksData.length === 0) {
                contentBody.innerHTML += '<p class="error">No books data found.</p>';
            } else {
                booksData.forEach(row => {
                    const book = row['Book']?.trim();
                    const link = row['Link']?.trim();
                    if (book && link) {
                        contentElements[book] = document.createElement('div');
                        contentElements[book].className = 'doc-content';
                        loadAndDisplayContent(link, 'book', book, contentElements[book]);
                    }
                });
            }

            // Populate sidebars
            populateSidebarList('.articles-list', articlesData, 'Articles', 'article');
            populateSidebarList('.books-list', booksData, 'Book', 'book');

            // Show the first article or book if available
            if (articlesData.length > 0) {
                showContent('article', articlesData[0]['Articles']);
            } else if (booksData.length > 0) {
                showContent('book', booksData[0]['Book']);
            }

            // Add MutationObserver to reapply tooltips on DOM changes
            const observer = new MutationObserver(() => {
                observer.disconnect(); // Prevent loop from own modifications
                highlightReferences(contentBody, tooltips);
                initializeTippy(contentBody);
                observer.observe(contentBody, { childList: true, subtree: true }); // Re-observe
            });
            observer.observe(contentBody, { childList: true, subtree: true });
        })
        .catch(error => {
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
                buildWisdomMap(articlesData);
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
        const article = row['Articles']?.trim();
        const tag = row['Tag']?.trim();
        const parent = row['Parent']?.trim();
        if (article) {
            nodes.add({
                id: article,
                label: article,
                group: tag,
                data: {parent: parent, content: contentElements[article] ? contentElements[article].innerHTML : 'Content not loaded'}
            });
            if (parent && parent !== 'Root' && parent !== 'Musing' && parent !== article) { // Avoid self-loops
                edges.add({from: article, to: parent});
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

// Function to show specific content (simplified toggle)
function showContent(type, title) {
    const contentBody = document.querySelector('.content-body');
    contentBody.innerHTML = ''; // Clear previous content
    const docContent = contentElements[title];
    if (docContent) {
        docContent.classList.add('active');
        contentBody.appendChild(docContent);
    } else {
        contentBody.innerHTML = `<h2>${type === 'article' ? 'Article' : 'Book'}: ${title} (Content not loaded)</h2><div class="doc-content"></div>`;
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
                    docContent.innerHTML += `<p>${(row[columns[0]] || '').replace(/\n/g, '<br/>')}</p>`;
                } else {
                    const rowTabs = document.createElement('div');
                    rowTabs.className = 'row-tabs';
                    columns.forEach((col, colIndex) => {
                        const tab = document.createElement('div');
                        tab.className = 'tab';
                        tab.textContent = colIndex + 1;
                        tab.dataset.column = col;
                        tab.dataset.rowIndex = rowIndex;
                        tab.addEventListener('click', () => {
                            rowTabs.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                            tab.classList.add('active');
                            docContent.innerHTML = `<p>${(row[col] || '').replace(/\n/g, '<br/>')}</p>`;
                            highlightReferences(docContent, tooltips);
                            initializeTippy(docContent);
                        });
                        rowTabs.appendChild(tab);
                    });
                    rowTabs.querySelector('.tab').classList.add('active');
                    docContent.appendChild(rowTabs);
                    docContent.innerHTML += `<p>${(row[columns[0]] || '').replace(/\n/g, '<br/>')}</p>`;
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
                arrow: true
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