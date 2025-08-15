function fetchGoogleSheetData() {
    const sheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?output=csv';
    return fetch(sheetUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
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

document.addEventListener('DOMContentLoaded', () => {
    fetchGoogleSheetData()
        .then(data => {
            // Find 'Book' and 'Link' columns in the header
            if (data.length === 0) {
                console.error('No data found in the CSV');
                return;
            }

            const sidebarList = document.querySelector('.sidebar ul');
            sidebarList.innerHTML = ''; // Clear existing list items

            data.forEach(row => {
                const book = row['Book']?.trim();
                const link = row['Link']?.trim();

                if (book && link) {
                    const listItem = document.createElement('li');
                    const linkElement = document.createElement('a');
                    linkElement.href = link;
                    linkElement.textContent = book;
                    linkElement.target = '_blank'; // Open links in a new tab
                    listItem.appendChild(linkElement);
                    sidebarList.appendChild(listItem);
                }
            });
        })
        .catch(error => {
            console.error('Error processing CSV data:', error);
            const sidebarList = document.querySelector('.sidebar ul');
            sidebarList.innerHTML = '<li>Error loading book data</li>';
        });
});