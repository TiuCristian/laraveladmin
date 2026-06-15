# -*- coding: utf-8 -*-
css_path = 'c:/laragon/www/LaravelCMShtml/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Remove the previously appended block
css_content = css_content.split('/* --- WordPress Hover Menu & Sidebar Layout Fixes --- */')[0]

new_css = '''
/* --- WordPress Hover Menu & Sidebar Layout Fixes --- */
:root {
  --app-menubar-tabs: 250px;
}

/* Full Sidebar State */
.app-menubar-tabs {
  width: var(--app-menubar-tabs) !important;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  background: #1e2225;
  z-index: 1040;
  transition: width 0.3s ease;
}
.app-menubar-tabs .app-tab-content {
  left: 0 !important;
  width: var(--app-menubar-tabs) !important;
  background: transparent !important;
  overflow: visible !important;
  transition: width 0.3s ease;
}
.app-wrapper {
  margin-left: var(--app-menubar-tabs) !important;
  transition: margin-left 0.3s ease;
}
.app-header {
  padding-left: var(--app-menubar-tabs) !important;
  transition: padding-left 0.3s ease;
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
  left: var(--app-menubar-tabs); /* Width of the sidebar */
  width: 200px;
  background-color: #2c3338;
  box-shadow: 0 3px 5px rgba(0,0,0,0.2);
  padding: 0;
  margin: 0;
  list-style: none;
  z-index: 1050;
  border-radius: 0 3px 3px 0;
  transition: left 0.3s ease;
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

/* --- Mini Sidebar Toggle State --- */
[data-app-sidebar="mini"] {
  --app-menubar-tabs: 80px;
}
[data-app-sidebar="mini"] .app-menubar-tabs .menu-label,
[data-app-sidebar="mini"] .app-menubar-tabs .app-side-brands {
  display: none !important;
}
[data-app-sidebar="mini"] .app-menubar-tabs .menu-link {
  justify-content: center !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
}
[data-app-sidebar="mini"] .app-menubar-tabs .menu-link i {
  margin-right: 0 !important;
  font-size: 1.5rem !important;
}
[data-app-sidebar="mini"] .side-menubar .wp-submenu.wp-submenu-wrap {
  left: 80px !important;
}
'''

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content + new_css)

print('Toggle CSS fixed.')
