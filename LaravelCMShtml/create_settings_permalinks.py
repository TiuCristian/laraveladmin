import re

with open('c:/laragon/www/LaravelCMShtml/settings-general.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Permalink Settings</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item"><a href="settings-general.html">Settings</a></li>
                <li class="breadcrumb-item active" aria-current="page">Permalinks</li>
              </ol>
            </nav>
          </div>
        </div>

        <div class="row">
          <div class="col-lg-10 col-xl-8">
            <form>
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-body p-4">
                  
                  <p class="text-muted mb-4">WordPress offers you the ability to create a custom URL structure for your permalinks and archives. Custom URL structures can improve the aesthetics, usability, and forward-compatibility of your links.</p>

                  <h5 class="fw-bold mb-4">Common Settings</h5>

                  <div class="row mb-4 align-items-start">
                    <div class="col-12">
                      
                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalinkStructure" id="plain">
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="plain">Plain</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">http://example.com/?p=123</code>
                      </div>

                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalinkStructure" id="dayName">
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="dayName">Day and name</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">http://example.com/2026/06/12/sample-post/</code>
                      </div>

                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalinkStructure" id="monthName">
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="monthName">Month and name</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">http://example.com/2026/06/sample-post/</code>
                      </div>

                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalinkStructure" id="numeric">
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="numeric">Numeric</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">http://example.com/archives/123</code>
                      </div>

                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalinkStructure" id="postName" checked>
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="postName">Post name</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">http://example.com/sample-post/</code>
                      </div>

                      <div class="form-check mb-3 d-flex flex-wrap align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalinkStructure" id="custom">
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="custom">Custom Structure</label>
                        <div class="d-flex align-items-center gap-1">
                          <code class="text-muted">http://example.com</code>
                          <input type="text" class="form-control form-control-sm font-monospace" style="width: 300px;" value="/%postname%/">
                        </div>
                      </div>

                      <div class="ps-4 mt-2">
                        <p class="small text-muted mb-2">Available tags:</p>
                        <div class="d-flex flex-wrap gap-2">
                          <button type="button" class="btn btn-sm btn-light border">%year%</button>
                          <button type="button" class="btn btn-sm btn-light border">%monthnum%</button>
                          <button type="button" class="btn btn-sm btn-light border">%day%</button>
                          <button type="button" class="btn btn-sm btn-light border">%hour%</button>
                          <button type="button" class="btn btn-sm btn-light border">%minute%</button>
                          <button type="button" class="btn btn-sm btn-light border">%second%</button>
                          <button type="button" class="btn btn-sm btn-light border">%post_id%</button>
                          <button type="button" class="btn btn-sm btn-primary">%postname%</button>
                          <button type="button" class="btn btn-sm btn-light border">%category%</button>
                          <button type="button" class="btn btn-sm btn-light border">%author%</button>
                        </div>
                      </div>

                    </div>
                  </div>

                  <hr class="my-4">

                  <h5 class="fw-bold mb-4">Optional</h5>
                  <p class="text-muted small mb-4">If you like, you may enter custom structures for your category and tag URLs here. For example, using <code>topics</code> as your category base would make your category links like <code>http://example.com/topics/uncategorized/</code>. If you leave these blank the defaults will be used.</p>

                  <div class="row mb-3 align-items-center">
                    <label for="categoryBase" class="col-sm-4 col-form-label fw-medium text-dark">Category base</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" id="categoryBase">
                    </div>
                  </div>

                  <div class="row align-items-center">
                    <label for="tagBase" class="col-sm-4 col-form-label fw-medium text-dark">Tag base</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" id="tagBase">
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

with open('c:/laragon/www/LaravelCMShtml/settings-permalinks.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created settings-permalinks.html")
