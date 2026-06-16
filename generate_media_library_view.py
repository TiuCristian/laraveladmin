import sys
import os

with open('resources/views/admin/dashboard.blade.php', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace active classes in sidebar
content = content.replace('class="menu-link active" href="{{ route(\'admin.dashboard\') }}"', 'class="menu-link" href="{{ route(\'admin.dashboard\') }}"')
content = content.replace('<li class="menu-item wp-has-submenu wp-has-current-submenu wp-menu-open">\n                    <a class="menu-link active" href="{{ route(\'admin.dashboard\') }}">', '<li class="menu-item wp-has-submenu">\n                    <a class="menu-link" href="{{ route(\'admin.dashboard\') }}">')

content = content.replace('<li class="menu-item wp-has-submenu">\n                    <a class="menu-link" href="media-list.html">\n                      <i class="fi fi-rr-picture"></i><span class="menu-label">Media</span>\n                    </a>', '<li class="menu-item wp-has-submenu wp-has-current-submenu wp-menu-open">\n                    <a class="menu-link active" href="{{ route(\'media.index\') }}">\n                      <i class="fi fi-rr-picture"></i><span class="menu-label">Media</span>\n                    </a>')
content = content.replace('<li class="wp-first-item"><a href="media-list.html" class="wp-first-item">Library</a></li>', '<li class="wp-first-item current"><a href="{{ route(\'media.index\') }}" class="wp-first-item current">Library</a></li>')

main_start = content.find('<main class="app-wrapper">')
main_end = content.find('</main>') + len('</main>')

before_main = content[:main_start]
after_main = content[main_end:]

media_main = """<main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0 d-inline-block me-2">Media Library</h3>
            <button class="btn btn-outline-primary btn-sm mb-1 waves-effect" type="button" data-bs-toggle="collapse" data-bs-target="#uploadZone" aria-expanded="false" aria-controls="uploadZone">
              Add New
            </button>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="{{ route('admin.dashboard') }}">Home</a></li>
                <li class="breadcrumb-item active" aria-current="page">Media</li>
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

        <!-- Upload Zone (Collapsible) -->
        <div class="collapse mb-4" id="uploadZone">
          <div class="card border-0 shadow-sm bg-light">
            <div class="card-body text-center py-5 m-3 rounded" style="border: 2px dashed var(--bs-primary);">
              <form action="{{ route('media.store') }}" class="dropzone" id="mediaDropzone" style="background: transparent; border: none;">
                @csrf
                <div class="dz-message" data-dz-message>
                  <div class="mb-3">
                    <i class="fi fi-rr-cloud-upload text-primary" style="font-size: 3rem;"></i>
                  </div>
                  <h4 class="fw-bold">Drop files to upload</h4>
                  <p class="text-muted mb-3">or</p>
                  <button type="button" class="btn btn-primary px-4 waves-effect">Select Files</button>
                  <p class="text-muted small mt-3 mb-0">Maximum upload file size: 50 MB.</p>
                </div>
              </form>
            </div>
          </div>
        </div>

        <!-- Filters & Views Row -->
        <div class="row mb-3">
          <div class="col-12 d-flex flex-wrap align-items-center justify-content-between gap-3">
            
            <!-- Left Side Controls -->
            <div class="d-flex flex-wrap align-items-center gap-3">
              <!-- View Switcher -->
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-sm btn-primary active"><i class="fi fi-rr-apps"></i></button>
                <button type="button" class="btn btn-sm btn-outline-secondary bg-white"><i class="fi fi-rr-list"></i></button>
              </div>
              
              <!-- Dropdown Filters -->
              <div class="d-flex align-items-center gap-2">
                <select class="form-select form-select-sm" style="width: auto;">
                  <option>All media items</option>
                  <option>Images</option>
                  <option>Audio</option>
                  <option>Video</option>
                  <option>Documents</option>
                </select>
              </div>
            </div>
            
            <!-- Right Side Controls (Search) -->
            <div class="d-flex align-items-center gap-2">
              <form action="{{ route('media.index') }}" method="GET" class="input-group input-group-sm">
                <input type="text" name="search" value="{{ request('search') }}" class="form-control bg-white" placeholder="Search media items...">
                <button class="btn btn-primary" type="submit"><i class="fi fi-rr-search"></i></button>
              </form>
            </div>
            
          </div>
        </div>

        <!-- Media Grid -->
        <div class="row g-3 mb-4">
          
          @forelse($mediaItems as $media)
          <div class="col-6 col-sm-4 col-md-3 col-lg-2 col-xl-2">
            <div class="card border border-light shadow-sm h-100 overflow-hidden position-relative media-item rounded">
              @if(str_starts_with($media->mime_type, 'image/'))
              <div class="bg-light d-flex align-items-center justify-content-center h-100 w-100" style="aspect-ratio: 1/1;">
                <img src="{{ $media->url }}" alt="{{ $media->alt_text ?? $media->filename }}" class="img-fluid w-100 h-100" style="object-fit: cover;">
              </div>
              @elseif(str_starts_with($media->mime_type, 'video/'))
              <div class="bg-dark d-flex flex-column align-items-center justify-content-center h-100 w-100 p-3" style="aspect-ratio: 1/1;">
                <i class="fi fi-rr-play-alt fs-1 text-white opacity-75 mb-2"></i>
                <span class="small text-white opacity-75 fw-medium text-truncate w-100 text-center" title="{{ $media->filename }}">{{ $media->filename }}</span>
              </div>
              @elseif(str_starts_with($media->mime_type, 'audio/'))
              <div class="bg-light d-flex flex-column align-items-center justify-content-center h-100 w-100 p-3" style="aspect-ratio: 1/1;">
                <i class="fi fi-rr-music-alt fs-1 text-info mb-2"></i>
                <span class="small text-dark fw-medium text-truncate w-100 text-center" title="{{ $media->filename }}">{{ $media->filename }}</span>
              </div>
              @else
              <div class="bg-light d-flex flex-column align-items-center justify-content-center h-100 w-100 p-3" style="aspect-ratio: 1/1;">
                <i class="fi fi-rr-document fs-1 text-primary mb-2"></i>
                <span class="small text-dark fw-medium text-truncate w-100 text-center" title="{{ $media->filename }}">{{ $media->filename }}</span>
              </div>
              @endif
              
              <!-- Hover Overlay -->
              <div class="position-absolute top-0 start-0 w-100 h-100 media-overlay d-flex flex-column align-items-center justify-content-center p-2">
                <a href="#" class="btn btn-sm btn-light w-100 mb-2 fw-medium">View/Edit</a>
                <form action="{{ route('media.destroy', $media->id) }}" method="POST" class="w-100" onsubmit="return confirm('Are you sure you want to delete this media item?');">
                    @csrf
                    @method('DELETE')
                    <button type="submit" class="btn btn-sm btn-danger w-100 fw-medium"><i class="fi fi-rr-trash me-1"></i> Delete</button>
                </form>
              </div>
            </div>
          </div>
          @empty
          <div class="col-12 text-center py-5">
              <p class="text-muted">No media items found.</p>
          </div>
          @endforelse
          
        </div>

        <!-- Pagination -->
        <div class="d-flex justify-content-center mt-4">
          {{ $mediaItems->links('pagination::bootstrap-5') }}
        </div>

      </div>
    </main>
"""

# Inject Dropzone CSS and JS into the layout
head_end = before_main.find('</head>')
if head_end != -1:
    before_main = before_main[:head_end] + '  <link rel="stylesheet" href="https://unpkg.com/dropzone@5/dist/min/dropzone.min.css" type="text/css" />\n' + before_main[head_end:]

body_end = after_main.find('</body>')
if body_end != -1:
    dz_script = """
    <script src="https://unpkg.com/dropzone@5/dist/min/dropzone.min.js"></script>
    <script>
        Dropzone.options.mediaDropzone = {
            paramName: "file",
            maxFilesize: 50, // MB
            acceptedFiles: "image/*,audio/*,video/*,application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            queuecomplete: function() {
                window.location.reload();
            }
        };
    </script>
"""
    after_main = after_main[:body_end] + dz_script + after_main[body_end:]

os.makedirs('resources/views/admin/media', exist_ok=True)
with open('resources/views/admin/media/index.blade.php', 'w', encoding='utf-8') as f:
    f.write(before_main + media_main + after_main)
print('Done!')
