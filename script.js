// script.js

// URL of the published Google Sheet CSV with CORS proxy
const csvUrl = 'https://cors-anywhere.herokuapp.com/https://docs.google.com/spreadsheets/d/e/2PACX-1vRdBGxonsMp06IcXX2nEbJmbtA4vYeVIRgPxwdGMtArWLMsuVZeJakOWpyub_pn-IcIkes2PTRJ6xw7/pub?gid=1556566616&single=true&output=csv';

// Fetch and process the CSV data with custom header
fetch(csvUrl, {
    method: 'GET',
    headers: {
        'X-Requested-With': 'XMLHttpRequest'
    }
})
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.statusText);
        }
        return response.text();
    })
    .then(data => {
        // Parse CSV using PapaParse with headers
        const parsedData = Papa.parse(data, { header: true });
        const rows = parsedData.data;

        // Get the content container
        const contentContainer = document.querySelector('.content-container');
        if (!contentContainer) {
            throw new Error('Content container not found in the DOM');
        }
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
