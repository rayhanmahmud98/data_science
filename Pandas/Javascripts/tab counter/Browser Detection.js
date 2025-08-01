// In background.js or popup.js
function getBrowser() {
  if (window.navigator.userAgent.includes("Edg")) return "edge";
  if (window.navigator.userAgent.includes("OPR")) return "opera";
  return "chrome";
}

// Example usage
const currentBrowser = getBrowser();
console.log(`Running in ${currentBrowser}`);