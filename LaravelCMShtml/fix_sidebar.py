import os
import re
import glob

# 1. Update CSS
css_path = 'c:/laragon/www/LaravelCMShtml/assets/css/styles.css'
with open(css_path, 'a', encoding='utf-8') as f:
    f.write('''\n\n/* Sidebar Layout Fixes */
:root {
  --app-menubar-tabs: 250px !important;
}
.app-menubar-tabs .app-tab-content {
  left: 0 !important;
  width: 250px !important;
}
.app-menubar-tabs {
  width: 250px !important;
  z-index: 1040;
}
.app-wrapper {
  margin-left: 250px !important;
}
.app-header {
  padding-left: 250px !important;
}
@media (max-width: 1199.98px) {
  .app-wrapper { margin-left: 0 !important; }
  .app-header { padding-left: 0 !important; }
}

/* Allow WP submenu to overflow */
.app-menubar-tabs,
.app-tab-content,
.app-content-inner,
.tab-content,
.tab-pane,
.app-navbar,
.side-menubar {
  overflow: visible !important;
}
.simplebar-content-wrapper,
.simplebar-mask,
.simplebar-offset {
  overflow: visible !important;
}

/* WP Submenu Hover CSS */
.wp-menu-has-submenu:hover .wp-submenu {
  display: block !important;
}
.wp-submenu a:hover {
  background-color: rgba(255,255,255,0.1) !important;
}
''')

# 2. Remove data-simplebar from HTML files to prevent simplebar from wrapping the nav and hiding overflow
html_files = glob.glob('c:/laragon/www/LaravelCMShtml/*.html')
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove data-simplebar
    new_content = content.replace('<nav class="app-navbar" data-simplebar>', '<nav class="app-navbar">')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print('Sidebar CSS and HTML fixed.')
