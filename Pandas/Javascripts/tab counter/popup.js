// DOM elements
const tabCountEl = document.getElementById('tabCount');
const refreshBtn = document.getElementById('refreshBtn');
const resetBtn = document.getElementById('resetBtn');

// 1. Load initial count
function updateDisplay(count) {
  tabCountEl.textContent = count;
  tabCountEl.style.color = count > 15 ? '#f44336' : '#1a73e8'; // Red if >15 tabs
}

// 2. Get count from storage and update display
function loadTabCount() {
  chrome.storage.local.get(['tabCount'], (result) => {
    updateDisplay(result.tabCount || 0);
  });
}

// 3. Setup event listeners
refreshBtn.addEventListener('click', () => {
  // Force recount all tabs
  chrome.tabs.query({currentWindow: true}, (tabs) => {
    const count = tabs.length;
    chrome.storage.local.set({tabCount: count});
    updateDisplay(count);
    chrome.runtime.sendMessage({action: "UPDATE_BADGE", count});
  });
});

resetBtn.addEventListener('click', () => {
  // Reset to zero
  chrome.storage.local.set({tabCount: 0});
  updateDisplay(0);
  chrome.runtime.sendMessage({action: "UPDATE_BADGE", count: 0});
});

// 4. Real-time updates from background.js
chrome.runtime.onMessage.addListener((message) => {
  if (message.action === "TAB_COUNT_UPDATE") {
    updateDisplay(message.count);
  }
});

// 5. Initialize
loadTabCount();

// 6. Request current count when popup opens
chrome.runtime.sendMessage({action: "GET_COUNT"}, (response) => {
  if (response?.count !== undefined) {
    updateDisplay(response.count);
  }
});