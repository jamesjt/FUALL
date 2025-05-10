// Hardcoded tree data (unchanged)
const treeData = {
    label: 'Wisdom',
    category: 'root',
    content: {
        sentence: 'The foundation of all understanding.',
        paragraph: 'Wisdom is the ability to think and act using knowledge, experience, understanding, common sense, and insight.',
        essay: '<p>Wisdom is often considered the pinnacle of human understanding, integrating knowledge from various domains. <img src="https://via.placeholder.com/150" alt="wisdom image"></p>'
    },
    children: [
        {
            label: 'Reality',
            category: 'reality',
            content: {
                sentence: 'The state of things as they actually exist.',
                paragraph: 'Reality encompasses the physical world, our perceptions, and the underlying truths of existence.',
                essay: '<p>Reality is the sum or aggregate of all that is real or existent within a system. <video controls src="https://www.w3schools.com/html/mov_bbb.mp4"></video></p>'
            },
            children: []
        },
        {
            label: 'Reason',
            category: 'reason',
            content: {
                sentence: 'The power of the mind to think, understand, and form judgments logically.',
                paragraph: 'Reason is the capacity for consciously making sense of things, applying logic, and adapting or justifying practices, institutions, and beliefs based on new or existing information.',
                essay: '<p>Reason is a fundamental aspect of human cognition, allowing us to process information and make decisions. <img src="https://via.placeholder.com/150" alt="reason image"></p>'
            },
            children: []
        },
        {
            label: 'Right',
            category: 'right',
            content: {
                sentence: 'Moral or legal entitlement to have or do something.',
                paragraph: 'Rights are legal, social, or ethical principles of freedom or entitlement; that is, rights are the fundamental normative rules about what is allowed of people or owed to people.',
                essay: '<p>The concept of rights is central to discussions of justice, democracy, and the rule of law. <video controls src="https://www.w3schools.com/html/mov_bbb.mp4"></video></p>'
            },
            children: []
        }
    ]
};

// Declare sheetData to store fetched data
let sheetData = { tabs: [] };

// Fetch data from Google Sheet using PapaParse
async function fetchSheetData() {
    // Replace with your actual Google Sheet ID
    const spreadsheetId = '1g6d_uNrqofuyeOEVvtioW0wz2LrLtOpU8jsyfg8zgR0';
    // Replace with actual tab names starting with "B:" from your sheet
    const bookTabs = ['B:Book1', 'B:Book2']; // Example; update with your tab names

    const fetchTab = (tab) => new Promise((resolve, reject) => {
        const url = `https://docs.google.com/spreadsheets/d/${spreadsheetId}/gviz/tq?tqx=out:csv&sheet=${encodeURIComponent(tab)}`;
        Papa.parse(url, {
            download: true,
            header: true, // Assumes first row is headers: title, author, content
            complete: function(results) {
                if (results.errors.length > 0) {
                    reject(results.errors);
                } else {
                    resolve({ name: tab, data: results.data });
                }
            },
            error: function(error) {
                reject(error);
            }
        });
    });

    try {
        const tabsData = await Promise.all(bookTabs.map(fetchTab));
        sheetData.tabs = tabsData;
        populateSidebar();
        populateLibrary();
        populateSimple();
    } catch (error) {
        console.error('Error fetching sheet data:', error);
        // Optional: Add UI feedback, e.g., "Failed to load data"
    }
}

// Populate sidebar with book links
function populateSidebar() {
    const bookList = document.getElementById('book-list');
    bookList.innerHTML = '';
    sheetData.tabs.forEach(tab => {
        if (tab.name.startsWith('B:')) {
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = `#${tab.name}`;
            a.textContent = tab.name.replace('B:', '');
            a.addEventListener('click', () => showBookContent(tab));
            li.appendChild(a);
            bookList.appendChild(li);
        }
    });
}

// Populate Library view with all books
function populateLibrary() {
    const libraryContent = document.getElementById('library-content');
    libraryContent.innerHTML = '';
    sheetData.tabs.forEach(tab => {
        if (tab.name.startsWith('B:')) {
            const section = document.createElement('div');
            section.innerHTML = `<h3>${tab.name.replace('B:', '')}</h3>`;
            tab.data.forEach(book => {
                section.innerHTML += `<p><strong>${book.title}</strong> by ${book.author}: ${book.content}</p>`;
            });
            libraryContent.appendChild(section);
        }
    });
}

// Populate Simple view with book titles
function populateSimple() {
    const simpleContent = document.getElementById('simple-content');
    simpleContent.innerHTML = '<h3>Book Titles</h3><ul>';
    sheetData.tabs.forEach(tab => {
        if (tab.name.startsWith('B:')) {
            tab.data.forEach(book => {
                simpleContent.innerHTML += `<li>${book.title}</li>`;
            });
        }
    });
    simpleContent.innerHTML += '</ul>';
}

// Show specific book content in Library view
function showBookContent(tab) {
    const libraryContent = document.getElementById('library-content');
    libraryContent.innerHTML = `<h3>${tab.name.replace('B:', '')}</h3>`;
    tab.data.forEach(book => {
        libraryContent.innerHTML += `<p><strong>${book.title}</strong> by ${book.author}: ${book.content}</p>`;
    });
    switchView('library');
}

