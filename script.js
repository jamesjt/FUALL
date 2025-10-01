document.addEventListener('DOMContentLoaded', () => {
    // Articles sheet URL
    const articlesSheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?gid=464648636&output=csv';

    // Books sheet URL
    const booksSheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?output=csv';

    // Fetch and populate Articles
    fetchGoogleSheetData(articlesSheetUrl)
        .then(data => {
            const articlesList = document.querySelector('.articles-list');
            articlesList.innerHTML = '';

            if (data.length === 0) {
                articlesList.innerHTML = '<li>No data found in the Articles CSV</li>';
                console.warn('No data found in the Articles CSV');
                return;
            }

            data.forEach(row => {
                const article = row['Articles']?.trim();
                const link = row['Link']?.trim();

                if (article && link) {
                    const listItem = document.createElement('li');
                    const buttonElement = document.createElement('button');
                    buttonElement.textContent = article;
                    buttonElement.classList.add('book-button');
                    buttonElement.addEventListener('click', () => {
                        loadArticleData(link, article);
                    });
                    listItem.appendChild(buttonElement);
                    articlesList.appendChild(listItem);
                }
            });

            if (articlesList.children.length === 0) {
                articlesList.innerHTML = '<li>No valid article/link pairs found</li>';
            }
        })
        .catch(error => {
            console.error('Error processing Articles CSV data:', error);
            const articlesList = document.querySelector('.articles-list');
            articlesList.innerHTML = '<li>Failed to load article data. Please try again later.</li>';
        });

    // Fetch and populate Books
    fetchGoogleSheetData(booksSheetUrl)
        .then(data => {
            const booksList = document.querySelector('.books-list');
            booksList.innerHTML = '';

            if (data.length === 0) {
                booksList.innerHTML = '<li>No data found in the Books CSV</li>';
                console.warn('No data found in the Books CSV');
                return;
            }

            data.forEach(row => {
                const book = row['Book']?.trim();
                const link = row['Link']?.trim();

                if (book && link) {
                    const listItem = document.createElement('li');
                    const buttonElement = document.createElement('button');
                    buttonElement.textContent = book;
                    buttonElement.classList.add('book-button');
                    buttonElement.addEventListener('click', () => {
                        loadCsvData(link, book);
                    });
                    listItem.appendChild(buttonElement);
                    booksList.appendChild(listItem);
                }
            });

            if (booksList.children.length === 0) {
                booksList.innerHTML = '<li>No valid book/link pairs found</li>';
            }
        })
        .catch(error => {
            console.error('Error processing Books CSV data:', error);
            const booksList = document.querySelector('.books-list');
            booksList.innerHTML = '<li>Failed to load book data. Please try again later.</li>';
        });
});

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

// Function to create a data container for CSV data
function createDataContainer(data, columns, defaultColumn, contentDiv) {
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
        dataContent.textContent = row[defaultColumn] || '';

        columnSelect.addEventListener('change', () => {
            dataContent.textContent = row[columnSelect.value] || '';
            dataContent.classList.add('updated');
            setTimeout(() => dataContent.classList.remove('updated'), 1000);
            synchronizeRowHeights(contentDiv);
        });

        masterSelect.addEventListener('change', () => {
            const rows = dataContainer.querySelectorAll('.data-row');
            rows.forEach((row, index) => {
                const select = row.querySelector('.column-select');
                const content = row.querySelector('.data-content');
                select.value = masterSelect.value;
                content.textContent = data[index][masterSelect.value] || '';
                content.classList.add('updated');
                setTimeout(() => dataContent.classList.remove('updated'), 1000);
            });
            synchronizeRowHeights(contentDiv);
        });

        dataRow.appendChild(columnSelect);
        dataRow.appendChild(dataContent);
        dataContainer.appendChild(dataRow);
    });

    contentDiv.querySelector('.content-body').appendChild(dataContainer);
    updateContainerButtons(contentDiv, data, columns, defaultColumn);
    synchronizeRowHeights(contentDiv);
}

