import sys

with open('resources/views/admin/settings/discussion.blade.php', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace active classes in sidebar
content = content.replace('<li class="current"><a href="{{ route(\'settings.discussion\') }}" class="current">Discussion</a></li>', '<li><a href="{{ route(\'settings.discussion\') }}">Discussion</a></li>')
content = content.replace('<li><a href="settings-media.html">Media</a></li>', '<li class="current"><a href="{{ route(\'settings.media\') }}" class="current">Media</a></li>')

main_start = content.find('<main class="app-wrapper">')
main_end = content.find('</main>') + len('</main>')

before_main = content[:main_start]
after_main = content[main_end:]

media_main = """<main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Media Settings</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="{{ route('admin.dashboard') }}">Home</a></li>
                <li class="breadcrumb-item"><a href="{{ route('settings.general') }}">Settings</a></li>
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

        <div class="row">
          <div class="col-lg-10 col-xl-8">
            <form action="{{ route('settings.media.update') }}" method="POST">
              @csrf
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-body p-4">
                  
                  <h5 class="fw-bold mb-4">Image sizes</h5>
                  <p class="text-muted small mb-4">The sizes listed below determine the maximum dimensions in pixels to use when adding an image to the Media Library.</p>

                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Thumbnail size</label>
                    <div class="col-sm-8">
                      <div class="d-flex flex-wrap align-items-center gap-3 mb-2">
                        <div class="d-flex align-items-center gap-2">
                          <label for="thumbnail_size_w" class="col-form-label small">Width</label>
                          <input type="number" class="form-control form-control-sm" name="thumbnail_size_w" id="thumbnail_size_w" value="{{ old('thumbnail_size_w', $settings['thumbnail_size_w'] ?? '150') }}" style="width: 80px;">
                        </div>
                        <div class="d-flex align-items-center gap-2">
                          <label for="thumbnail_size_h" class="col-form-label small">Height</label>
                          <input type="number" class="form-control form-control-sm" name="thumbnail_size_h" id="thumbnail_size_h" value="{{ old('thumbnail_size_h', $settings['thumbnail_size_h'] ?? '150') }}" style="width: 80px;">
                        </div>
                      </div>
                      <div class="form-check mt-2">
                        <input class="form-check-input" type="checkbox" name="thumbnail_crop" value="1" id="thumbnail_crop" {{ old('thumbnail_crop', $settings['thumbnail_crop'] ?? '1') == '1' ? 'checked' : '' }}>
                        <label class="form-check-label text-dark small" for="thumbnail_crop">Crop thumbnail to exact dimensions (normally thumbnails are proportional)</label>
                      </div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Medium size</label>
                    <div class="col-sm-8">
                      <div class="d-flex flex-wrap align-items-center gap-3">
                        <div class="d-flex align-items-center gap-2">
                          <label for="medium_size_w" class="col-form-label small">Max Width</label>
                          <input type="number" class="form-control form-control-sm" name="medium_size_w" id="medium_size_w" value="{{ old('medium_size_w', $settings['medium_size_w'] ?? '300') }}" style="width: 80px;">
                        </div>
                        <div class="d-flex align-items-center gap-2">
                          <label for="medium_size_h" class="col-form-label small">Max Height</label>
                          <input type="number" class="form-control form-control-sm" name="medium_size_h" id="medium_size_h" value="{{ old('medium_size_h', $settings['medium_size_h'] ?? '300') }}" style="width: 80px;">
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Large size</label>
                    <div class="col-sm-8">
                      <div class="d-flex flex-wrap align-items-center gap-3">
                        <div class="d-flex align-items-center gap-2">
                          <label for="large_size_w" class="col-form-label small">Max Width</label>
                          <input type="number" class="form-control form-control-sm" name="large_size_w" id="large_size_w" value="{{ old('large_size_w', $settings['large_size_w'] ?? '1024') }}" style="width: 80px;">
                        </div>
                        <div class="d-flex align-items-center gap-2">
                          <label for="large_size_h" class="col-form-label small">Max Height</label>
                          <input type="number" class="form-control form-control-sm" name="large_size_h" id="large_size_h" value="{{ old('large_size_h', $settings['large_size_h'] ?? '1024') }}" style="width: 80px;">
                        </div>
                      </div>
                    </div>
                  </div>

                  <hr class="my-4">

                  <h5 class="fw-bold mb-4">Uploading Files</h5>

                  <div class="row align-items-start">
                    <div class="col-sm-8 offset-sm-4 pt-2">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="uploads_use_yearmonth_folders" value="1" id="uploads_use_yearmonth_folders" {{ old('uploads_use_yearmonth_folders', $settings['uploads_use_yearmonth_folders'] ?? '1') == '1' ? 'checked' : '' }}>
                        <label class="form-check-label text-dark" for="uploads_use_yearmonth_folders">Organize my uploads into month- and year-based folders</label>
                      </div>
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
    </main>"""

with open('resources/views/admin/settings/media.blade.php', 'w', encoding='utf-8') as f:
    f.write(before_main + media_main + after_main)
print('Done!')
