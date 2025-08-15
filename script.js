document.addEventListener('DOMContentLoaded', () => {
    const proxyUrl = 'https://cors-anywhere.herokuapp.com/';
    const sheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?output=csv';

    fetchGoogleSheetData(proxyUrl + sheetUrl)
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
                    const bookElement = document.createElement('span');
                    bookElement.textContent = book;
                    bookElement.style.cursor = 'pointer';
                    bookElement.style.color = '#333';
                    bookElement.style.fontSize = '1.1em';
                    bookElement.addEventListener('mouseover', () => {
                        bookElement.style.color = '#007bff';
                    });
                    bookElement.addEventListener('mouseout', () => {
                        bookElement.style.color = '#333';
                    });
                    bookElement.addEventListener('click', () => {
                        const bookContent = document.querySelector('.book-content');
                        bookContent.innerHTML = '<p>Loading...</p>';

                        fetchGoogleSheetData(proxyUrl + link)
                            .then(linkedData => {
                                if (linkedData.length === 0) {
                                    bookContent.innerHTML = '<p>No data found in the linked CSV</p>';
                                    return;
                                }

                                const originalData = linkedData
                                    .map(row => row['Original']?.trim())
                                    .filter(text => text)
                                    .join('<br>');

                                if (originalData) {
                                    bookContent.innerHTML = `<p>${originalData}</p>`;
                                } else {
                                    bookContent.innerHTML = '<p>No "Original" column data found</p>';
                                }
                            })
                            .catch(error => {
                                console.error('Error fetching linked CSV:', error);
                                bookContent.innerHTML = `<p>Error loading data: ${error.message}</p>`;
                            });
                    });

                    listItem.appendChild(bookElement);
                    sidebarList.appendChild(listItem);
                }
            });

            if (sidebarList.children.length === 0) {
                sidebarList.innerHTML = '<li>No valid book/link pairs found</li>';
            }
        })
        .catch(error => {
            console.error('Error processing main CSV:', error);
            const sidebarList = document.querySelector('.sidebar ul');
            sidebarList.innerHTML = `<li>Error loading book data: ${error.message}</li>`;
        });
});

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
            console.error('Error fetching Google Sheet:', error);
            throw error;
        });
}