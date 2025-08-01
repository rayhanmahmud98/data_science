// Initialize badge and storage
chrome.runtime.onInstalled.addListener(initializeCounter);
chrome.runtime.onStartup.addListener(initializeCounter);

function initializeCounter() {
  chrome.tabs.query({currentWindow: true}, (tabs) => {
    const count = tabs.length;
    updateBadge(count);
    chrome.storage.local.set({tabCount: count});
  });
  
  // Set badge style
  chrome.action.setBadgeBackgroundColor({color: '#1a73e8'});
  chrome.action.setBadgeTextColor({color: 'white'});
}

// Tab event listeners
chrome.tabs.onCreated.addListener(() => handleTabChange(1));
chrome.tabs.onRemoved.addListener(() => handleTabChange(-1));
chrome.tabs.onAttached.addListener(initializeCounter);
chrome.tabs.onDetached.addListener(initializeCounter);

function handleTabChange(change) {
  chrome.storage.local.get(['tabCount'], (result) => {
    const newCount = Math.max(0, (result.tabCount || 0) + change);
    updateBadge(newCount);
    chrome.storage.local.set({tabCount: newCount});
  });
}

function updateBadge(count) {
  chrome.action.setBadgeText({
    text: count > 0 ? count.toString() : ""
  });
}