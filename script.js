let contentElements = {}; // Global object to store preloaded content
let tooltips = {}; // Global tooltips object to store refs data

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
                if (row.Word && row.Tooltip) {
                    acc[row.Word.trim()] = row.Tooltip.trim();
                }
                return acc;
            }, {});
            console.log('Tooltips loaded:', tooltips);

            // Store articles and books data
            articlesData = articles || [];
            booksData = books || [];

            // Preload and store all content
            const contentBody = document.querySelector('.content-body');
            if (articlesData.length === 0) {
                contentBody.innerHTML = '<p class="error">No articles data found.</p>';
                console.warn('No data found in the Articles CSV');
            } else {
                articlesData.forEach(row => {
                    const article = row['Articles']?.trim();
                    const link = row['Link']?.trim();
                    if (article && link) {
                        contentElements[article] = document.createElement('div');
                        contentElements[article].className = 'doc-content';
                        loadAndDisplayContent(link, 'article', article, contentElements[article]);
                    }
                });
            }

            if (booksData.length === 0) {
                contentBody.innerHTML += '<p class="error">No books data found.</p>';
                console.warn('No data found in the Books CSV');
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

            // Populate Articles sidebar
            const articlesList = document.querySelector('.articles-list');
            articlesList.innerHTML = '';
            articlesData.forEach(row => {
                const article = row['Articles']?.trim();
                if (article && contentElements[article]) {
                    const listItem = document.createElement('li');
                    const buttonElement = document.createElement('button');
                    buttonElement.textContent = article;
                    buttonElement.classList.add('book-button');
                    buttonElement.addEventListener('click', () => showContent('article', article));
                    listItem.appendChild(buttonElement);
                    articlesList.appendChild(listItem);
                }
            });
            if (articlesList.children.length === 0) {
                articlesList.innerHTML = '<li>No valid article/link pairs found</li>';
            }

            // Populate Books sidebar
            const booksList = document.querySelector('.books-list');
            booksList.innerHTML = '';
            booksData.forEach(row => {
                const book = row['Book']?.trim();
                if (book && contentElements[book]) {
                    const listItem = document.createElement('li');
                    const buttonElement = document.createElement('button');
                    buttonElement.textContent = book;
                    buttonElement.classList.add('book-button');
                    buttonElement.addEventListener('click', () => showContent('book', book));
                    listItem.appendChild(buttonElement);
                    booksList.appendChild(listItem);
                }
            });
            if (booksList.children.length === 0) {
                booksList.innerHTML = '<li>No valid book/link pairs found</li>';
            }

            // Show the first article or book if available
            if (articlesData.length > 0) {
                showContent('article', articlesData[0]['Articles']);
            } else if (booksData.length > 0) {
                showContent('book', booksData[0]['Book']);
            }

            // Add MutationObserver to reapply tooltips on DOM changes
            const observer = new MutationObserver(() => {
                console.log('DOM mutation detected, reinitializing tooltips');
                observer.disconnect(); // Prevent loop from own modifications
                highlightReferences(contentBody, tooltips);
                initializeTippy(contentBody);
                observer.observe(contentBody, { childList: true, subtree: true }); // Re-observe
            });
            observer.observe(contentBody, { childList: true, subtree: true });
        })
        .catch(error => {
            console.error('Error loading data:', error);
        });
});

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
    console.log('Showing content for:', title, 'DOM:', contentBody.innerHTML); // Debug DOM state
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
                console.warn('No data found for:', title);
                return;
            }

            const columns = Object.keys(data[0] || {}).filter(key => key.startsWith('D:'));
            if (columns.length === 0) {
                docContent.innerHTML = '<p class="error">No columns with "D:" found for ' + title + '.</p>';
                console.warn('No "D:" columns found for:', title);
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
        console.log('Content rendered for:', title, 'HTML:', docContent.innerHTML); // Debug rendered content
        highlightReferences(docContent, tooltips);
        initializeTippy(docContent);
    } catch (error) {
        console.error('Error loading content for ' + title + ':', error);
        docContent.innerHTML = '<p class="error">Failed to load data for ' + title + '. Please try again later.</p>';
    }
}

// Function to synchronize row heights across data containers
function synchronizeRowHeights(contentDiv) {
    const containers = contentDiv.querySelectorAll('.data-container');
    
    if (containers.length < 2) {
        containers.forEach(container => {
            const rows = container.querySelectorAll('.data-row');
            rows.forEach(row => {
                row.style.height = 'auto';
            });
        });
        return;
    }

    containers.forEach(container => {
        const rows = container.querySelectorAll('.data-row');
        rows.forEach(row => {
            row.style.height = 'auto';
        });
    });

    const maxHeights = [];
    containers.forEach(container => {
        const rows = container.querySelectorAll('.data-row');
        rows.forEach((row, index) => {
            const height = row.offsetHeight;
            maxHeights[index] = Math.max(maxHeights[index] || 0, height);
        });
    });

    containers.forEach(container => {
        const rows = container.querySelectorAll('.data-row');
        rows.forEach((row, index) => {
            row.style.height = `${maxHeights[index]}px`;
        });
    });
}

