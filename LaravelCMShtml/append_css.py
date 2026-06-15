# -*- coding: utf-8 -*-
css_path = 'c:/laragon/www/LaravelCMShtml/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Append pure WordPress hover CSS
new_css = '''
/* --- WordPress Hover Menu & Sidebar Layout Fixes --- */
:root {
  --app-menubar-tabs: 250px;
}
.app-menubar-tabs {
  width: var(--app-menubar-tabs) !important;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  background: #1e2225;
  z-index: 1040;
}
.app-menubar-tabs .app-tab-content {
  left: 0 !important;
  width: 250px !important;
  background: transparent !important;
  overflow: visible !important;
}
.app-wrapper {
  margin-left: 250px !important;
}
.app-header {
  padding-left: 250px !important;
}

/* Ensure containers don't clip absolute submenus */
.app-menubar-tabs,
.app-tab-content,
.app-content-inner,
.tab-content,
.tab-pane,
.app-navbar,
.side-menubar {
  overflow: visible !important;
}

/* WP Hover Menu Base Styles */
.side-menubar .menu-item.wp-has-submenu {
  position: relative;
}
.side-menubar .wp-submenu.wp-submenu-wrap {
  display: none;
  position: absolute;
  top: 0;
  left: 250px; /* Width of the sidebar */
  width: 200px;
  background-color: #2c3338;
  box-shadow: 0 3px 5px rgba(0,0,0,0.2);
  padding: 0;
  margin: 0;
  list-style: none;
  z-index: 1050;
  border-radius: 0 3px 3px 0;
}
/* Show on hover */
.side-menubar .menu-item.wp-has-submenu:hover .wp-submenu.wp-submenu-wrap {
  display: block;
}

/* WP Submenu Links Styling */
.wp-submenu-wrap li.wp-submenu-head {
  background-color: #1e2225;
  color: #fff;
  padding: 10px 15px;
  font-weight: 600;
  font-size: 0.9rem;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}
.wp-submenu-wrap li a {
  display: block;
  padding: 8px 15px;
  color: rgba(255,255,255,0.8);
  text-decoration: none;
  font-size: 0.85rem;
  transition: all 0.2s ease;
}
.wp-submenu-wrap li a:hover {
  background-color: rgba(255,255,255,0.1);
  color: #fff;
}
'''

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content + new_css)

print('Appended CSS successfully.')
