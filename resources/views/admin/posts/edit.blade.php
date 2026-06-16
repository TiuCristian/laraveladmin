<!DOCTYPE html>
<html lang="en">
<head>
  <!-- begin::NexLink Meta Basic -->
  <meta charset="utf-8">
  <meta name="theme-color" content="#5955D1">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Add New Post | CMS Admin Panel</title>
  
  <!-- begin::NexLink Favicon Tags -->
  <link rel="icon" type="image/png" href="/assets/images/favicon.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/images/apple-touch-icon.png">

  <!-- begin::NexLink Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">

  <!-- begin::NexLink Required Stylesheet -->
  <link rel="stylesheet" href="/assets/libs/flaticon/css/all/all.css">
  <link rel="stylesheet" href="/assets/libs/lucide/lucide.css">
  <link rel="stylesheet" href="/assets/libs/fontawesome/css/all.min.css">
  <link rel="stylesheet" href="/assets/libs/simplebar/simplebar.css">
  <link rel="stylesheet" href="/assets/libs/node-waves/waves.css">
  <link rel="stylesheet" href="/assets/libs/bootstrap-select/css/bootstrap-select.min.css">
  <link rel="stylesheet" href="/assets/libs/flatpickr/flatpickr.min.css">
  
  <!-- begin::NexLink CSS Stylesheet -->
  <link rel="stylesheet" href="/assets/libs/datatables/datatables.min.css">
  <link rel="stylesheet" href="/assets/css/styles.css">

  
