document.addEventListener('DOMContentLoaded', () => {
    // Main Google Sheet URL for Books sheet (first tab, gid=0 by default)
    const booksSheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?output=csv';

    // Articles sheet URL (second tab, gid=464648636)
    const articlesSheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?gid=464648636&output=csv';

    // Fetch and populate Articles
    fetchGoogleSheetData(articlesSheetUrl)
        .then(data => {
            const articlesList = document.querySelector('.articles-list');
            articlesList.innerHTML = ''; // Clear existing list items

            if (data.length === 0) {
                articlesList.innerHTML = '<li>No data found in the Articles CSV</li>';
                console.warn('No data found in the Articles CSV');
                return;
            }

            data.forEach(row => {
                const article = row['Articles']?.trim(); // Changed from 'Article' to 'Articles'
                const link = row['Link']?.trim();

                if (article && link) {
                    const listItem = document.createElement('li');
                    const buttonElement = document.createElement('button');
                    buttonElement.textContent = article;
                    buttonElement.classList.add('book-button'); // Reuse style for consistency
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
            booksList.innerHTML = ''; // Clear existing list items

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
    
    // If only one container, reset row heights to auto
    if (containers.length < 2) {
        containers.forEach(container => {
            const rows = container.querySelectorAll('.data-row');
            rows.forEach(row => {
                row.style.height = 'auto';
            });
        });
        return;
    }

    // Reset heights to measure natural height
    containers.forEach(container => {
        const rows = container.querySelectorAll('.data-row');
        rows.forEach(row => {
            row.style.height = 'auto';
        });
    });

    // Find maximum height for each row index
    const maxHeights = [];
    containers.forEach(container => {
        const rows = container.querySelectorAll('.data-row');
        rows.forEach((row, index) => {
            const height = row.offsetHeight;
            maxHeights[index] = Math.max(maxHeights[index] || 0, height);
        });
    });

    // Apply maximum height to each row
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

        // Add plus button
        const addButton = document.createElement('button');
        addButton.textContent = '+';
        addButton.classList.add('add-container-button');
        addButton.setAttribute('aria-label', 'Add new data column');
        addButton.addEventListener('click', () => {
            createDataContainer(data, columns, defaultColumn, contentDiv);
            synchronizeRowHeights(contentDiv);
        });
        masterSelectContainer.appendChild(addButton);

        // Add minus button only if there are at least two containers
        if (containers.length > 1) {
            const removeButton = document.createElement('button');
            removeButton.textContent = '−';
            removeButton.classList.add('remove-container-button');
            removeButton.setAttribute('aria-label', 'Remove data column');
            removeButton.addEventListener('click', () => {
                rightmostContainer.remove();
                updateContainerButtons(contentDiv, data, columns, defaultColumn);
                synchronizeRowHeights(contentDiv);
            });
            masterSelectContainer.appendChild(removeButton);
        }
    }

    synchronizeRowHeights(contentDiv);
}

// Function to create a data container with dropdowns and data rows
function createDataContainer(data, columns, defaultColumn, contentDiv) {
    const dataContainer = document.createElement('div');
    dataContainer.classList.add('data-container');

    // Create master dropdown
    const masterSelectContainer = document.createElement('div');
    masterSelectContainer.classList.add('master-select-container');
    const masterLabel = document.createElement('label');
    masterLabel.textContent = 'Set All Data: ';
    masterLabel.setAttribute('for', `master-select-${Date.now()}`); // Unique ID
    const masterSelect = document.createElement('select');
    masterSelect.id = `master-select-${Date.now()}`; // Unique ID to avoid conflicts
    masterSelect.classList.add('master-select');
    columns.forEach(column => {
        const option = document.createElement('option');
        option.value = column;
        option.textContent = column.replace(/^D:\s*/, ''); // Remove "D:" for display
        if (column === defaultColumn) {
            option.selected = true;
        }
        masterSelect.appendChild(option);
    });

    // Add event listener to master dropdown to update all row dropdowns
    masterSelect.addEventListener('change', () => {
        const rowSelects = dataContainer.querySelectorAll('.column-select');
        rowSelects.forEach(select => {
            select.value = masterSelect.value;
            select.dispatchEvent(new Event('change')); // Trigger update of data-content
        });
        synchronizeRowHeights(contentDiv);
    });

    masterSelectContainer.appendChild(masterLabel);
    masterSelectContainer.appendChild(masterSelect);
    dataContainer.appendChild(masterSelectContainer);

    // Create a row for each data entry
    data.forEach((row, index) => {
        if (Object.values(row).some(value => value?.trim())) { // Skip empty rows
            const rowDiv = document.createElement('div');
            rowDiv.classList.add('data-row');

            // Create dropdown for selecting "D:" columns
            const select = document.createElement('select');
            select.classList.add('column-select');
            columns.forEach(column => {
                const option = document.createElement('option');
                option.value = column;
                option.textContent = column.replace(/^D:\s*/, ''); // Remove "D:" for display
                if (column === defaultColumn) {
                    option.selected = true;
                }
                select.appendChild(option);
            });

            // Create div for displaying data
            const dataDiv = document.createElement('div');
            dataDiv.classList.add('data-content');
            dataDiv.textContent = row[defaultColumn]?.trim() || '.';

            // Update data when dropdown changes
            select.addEventListener('change', () => {
                dataDiv.textContent = row[select.value]?.trim() || '.';
                dataDiv.classList.add('updated');
                setTimeout(() => dataDiv.classList.remove('updated'), 500);
                synchronizeRowHeights(contentDiv);
            });

            rowDiv.appendChild(select);
            rowDiv.appendChild(dataDiv);
            dataContainer.appendChild(rowDiv);
        }
    });

    contentDiv.appendChild(dataContainer);
    updateContainerButtons(contentDiv, data, columns, defaultColumn);
}

// Function to load article data (handles both Google Docs and Sheets)
async function loadArticleData(link, articleName) {
    const contentDiv = document.querySelector('.content');
    contentDiv.innerHTML = '<p class="loading">Loading data for ' + articleName + '...</p>'; // Show loading state

    try {
        if (link.includes('document')) {
            // Handle Google Doc: Fetch as HTML to maintain formatting and links
            const htmlLink = link.replace('/edit', '/export?format=html');
            const response = await fetch(htmlLink);
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const htmlText = await response.text();
            // Create a temporary container to extract the body content
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = htmlText;
            const bodyContent = tempDiv.querySelector('body')?.innerHTML || htmlText;
            contentDiv.innerHTML = '<div class="doc-content">' + bodyContent + '</div>';
        } else if (link.includes('spreadsheets')) {
            // Handle Google Sheet: Fetch as CSV and display with dropdowns
            const csvLink = link.replace('/edit', '/pub?output=csv');
            loadCsvData(csvLink, articleName);
        } else {
            contentDiv.innerHTML = '<p class="error">Unsupported link type for ' + articleName + '.</p>';
            console.warn('Unsupported link type for:', articleName);
        }
    } catch (error) {
        console.error('Error loading article data for ' + articleName + ':', error);
        contentDiv.innerHTML = '<p class="error">Failed to load data for ' + articleName + '. Please try again later.</p>';
    }
}

// Function to load CSV data (for Sheets and Books)
function loadCsvData(link, name) {
    const contentDiv = document.querySelector('.content');
    contentDiv.innerHTML = '<p class="loading">Loading data for ' + name + '...</p>'; // Show loading state

    fetchGoogleSheetData(link)
        .then(data => {
            // Get columns with headers containing "D:"
            const columns = Object.keys(data[0] || {}).filter(key => key.startsWith('D:'));
            if (columns.length === 0) {
                contentDiv.innerHTML = '<p class="error">No columns with "D:" found for ' + name + '.</p>';
                console.warn('No "D:" columns found for:', name);
                return;
            }

            // Set default column to "D: Original" or the first "D:" column
            const defaultColumn = columns.includes('D: Original') ? 'D: Original' : columns[0];

            // Clear existing content and create the first data container
            contentDiv.innerHTML = '';
            createDataContainer(data, columns, defaultColumn, contentDiv);

            if (contentDiv.querySelectorAll('.data-row').length === 0) {
                contentDiv.innerHTML = '<p class="error">No valid data found for ' + name + '.</p>';
                console.warn('No valid data for:', name);
                return;
            }
        })
        .catch(error => {
            console.error('Error loading CSV data for ' + name + ':', error);
            contentDiv.innerHTML = '<p class="error">Failed to load data for ' + name + '. Please try again later.</p>';
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