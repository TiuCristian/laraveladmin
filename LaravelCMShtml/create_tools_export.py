import re

with open('c:/laragon/www/LaravelCMShtml/tools-index.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Export</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item"><a href="tools-index.html">Tools</a></li>
                <li class="breadcrumb-item active" aria-current="page">Export</li>
              </ol>
            </nav>
          </div>
        </div>

        <div class="row">
          <div class="col-lg-8 col-xl-6">
            <div class="card border-0 shadow-sm mb-4">
              <div class="card-body p-4">
                
                <p class="text-muted mb-4">When you click the button below LaravelCMS will create an XML file for you to save to your computer.</p>
                <p class="text-muted mb-4">This format, which we call LaravelCMS eXtended RSS or WXR, will contain your posts, pages, comments, custom fields, categories, and tags.</p>
                <p class="text-muted mb-4">Once you've saved the download file, you can use the Import function in another LaravelCMS installation to import the content from this site.</p>

                <h6 class="fw-bold mb-3">Choose what to export</h6>

                <form>
                  <div class="form-check mb-2">
                    <input class="form-check-input" type="radio" name="exportOption" id="exportAll" checked>
                    <label class="form-check-label fw-medium text-dark" for="exportAll">All content</label>
                    <div class="form-text mt-0">This will contain all of your posts, pages, comments, custom fields, terms, navigation menus, and custom posts.</div>
                  </div>

                  <div class="form-check mb-2">
                    <input class="form-check-input" type="radio" name="exportOption" id="exportPosts">
                    <label class="form-check-label fw-medium text-dark" for="exportPosts">Posts</label>
                  </div>

                  <div class="form-check mb-2">
                    <input class="form-check-input" type="radio" name="exportOption" id="exportPages">
                    <label class="form-check-label fw-medium text-dark" for="exportPages">Pages</label>
                  </div>

                  <div class="form-check mb-4">
                    <input class="form-check-input" type="radio" name="exportOption" id="exportMedia">
                    <label class="form-check-label fw-medium text-dark" for="exportMedia">Media</label>
                  </div>

                  <button type="submit" class="btn btn-primary px-4 waves-effect">Download Export File</button>
                </form>

              </div>
            </div>
          </div>
        </div>

      </div>
    </main>
    <!-- end::Main Content Area -->'''

pattern = r'<!-- begin::Main Content Area -->.*?<!-- end::Main Content Area -->'
new_html = re.sub(pattern, main_content, html, flags=re.DOTALL)

with open('c:/laragon/www/LaravelCMShtml/tools-export.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created tools-export.html")
