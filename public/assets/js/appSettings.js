(() => {
    'use strict';
	
	const APP_SIDEBAR_BREAKPOINT = 1191;
	var docEl = document.documentElement;

	// Helper to get cookie
	const getCookie = (name) => {
	  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
	  return match ? match[2] : null;
	};

	// App settings default
	let appSettings = {
		appTheme: getCookie('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'),
		appSidebar: 'full',
		appColor: 'blue',
	};

	// Update settings
	function setAppSettings(newSettings = {}) {
		appSettings = {
			...appSettings,
			...newSettings
		};
		applySettings();
	}

	// Apply settings to DOM
	function applySettings() {
		docEl.setAttribute("data-bs-theme", appSettings.appTheme);

		if (window.innerWidth >= APP_SIDEBAR_BREAKPOINT) {
			docEl.setAttribute("data-app-sidebar", appSettings.appSidebar);
		}

		docEl.setAttribute("data-color-theme", appSettings.appColor);
	}

	// Initialize
	document.addEventListener("DOMContentLoaded", applySettings);
	window.setAppSettings = setAppSettings;

})();