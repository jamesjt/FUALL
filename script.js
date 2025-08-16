document.addEventListener('DOMContentLoaded', () => {
    // Main Google Sheet URL (ensure it is published and publicly accessible)
    const sheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?output=csv';

    fetchGoogleSheetData(sheetUrl)
        .then(data => {
            const sidebarList = document.querySelector('.sidebar ul');
            sidebarList.innerHTML = ''; // Clear existing list items

            if (data.length === 0) {
                sidebarList.innerHTML = '<li>No data found in the CSV</li>';
                console.warn('No data found in the CSV');
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
                        loadBookData(link, book);
                    });
                    listItem.appendChild(buttonElement);
                    sidebarList.appendChild(listItem);
                }
            });

            if (sidebarList.children.length === 0) {
                sidebarList.innerHTML = '<li>No valid book/link pairs found</li>';
            }
        })
        .catch(error => {
            console.error('Error processing main CSV data:', error);
            const sidebarList = document.querySelector('.sidebar ul');
            sidebarList.innerHTML = '<li>Failed to load book data. Please try again later.</li>';
        });
});

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
    });

    masterSelectContainer.appendChild(masterLabel);
    masterSelectContainer.appendChild(masterSelect);

    // Add plus button to the first master-select-container
    if (contentDiv.querySelectorAll('.data-container').length === 0) {
        const addButton = document.createElement('button');
        addButton.textContent = '+';
        addButton.classList.add('add-container-button');
        addButton.setAttribute('aria-label', 'Add new data column');
        addButton.addEventListener('click', () => {
            createDataContainer(data, columns, defaultColumn, contentDiv);
        });
        masterSelectContainer.appendChild(addButton);
    }

    // Add minus button to remove this data container (if not the last one)
    const removeButton = document.createElement('button');
    removeButton.textContent = '−';
    removeButton.classList.add('remove-container-button');
    removeButton.setAttribute('aria-label', 'Remove data column');
    removeButton.addEventListener('click', () => {
        if (contentDiv.querySelectorAll('.data-container').length > 1) {
            dataContainer.remove();
        }
    });
    masterSelectContainer.appendChild(removeButton);

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
            dataDiv.textContent = row[defaultColumn]?.trim() || 'No data';

            // Update data when dropdown changes
            select.addEventListener('change', () => {
                dataDiv.textContent = row[select.value]?.trim() || 'No data';
                dataDiv.classList.add('updated');
                setTimeout(() => dataDiv.classList.remove('updated'), 500);
            });

            rowDiv.appendChild(select);
            rowDiv.appendChild(dataDiv);
            dataContainer.appendChild(rowDiv);
        }
    });

    contentDiv.appendChild(dataContainer);
}

// Function to fetch and display data from a linked Google Sheet
function loadBookData(link, bookName) {
    const contentDiv = document.querySelector('.content');
    contentDiv.innerHTML = '<p class="loading">Loading data for ' + bookName + '...</p>'; // Show loading state

    fetchGoogleSheetData(link)
        .then(data => {
            // Get columns with headers containing "D:"
            const columns = Object.keys(data[0] || {}).filter(key => key.startsWith('D:'));
            if (columns.length === 0) {
                contentDiv.innerHTML = '<p class="error">No columns with "D:" found for ' + bookName + '.</p>';
                console.warn('No "D:" columns found for:', bookName);
                return;
            }

            // Set default column to "D: Original" or the first "D:" column
            const defaultColumn = columns.includes('D: Original') ? 'D: Original' : columns[0];

            // Clear existing content and create the first data container
            contentDiv.innerHTML = '';
            createDataContainer(data, columns, defaultColumn, contentDiv);

            if (contentDiv.querySelectorAll('.data-row').length === 0) {
                contentDiv.innerHTML = '<p class="error">No valid data found for ' + bookName + '.</p>';
                console.warn('No valid data for:', bookName);
                return;
            }
        })
        .catch(error => {
            console.error('Error loading data for ' + bookName + ':', error);
            contentDiv.innerHTML = '<p class="error">Failed to load data for ' + bookName + '. Please try again later.</p>';
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