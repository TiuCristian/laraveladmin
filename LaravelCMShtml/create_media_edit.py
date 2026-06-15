import re

with open('c:/laragon/www/LaravelCMShtml/media-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Edit Media</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item"><a href="media-list.html">Media</a></li>
                <li class="breadcrumb-item active" aria-current="page">Edit Media</li>
              </ol>
            </nav>
          </div>
        </div>

        <div class="row">
          
          <!-- Left Column: Image & Metadata -->
          <div class="col-xl-8 col-lg-7 mb-4">
            
            <div class="card border-0 shadow-sm mb-4">
              <div class="card-body p-4 text-center bg-light">
                <img src="https://via.placeholder.com/800x400?text=Sample+Image" class="img-fluid border shadow-sm rounded" style="max-height: 400px; object-fit: contain;" alt="Sample Image">
                <div class="mt-3">
                  <button class="btn btn-outline-secondary btn-sm"><i class="fi fi-rr-crop"></i> Edit Image</button>
                </div>
              </div>
            </div>

            <form>
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-body p-4">
                  
                  <div class="row mb-4 align-items-start">
                    <label for="altText" class="col-sm-3 col-form-label fw-medium text-dark text-sm-end">Alternative Text</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" id="altText">
                      <div class="form-text">Learn how to describe the purpose of the image. Leave empty if the image is purely decorative.</div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label for="imageTitle" class="col-sm-3 col-form-label fw-medium text-dark text-sm-end">Title</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" id="imageTitle" value="sample-image-1">
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label for="imageCaption" class="col-sm-3 col-form-label fw-medium text-dark text-sm-end">Caption</label>
                    <div class="col-sm-9">
                      <textarea class="form-control" id="imageCaption" rows="3"></textarea>
                    </div>
                  </div>

                  <div class="row align-items-start">
                    <label for="imageDescription" class="col-sm-3 col-form-label fw-medium text-dark text-sm-end">Description</label>
                    <div class="col-sm-9">
                      <textarea class="form-control" id="imageDescription" rows="5"></textarea>
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
                    <span class="fw-medium text-dark">Uploaded on:</span> 
                    <span>Jun 12, 2026 at 10:42 AM</span>
                  </div>
                  <div class="mb-2 d-flex justify-content-between border-bottom pb-2">
                    <span class="fw-medium text-dark">File name:</span> 
                    <span>sample-image-1.jpg</span>
                  </div>
                  <div class="mb-2 d-flex justify-content-between border-bottom pb-2">
                    <span class="fw-medium text-dark">File type:</span> 
                    <span>image/jpeg</span>
                  </div>
                  <div class="mb-2 d-flex justify-content-between border-bottom pb-2">
                    <span class="fw-medium text-dark">File size:</span> 
                    <span>245 KB</span>
                  </div>
                  <div class="d-flex justify-content-between">
                    <span class="fw-medium text-dark">Dimensions:</span> 
                    <span>800 by 400 pixels</span>
                  </div>
                </div>

                <div class="mb-3">
                  <label class="form-label fw-medium text-dark small">File URL:</label>
                  <input type="text" class="form-control form-control-sm bg-light" value="http://localhost/uploads/2026/06/sample-image-1.jpg" readonly>
                  <button class="btn btn-outline-secondary btn-sm mt-2 w-100">Copy URL to clipboard</button>
                </div>

              </div>
              <div class="card-footer bg-light border-top p-3 d-flex align-items-center justify-content-between">
                <a href="#" class="text-danger small text-decoration-none hover-danger">Delete permanently</a>
                <button type="button" class="btn btn-primary px-3 shadow-sm">Update</button>
              </div>
            </div>

          </div>

        </div>

      </div>
    </main>
    <!-- end::Main Content Area -->'''

pattern = r'<!-- begin::Main Content Area -->.*?<!-- end::Main Content Area -->'
new_html = re.sub(pattern, main_content, html, flags=re.DOTALL)

with open('c:/laragon/www/LaravelCMShtml/media-edit.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created media-edit.html")