// Switch between views
function switchView(view) {
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
    document.getElementById(`${view}-view`).classList.add('active');
}

// Navbar click handlers
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const view = e.target.dataset.view;
        switchView(view);
    });
});

// Tree visualization (unchanged)
const canvas = document.getElementById('treeCanvas');
const ctx = canvas.getContext('2d');
let currentScale = 1;
let currentTranslateX = 0;
let currentTranslateY = 0;
let filteredTree = treeData;

assignPositions(filteredTree, 400, 300, 200, 100);

function assignPositions(node, x, y, dx, dy, parent = null) {
    node.x = x;
    node.y = y;
    node.parent = parent;
    const numChildren = node.children.length;
    if (numChildren > 0) {
        const startX = x - (numChildren - 1) * dx / 2;
        for (let i = 0; i < numChildren; i++) {
            assignPositions(node.children[i], startX + i * dx, y - dy, dx / 2, dy, node);
        }
    }
}

function drawTree(node) {
    if (node.parent) {
        ctx.beginPath();
        ctx.moveTo(node.parent.x, node.parent.y);
        ctx.lineTo(node.x, node.y);
        ctx.stroke();
    }
    ctx.beginPath();
    ctx.arc(node.x, node.y, 10 / currentScale, 0, Math.PI * 2);
    ctx.stroke();
    ctx.fillText(node.label, node.x + 15 / currentScale, node.y);
    for (let child of node.children) {
        drawTree(child);
    }
}

function redraw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.save();
    ctx.translate(currentTranslateX, currentTranslateY);
    ctx.scale(currentScale, currentScale);
    drawTree(filteredTree);
    ctx.restore();
}

function getFilteredTree(filter) {
    if (filter === 'all') {
        return treeData;
    } else {
        const filteredChildren = treeData.children.filter(child => child.category === filter);
        return { ...treeData, children: filteredChildren };
    }
}

document.getElementById('filter').addEventListener('change', (e) => {
    const filter = e.target.value;
    filteredTree = getFilteredTree(filter);
    assignPositions(filteredTree, 400, 300, 200, 100);
    redraw();
});

let isPanning = false;
let startX, startY;
canvas.addEventListener('mousedown', (e) => {
    isPanning = true;
    startX = e.clientX;
    startY = e.clientY;
});
canvas.addEventListener('mousemove', (e) => {
    if (isPanning) {
        const dx = e.clientX - startX;
        const dy = e.clientY - startY;
        currentTranslateX += dx;
        currentTranslateY += dy;
        startX = e.clientX;
        startY = e.clientY;
        redraw();
    }
});
canvas.addEventListener('mouseup', () => {
    isPanning = false;
});
canvas.addEventListener('mouseleave', () => {
    isPanning = false;
});
canvas.addEventListener('wheel', (e) => {
    e.preventDefault();
    const zoomAmount = e.deltaY * -0.01;
    currentScale *= (1 + zoomAmount);
    currentScale = Math.min(Math.max(0.5, currentScale), 4);
    redraw();
});
canvas.addEventListener('click', (e) => {
    const rect = canvas.getBoundingClientRect();
    const mouseX = (e.clientX - rect.left - currentTranslateX) / currentScale;
    const mouseY = (e.clientY - rect.top - currentTranslateY) / currentScale;
    const node = findNodeAtPosition(mouseX, mouseY);
    if (node) {
        showInfoPanel(node);
    }
});

function findNodeAtPosition(x, y, tree = filteredTree) {
    if (Math.hypot(tree.x - x, tree.y - y) < 20 / currentScale) {
        return tree;
    }
    for (let child of tree.children) {
        const found = findNodeAtPosition(x, y, child);
        if (found) return found;
    }
    return null;
}

function showInfoPanel(node) {
    const panel = document.createElement('div');
    panel.className = 'info-panel';
    const rect = canvas.getBoundingRect();
    const screenX = rect.left + (node.x * currentScale + currentTranslateX);
    const screenY = rect.top + (node.y * currentScale + currentTranslateY);
    panel.style.left = `${screenX + 20}px`;
    panel.style.top = `${screenY + 20}px`;
    panel.innerHTML = `
        <div class="panel-header">${node.label}</div>
        <div class="panel-content">${node.content.essay}</div>
        <button onclick="this.parentElement.remove()">Close</button>
    `;
    document.getElementById('infoPanels').appendChild(panel);
    makeDraggable(panel);
}

function makeDraggable(element) {
    let isDragging = false;
    let offsetX, offsetY;
    element.addEventListener('mousedown', (e) => {
        if (e.target === element) {
            isDragging = true;
            offsetX = e.clientX - element.offsetLeft;
            offsetY = e.clientY - element.offsetTop;
        }
    });
    document.addEventListener('mousemove', (e) => {
        if (isDragging) {
            element.style.left = `${e.clientX - offsetX}px`;
            element.style.top = `${e.clientY - offsetY}px`;
        }
    });
    document.addEventListener('mouseup', () => {
        isDragging = false;
    });
}

// Initialize the page
fetchSheetData();
redraw();
switchView('tree');
