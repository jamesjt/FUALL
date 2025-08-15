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
                    buttonElement.classList.add('book-button'); // Add class for styling
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

// Function to fetch and display data from a linked Google Sheet
function loadBookData(link, bookName) {
    const contentDiv = document.querySelector('.content');
    contentDiv.innerHTML = '<p>Loading data for ' + bookName + '...</p>'; // Show loading state

    fetchGoogleSheetData(link)
        .then(data => {
            // Extract data from the "Original" column
            const originalData = data
                .map(row => row['Original']?.trim())
                .filter(data => data); // Remove undefined or empty entries

            if (originalData.length === 0) {
                contentDiv.innerHTML = '<p>No data found in the "Original" column for ' + bookName + '.</p>';
                console.warn('No data in "Original" column for:', bookName);
                return;
            }

            // Display the data as a list
            const list = document.createElement('ul');
            originalData.forEach(item => {
                const listItem = document.createElement('li');
                listItem.textContent = item;
                list.appendChild(listItem);
            });
            contentDiv.innerHTML = ''; // Clear loading state
            contentDiv.appendChild(list);
        })
        .catch(error => {
            console.error('Error loading data for ' + bookName + ':', error);
            contentDiv.innerHTML = '<p>Failed to load data for ' + bookName + '. Please try again later.</p>';
        });
}

// Reusable function to fetch and parse CSV data from a Google Sheet
function fetchGoogleSheetData(url) {
    console.log('Fetching URL:', url); // Debugging log
    return fetch(url)
        .then(response => {
            console.log('Response status:', response.status); // Debugging log
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(csvText => {
            console.log('CSV text:', csvText); // Debugging log
            return new Promise((resolve, reject) => {
                Papa.parse(csvText, {
                    header: true,
                    complete: function(results) {
                        console.log('Parsed CSV:', results.data); // Debugging log
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