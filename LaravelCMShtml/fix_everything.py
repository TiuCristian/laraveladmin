# -*- coding: utf-8 -*-
import os
import glob
import re

# 1. Fix Edit Pages
def fix_edit_page(filepath, title_text, input_value):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Change "Add New Page/Post" to "Edit Page/Post"
    content = content.replace('>Add New Page<', f'>Edit {title_text}<')
    content = content.replace('>Add New Post<', f'>Edit {title_text}<')
    content = content.replace('>Add New<', '>Edit<')
    
    # Add input value
    content = content.replace('placeholder="Add title"', f'placeholder="Add title" value="{input_value}"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_edit_page('c:/laragon/www/LaravelCMShtml/pages-edit.html', 'Page', 'Home - Front Page')
fix_edit_page('c:/laragon/www/LaravelCMShtml/posts-edit.html', 'Post', 'Hello World!')

# 2. Rebuild Sidebar with exact WordPress classes
sidebar_html = '''    <!-- begin::Sidebar Menu -->
    <aside class="app-menubar-tabs" id="appMenubar">
      <div class="app-tab-content" style="width: 250px; left: 0;">
        <div class="app-content-inner">
          <div class="tab-content" id="appMenubarTabsContent">
            
            <div class="tab-pane fade show active" id="mainMenuTab" role="tabpanel" tabindex="0">
              <nav class="app-navbar">
                <ul class="side-menubar">
                  
                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="dashboard.html">
                      <i class="fi fi-rr-dashboard"></i><span class="menu-label">Dashboard</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Dashboard</li>
                      <li class="wp-first-item"><a href="dashboard.html" class="wp-first-item">Home</a></li>
                      <li><a href="dashboard-updates.html">Updates</a></li>
                    </ul>
                  </li>
                  
                  <li><div class="menu-divider"></div></li>
                  
                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="posts-list.html">
                      <i class="fi fi-rr-thumbtack"></i><span class="menu-label">Posts</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Posts</li>
                      <li class="wp-first-item"><a href="posts-list.html" class="wp-first-item">All Posts</a></li>
                      <li><a href="posts-add.html">Add New</a></li>
                      <li><a href="posts-categories.html">Categories</a></li>
                      <li><a href="posts-tags.html">Tags</a></li>
                    </ul>
                  </li>

                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="media-list.html">
                      <i class="fi fi-rr-picture"></i><span class="menu-label">Media</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Media</li>
                      <li class="wp-first-item"><a href="media-list.html" class="wp-first-item">Library</a></li>
                      <li><a href="media-add.html">Add New</a></li>
                    </ul>
                  </li>

                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="pages-list.html">
                      <i class="fi fi-rr-document"></i><span class="menu-label">Pages</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Pages</li>
                      <li class="wp-first-item"><a href="pages-list.html" class="wp-first-item">All Pages</a></li>
                      <li><a href="pages-add.html">Add New</a></li>
                    </ul>
                  </li>

                  <li class="menu-item">
                    <a class="menu-link" href="comments-list.html">
                      <i class="fi fi-rr-comment"></i><span class="menu-label">Comments</span>
                    </a>
                  </li>
                  
                  <li><div class="menu-divider"></div></li>
                  
                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="appearance-themes.html">
                      <i class="fi fi-rr-paint-roller"></i><span class="menu-label">Appearance</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Appearance</li>
                      <li class="wp-first-item"><a href="appearance-themes.html" class="wp-first-item">Themes</a></li>
                      <li><a href="appearance-menus.html">Menus</a></li>
                      <li><a href="appearance-widgets.html">Widgets</a></li>
                    </ul>
                  </li>

                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="plugins-list.html">
                      <i class="fi fi-rr-puzzle-piece"></i><span class="menu-label">Plugins</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Plugins</li>
                      <li class="wp-first-item"><a href="plugins-list.html" class="wp-first-item">Installed Plugins</a></li>
                      <li><a href="plugins-add.html">Add New</a></li>
                    </ul>
                  </li>

                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="users-list.html">
                      <i class="fi fi-rr-users"></i><span class="menu-label">Users</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Users</li>
                      <li class="wp-first-item"><a href="users-list.html" class="wp-first-item">All Users</a></li>
                      <li><a href="users-add.html">Add New</a></li>
                      <li><a href="users-profile.html">Profile</a></li>
                    </ul>
                  </li>
                  
                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="tools-index.html">
                      <i class="fi fi-rr-wrench"></i><span class="menu-label">Tools</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Tools</li>
                      <li class="wp-first-item"><a href="tools-index.html" class="wp-first-item">Available Tools</a></li>
                      <li><a href="tools-import.html">Import</a></li>
                      <li><a href="tools-export.html">Export</a></li>
                      <li><a href="tools-health.html">Site Health</a></li>
                    </ul>
                  </li>

                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="settings-general.html">
                      <i class="fi fi-rr-settings"></i><span class="menu-label">Settings</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Settings</li>
                      <li class="wp-first-item"><a href="settings-general.html" class="wp-first-item">General</a></li>
                      <li><a href="settings-writing.html">Writing</a></li>
                      <li><a href="settings-reading.html">Reading</a></li>
                      <li><a href="settings-discussion.html">Discussion</a></li>
                      <li><a href="settings-media.html">Media</a></li>
                      <li><a href="settings-permalinks.html">Permalinks</a></li>
                    </ul>
                  </li>
                </ul>
              </nav>
            </div>

          </div>
        </div>
      </div>
    </aside>
    <!-- end::Sidebar Menu -->'''

html_files = glob.glob('c:/laragon/www/LaravelCMShtml/*.html')
for file_path in html_files:
    filename = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace sidebar
    pattern = r'<!-- begin::Sidebar Menu -->.*?<!-- end::Sidebar Menu -->'
    content = re.sub(pattern, sidebar_html, content, flags=re.DOTALL)
    
    # Set active class dynamically
    prefix = filename.split('-')[0] + '-list.html'
    if filename in ['dashboard.html', 'dashboard-updates.html']:
        prefix = 'dashboard.html'
    elif filename in ['appearance-themes.html', 'appearance-menus.html', 'appearance-widgets.html']:
        prefix = 'appearance-themes.html'
    elif filename in ['settings-general.html', 'settings-writing.html', 'settings-reading.html', 'settings-discussion.html', 'settings-media.html', 'settings-permalinks.html']:
        prefix = 'settings-general.html'

    target_link = f'class="menu-link" href="{prefix}"'
    replacement_link = f'class="menu-link active" href="{prefix}"'
    content = content.replace(target_link, replacement_link)
    
    # Clean up any leftover inline style scripts I injected in <head>
    content = re.sub(r'<!-- begin::WP Hover Menu CSS.*?-->\s*<style>.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- begin::WP Hover Menu CSS.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style>.*?\.wp-menu-has-submenu.*?</style>', '', content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Fix CSS globally
css_path = 'c:/laragon/www/LaravelCMShtml/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Remove old hacks if present
css_content = css_content.split('/* --- WordPress Hover Menu & Sidebar Layout Fixes --- */')[0]
css_content = css_content.split('/* Sidebar Layout Fixes */')[0]
css_content = css_content.split('/* WP Submenu Hover CSS */')[0]
css_content = css_content.split('.app-menubar-tabs,')[0] # Remove the old overflow visible hack

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

print('Sidebar completely fixed with strict WP classes.')