</head>
<body>
  <div class="page-layout">
    
    <!-- begin::Page Header -->
    <header class="app-header">
      <div class="app-header-inner">
        <!-- Sidebar Toggle -->
        <button class="app-toggler" type="button" aria-label="app toggler">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M7.66699 12.6668L3.66699 8.00016L7.66699 3.3335" stroke="#1C274C" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" />
            <path opacity="0.5" d="M12.667 12.6668L8.66699 8.00016L12.667 3.3335" stroke="#1C274C" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
        </button>

        <!-- Top Bar Left Action Buttons -->
        <div class="app-header-start d-none d-md-flex align-items-center">
          <a href="#" class="btn btn-light btn-sm me-2 d-flex align-items-center gap-1">
            <i class="fi fi-rr-home"></i> View Site
          </a>
          <a href="#" class="btn btn-light btn-sm d-flex align-items-center gap-1">
            <i class="fi fi-rr-add"></i> New
          </a>
        </div>

        <!-- Top Bar Right User Menu -->
        <div class="app-header-end d-flex align-items-center">
          <a href="javascript:void(0);" class="theme-btn active me-3">
            <svg class="icon-light" width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M14.1663 10.5002C14.1663 12.8013 12.3008 14.6668 9.99967 14.6668C7.69849 14.6668 5.83301 12.8013 5.83301 10.5002C5.83301 8.19898 7.69849 6.3335 9.99967 6.3335C12.3008 6.3335 14.1663 8.19898 14.1663 10.5002Z" fill="var(--bs-heading-color)"></path>
              <path fill-rule="evenodd" clip-rule="evenodd" d="M10.0003 1.5415C10.3455 1.5415 10.6253 1.82133 10.6253 2.1665V3.83317C10.6253 4.17834 10.3455 4.45817 10.0003 4.45817C9.65516 4.45817 9.37532 4.17834 9.37532 3.83317V2.1665C9.37532 1.82133 9.65516 1.5415 10.0003 1.5415ZM1.04199 10.4998C1.04199 10.1547 1.32182 9.87484 1.66699 9.87484H3.33366C3.67883 9.87484 3.95866 10.1547 3.95866 10.4998C3.95866 10.845 3.67883 11.1248 3.33366 11.1248H1.66699C1.32182 11.1248 1.04199 10.845 1.04199 10.4998ZM16.042 10.4998C16.042 10.1547 16.3218 9.87484 16.667 9.87484H18.3337C18.6788 9.87484 18.9587 10.1547 18.9587 10.4998C18.9587 10.845 18.6788 11.1248 18.3337 11.1248H16.667C16.3218 11.1248 16.042 10.845 16.042 10.4998ZM10.0003 16.5415C10.3455 16.5415 10.6253 16.8213 10.6253 17.1665V18.8332C10.6253 19.1783 10.3455 19.4582 10.0003 19.4582C9.65516 19.4582 9.37532 19.1783 9.37532 18.8332V17.1665C9.37532 16.8213 9.65516 16.5415 10.0003 16.5415Z" fill="var(--bs-heading-color)"></path>
              <g opacity="0.5">
                <path d="M3.05729 3.59633C3.29021 3.34158 3.68554 3.32389 3.94029 3.55681L5.79198 5.24979C6.04673 5.48271 6.06442 5.87804 5.8315 6.13279C5.59858 6.38754 5.20325 6.40524 4.94851 6.17232L3.09683 4.47933C2.84208 4.24642 2.82438 3.85108 3.05729 3.59633Z" fill="var(--bs-heading-color)"></path>
                <path d="M16.9428 3.59633C17.1758 3.85108 17.1581 4.24642 16.9033 4.47933L15.0516 6.17232C14.7968 6.40524 14.4015 6.38754 14.1686 6.13279C13.9357 5.87804 13.9534 5.48271 14.2082 5.24979L16.0598 3.55681C16.3146 3.32389 16.7099 3.34158 16.9428 3.59633Z" fill="var(--bs-heading-color)"></path>
                <path d="M14.188 14.6874C14.4321 14.4433 14.8277 14.4434 15.0718 14.6875L16.9235 16.5394C17.1676 16.7835 17.1676 17.1792 16.9235 17.4232C16.6794 17.6673 16.2837 17.6673 16.0396 17.4232L14.1879 15.5713C13.9438 15.3272 13.9439 14.9315 14.188 14.6874Z" fill="var(--bs-heading-color)"></path>
                <path d="M5.81235 14.6875C6.05643 14.9315 6.05643 15.3272 5.81235 15.5713L3.9605 17.4231C3.71642 17.6672 3.32069 17.6672 3.07662 17.4231C2.83253 17.179 2.83253 16.7834 3.07662 16.5393L4.92847 14.6874C5.17254 14.4434 5.56828 14.4434 5.81235 14.6875Z" fill="var(--bs-heading-color)"></path>
              </g>
            </svg>
            <div class="theme-toggle"></div>
            <svg class="icon-dark" width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M16.5835 2.4225C16.4495 2.08117 15.9681 2.08117 15.834 2.4225L15.4754 3.33523C15.4345 3.43944 15.3523 3.52193 15.2485 3.56303L14.339 3.92301C13.999 4.05762 13.999 4.54067 14.339 4.67529L15.2485 5.03527C15.3523 5.07637 15.4345 5.15886 15.4754 5.26306L15.834 6.1758C15.9681 6.51712 16.4495 6.51712 16.5835 6.17581L16.9422 5.26306C16.9831 5.15886 17.0653 5.07637 17.1691 5.03527L18.0785 4.67529C18.4186 4.54067 18.4186 4.05762 18.0785 3.92301L17.1691 3.56303C17.0653 3.52193 16.9831 3.43944 16.9422 3.33523L16.5835 2.4225Z" fill="var(--bs-heading-color)"></path>
              <path d="M13.3609 7.27454C13.2267 6.93323 12.7455 6.93323 12.6113 7.27454L12.4806 7.60733C12.4396 7.71154 12.3575 7.79403 12.2536 7.83513L11.9221 7.96638C11.582 8.10099 11.582 8.58404 11.9221 8.71866L12.2536 8.8499C12.3575 8.89098 12.4396 8.97348 12.4806 9.07773L12.6113 9.41048C12.7455 9.75182 13.2267 9.75182 13.3609 9.41048L13.4916 9.07773C13.5326 8.97348 13.6147 8.89098 13.7186 8.8499L14.0501 8.71866C14.3902 8.58404 14.3902 8.10099 14.0501 7.96638L13.7186 7.83513C13.6147 7.79403 13.5326 7.71154 13.4916 7.60733L13.3609 7.27454Z" fill="var(--bs-heading-color)"></path>
              <path opacity="0.5" d="M10.0003 18.8332C14.6027 18.8332 18.3337 15.1022 18.3337 10.4998C18.3337 10.1143 17.7557 10.0505 17.5563 10.3805C16.6077 11.9503 14.8849 12.9998 12.917 12.9998C9.92541 12.9998 7.50032 10.5748 7.50032 7.58317C7.50032 5.61521 8.54982 3.89238 10.1197 2.9438C10.4497 2.7444 10.3859 2.1665 10.0003 2.1665C5.39795 2.1665 1.66699 5.89746 1.66699 10.4998C1.66699 15.1022 5.39795 18.8332 10.0003 18.8332Z" fill="var(--bs-heading-color)"></path>
            </svg>
          </a>

          <div class="dropdown text-end ms-sm-3 ms-2 ms-lg-4">
            <a href="#" class="d-flex align-items-center py-2 text-decoration-none" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="true">
              <div class="text-end me-2 d-none d-lg-inline-block">
                <div class="fw-bold text-dark">Admin User</div>
                <small class="text-body d-block lh-sm">Administrator</small>
              </div>
              <div class="avatar avatar-sm rounded-circle avatar-status-success">
                <img src="/assets/images/avatar/avatar1.webp" alt="User Avatar">
              </div>
            </a>
            <ul class="dropdown-menu dropdown-menu-end w-225px mt-1">
              <li><a class="dropdown-item d-flex align-items-center gap-2" href="{{ route('profile.edit') }}"><i class="fi fi-rr-user"></i> Edit Profile</a></li>
              <li><div class="dropdown-divider my-1"></div></li>
              <li><a class="dropdown-item d-flex align-items-center gap-2 text-danger" href="#"><i class="fi fi-sr-exit"></i> Log Out</a></li>
            </ul>
          </div>
        </div>
      </div>
    </header>
    <!-- end::Page Header -->

            <!-- begin::Sidebar Menu -->
    <aside class="app-menubar-tabs" id="appMenubar">
      <div class="app-tab-content" style="width: 250px; left: 0;">
        <div class="app-content-inner">
          <div class="tab-content" id="appMenubarTabsContent">
            
            <div class="tab-pane fade show active" id="mainMenuTab" role="tabpanel" tabindex="0">
              <nav class="app-navbar">
                <ul class="side-menubar">
                  
                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="{{ route('admin.dashboard') }}">
                      <i class="fi fi-rr-dashboard"></i><span class="menu-label">Dashboard</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Dashboard</li>
                      <li class="wp-first-item"><a href="{{ route('admin.dashboard') }}" class="wp-first-item">Home</a></li>
                      <li><a href="dashboard-updates.html">Updates</a></li>
                    </ul>
                  </li>
                  
                  <li><div class="menu-divider"></div></li>
                  
                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link active" href="{{ route('posts.index') }}">
                      <i class="fi fi-rr-thumbtack"></i><span class="menu-label">Posts</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Posts</li>
                      <li class="wp-first-item"><a href="{{ route('posts.index') }}" class="wp-first-item">All Posts</a></li>
                      <li><a href="{{ route('posts.create') }}">Add New</a></li>
                      <li><a href="{{ route('categories.index') }}">Categories</a></li>
                      <li><a href="{{ route('tags.index') }}">Tags</a></li>
                    </ul>
                  </li>

                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="{{ route('media.index') }}">
                      <i class="fi fi-rr-picture"></i><span class="menu-label">Media</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Media</li>
                      <li class="wp-first-item"><a href="{{ route('media.index') }}" class="wp-first-item">Library</a></li>
                      <li><a href="media-add.html">Add New</a></li>
                    </ul>
                  </li>

                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="{{ route('pages.index') }}">
                      <i class="fi fi-rr-document"></i><span class="menu-label">Pages</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Pages</li>
                      <li class="wp-first-item"><a href="{{ route('pages.index') }}" class="wp-first-item">All Pages</a></li>
                      <li><a href="{{ route('pages.create') }}">Add New</a></li>
                    </ul>
                  </li>

                  <li class="menu-item">
                    <a class="menu-link" href="{{ route('comments.index') }}">
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
                    <a class="menu-link" href="{{ route('users.index') }}">
                      <i class="fi fi-rr-users"></i><span class="menu-label">Users</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Users</li>
                      <li class="wp-first-item"><a href="{{ route('users.index') }}" class="wp-first-item">All Users</a></li>
                      <li><a href="{{ route('users.create') }}">Add New</a></li>
                      <li><a href="{{ route('profile.edit') }}">Profile</a></li>
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
                    <a class="menu-link" href="{{ route('settings.general') }}">
                      <i class="fi fi-rr-settings"></i><span class="menu-label">Settings</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Settings</li>
                      <li class="wp-first-item"><a href="{{ route('settings.general') }}" class="wp-first-item">General</a></li>
                      <li><a href="{{ route('settings.writing') }}">Writing</a></li>
                      <li><a href="{{ route('settings.reading') }}">Reading</a></li>
                      <li><a href="{{ route('settings.discussion') }}">Discussion</a></li>
                      <li><a href="{{ route('settings.media') }}">Media</a></li>
                      <li><a href="{{ route('settings.permalinks') }}">Permalinks</a></li>
                    </ul>
                  </li>
                </ul>
              </nav>
            </div>

          </div>
        </div>
      </div>
    </aside>
    <!-- end::Sidebar Menu -->

    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Edit Post</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="{{ route('admin.dashboard') }}">Home</a></li>
                <li class="breadcrumb-item"><a href="{{ route('posts.index') }}">Posts</a></li>
                <li class="breadcrumb-item active" aria-current="page">Edit Post</li>
              </ol>
            </nav>
          </div>
          <div class="d-flex align-items-center gap-2">
            @php
                $catSlug = $post->categories->count() > 0 ? $post->categories->first()->slug : 'uncategorized';
            @endphp
            <a href="{{ route('frontend.post', ['category' => $catSlug, 'slug' => $post->slug]) }}" target="_blank" class="btn btn-light border btn-sm d-flex align-items-center justify-content-center" title="Preview on Frontend" style="width: 32px; height: 32px; padding: 0;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="3" rx="2"></rect><line x1="8" x2="16" y1="21" y2="21"></line><line x1="12" x2="12" y1="17" y2="21"></line></svg>
            </a>
            <button type="submit" form="editForm" onclick="document.querySelector('select[name=\'status\']').value='draft';" class="btn btn-outline-secondary btn-sm">Save Draft</button>
            @if($post->status == 'published')
                <button type="submit" form="editForm" class="btn btn-primary btn-sm">Save</button>
            @else
                <button type="submit" form="editForm" onclick="document.querySelector('select[name=\'status\']').value='published';" class="btn btn-primary btn-sm">Publish</button>
            @endif
          </div>
        </div>

        <form action="{{ route('posts.update', $post) }}" method="POST" id="editForm" enctype="multipart/form-data">
