const indexSheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?output=csv';

function loadIndexSheet() {
    Papa.parse(indexSheetUrl, {
        download: true,
        header: true,
        complete: function(results) {
            const sheets = results.data;
            const sheetList = document.getElementById('sheet-list');
            sheetList.innerHTML = ''; // Clear existing list

            sheets.forEach(sheet => {
                if (sheet.Name && sheet.URL) { // Assuming columns 'Name' and 'URL'
                    const li = document.createElement('li');
                    const a = document.createElement('a');
                    a.href = '#';
                    a.textContent = sheet.Name;
                    a.onclick = () => loadSheetData(sheet.URL, sheet.Name);
                    li.appendChild(a);
                    sheetList.appendChild(li);
                }
            });
        },
        error: function(error) {
            console.error('Error loading index sheet:', error);
            document.getElementById('content').innerHTML = 'Error loading sheet data.';
        }
    });
}

function loadSheetData(url, name) {
    Papa.parse(url, {
        download: true,
        header: true,
        complete: function(results) {
            const data = results.data;
            const content = document.getElementById('content');
            content.innerHTML = `<h2>${name}</h2>`;

            if (data.length === 0) {
                content.innerHTML += '<p>No data available.</p>';
                return;
            }

            // Create a table for the sheet data
            const table = document.createElement('table');
            table.border = '1';
            const thead = document.createElement('thead');
            const tbody = document.createElement('tbody');
            const headers = Object.keys(data[0]);

            // Create header row
            const headerRow = document.createElement('tr');
            headers.forEach(header => {
                const th = document.createElement('th');
                th.textContent = header;
                headerRow.appendChild(th);
            });
            thead.appendChild(headerRow);

            // Create data rows
            data.forEach(row => {
                const tr = document.createElement('tr');
                headers.forEach(header => {
                    const td = document.createElement('td');
                    td.textContent = row[header] || '';
                    tr.appendChild(td);
                });
                tbody.appendChild(tr);
            });

            table.appendChild(thead);
            table.appendChild(tbody);
            content.appendChild(table);
        },
        error: function(error) {
            console.error('Error loading sheet:', error);
            document.getElementById('content').innerHTML = 'Error loading sheet data.';
        }
    });
}

// Load the index sheet on page load
document.addEventListener('DOMContentLoaded', loadIndexSheet);