// Function to load article data (HTML or CSV)
async function loadArticleData(link, articleName) {
    const contentDiv = document.querySelector('.content');
    const tabsDiv = contentDiv.querySelector('.tabs');
    const contentBody = contentDiv.querySelector('.content-body');

    // Debug: Log DOM elements
    console.log('contentDiv:', contentDiv);
    console.log('tabsDiv:', tabsDiv);
    console.log('contentBody:', contentBody);

    if (!contentBody) {
        console.error('Error: .content-body element not found in the DOM');
        contentDiv.innerHTML = '<p class="error">Error: Content area not found. Please check the HTML structure.</p>';
        return;
    }

    contentBody.innerHTML = '<p class="loading">Loading data for ' + articleName + '...</p>';

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
                if (bannersDiv) {
                    bannersDiv.remove();
                }
                const elements = bodyContent.querySelectorAll('p, div, span, footer, header');
                elements.forEach(element => {
                    const text = element.textContent.toLowerCase();
                    if (
                        text.includes('published by google') ||
                        text.includes(articleName.toLowerCase()) ||
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
                        if (children[0].textContent.trim().length < 50) {
                            children[0].remove();
                        }
                    }
                    if (children.length > 0 && (children[children.length - 1].tagName.toLowerCase() === 'div' || children[children.length - 1].tagName.toLowerCase() === 'p')) {
                        if (children[children.length - 1].textContent.trim().length < 50) {
                            children[children.length - 1].remove();
                        }
                    }
                }
                tabsDiv.innerHTML = ''; // Clear tabs for Google Docs
                contentBody.innerHTML = '<div class="doc-content">' + bodyContent.innerHTML + '</div>';
            } else {
                const fallbackDiv = document.createElement('div');
                fallbackDiv.innerHTML = htmlText;
                fallbackDiv.querySelectorAll('style').forEach(style => style.remove());
                fallbackDiv.querySelectorAll('#banners').forEach(banner => banner.remove());
                tabsDiv.innerHTML = ''; // Clear tabs for Google Docs
                contentBody.innerHTML = '<div class="doc-content">' + fallbackDiv.innerHTML + '</div>';
            }
        } else if (link.includes('spreadsheets')) {
            const csvLink = link.replace('/edit', '/pub?output=csv');
            fetchGoogleSheetData(csvLink)
                .then(data => {
                    if (!data || data.length === 0) {
                        contentBody.innerHTML = '<p class="error">No data found for ' + articleName + '.</p>';
                        console.warn('No data found for:', articleName);
                        return;
                    }

                    const columns = Object.keys(data[0] || {}).filter(key => key.startsWith('D:'));
                    if (columns.length === 0) {
                        contentBody.innerHTML = '<p class="error">No columns with "D:" found for ' + articleName + '.</p>';
                        console.warn('No "D:" columns found for:', articleName);
                        return;
                    }

                    tabsDiv.innerHTML = ''; // Clear main tabs
                    contentBody.innerHTML = '';

                    // Create a row container for each CSV row
                    data.forEach((row, rowIndex) => {
                        const rowContainer = document.createElement('div');
                        rowContainer.className = 'row-container';

                        let rowTabs = null;
                        if (columns.length > 1) {
                            // Only create tabs if there are multiple D: columns
                            rowTabs = document.createElement('div');
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
                                    const rowContent = rowContainer.querySelector('.row-content');
                                    rowContent.innerHTML = row[col] || '';
                                });
                                rowTabs.appendChild(tab);
                            });

                            // Set first tab as active
                            rowTabs.querySelector('.tab').classList.add('active');
                        }

                        const rowContent = document.createElement('div');
                        rowContent.className = 'row-content';
                        rowContent.innerHTML = row[columns[0]] || ''; // Default to first D: column

                        if (rowTabs) {
                            rowContainer.appendChild(rowTabs);
                        }
                        rowContainer.appendChild(rowContent);
                        contentBody.appendChild(rowContainer);
                    });
                })
                .catch(error => {
                    console.error('Error loading CSV data for ' + articleName + ':', error);
                    contentBody.innerHTML = '<p class="error">Failed to load data for ' + articleName + '. Please try again later.</p>';
                });
        } else {
            contentBody.innerHTML = '<p class="error">Unsupported link type for ' + articleName + '.</p>';
            console.warn('Unsupported link type for:', articleName);
        }
    } catch (error) {
        console.error('Error loading article data for ' + articleName + ':', error);
        contentBody.innerHTML = '<p class="error">Failed to load data for ' + articleName + '. Please try again later.</p>';
    }
}

// Function to load CSV data (for Books)
function loadCsvData(link, name) {
    const contentDiv = document.querySelector('.content');
    const contentBody = contentDiv.querySelector('.content-body');

    // Debug: Log DOM elements
    console.log('contentDiv:', contentDiv);
    console.log('contentBody:', contentBody);

    if (!contentBody) {
        console.error('Error: .content-body element not found in the DOM');
        contentDiv.innerHTML = '<p class="error">Error: Content area not found. Please check the HTML structure.</p>';
        return;
    }

    contentBody.innerHTML = '<p class="loading">Loading data for ' + name + '...</p>';

    fetchGoogleSheetData(link)
        .then(data => {
            const columns = Object.keys(data[0] || {}).filter(key => key.startsWith('D:'));
            if (columns.length === 0) {
                contentBody.innerHTML = '<p class="error">No columns with "D:" found for ' + name + '.</p>';
                console.warn('No "D:" columns found for:', name);
                return;
            }

            const defaultColumn = columns.includes('D: Original') ? 'D: Original' : columns[0];
            contentDiv.querySelector('.tabs').innerHTML = ''; // Clear tabs for Books
            contentBody.innerHTML = '';
            createDataContainer(data, columns, defaultColumn, contentDiv);
        })
        .catch(error => {
            console.error('Error loading CSV data for ' + name + ':', error);
            contentBody.innerHTML = '<p class="error">Failed to load data for ' + name + '. Please try again later.</p>';
        });
}

// Reusable function to fetch and parse CSV data from a Google Sheet
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