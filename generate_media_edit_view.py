import sys
import os

with open('resources/views/admin/dashboard.blade.php', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace active classes in sidebar
content = content.replace('class="menu-link active" href="{{ route(\'admin.dashboard\') }}"', 'class="menu-link" href="{{ route(\'admin.dashboard\') }}"')
content = content.replace('<li class="menu-item wp-has-submenu wp-has-current-submenu wp-menu-open">\n                    <a class="menu-link active" href="{{ route(\'admin.dashboard\') }}">', '<li class="menu-item wp-has-submenu">\n                    <a class="menu-link" href="{{ route(\'admin.dashboard\') }}">')

content = content.replace('<li class="menu-item wp-has-submenu">\n                    <a class="menu-link" href="{{ route(\'media.index\') }}">\n                      <i class="fi fi-rr-picture"></i><span class="menu-label">Media</span>\n                    </a>', '<li class="menu-item wp-has-submenu wp-has-current-submenu wp-menu-open">\n                    <a class="menu-link active" href="{{ route(\'media.index\') }}">\n                      <i class="fi fi-rr-picture"></i><span class="menu-label">Media</span>\n                    </a>')
# 'media-list.html' was already replaced by {{ route('media.index') }} in the script previously, so I'll target the correct text.

main_start = content.find('<main class="app-wrapper">')
main_end = content.find('</main>') + len('</main>')

before_main = content[:main_start]
after_main = content[main_end:]

edit_main = """<main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Edit Media</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="{{ route('admin.dashboard') }}">Home</a></li>
                <li class="breadcrumb-item"><a href="{{ route('media.index') }}">Media</a></li>
                <li class="breadcrumb-item active" aria-current="page">Edit Media</li>
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
          
          <!-- Left Column: Image & Metadata -->
          <div class="col-xl-8 col-lg-7 mb-4">
            
            <div class="card border-0 shadow-sm mb-4">
              <div class="card-body p-4 text-center bg-body-tertiary">
                @if(str_starts_with($media->mime_type, 'image/'))
                    <img src="{{ $media->url }}" class="img-fluid border shadow-sm rounded" style="max-height: 400px; object-fit: contain;" alt="{{ $media->alt_text ?? $media->filename }}">
                @elseif(str_starts_with($media->mime_type, 'video/'))
                    <video controls src="{{ $media->url }}" style="max-height: 400px; max-width: 100%;"></video>
                @elseif(str_starts_with($media->mime_type, 'audio/'))
                    <audio controls src="{{ $media->url }}"></audio>
                @else
                    <i class="fi fi-rr-document fs-1 text-primary"></i>
                    <p class="mt-3 mb-0">{{ $media->filename }}</p>
                @endif
                <div class="mt-3">
                  <button type="button" class="btn btn-outline-secondary btn-sm" disabled><i class="fi fi-rr-crop"></i> Edit Image</button>
                  <small class="d-block text-muted mt-1">Image cropping is not currently available.</small>
                </div>
              </div>
            </div>

            <form action="{{ route('media.update', $media->id) }}" method="POST" id="mediaEditForm">
              @csrf
              @method('PUT')
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-body p-4">
                  
                  <div class="row mb-4 align-items-start">
                    <label for="alt_text" class="col-sm-3 col-form-label fw-medium text-body text-sm-end">Alternative Text</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" name="alt_text" id="alt_text" value="{{ old('alt_text', $media->alt_text) }}">
                      <div class="form-text">Learn how to describe the purpose of the image. Leave empty if the image is purely decorative.</div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label for="title" class="col-sm-3 col-form-label fw-medium text-body text-sm-end">Title</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" name="title" id="title" value="{{ old('title', $media->title ?? $media->filename) }}">
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label for="caption" class="col-sm-3 col-form-label fw-medium text-body text-sm-end">Caption</label>
                    <div class="col-sm-9">
                      <textarea class="form-control" name="caption" id="caption" rows="3">{{ old('caption', $media->caption) }}</textarea>
                    </div>
                  </div>

                  <div class="row align-items-start">
                    <label for="description" class="col-sm-3 col-form-label fw-medium text-body text-sm-end">Description</label>
                    <div class="col-sm-9">
                      <textarea class="form-control" name="description" id="description" rows="5">{{ old('description', $media->description) }}</textarea>
                    </div>
                  </div>

                </div>
              </div>
            </form>

          </div>

          <!-- Right Column: Save & Details -->
          <div class="col-xl-4 col-lg-5">
            
            <div class="card border-0 shadow-sm mb-4">
              <div class="card-header bg-transparent border-bottom">
                <h6 class="fw-bold mb-0">Save</h6>
              </div>
              <div class="card-body p-4">
                
                <div class="small text-muted mb-4">
                  <div class="mb-2 d-flex justify-content-between border-bottom pb-2">
                    <span class="fw-medium text-body">Uploaded on:</span> 
                    <span>{{ $media->created_at->format('M d, Y \\a\\t g:i A') }}</span>
                  </div>
                  @if($media->user)
                  <div class="mb-2 d-flex justify-content-between border-bottom pb-2">
                    <span class="fw-medium text-body">Uploaded by:</span> 
                    <span>{{ $media->user->name }}</span>
                  </div>
                  @endif
                  <div class="mb-2 d-flex justify-content-between border-bottom pb-2">
                    <span class="fw-medium text-body">File name:</span> 
                    <span>{{ $media->filename }}</span>
                  </div>
                  <div class="mb-2 d-flex justify-content-between border-bottom pb-2">
                    <span class="fw-medium text-body">File type:</span> 
                    <span>{{ $media->mime_type }}</span>
                  </div>
                  <div class="mb-2 d-flex justify-content-between border-bottom pb-2">
                    <span class="fw-medium text-body">File size:</span> 
                    <span>{{ number_format($media->size / 1024, 2) }} KB</span>
                  </div>
                  @if($media->dimensions)
                  <div class="d-flex justify-content-between">
                    <span class="fw-medium text-body">Dimensions:</span> 
                    <span>{{ $media->dimensions }}</span>
                  </div>
                  @endif
                </div>

                <div class="mb-3">
                  <label class="form-label fw-medium text-body small">File URL:</label>
                  <input type="text" id="fileUrlInput" class="form-control form-control-sm bg-body-tertiary" value="{{ asset($media->url) }}" readonly>
                  <button type="button" class="btn btn-outline-secondary btn-sm mt-2 w-100" onclick="copyToClipboard()">Copy URL to clipboard</button>
                </div>

              </div>
              <div class="card-footer bg-body-tertiary border-top p-3 d-flex align-items-center justify-content-between">
                <form action="{{ route('media.destroy', $media->id) }}" method="POST" onsubmit="return confirm('Are you sure you want to delete this media item permanently?');" class="m-0">
                    @csrf
                    @method('DELETE')
                    <button type="submit" class="btn btn-link text-danger small text-decoration-none p-0 border-0 hover-danger" style="background:none;">Delete permanently</button>
                </form>
                <button type="button" class="btn btn-primary px-3 shadow-sm" onclick="document.getElementById('mediaEditForm').submit();">Update</button>
              </div>
            </div>

          </div>

        </div>

      </div>
    </main>
    <script>
        function copyToClipboard() {
            var copyText = document.getElementById("fileUrlInput");
            copyText.select();
            copyText.setSelectionRange(0, 99999); // For mobile devices
            navigator.clipboard.writeText(copyText.value).then(() => {
                alert("Copied URL to clipboard!");
            }).catch(err => {
                console.error('Failed to copy!', err);
            });
        }
    </script>
"""

with open('resources/views/admin/media/edit.blade.php', 'w', encoding='utf-8') as f:
    f.write(before_main + edit_main + after_main)
print('Done!')
