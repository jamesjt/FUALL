// script.js

// URL of the published Google Sheet CSV (assumed to be "B: On Liberty")
const csvUrl = 'https://docs.google.com/spreadsheets/d/1g6d_uNrqofuyeOEVvtioW0wz2LrLtOpU8jsyfg8zgR0/pub?output=csv';

// Fetch and process the CSV data
fetch(csvUrl)
    .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.text();
    })
    .then(data => {
        // Parse CSV using PapaParse with headers
        const parsedData = Papa.parse(data, { header: true });
        const rows = parsedData.data;

        // Get the content container
        const contentContainer = document.querySelector('.content-container');
        contentContainer.innerHTML = ''; // Clear any existing content

        // Create a content row for each CSV row
        rows.forEach(row => {
            // Skip if row is empty or missing key columns
            if (!row || !row['Index'] || !row['D: Original']) return;

            // Create content-row div
            const contentRow = document.createElement('div');
            contentRow.classList.add('content-row');

            // Index div
            const indexDiv = document.createElement('div');
            indexDiv.classList.add('index');
            indexDiv.textContent = row['Index'];

            // Indicator div with round button
            const indicatorDiv = document.createElement('div');
            indicatorDiv.classList.add('indicator');
            const cycleButton = document.createElement('div');
            cycleButton.classList.add('cycle-button');
            indicatorDiv.appendChild(cycleButton);

            // Content div
            const contentDiv = document.createElement('div');
            contentDiv.classList.add('content');
            contentDiv.textContent = row['D: Original'];

            // Append child divs to content-row
            contentRow.appendChild(indexDiv);
            contentRow.appendChild(indicatorDiv);
            contentRow.appendChild(contentDiv);

            // Append content-row to content-container
            contentContainer.appendChild(contentRow);
        });
    })
    .catch(error => {
        console.error('Error fetching or processing CSV:', error);
    });