@csrf
        @method('PUT')

<div class="row">
          
          <!-- Main Editor Area -->
          <div class="col-lg-8 pe-lg-5">
            <div class="mb-4">
              <label for="postTitle" class="form-label visually-hidden">Add Title</label>
              <input type="text" class="form-control form-control-lg border-0 fs-1 fw-bold px-0 shadow-none bg-transparent text-body" id="postTitle" name="title" placeholder="Add title" value="{{ $post->title }}" style="height: 80px;">
            </div>
            
            <div class="d-none">
            <div class="d-flex flex-wrap align-items-center gap-2 border-bottom pb-2 mb-3">
              <button class="btn btn-sm btn-light border"><i class="fi fi-rr-bold"></i></button>
              <button class="btn btn-sm btn-light border"><i class="fi fi-rr-italic"></i></button>
              <button class="btn btn-sm btn-light border"><i class="fi fi-rr-underline"></i></button>
              <div class="vr mx-1"></div>
              <button class="btn btn-sm btn-light border"><i class="fi fi-rr-list"></i></button>
              <button class="btn btn-sm btn-light border"><i class="fi fi-rr-list-check"></i></button>
              <div class="vr mx-1"></div>
              <button class="btn btn-sm btn-light border"><i class="fi fi-rr-picture"></i> Add Media</button>
            </div>
            </div>

            <!-- Editor Textarea -->
            <div id="editorjs" class="mt-2" style="min-height: 600px; font-family: 'Instrument Sans', sans-serif;"></div>
            <input type="hidden" name="content" id="contentInput" value="{{ $post->content }}">
            <style>
              .ce-block__content, .ce-toolbar__content { max-width: 800px; margin-left: 60px; }
              .codex-editor__redactor { padding-bottom: 50px !important; }
              .ce-paragraph { font-size: 1.1rem; line-height: 1.6; color: var(--bs-body-color); }
              .ce-toolbar__plus, .ce-toolbar__settings-btn { color: var(--bs-body-color); }
              .ce-toolbar__plus:hover, .ce-toolbar__settings-btn:hover { background-color: var(--bs-tertiary-bg); color: var(--bs-primary); }
              .ce-popover, .ce-inline-toolbar, .ce-conversion-toolbar { background-color: var(--bs-body-bg); border: 1px solid var(--bs-border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
              .ce-popover-item, .ce-inline-tool, .ce-conversion-tool { color: var(--bs-body-color); }
              .ce-popover-item:hover, .ce-popover-item--active, .ce-inline-tool:hover, .ce-conversion-tool:hover { background-color: var(--bs-tertiary-bg); color: var(--bs-primary); }
              .ce-popover-item__icon, .ce-popover-item__title { color: inherit; }
              .ce-popover__search { background-color: var(--bs-tertiary-bg); color: var(--bs-body-color); border: 1px solid var(--bs-border-color); }
              .cdx-search-field__input { color: var(--bs-body-color); }
              ::selection { background-color: rgba(89, 85, 209, 0.2); }
            </style>
          </div>

          <!-- Sidebar Meta Boxes (Right Column) -->
          <div class="col-lg-4">
            
            <div class="card border-0 shadow-sm rounded-0 h-100 bg-body border-start">
              
              <!-- Tabs -->
              <ul class="nav nav-tabs border-bottom bg-body px-2 pt-2 d-flex flex-nowrap" id="sidebarTabs" role="tablist" style="border-bottom-width: 1px;">
                <li class="nav-item" role="presentation">
                  <button class="nav-link active text-body fw-medium py-2 px-3 fs-6 rounded-0 border-0 bg-transparent" id="post-tab" data-bs-toggle="tab" data-bs-target="#post-pane" type="button" role="tab" style="box-shadow: inset 0 -2px 0 0 var(--bs-dark); margin-bottom: -1px;">Post</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link text-muted py-2 px-3 fs-6 rounded-0 border-0 bg-transparent hover-dark" id="block-tab" data-bs-toggle="tab" data-bs-target="#block-pane" type="button" role="tab" style="margin-bottom: -1px;">Block</button>
                </li>
                <li class="nav-item ms-auto" role="presentation">
                  <button class="nav-link text-muted px-2 hover-dark bg-transparent border-0"><i class="fi fi-rr-cross-small"></i></button>
                </li>
              </ul>

              <div class="tab-content" id="sidebarTabsContent">
                
                <!-- Post Pane -->
                <div class="tab-pane fade show active" id="post-pane" role="tabpanel" aria-labelledby="post-tab">
                  <div class="card-body p-4">
                    
                    <div class="d-flex align-items-center justify-content-between mb-3">
                      <div class="fw-bold d-flex align-items-center gap-2 text-body">
                        <i class="fi fi-rr-thumbtack"></i> <span id="sidebarPostTitle">{{ $post->title ?: 'No title' }}</span>
                      </div>
                      <button class="btn btn-sm btn-link text-muted p-0 hover-dark"><i class="fi fi-rr-menu-dots-vertical"></i></button>
                    </div>

                    <div class="mb-3">
                      @if($post->featured_image)
                        <div class="position-relative mb-2">
                          <img src="{{ Storage::url($post->featured_image) }}" alt="Featured Image" class="img-fluid border rounded" id="featuredImagePreview">
                          <button type="button" class="btn btn-sm btn-danger position-absolute top-0 end-0 m-2" onclick="document.getElementById('featuredImageInput').value = ''; document.getElementById('featuredImagePreview').classList.add('d-none');">
                            <i class="fas fa-trash"></i>
                          </button>
                        </div>
                        <button type="button" class="btn w-100 py-2 text-body bg-body border border-secondary-subtle" style="font-size: 0.9rem;" onclick="document.getElementById('featuredImageInput').click();">Replace featured image</button>
                      @else
                        <img src="" alt="Featured Image" class="img-fluid border rounded mb-2 d-none" id="featuredImagePreview">
                        <button type="button" class="btn w-100 py-2 text-body bg-body border border-secondary-subtle" style="font-size: 0.9rem;" onclick="document.getElementById('featuredImageInput').click();">Set featured image</button>
                      @endif
                      <input type="file" form="editForm" name="featured_image" id="featuredImageInput" class="d-none" accept="image/*" onchange="const file = this.files[0]; if(file) { const reader = new FileReader(); reader.onload = function(e) { const img = document.getElementById('featuredImagePreview'); img.src = e.target.result; img.classList.remove('d-none'); }; reader.readAsDataURL(file); }">
                    </div>

                    <div class="mb-3">
                      <a href="#excerptCollapseInline" data-bs-toggle="collapse" class="text-decoration-none text-primary small">Add an excerpt...</a>
                      <div class="collapse mt-2" id="excerptCollapseInline">
                        <textarea form="editForm" name="excerpt" class="form-control" rows="3" placeholder="Write an excerpt (optional)">{{ $post->excerpt }}</textarea>
                      </div>
                    </div>

                    <p class="text-muted small mb-4">Last edited a second ago.</p>

                    <!-- Status & Publish Properties -->
                    <div class="mb-4">
                      <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body small">Status</span>
                        <select form="editForm" name="status" class="form-select form-select-sm w-auto" style="max-width: 120px;">
                            <option value="draft" {{ $post->status == 'draft' ? 'selected' : '' }}>Draft</option>
                            <option value="published" {{ $post->status == 'published' ? 'selected' : '' }}>Published</option>
                        </select>
                      </div>
                      <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body small">Publish</span>
                        <input type="datetime-local" form="editForm" name="published_at" class="form-control form-control-sm w-auto" value="" style="max-width: 150px;">
                      </div>
                      <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body small">Slug</span>
                        <input type="text" form="editForm" name="slug" class="form-control form-control-sm w-auto" value="{{ $post->slug }}" placeholder="auto-generated" style="max-width: 120px;">
                      </div>
                      <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body small">Author</span>
                        <select form="editForm" name="author_id" class="form-select form-select-sm w-auto" style="max-width: 120px;">
                            <option value="1">Admin User</option>
                        </select>
                      </div>

                      <div class="form-check form-switch d-flex align-items-center gap-2 mb-0 mt-3">
                        <input class="form-check-input mt-0" type="checkbox" role="switch" id="allowComments" name="allow_comments" value="1" form="editForm" {{ $post->allow_comments ? 'checked' : '' }}>
                        <label class="form-check-label small text-body" for="allowComments">Discussion (Allow Comments)</label>
                      </div>

                      <div class="form-check form-switch d-flex align-items-center gap-2 mb-0 mt-3">
                        <input class="form-check-input mt-0" type="checkbox" role="switch" id="lockModifiedDate">
                        <label class="form-check-label small text-body" for="lockModifiedDate">Lock Modified Date</label>
                      </div>
                    </div>

                    <hr class="my-4 border-secondary-subtle">
                    
                    <!-- Categories Accordion -->
                    <div class="accordion accordion-flush" id="categoriesAccordion">
                      <div class="accordion-item bg-transparent border-0">
                        <h2 class="accordion-header">
                          <button class="accordion-button collapsed bg-transparent px-0 py-2 shadow-none text-body fw-medium" type="button" data-bs-toggle="collapse" data-bs-target="#categoriesCollapse">
                            Categories
                          </button>
                        </h2>
                        <div id="categoriesCollapse" class="accordion-collapse collapse" data-bs-parent="#categoriesAccordion">
                          <div class="accordion-body px-0 pt-3 pb-0">
                            <div class="mb-3" style="max-height: 150px; overflow-y: auto;" data-simplebar>
                              @foreach(\App\Models\Category::all() as $category)
                              <div class="form-check mb-1">
                                <input class="form-check-input" type="checkbox" id="cat{{ $category->id }}" name="categories[]" value="{{ $category->id }}" form="editForm" {{ $post->categories->contains($category->id) ? 'checked' : '' }}>
                                <label class="form-check-label small text-body" for="cat{{ $category->id }}">{{ $category->name }}</label>
                              </div>
                              @endforeach
                            </div>
                            <a href="#" class="text-decoration-none text-primary small d-flex align-items-center"><i class="fi fi-rr-add me-1"></i> Add New Category</a>
                          </div>
                        </div>
                      </div>
                    </div>

                    <hr class="my-4 border-secondary-subtle">

                    <!-- Tags Accordion -->
                    <div class="accordion accordion-flush" id="tagsAccordion">
                      <div class="accordion-item bg-transparent border-0">
                        <h2 class="accordion-header">
                          <button class="accordion-button collapsed bg-transparent px-0 py-2 shadow-none text-body fw-medium" type="button" data-bs-toggle="collapse" data-bs-target="#tagsCollapse">
                            Tags
                          </button>
                        </h2>
                        <div id="tagsCollapse" class="accordion-collapse collapse" data-bs-parent="#tagsAccordion">
                          <div class="accordion-body px-0 pt-3 pb-0">
                            <div class="input-group mb-2">
                              <input type="text" id="tagInput" class="form-control form-control-sm" placeholder="Add new tag" list="allTagsList">
                              <datalist id="allTagsList">
                                @foreach(\App\Models\Tag::all() as $t)
                                  <option value="{{ $t->name }}">
                                @endforeach
                              </datalist>
                              <button id="addTagBtn" class="btn btn-sm btn-outline-secondary" type="button">Add</button>
                            </div>
                            <small class="text-muted d-block mb-3">Separate tags with commas or Enter</small>
                            <div class="d-flex flex-wrap gap-2" id="tagsContainer">
                              @foreach($post->tags as $tag)
                                <div class="badge bg-secondary d-flex align-items-center gap-1 tag-badge">
                                  <span>{{ $tag->name }}</span>
                                  <i class="fi fi-rr-cross-small ms-1 cursor-pointer" onclick="this.parentElement.remove(); document.getElementById('tag_input_{{ str_replace(' ', '_', $tag->name) }}').remove();"></i>
                                </div>
                                <input type="hidden" form="editForm" name="tags[]" value="{{ $tag->name }}" id="tag_input_{{ str_replace(' ', '_', $tag->name) }}">
                              @endforeach
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                  </div>
                </div>

                <!-- Block Pane -->
                <div class="tab-pane fade" id="block-pane" role="tabpanel" aria-labelledby="block-tab">
                  <div class="card-body p-4">
                    
                    <!-- Block Header -->
                    <div class="d-flex align-items-start gap-3 mb-4">
                      <i class="fi fi-rr-paragraph fs-3 text-body mt-1"></i>
                      <div>
                        <h6 class="fw-bold mb-1 text-body">Paragraph</h6>
                        <p class="small text-muted mb-0">Start with the basic building block of all narrative.</p>
                      </div>
                    </div>
                    
                    <hr class="my-4 border-secondary-subtle">

                    <!-- Color Section -->
                    <div class="mb-4">
                      <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body fw-medium">Color</span>
                        <button class="btn btn-sm btn-link text-muted p-0 hover-dark"><i class="fi fi-rr-menu-dots-vertical"></i></button>
                      </div>
                      
                      <div class="border rounded bg-body">
                        <button class="btn w-100 text-start px-3 py-2 border-0 border-bottom d-flex align-items-center gap-3 rounded-0 bg-transparent text-body">
                          <div class="rounded-circle border" style="width: 20px; height: 20px; background: linear-gradient(135deg, transparent 45%, var(--bs-border-color) 45%, var(--bs-border-color) 55%, transparent 55%);"></div> Text
                        </button>
                        <button class="btn w-100 text-start px-3 py-2 border-0 d-flex align-items-center gap-3 rounded-0 bg-transparent text-primary fw-medium">
                          <div class="rounded-circle border border-primary" style="width: 20px; height: 20px; background: linear-gradient(135deg, transparent 45%, var(--bs-primary) 45%, var(--bs-primary) 55%, transparent 55%);"></div> Background
                        </button>
                      </div>
                    </div>

                    <hr class="my-4 border-secondary-subtle">

                    <!-- Typography Section -->
                    <div class="mb-4">
                      <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body fw-medium">Typography</span>
                        <button class="btn btn-sm btn-link text-muted p-0 hover-dark"><i class="fi fi-rr-menu-dots-vertical"></i></button>
                      </div>
                      
                      <div class="d-flex justify-content-between align-items-center mb-2">
                        <span class="text-muted small fw-medium" style="font-size: 0.75rem; letter-spacing: 0.5px;">FONT SIZE</span>
                        <button class="btn btn-sm btn-link text-body p-0 hover-dark"><i class="fi fi-rr-settings-sliders"></i></button>
                      </div>

                      <div class="btn-group w-100 border rounded" role="group">
                        <button type="button" class="btn btn-light bg-body border-0 border-end text-muted py-2 hover-dark" style="font-size: 0.85rem;">S</button>
                        <button type="button" class="btn btn-light bg-body border-0 border-end text-muted py-2 hover-dark" style="font-size: 0.85rem;">M</button>
                        <button type="button" class="btn btn-light bg-body border-0 border-end text-muted py-2 hover-dark" style="font-size: 0.85rem;">L</button>
                        <button type="button" class="btn btn-light bg-body border-0 text-muted py-2 hover-dark" style="font-size: 0.85rem;">XL</button>
                      </div>
                    </div>
                    
                    <hr class="my-4 border-secondary-subtle">
                    
                    <!-- Advanced Section -->
                    <div class="accordion accordion-flush" id="advancedAccordion">
                      <div class="accordion-item bg-transparent border-0">
                        <h2 class="accordion-header">
                          <button class="accordion-button collapsed bg-transparent px-0 py-2 shadow-none text-body fw-medium" type="button" data-bs-toggle="collapse" data-bs-target="#advancedCollapse">
                            Advanced
                          </button>
                        </h2>
                        <div id="advancedCollapse" class="accordion-collapse collapse" data-bs-parent="#advancedAccordion">
                          <div class="accordion-body px-0 pt-3 pb-0">
                            <label class="form-label text-muted small fw-medium mb-2" style="font-size: 0.75rem; letter-spacing: 0.5px;">HTML ANCHOR</label>
                            <input type="text" class="form-control mb-3">
                            <p class="small text-muted mb-4" style="font-size: 0.8rem; line-height: 1.5;">Enter a word or two &mdash; without spaces &mdash; to make a unique web address just for this block, called an "anchor". Then, you'll be able to link directly to this section of your page. <a href="#" class="text-decoration-none">Learn more about anchors <i class="fi fi-rr-arrow-up-right small"></i></a></p>
                            
                            <label class="form-label text-muted small fw-medium mb-2" style="font-size: 0.75rem; letter-spacing: 0.5px;">ADDITIONAL CSS CLASS(ES)</label>
                            <input type="text" class="form-control">
                          </div>
                        </div>
                      </div>
                    </div>

                  </div>
                </div>

              </div>
            </div>
          </div>
        </div>
        </form>

      </div>
    </main>
    <!-- end::Main Content Area -->

    <!-- begin::Footer -->
    <footer class="footer-wrapper bg-body border-top mt-auto">
      <div class="container-fluid">
        <div class="row g-2 align-items-center">
          <div class="col-lg-6 col-md-7 text-center text-md-start">
            <p class="mb-0 text-muted">Thank you for creating with <a href="#" class="text-decoration-none fw-medium">Laravel CMS</a>.</p>
          </div>
          <div class="col-lg-6 col-md-5">
            <ul class="d-flex list-inline mb-0 gap-3 flex-wrap justify-content-center justify-content-md-end">
              <li><span class="text-muted fw-medium">Version 1.0.0</span></li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
    <!-- end::Footer -->

  </div>

  <!-- begin::NexLink Page Scripts -->
  <script src="/assets/libs/global/global.min.js"></script>
  <script src="/assets/libs/sortable/Sortable.min.js"></script>
  <script src="/assets/libs/chartjs/chart.js"></script>
  <script src="/assets/libs/flatpickr/flatpickr.min.js"></script>
  <script src="/assets/libs/apexcharts/apexcharts.min.js"></script>
  <script src="/assets/js/plugins/todolist.js"></script>
  <script src="/assets/js/appSettings.js"></script>
  <script src="/assets/js/main.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@editorjs/editorjs@latest"></script>
  <script src="https://cdn.jsdelivr.net/npm/@editorjs/header@latest"></script>
  <script src="https://cdn.jsdelivr.net/npm/@editorjs/list@latest"></script>
  <!-- end::NexLink Page Scripts -->

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const tagInput = document.getElementById('tagInput');
      const addTagBtn = document.getElementById('addTagBtn');
      const tagsContainer = document.getElementById('tagsContainer');
      const editForm = document.getElementById('editForm');
      
      function addTag(tagName) {
        tagName = tagName.trim();
        if(!tagName) return;
        
        // Check if already added
        const existing = Array.from(tagsContainer.querySelectorAll('.tag-badge span')).map(el => el.textContent);
        if(existing.includes(tagName)) return;

        // Create badge
        const badge = document.createElement('div');
        badge.className = 'badge bg-secondary d-flex align-items-center gap-1 tag-badge';
        badge.innerHTML = `<span>${tagName}</span> <i class="fi fi-rr-cross-small ms-1 cursor-pointer" onclick="this.parentElement.remove(); document.getElementById('tag_input_${tagName.replace(/ /g, '_')}').remove();"></i>`;
        
        // Create hidden input
        const hiddenInput = document.createElement('input');
        hiddenInput.type = 'hidden';
        hiddenInput.name = 'tags[]';
        hiddenInput.value = tagName;
        hiddenInput.id = `tag_input_${tagName.replace(/ /g, '_')}`;
        hiddenInput.setAttribute('form', 'editForm');
        
        tagsContainer.appendChild(badge);
        editForm.appendChild(hiddenInput);
      }
      
      if(addTagBtn) {
          addTagBtn.addEventListener('click', function() {
            addTag(tagInput.value);
            tagInput.value = '';
          });
          
          tagInput.addEventListener('keydown', function(e) {
            if(e.key === ',' || e.key === 'Enter') {
                e.preventDefault();
                addTag(this.value);
                this.value = '';
            }
          });
      }

      const postTitleInput = document.getElementById('postTitle');
      const sidebarPostTitle = document.getElementById('sidebarPostTitle');
      if (postTitleInput && sidebarPostTitle) {
          postTitleInput.addEventListener('input', function() {
              sidebarPostTitle.textContent = this.value.trim() || 'No title';
          });
      }
    });
  </script>
  <script src="https://cdn.jsdelivr.net/npm/@editorjs/paragraph@latest"></script>
  <script src="https://cdn.jsdelivr.net/npm/@editorjs/image@2.3.0"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      let editorData = document.getElementById('contentInput').value || '{"blocks":[]}';
      
      let parsedData = {"blocks":[]};
      try {
          parsedData = typeof editorData === 'string' ? JSON.parse(editorData) : editorData;
      } catch (e) { console.log(e); }

      const editor = new EditorJS({
        holder: 'editorjs',
        tools: {
          header: { class: Header, inlineToolbar: true },
          list: { class: typeof EditorjsList !== 'undefined' ? EditorjsList : List, inlineToolbar: true },
          paragraph: { class: Paragraph, inlineToolbar: true },
          image: {
            class: ImageTool,
            config: {
              endpoints: {
                byFile: '{{ route('admin.upload.image') }}',
                byUrl: '{{ route('admin.upload.fetchUrl') }}',
              },
              additionalRequestHeaders: {
                'X-CSRF-TOKEN': '{{ csrf_token() }}'
              }
            }
          }
        },
        data: parsedData,
        onChange: () => {
          editor.save().then((outputData) => {
            document.getElementById('contentInput').value = JSON.stringify(outputData);
          });
        },
        onReady: () => {
            editor.save().then((outputData) => {
                document.getElementById('contentInput').value = JSON.stringify(outputData);
            });
        }
      });
    });
  </script>
  <!-- end::NexLink Page Scripts -->


  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const postTab = document.getElementById('post-tab');
      const blockTab = document.getElementById('block-tab');
      
      if(postTab && blockTab) {
        postTab.addEventListener('shown.bs.tab', function (event) {
          postTab.classList.add('text-body');
          postTab.classList.remove('text-muted');
          postTab.style.boxShadow = 'inset 0 -2px 0 0 var(--bs-dark)';
          
          blockTab.classList.remove('text-body');
          blockTab.classList.add('text-muted');
          blockTab.style.boxShadow = 'none';
        });
        
        blockTab.addEventListener('shown.bs.tab', function (event) {
          blockTab.classList.add('text-body');
          blockTab.classList.remove('text-muted');
          blockTab.style.boxShadow = 'inset 0 -2px 0 0 var(--bs-dark)';
          
          postTab.classList.remove('text-body');
          postTab.classList.add('text-muted');
          postTab.style.boxShadow = 'none';
        });
      }
    });
  </script>
</body>
</html>
