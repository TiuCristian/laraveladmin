import os
import re
import glob

sidebar_html = '''    <!-- begin::Sidebar Menu -->
    <aside class="app-menubar-tabs" id="appMenubar">
      <div class="app-tab-content" style="width: 100%; margin-left: 0;">
        <div class="app-side-brands" style="padding-left: 20px;">
          <a class="navbar-brand-text text-decoration-none fw-bold" href="dashboard.html">CMS Admin</a>
        </div>
        <div class="app-content-inner">
          <div class="tab-content" id="appMenubarTabsContent">
            
            <div class="tab-pane fade show active" id="mainMenuTab" role="tabpanel" tabindex="0">
              <nav class="app-navbar" data-simplebar>
                <ul class="side-menubar">
                  
                  <li class="menu-item wp-menu-has-submenu position-relative">
                    <a class="menu-link" href="dashboard.html">
                      <i class="fi fi-rr-dashboard"></i><span class="menu-label">Dashboard</span>
                    </a>
                    <ul class="wp-submenu list-unstyled position-absolute shadow-sm d-none" style="left: 100%; top: 0; min-width: 180px; z-index: 1050; background-color: #2c3338;">
                      <li class="fw-bold px-3 py-2 text-white border-bottom border-secondary d-none d-md-block" style="background-color: #1e2225;">Dashboard</li>
                      <li><a href="dashboard.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Home</a></li>
                      <li><a href="dashboard-updates.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Updates</a></li>
                    </ul>
                  </li>
                  
                  <li><div class="menu-divider"></div></li>
                  
                  <li class="menu-item wp-menu-has-submenu position-relative">
                    <a class="menu-link" href="posts-list.html">
                      <i class="fi fi-rr-thumbtack"></i><span class="menu-label">Posts</span>
                    </a>
                    <ul class="wp-submenu list-unstyled position-absolute shadow-sm d-none" style="left: 100%; top: 0; min-width: 180px; z-index: 1050; background-color: #2c3338;">
                      <li class="fw-bold px-3 py-2 text-white border-bottom border-secondary d-none d-md-block" style="background-color: #1e2225;">Posts</li>
                      <li><a href="posts-list.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">All Posts</a></li>
                      <li><a href="posts-add.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Add New</a></li>
                      <li><a href="posts-categories.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Categories</a></li>
                      <li><a href="posts-tags.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Tags</a></li>
                    </ul>
                  </li>

                  <li class="menu-item wp-menu-has-submenu position-relative">
                    <a class="menu-link" href="media-list.html">
                      <i class="fi fi-rr-picture"></i><span class="menu-label">Media</span>
                    </a>
                    <ul class="wp-submenu list-unstyled position-absolute shadow-sm d-none" style="left: 100%; top: 0; min-width: 180px; z-index: 1050; background-color: #2c3338;">
                      <li class="fw-bold px-3 py-2 text-white border-bottom border-secondary d-none d-md-block" style="background-color: #1e2225;">Media</li>
                      <li><a href="media-list.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Library</a></li>
                      <li><a href="media-add.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Add New</a></li>
                    </ul>
                  </li>

                  <li class="menu-item wp-menu-has-submenu position-relative">
                    <a class="menu-link" href="pages-list.html">
                      <i class="fi fi-rr-document"></i><span class="menu-label">Pages</span>
                    </a>
                    <ul class="wp-submenu list-unstyled position-absolute shadow-sm d-none" style="left: 100%; top: 0; min-width: 180px; z-index: 1050; background-color: #2c3338;">
                      <li class="fw-bold px-3 py-2 text-white border-bottom border-secondary d-none d-md-block" style="background-color: #1e2225;">Pages</li>
                      <li><a href="pages-list.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">All Pages</a></li>
                      <li><a href="pages-add.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Add New</a></li>
                    </ul>
                  </li>

                  <li class="menu-item position-relative">
                    <a class="menu-link" href="comments-list.html">
                      <i class="fi fi-rr-comment"></i><span class="menu-label">Comments</span>
                    </a>
                  </li>
                  
                  <li><div class="menu-divider"></div></li>
                  
                  <li class="menu-item wp-menu-has-submenu position-relative">
                    <a class="menu-link" href="appearance-themes.html">
                      <i class="fi fi-rr-paint-roller"></i><span class="menu-label">Appearance</span>
                    </a>
                    <ul class="wp-submenu list-unstyled position-absolute shadow-sm d-none" style="left: 100%; top: 0; min-width: 180px; z-index: 1050; background-color: #2c3338;">
                      <li class="fw-bold px-3 py-2 text-white border-bottom border-secondary d-none d-md-block" style="background-color: #1e2225;">Appearance</li>
                      <li><a href="appearance-themes.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Themes</a></li>
                      <li><a href="appearance-menus.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Menus</a></li>
                      <li><a href="appearance-widgets.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Widgets</a></li>
                    </ul>
                  </li>

                  <li class="menu-item wp-menu-has-submenu position-relative">
                    <a class="menu-link" href="plugins-list.html">
                      <i class="fi fi-rr-puzzle-piece"></i><span class="menu-label">Plugins</span>
                    </a>
                    <ul class="wp-submenu list-unstyled position-absolute shadow-sm d-none" style="left: 100%; top: 0; min-width: 180px; z-index: 1050; background-color: #2c3338;">
                      <li class="fw-bold px-3 py-2 text-white border-bottom border-secondary d-none d-md-block" style="background-color: #1e2225;">Plugins</li>
                      <li><a href="plugins-list.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Installed Plugins</a></li>
                      <li><a href="plugins-add.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Add New</a></li>
                    </ul>
                  </li>

                  <li class="menu-item wp-menu-has-submenu position-relative">
                    <a class="menu-link" href="users-list.html">
                      <i class="fi fi-rr-users"></i><span class="menu-label">Users</span>
                    </a>
                    <ul class="wp-submenu list-unstyled position-absolute shadow-sm d-none" style="left: 100%; top: 0; min-width: 180px; z-index: 1050; background-color: #2c3338;">
                      <li class="fw-bold px-3 py-2 text-white border-bottom border-secondary d-none d-md-block" style="background-color: #1e2225;">Users</li>
                      <li><a href="users-list.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">All Users</a></li>
                      <li><a href="users-add.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Add New</a></li>
                      <li><a href="users-profile.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Profile</a></li>
                    </ul>
                  </li>
                  
                  <li class="menu-item wp-menu-has-submenu position-relative">
                    <a class="menu-link" href="tools-index.html">
                      <i class="fi fi-rr-wrench"></i><span class="menu-label">Tools</span>
                    </a>
                    <ul class="wp-submenu list-unstyled position-absolute shadow-sm d-none" style="left: 100%; top: 0; min-width: 180px; z-index: 1050; background-color: #2c3338;">
                      <li class="fw-bold px-3 py-2 text-white border-bottom border-secondary d-none d-md-block" style="background-color: #1e2225;">Tools</li>
                      <li><a href="tools-index.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Available Tools</a></li>
                      <li><a href="tools-import.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Import</a></li>
                      <li><a href="tools-export.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Export</a></li>
                      <li><a href="tools-health.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Site Health</a></li>
                    </ul>
                  </li>

                  <li class="menu-item wp-menu-has-submenu position-relative">
                    <a class="menu-link" href="settings-general.html">
                      <i class="fi fi-rr-settings"></i><span class="menu-label">Settings</span>
                    </a>
                    <ul class="wp-submenu list-unstyled position-absolute shadow-sm d-none" style="left: 100%; top: 0; min-width: 180px; z-index: 1050; background-color: #2c3338;">
                      <li class="fw-bold px-3 py-2 text-white border-bottom border-secondary d-none d-md-block" style="background-color: #1e2225;">Settings</li>
                      <li><a href="settings-general.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">General</a></li>
                      <li><a href="settings-writing.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Writing</a></li>
                      <li><a href="settings-reading.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Reading</a></li>
                      <li><a href="settings-discussion.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Discussion</a></li>
                      <li><a href="settings-media.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Media</a></li>
                      <li><a href="settings-permalinks.html" class="d-block px-3 py-2 text-white text-decoration-none" style="opacity: 0.8;">Permalinks</a></li>
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
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to find the aside block
    # Start: <!-- begin::Sidebar Menu -->
    # End: <!-- end::Sidebar Menu -->
    pattern = r'<!-- begin::Sidebar Menu -->.*?<!-- end::Sidebar Menu -->'
    
    new_content = re.sub(pattern, sidebar_html, content, flags=re.DOTALL)
    
    # Also inject the custom CSS into the head if not already there
    css_injection = """
  <!-- begin::WP Hover Menu CSS -->
  <style>
    .wp-menu-has-submenu:hover .wp-submenu {
      display: block !important;
    }
    .wp-submenu a:hover {
      opacity: 1 !important;
      background-color: rgba(255,255,255,0.1);
    }
    .app-wrapper {
      margin-left: 250px !important; /* Adjust based on sidebar width without left tabs */
    }
    @media (max-width: 991.98px) {
      .app-wrapper { margin-left: 0 !important; }
    }
    /* Fix sidebar width since we removed the left tabs */
    .app-menubar-tabs {
      width: 250px;
    }
  </style>
</head>"""
    if "<!-- begin::WP Hover Menu CSS -->" not in new_content:
        new_content = new_content.replace('</head>', css_injection)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print('Sidebar updated in all HTML files.')
