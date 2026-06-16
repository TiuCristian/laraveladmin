<!DOCTYPE html>
<html lang="en">
<head>
  <!-- begin::NexLink Meta Basic -->
  <meta charset="utf-8">
  <meta name="theme-color" content="#5955D1">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dashboard | CMS Admin Panel</title>
  
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
                <div class="fw-bold text-dark">{{ auth()->user()->name }}</div>
                <small class="text-body d-block lh-sm" style="text-transform: capitalize;">{{ auth()->user()->role }}</small>
              </div>
              <div class="avatar avatar-sm rounded-circle avatar-status-success">
                <img src="{{ auth()->user()->avatar_url }}" alt="User Avatar" style="object-fit: cover; width: 100%; height: 100%;">
              </div>
            </a>
            <ul class="dropdown-menu dropdown-menu-end w-225px mt-1">
              <li><a class="dropdown-item d-flex align-items-center gap-2" href="{{ route('profile.edit') }}"><i class="fi fi-rr-user"></i> Edit Profile</a></li>
              <li><div class="dropdown-divider my-1"></div></li>
              <li><form action="{{ route('logout') }}" method="POST">@csrf<button type="submit" style="background: none; border: none; width: 100%; text-align: left;" class="dropdown-item d-flex align-items-center gap-2 text-danger"><i class="fi fi-sr-exit"></i> Log Out</button></form></li>
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
                    <a class="menu-link" href="{{ route('posts.index') }}">
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

                  <li class="menu-item wp-has-submenu wp-has-current-submenu wp-menu-open">
                    <a class="menu-link active" href="{{ route('settings.general') }}">
                      <i class="fi fi-rr-settings"></i><span class="menu-label">Settings</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Settings</li>
                      <li class="wp-first-item"><a href="{{ route('settings.general') }}" class="wp-first-item">General</a></li>
                      <li><a href="{{ route('settings.writing') }}">Writing</a></li>
                      <li><a href="{{ route('settings.reading') }}">Reading</a></li>
                      <li><a href="{{ route('settings.discussion') }}">Discussion</a></li>
                      <li><a href="{{ route('settings.media') }}">Media</a></li>
                      <li class="current"><a href="{{ route('settings.permalinks') }}" class="current">Permalinks</a></li>
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
            <h3 class="mb-0">Permalink Settings</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="{{ route('admin.dashboard') }}">Home</a></li>
                <li class="breadcrumb-item"><a href="{{ route('settings.general') }}">Settings</a></li>
                <li class="breadcrumb-item active" aria-current="page">Permalinks</li>
              </ol>
            </nav>
          </div>
        </div>

        @if(session('success'))
            <div class="alert alert-success alert-dismissible fade show mb-4" role="alert">
                {{ session('success') }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        @endif

        <div class="row">
          <div class="col-lg-10 col-xl-8">
            <form action="{{ route('settings.permalinks.update') }}" method="POST">
              @csrf
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-body p-4">
                  
                  <p class="text-muted mb-4">Laravel CMS offers you the ability to create a custom URL structure for your permalinks and archives. Custom URL structures can improve the aesthetics, usability, and forward-compatibility of your links.</p>

                  <h5 class="fw-bold mb-4">Common Settings</h5>

                  <div class="row mb-4 align-items-start">
                    <div class="col-12">
                      @php $p_struct = old('permalink_structure', $settings['permalink_structure'] ?? '/%postname%/'); @endphp
                      
                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalink_structure" id="plain" value="plain" {{ $p_struct == 'plain' ? 'checked' : '' }}>
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="plain">Plain</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">{{ url('/') }}/?p=123</code>
                      </div>

                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalink_structure" id="dayName" value="/%year%/%monthnum%/%day%/%postname%/" {{ $p_struct == '/%year%/%monthnum%/%day%/%postname%/' ? 'checked' : '' }}>
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="dayName">Day and name</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">{{ url('/') }}/{{ date('Y/m/d') }}/sample-post/</code>
                      </div>

                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalink_structure" id="monthName" value="/%year%/%monthnum%/%postname%/" {{ $p_struct == '/%year%/%monthnum%/%postname%/' ? 'checked' : '' }}>
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="monthName">Month and name</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">{{ url('/') }}/{{ date('Y/m') }}/sample-post/</code>
                      </div>

                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalink_structure" id="numeric" value="/archives/%post_id%" {{ $p_struct == '/archives/%post_id%' ? 'checked' : '' }}>
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="numeric">Numeric</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">{{ url('/') }}/archives/123</code>
                      </div>

                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalink_structure" id="postName" value="/%postname%/" {{ $p_struct == '/%postname%/' ? 'checked' : '' }}>
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="postName">Post name</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">{{ url('/') }}/sample-post/</code>
                      </div>

                      <div class="form-check mb-3 d-flex flex-wrap align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalink_structure" id="custom" value="custom" {{ !in_array($p_struct, ['plain', '/%year%/%monthnum%/%day%/%postname%/', '/%year%/%monthnum%/%postname%/', '/archives/%post_id%', '/%postname%/']) ? 'checked' : '' }}>
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="custom">Custom Structure</label>
                        <div class="d-flex align-items-center gap-1">
                          <code class="text-muted">{{ url('/') }}</code>
                          <input type="text" name="custom_permalink_structure" class="form-control form-control-sm font-monospace" style="width: 300px;" value="{{ old('custom_permalink_structure', (!in_array($p_struct, ['plain', '/%year%/%monthnum%/%day%/%postname%/', '/%year%/%monthnum%/%postname%/', '/archives/%post_id%', '/%postname%/']) ? $p_struct : '/%postname%/')) }}">
                        </div>
                      </div>

                      <div class="ps-4 mt-2">
                        <p class="small text-muted mb-2">Available tags:</p>
                        <div class="d-flex flex-wrap gap-2">
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%year%')">%year%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%monthnum%')">%monthnum%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%day%')">%day%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%hour%')">%hour%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%minute%')">%minute%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%second%')">%second%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%post_id%')">%post_id%</button>
                          <button type="button" class="btn btn-sm btn-primary" onclick="appendTag('%postname%')">%postname%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%category%')">%category%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%author%')">%author%</button>
                        </div>
                      </div>

                    </div>
                  </div>

                  <hr class="my-4">

                  <h5 class="fw-bold mb-4">Optional</h5>
                  <p class="text-muted small mb-4">If you like, you may enter custom structures for your category and tag URLs here. For example, using <code>topics</code> as your category base would make your category links like <code>{{ url('/') }}/topics/uncategorized/</code>. If you leave these blank the defaults will be used.</p>

                  <div class="row mb-3 align-items-center">
                    <label for="category_base" class="col-sm-4 col-form-label fw-medium text-dark">Category base</label>
                    <div class="col-sm-8">
                      <input type="text" name="category_base" class="form-control" id="category_base" value="{{ old('category_base', $settings['category_base'] ?? '') }}">
                    </div>
                  </div>

                  <div class="row align-items-center">
                    <label for="tag_base" class="col-sm-4 col-form-label fw-medium text-dark">Tag base</label>
                    <div class="col-sm-8">
                      <input type="text" name="tag_base" class="form-control" id="tag_base" value="{{ old('tag_base', $settings['tag_base'] ?? '') }}">
                    </div>
                  </div>

                </div>
              </div>
              
              <div class="mb-5 pb-5">
                <button type="submit" class="btn btn-primary px-4 py-2 fw-bold shadow-sm waves-effect">Save Changes</button>
              </div>

            </form>
          </div>
        </div>

      </div>
    </main>
    <script>
        function appendTag(tag) {
            document.getElementById('custom').checked = true;
            let input = document.querySelector('input[name="custom_permalink_structure"]');
            if (input.value && !input.value.endsWith('/')) {
                input.value += '/';
            }
            input.value += tag + '/';
        }
    </script>
    
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
  <script src="/assets/libs/datatables/datatables.min.js"></script>
  <script src="/assets/js/plugins/todolist.js"></script>
  <script src="/assets/js/appSettings.js"></script>
  <script src="/assets/js/main.js"></script>
  <!-- end::NexLink Page Scripts -->
</body>
</html>

