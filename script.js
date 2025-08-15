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