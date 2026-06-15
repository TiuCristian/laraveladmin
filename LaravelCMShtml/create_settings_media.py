import re

with open('c:/laragon/www/LaravelCMShtml/settings-general.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Media Settings</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item"><a href="settings-general.html">Settings</a></li>
                <li class="breadcrumb-item active" aria-current="page">Media</li>
              </ol>
            </nav>
          </div>
        </div>

        <div class="row">
          <div class="col-lg-10 col-xl-8">
            <form>
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-body p-4">
                  
                  <h5 class="fw-bold mb-4">Image sizes</h5>
                  <p class="text-muted small mb-4">The sizes listed below determine the maximum dimensions in pixels to use when adding an image to the Media Library.</p>

                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Thumbnail size</label>
                    <div class="col-sm-8">
                      <div class="d-flex flex-wrap align-items-center gap-3 mb-2">
                        <div class="d-flex align-items-center gap-2">
                          <label for="thumbWidth" class="col-form-label small">Width</label>
                          <input type="number" class="form-control form-control-sm" id="thumbWidth" value="150" style="width: 80px;">
                        </div>
                        <div class="d-flex align-items-center gap-2">
                          <label for="thumbHeight" class="col-form-label small">Height</label>
                          <input type="number" class="form-control form-control-sm" id="thumbHeight" value="150" style="width: 80px;">
                        </div>
                      </div>
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="cropThumbnail" checked>
                        <label class="form-check-label text-dark small" for="cropThumbnail">Crop thumbnail to exact dimensions (normally thumbnails are proportional)</label>
                      </div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Medium size</label>
                    <div class="col-sm-8">
                      <div class="d-flex flex-wrap align-items-center gap-3">
                        <div class="d-flex align-items-center gap-2">
                          <label for="mediumWidth" class="col-form-label small">Max Width</label>
                          <input type="number" class="form-control form-control-sm" id="mediumWidth" value="300" style="width: 80px;">
                        </div>
                        <div class="d-flex align-items-center gap-2">
                          <label for="mediumHeight" class="col-form-label small">Max Height</label>
                          <input type="number" class="form-control form-control-sm" id="mediumHeight" value="300" style="width: 80px;">
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Large size</label>
                    <div class="col-sm-8">
                      <div class="d-flex flex-wrap align-items-center gap-3">
                        <div class="d-flex align-items-center gap-2">
                          <label for="largeWidth" class="col-form-label small">Max Width</label>
                          <input type="number" class="form-control form-control-sm" id="largeWidth" value="1024" style="width: 80px;">
                        </div>
                        <div class="d-flex align-items-center gap-2">
                          <label for="largeHeight" class="col-form-label small">Max Height</label>
                          <input type="number" class="form-control form-control-sm" id="largeHeight" value="1024" style="width: 80px;">
                        </div>
                      </div>
                    </div>
                  </div>

                  <hr class="my-4">

                  <h5 class="fw-bold mb-4">Uploading Files</h5>

                  <div class="row align-items-start">
                    <div class="col-sm-8 offset-sm-4 pt-2">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="organizeUploads" checked>
                        <label class="form-check-label text-dark" for="organizeUploads">Organize my uploads into month- and year-based folders</label>
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
    </main>
    <!-- end::Main Content Area -->'''

pattern = r'<!-- begin::Main Content Area -->.*?<!-- end::Main Content Area -->'
new_html = re.sub(pattern, main_content, html, flags=re.DOTALL)

with open('c:/laragon/www/LaravelCMShtml/settings-media.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created settings-media.html")
