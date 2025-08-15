const indexSheetUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQO5WGpGvmUNEt4KdK6UFHq7Q9Q-L-p7pOho1u0afMoM0j-jpWdMGqD7VNm7Fp4e9ktcTZXFknLnfUL/pub?output=csv';

let map, markers, events = [], currentView = 'map', focusedEvent = null;

// Initialize the map
function initMap() {
    map = L.map('map', {
        zoomControl: true,
        zoomControlOptions: { position: 'bottomright' }
    }).setView([48.3794, 31.1656], 6);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    markers = L.markerClusterGroup({
        spiderfyOnMaxZoom: true,
        showCoverageOnHover: false,
        zoomToBoundsOnClick: true,
        maxClusterRadius: 40,
        disableClusteringAtZoom: 15
    });
    map.addLayer(markers);
}

// Load the index sheet to populate the sidebar
function loadIndexSheet() {
    Papa.parse(indexSheetUrl, {
        download: true,
        header: true,
        complete: function(results) {
            const sheets = results.data;
            const sheetList = document.getElementById('sheet-list');
            sheetList.innerHTML = '';

            sheets.forEach(sheet => {
                if (sheet.Name && sheet.URL) {
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

// Load and process data from the selected sheet
function loadSheetData(url, name) {
    document.getElementById('content').innerHTML = `<h2>${name}</h2>`;
    markers.clearLayers();
    events = [];

    Papa.parse(url, {
        download: true,
        header: true,
        complete: function(results) {
            console.log('Parsed CSV data:', results.data);
            events = results.data.map((row, index) => {
                const dateStr = row['Date-MDY']?.trim() || 'Unknown Date';
                const shortSummary = row['Short Summary - Date']?.trim() || 'No Short Summary';
                const summary = row['Summary - Date']?.trim() || 'No Summary';
                const blurb = row['Blurb']?.trim() || 'No Blurb';
                const locationStr = row['Location']?.trim() || '';
                const locationName = row['Location Name']?.trim() || '';
                const documentNames = row['Document Name']?.split(',').map(name => name.trim()) || [];
                const documentLinks = row['Document Link']?.split(',').map(link => link.trim()) || [];
                const linkNames = row['Link Name']?.split(',').map(name => name.trim()) || [];
                const links = row['Links']?.split(',').map(link => link.trim()) || [];
                const videoLinks = row['Video']?.split(',').map(link => link.trim()).filter(link => link) || [];
                const imageUrl = row['Image']?.trim() || '';
                const twitter = row['Twitter']?.trim() || '';
                const podcast = row['Podcast']?.trim() || '';
                const videoRaw = row['Video']?.trim() || '';
                const imageRaw = row['Image']?.trim() || '';
                const linksRaw = row['Links']?.trim() || '';
                const documentLinkRaw = row['Document Link']?.trim() || '';

                // Format date for graph view
                let formattedDate = dateStr;
                if (/^\d{1,2}\/\d{1,2}\/\d{4}$/.test(dateStr)) {
                    const [month, day, year] = dateStr.split('/').map(Number);
                    const fullMonths = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
                    const getOrdinal = (day) => {
                        if (day > 3 && day < 21) return `${day}th`;
                        switch (day % 10) {
                            case 1: return `${day}st`;
                            case 2: return `${day}nd`;
                            case 3: return `${day}rd`;
                            default: return `${day}th`;
                        }
                    };
                    formattedDate = `${fullMonths[month - 1]} ${getOrdinal(day)}, ${year}`;
                }

                // Format display date for list view
                let displayDate = dateStr;
                if (/^\d{1,2}\/\d{1,2}\/\d{4}$/.test(dateStr)) {
                    const [month, day, year] = dateStr.split('/').map(Number);
                    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
                    const getOrdinal = (day) => {
                        if (day > 3 && day < 21) return `${day}th`;
                        switch (day % 10) {
                            case 1: return `${day}st`;
                            case 2: return `${day}nd`;
                            case 3: return `${day}rd`;
                            default: return `${day}th`;
                        }
                    };
                    displayDate = `${months[month - 1]} ${getOrdinal(day)}`;
                }

                const validDocuments = [];
                for (let i = 0; i < Math.min(documentNames.length, documentLinks.length); i++) {
                    if (documentNames[i]?.trim() && documentLinks[i]?.trim()) {
                        validDocuments.push({ name: documentNames[i], link: documentLinks[i] });
                    }
                }

                const validLinks = [];
                for (let i = 0; i < Math.min(linkNames.length, links.length); i++) {
                    if (linkNames[i]?.trim() && links[i]?.trim()) {
                        validLinks.push({ name: linkNames[i], link: links[i] });
                    }
                }

                const videoEmbeds = videoLinks.map(link => {
                    if (link.includes('embed/')) {
                        return `<iframe width="100%" height="100%" src="${link}" frameborder="0" allowfullscreen></iframe>`;
                    } else if (link.includes('youtube.com') || link.includes('youtu.be')) {
                        const videoId = link.split('v=')[1]?.split('&')[0] || link.split('/').pop();
                        if (videoId) {
                            return `<iframe width="100%" height="100%" src="https://www.youtube.com/embed/${videoId}" frameborder="0" allowfullscreen></iframe>`;
                        }
                    }
                    return '';
                }).filter(embed => embed);

                let location = null, marker = null;
                if (locationStr) {
                    const [latStr, lonStr] = locationStr.split(',').map(coord => coord.trim());
                    const lat = parseFloat(latStr);
                    const lon = parseFloat(lonStr);
                    if (!isNaN(lat) && !isNaN(lon)) {
                        location = [lat, lon];
                        const numberedIcon = L.divIcon({
                            className: 'numbered-marker',
                            html: `<div>${index + 1}</div>`,
                            iconSize: [24, 24],
                            iconAnchor: [12, 12],
                            popupAnchor: [0, -12]
                        });

                        let popupContent = `
                            <div class="popup-text">
                                <span class="popup-event-date">${dateStr}</span><br>
                                <span class="popup-short-summary">${shortSummary}</span><br>
                                <span class="popup-blurb">${blurb}</span>
                            </div>
                        `;
                        if (imageUrl) popupContent += `<br><img src="${imageUrl}" class="clickable-image" alt="Event Image">`;
                        if (videoEmbeds.length > 0) {
                            popupContent += videoEmbeds.map(embed => `<div class="video-container">${embed}</div>`).join('');
                        }
                        if (validLinks.length > 0) {
                            popupContent += `<div class="popup-links">` + validLinks.map(linkObj => `
                                <div class="link-entry">
                                    <img src="icon-link.png" alt="Link">
                                    <a href="${linkObj.link}" target="_blank">${linkObj.name}</a>
                                </div>`).join('') + `</div>`;
                        }
                        if (validDocuments.length > 0) {
                            popupContent += `<div class="popup-documents">` + validDocuments.map(doc => `
                                <div class="document-link">
                                    <img src="icon-document.png" alt="Document">
                                    <a href="${doc.link}" target="_blank">${doc.name}</a>
                                </div>`).join('') + `</div>`;
                        }

                        marker = L.marker(location, { icon: numberedIcon });
                        marker.eventIndex = index;
                        marker.bindPopup(popupContent, { maxWidth: 320 });
                        marker.on('popupopen', () => setFocusedEvent(events[index]));
                        marker.on('popupclose', () => clearFocusedEvent());
                        markers.addLayer(marker);
                    }
                }

                const isValidDate = /^\d{1,2}\/\d{1,2}\/\d{4}$/.test(dateStr);
                return {
                    date: dateStr,
                    timestamp: isValidDate ? new Date(dateStr).getTime() : null,
                    shortSummary,
                    summary,
                    blurb,
                    location,
                    marker,
                    index,
                    summaryState: 0,
                    documentNames,
                    documentLinks,
                    videoEmbeds,
                    imageUrl,
                    validDocuments,
                    validLinks,
                    displayDate,
                    formattedDate,
                    locationName,
                    twitter,
                    podcast,
                    videoRaw,
                    imageRaw,
                    linksRaw,
                    documentLinkRaw
                };
            }).filter(event => event.timestamp);

            console.log('Processed events:', events);
            switchView(currentView); // Render the current view
            setupD3Timeline();
        },
        error: function(error) {
            console.error('Error loading sheet:', error);
            document.getElementById('content').innerHTML = 'Error loading sheet data.';
        }
    });
}

// Timeline setup
let svg, g, gX, eventGroup, circles, xScale, height = 120, margin = { top: 20, right: 20, bottom: 20, left: 20 };

function setupD3Timeline() {
    const timelineDiv = document.getElementById('graph-view');
    timelineDiv.innerHTML = '';

    svg = d3.select('#graph-view')
        .append('svg')
        .attr('height', height)
        .attr('width', '100%');

    g = svg.append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

    const minTime = d3.min(events, d => d.timestamp);
    const maxTime = d3.max(events, d => d.timestamp);
    const oneYearInMs = 365 * 24 * 60 * 60 * 1000;

    xScale = d3.scaleTime()
        .domain([new Date(minTime - oneYearInMs), new Date(maxTime + oneYearInMs)])
        .range([0, timelineDiv.clientWidth - margin.left - margin.right]);

    const xAxis = d3.axisBottom(xScale)
        .ticks(d3.timeYear.every(1))
        .tickFormat(d3.timeFormat('%Y'));

    const axisYPosition = (height - margin.top - margin.bottom) / 2;
    gX = g.append('g')
        .attr('class', 'axis axis--x')
        .attr('transform', `translate(0,${axisYPosition})`)
        .call(xAxis);

    eventGroup = g.append('g')
        .attr('class', 'event-group');

    circles = eventGroup.selectAll('.event-circle')
        .data(events)
        .enter()
        .append('circle')
        .attr('class', 'event-circle')
        .attr('cx', d => xScale(d.timestamp))
        .attr('cy', (d, i) => (i % 2 === 0 ? axisYPosition - 20 : axisYPosition + 30))
        .attr('r', 8)
        .attr('fill', d => d.location ? 'rgba(33, 150, 243, 0.7)' : 'rgba(76, 175, 80, 0.7)')
        .attr('stroke', d => d.location ? '#2196F3' : '#4CAF50')
        .attr('stroke-width', 2)
        .on('click', (event, d) => setFocusedEvent(d))
        .on('mouseover', function(event, d) {
            d3.select(this).transition().duration(200).attr('r', 10);
        })
        .on('mouseout', function() {
            d3.select(this).transition().duration(200).attr('r', 8);
        });
}

// Render list view
function renderListView() {
    const listView = document.getElementById('list-view');
    listView.innerHTML = '';

    if (!events || events.length === 0) {
        listView.innerHTML = 'No events available.';
        return;
    }

    events.forEach(event => {
        const eventEntry = document.createElement('div');
        eventEntry.className = 'event-entry';

        const eventHeader = document.createElement('div');
        eventHeader.className = 'event-header';
        eventHeader.innerHTML = `
            <span class="event-number">Event ${event.index + 1}: </span>
            <span class="event-summary">${event.shortSummary}</span>
        `;

        const eventDetails = document.createElement('div');
        eventDetails.className = 'event-details';
        const details = [
            { label: 'Video', data: event.videoRaw },
            { label: 'Image', data: event.imageRaw },
            { label: 'Links', data: event.linksRaw },
            { label: 'Document Link', data: event.documentLinkRaw }
        ];

        details.forEach(detail => {
            if (detail.data && detail.data.trim() !== '') {
                const detailElement = document.createElement('div');
                detailElement.className = 'event-detail';
                detailElement.textContent = `${detail.label}: ${detail.data}`;
                eventDetails.appendChild(detailElement);
            }
        });

        eventEntry.appendChild(eventHeader);
        if (eventDetails.children.length > 0) {
            eventEntry.appendChild(eventDetails);
        }
        listView.appendChild(eventEntry);
    });
}

// View switching logic
function switchView(view) {
    currentView = view;
    document.getElementById('map').style.display = 'none';
    document.getElementById('graph-view').style.display = 'none';
    document.getElementById('list-view').style.display = 'none';
    document.getElementById('content').style.display = 'none';

    document.querySelectorAll('.view-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelector(`.view-btn[data-view="${view}"]`).classList.add('active');

    if (view === 'map') {
        document.getElementById('map').style.display = 'block';
        setTimeout(() => map.invalidateSize(), 100);
    } else if (view === 'graph') {
        document.getElementById('graph-view').style.display = 'block';
        setupD3Timeline();
    } else if (view === 'list') {
        document.getElementById('list-view').style.display = 'block';
        renderListView();
    }
}

// Event focus handling
function setFocusedEvent(event) {
    focusedEvent = event;
    if (currentView === 'map' && event.marker) {
        const cluster = markers.getVisibleParent(event.marker);
        if (cluster && cluster !== event.marker) {
            cluster.spiderfy();
            setTimeout(() => event.marker.openPopup(), 300);
        } else {
            event.marker.openPopup();
        }
    } else if (currentView === 'graph') {
        // Implement graph view focus logic if needed
    }
}

function clearFocusedEvent() {
    focusedEvent = null;
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    initMap();
    loadIndexSheet();

    document.querySelector('.view-btn[data-view="map"]').addEventListener('click', () => switchView('map'));
    document.querySelector('.view-btn[data-view="graph"]').addEventListener('click', () => switchView('graph'));
    document.querySelector('.view-btn[data-view="list"]').addEventListener('click', () => switchView('list'));
});