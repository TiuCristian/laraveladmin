import sys

with open('resources/views/admin/dashboard.blade.php', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace active classes in sidebar
content = content.replace('class="menu-link active" href="{{ route(\'admin.dashboard\') }}"', 'class="menu-link" href="{{ route(\'admin.dashboard\') }}"')
content = content.replace('<li class="menu-item wp-has-submenu wp-has-current-submenu wp-menu-open">\n                    <a class="menu-link active" href="{{ route(\'admin.dashboard\') }}">', '<li class="menu-item wp-has-submenu">\n                    <a class="menu-link" href="{{ route(\'admin.dashboard\') }}">')

content = content.replace('<li class="menu-item wp-has-submenu">\n                    <a class="menu-link" href="{{ route(\'media.index\') }}">\n                      <i class="fi fi-rr-picture"></i><span class="menu-label">Media</span>\n                    </a>', '<li class="menu-item wp-has-submenu wp-has-current-submenu wp-menu-open">\n                    <a class="menu-link active" href="{{ route(\'media.index\') }}">\n                      <i class="fi fi-rr-picture"></i><span class="menu-label">Media</span>\n                    </a>')

main_start = content.find('<main class="app-wrapper">')
main_end = content.find('</main>') + len('</main>')

before_main = content[:main_start]
after_main = content[main_end:]

edit_main = """<main class="app-wrapper p-0 bg-secondary bg-opacity-10">
      <div class="container-fluid p-4">
        
        @if(session('success'))
            <div class="alert alert-success alert-dismissible fade show mb-4" role="alert">
                {{ session('success') }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        @endif

        <div class="card border-0 shadow-sm rounded-0">
          
          <!-- Modal-like Header -->
          <div class="card-header bg-white border-bottom py-3 d-flex align-items-center justify-content-between">
            <h5 class="mb-0 fw-bold fs-5">Attachment details</h5>
            <div class="d-flex align-items-center gap-1">
              <!-- Dummy nav buttons for visual fidelity -->
              <button type="button" class="btn btn-light btn-sm px-3 bg-white border"><i class="fi fi-rr-angle-left"></i></button>
              <button type="button" class="btn btn-light btn-sm px-3 bg-white border me-2"><i class="fi fi-rr-angle-right"></i></button>
              <a href="{{ route('media.index') }}" class="btn btn-light btn-sm px-3 bg-white border"><i class="fi fi-rr-cross"></i></a>
            </div>
          </div>

          <div class="card-body p-0">
            <div class="row g-0">
              
              <!-- Left Column: Image -->
              <div class="col-lg-7 p-4 bg-light border-end d-flex flex-column align-items-center justify-content-start" style="min-height: 600px;">
                @if(str_starts_with($media->mime_type, 'image/'))
                    <img src="{{ $media->url }}" class="img-fluid border shadow-sm w-100" style="max-height: 700px; object-fit: contain; background:#fff;" alt="{{ $media->alt_text ?? $media->filename }}">
                @elseif(str_starts_with($media->mime_type, 'video/'))
                    <video controls src="{{ $media->url }}" class="w-100 shadow-sm" style="max-height: 700px;"></video>
                @elseif(str_starts_with($media->mime_type, 'audio/'))
                    <audio controls src="{{ $media->url }}" class="w-100 mt-5"></audio>
                @else
                    <div class="d-flex flex-column align-items-center justify-content-center h-100 mt-5 pt-5">
                      <i class="fi fi-rr-document text-secondary" style="font-size: 8rem;"></i>
                      <h4 class="mt-4 fw-bold">{{ $media->filename }}</h4>
                    </div>
                @endif
                
                <div class="mt-4 text-center">
                  <button type="button" class="btn btn-outline-primary btn-sm px-4">Edit Image</button>
                </div>
              </div>

              <!-- Right Column: Metadata & Form -->
              <div class="col-lg-5 p-4 bg-white overflow-auto" style="max-height: 800px;">
                
                <!-- Metadata Section -->
                <div class="small mb-4 text-secondary" style="font-size: 0.85rem; line-height: 1.6;">
                  <div class="mb-1"><strong class="fw-semibold text-dark">Uploaded on:</strong> {{ $media->created_at->format('F j, Y') }}</div>
                  
                  @if($media->user)
                  <div class="mb-1"><strong class="fw-semibold text-dark">Uploaded by:</strong> <a href="#" class="text-decoration-none">{{ $media->user->name }}</a></div>
                  @endif
                  
                  <div class="mb-1"><strong class="fw-semibold text-dark">Uploaded to:</strong> <a href="#" class="text-decoration-none">(Unattached)</a></div>
                  <div class="mb-1"><strong class="fw-semibold text-dark">File name:</strong> {{ $media->filename }}</div>
                  <div class="mb-1"><strong class="fw-semibold text-dark">File type:</strong> {{ $media->mime_type }}</div>
                  <div class="mb-1"><strong class="fw-semibold text-dark">File size:</strong> {{ number_format($media->size / 1024 / 1024, 2) }} MB</div>
                  @if($media->dimensions)
                  <div class="mb-1"><strong class="fw-semibold text-dark">Dimensions:</strong> {{ $media->dimensions }}</div>
                  @endif
                  
                  <div class="mt-3">
                    <form action="{{ route('media.destroy', $media->id) }}" method="POST" onsubmit="return confirm('Are you sure you want to delete this media item permanently?');" class="d-inline">
                        @csrf
                        @method('DELETE')
                        <button type="submit" class="btn btn-link text-danger p-0 border-0 text-decoration-none small hover-danger" style="background:none;">Delete permanently</button>
                    </form>
                  </div>
                </div>

                <hr class="text-black-50 mb-4">

                <!-- Edit Form -->
                <form action="{{ route('media.update', $media->id) }}" method="POST" id="mediaEditForm">
                  @csrf
                  @method('PUT')
                  
                  <div class="mb-4 row">
                    <label for="alt_text" class="col-sm-4 col-form-label text-sm-end fw-medium text-secondary small pt-1">Alternative Text</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control form-control-sm" name="alt_text" id="alt_text" value="{{ old('alt_text', $media->alt_text) }}">
                      <div class="form-text small" style="font-size: 0.75rem;"><a href="#" class="text-decoration-none">Learn how to describe the purpose of the image.</a> Leave empty if the image is purely decorative.</div>
                    </div>
                  </div>

                  <div class="mb-3 row">
                    <label for="title" class="col-sm-4 col-form-label text-sm-end fw-medium text-secondary small pt-1">Title</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control form-control-sm" name="title" id="title" value="{{ old('title', $media->title ?? $media->filename) }}">
                    </div>
                  </div>

                  <div class="mb-3 row">
                    <label for="caption" class="col-sm-4 col-form-label text-sm-end fw-medium text-secondary small pt-1">Caption</label>
                    <div class="col-sm-8">
                      <textarea class="form-control form-control-sm" name="caption" id="caption" rows="3">{{ old('caption', $media->caption) }}</textarea>
                    </div>
                  </div>

                  <div class="mb-3 row">
                    <label for="description" class="col-sm-4 col-form-label text-sm-end fw-medium text-secondary small pt-1">Description</label>
                    <div class="col-sm-8">
                      <textarea class="form-control form-control-sm" name="description" id="description" rows="4">{{ old('description', $media->description) }}</textarea>
                    </div>
                  </div>

                  <div class="mb-3 row">
                    <label class="col-sm-4 col-form-label text-sm-end fw-medium text-secondary small pt-1">File URL:</label>
                    <div class="col-sm-8">
                      <input type="text" id="fileUrlInput" class="form-control form-control-sm bg-light" value="{{ asset($media->url) }}" readonly>
                      <button type="button" class="btn btn-outline-secondary btn-sm mt-2" onclick="copyToClipboard()">Copy URL to clipboard</button>
                    </div>
                  </div>

                  <div class="row mt-4">
                    <div class="col-sm-8 offset-sm-4">
                      <p class="text-danger small mb-3">Required fields are marked *</p>
                      <button type="submit" class="btn btn-primary btn-sm px-4 shadow-sm">Update Details</button>
                    </div>
                  </div>

                </form>

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
            copyText.setSelectionRange(0, 99999);
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