// Function to update plus and minus buttons (only on the rightmost data container)
function updateContainerButtons(contentDiv, data, columns, defaultColumn) {
    const containers = contentDiv.querySelectorAll('.data-container');
    containers.forEach(container => {
        const masterSelectContainer = container.querySelector('.master-select-container');
        const addButton = masterSelectContainer.querySelector('.add-container-button');
        const removeButton = masterSelectContainer.querySelector('.remove-container-button');
        if (addButton) addButton.remove();
        if (removeButton) removeButton.remove();
    });

    const rightmostContainer = containers[containers.length - 1];
    if (rightmostContainer) {
        const masterSelectContainer = rightmostContainer.querySelector('.master-select-container');
        const addButton = document.createElement('button');
        addButton.className = 'add-container-button';
        addButton.textContent = '+';
        addButton.addEventListener('click', () => {
            createDataContainer(data, columns, defaultColumn, contentDiv);
            synchronizeRowHeights(contentDiv);
        });

        const removeButton = document.createElement('button');
        removeButton.className = 'remove-container-button';
        removeButton.textContent = '−';
        removeButton.addEventListener('click', () => {
            rightmostContainer.remove();
            synchronizeRowHeights(contentDiv);
            updateContainerButtons(contentDiv, data, columns, defaultColumn);
        });

        masterSelectContainer.appendChild(addButton);
        masterSelectContainer.appendChild(removeButton);
    }
}

// Function to create a data container for CSV data (not used with preloading, kept for consistency)
function createDataContainer(data, columns, defaultColumn, contentDiv, tooltips) {
    const dataContainer = document.createElement('div');
    dataContainer.className = 'data-container';

    const masterSelectContainer = document.createElement('div');
    masterSelectContainer.className = 'master-select-container';

    const masterSelectLabel = document.createElement('label');
    masterSelectLabel.textContent = 'Select Column:';
    const masterSelect = document.createElement('select');
    masterSelect.className = 'master-select';

    columns.forEach(col => {
        const option = document.createElement('option');
        option.value = col;
        option.textContent = col;
        if (col === defaultColumn) option.selected = true;
        masterSelect.appendChild(option);
    });

    masterSelectContainer.appendChild(masterSelectLabel);
    masterSelectContainer.appendChild(masterSelect);

    dataContainer.appendChild(masterSelectContainer);

    data.forEach(row => {
        const dataRow = document.createElement('div');
        dataRow.className = 'data-row';
        const columnSelect = document.createElement('select');
        columnSelect.className = 'column-select';

        columns.forEach(col => {
            const option = document.createElement('option');
            option.value = col;
            option.textContent = col;
            if (col === defaultColumn) option.selected = true;
            columnSelect.appendChild(option);
        });

        const dataContent = document.createElement('div');
        dataContent.className = 'data-content';
        dataContent.innerHTML = (row[defaultColumn] || '').replace(/\n/g, '<br/>');

        columnSelect.addEventListener('change', () => {
            dataContent.innerHTML = (row[columnSelect.value] || '').replace(/\n/g, '<br/>');
            dataContent.classList.add('updated');
            setTimeout(() => dataContent.classList.remove('updated'), 1000);
            synchronizeRowHeights(contentDiv);
            initializeTippy(contentDiv.querySelector('.content-body')); // Reinitialize tooltips
        });

        masterSelect.addEventListener('change', () => {
            const rows = dataContainer.querySelectorAll('.data-row');
            rows.forEach((row, index) => {
                const select = row.querySelector('.column-select');
                const content = row.querySelector('.data-content');
                select.value = masterSelect.value;
                content.innerHTML = (data[index][masterSelect.value] || '').replace(/\n/g, '<br/>');
                content.classList.add('updated');
                setTimeout(() => dataContent.classList.remove('updated'), 1000);
            });
            synchronizeRowHeights(contentDiv);
            initializeTippy(contentDiv.querySelector('.content-body')); // Reinitialize tooltips
        });

        dataRow.appendChild(columnSelect);
        dataRow.appendChild(dataContent);
        dataContainer.appendChild(dataRow);
    });

    contentDiv.querySelector('.content-body').appendChild(dataContainer);
    updateContainerButtons(contentDiv, data, columns, defaultColumn);
    synchronizeRowHeights(contentDiv);
    initializeTippy(contentDiv.querySelector('.content-body')); // Initialize tooltips after adding container
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
    console.log('Found refs in container:', container, 'Count:', refs.length); // Debug: Check container and number of .ref elements
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
            console.log('Tippy attached for:', keyPhrase);
        }
    });
}

// Function to fetch and parse CSV data from a Google Sheet
function fetchGoogleSheetData(url) {
    console.log('Fetching URL:', url);
    return fetch(url)
        .then(response => {
            console.log('Response status:', response.status);
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(csvText => {
            console.log('CSV text:', csvText);
            return new Promise((resolve, reject) => {
                Papa.parse(csvText, {
                    header: true,
                    complete: function(results) {
                        console.log('Parsed CSV:', results.data);
                        resolve(results.data);
                    },
                    error: function(error) {
                        console.error('Papa Parse error:', error);
                        reject(error);
                    }
                });
            });
        })
        .catch(error => {
            console.error('Error fetching Google Sheet:', error);
            throw error;
        });
}