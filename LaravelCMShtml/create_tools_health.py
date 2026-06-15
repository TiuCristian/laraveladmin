import re

with open('c:/laragon/www/LaravelCMShtml/tools-index.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Site Health</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item"><a href="tools-index.html">Tools</a></li>
                <li class="breadcrumb-item active" aria-current="page">Site Health</li>
              </ol>
            </nav>
          </div>
        </div>

        <ul class="nav nav-tabs mb-4">
          <li class="nav-item">
            <a class="nav-link active" href="#">Status</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-muted" href="#">Info</a>
          </li>
        </ul>

        <div class="row">
          <div class="col-lg-8 col-xl-6">
            
            <div class="card border-0 shadow-sm mb-4">
              <div class="card-body p-4 text-center">
                <div class="mb-3">
                  <div class="d-inline-flex align-items-center justify-content-center bg-success-subtle text-success rounded-circle" style="width: 80px; height: 80px;">
                    <i class="fi fi-rr-check fs-1"></i>
                  </div>
                </div>
                <h4 class="fw-bold mb-2">Good</h4>
                <p class="text-muted mb-0">Your site is currently passing all critical health checks.</p>
              </div>
            </div>

            <h5 class="fw-bold mb-3">1 Recommended Improvement</h5>
            
            <div class="accordion mb-4" id="healthAccordion">
              <div class="accordion-item border-0 shadow-sm mb-3 rounded overflow-hidden">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed py-3" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne">
                    <i class="fi fi-rr-shield-interrogation text-warning me-2"></i>
                    <span class="fw-medium text-dark">You should remove inactive plugins</span>
                  </button>
                </h2>
                <div id="collapseOne" class="accordion-collapse collapse" data-bs-parent="#healthAccordion">
                  <div class="accordion-body text-muted pt-0 pb-4">
                    <p>Plugins extend your site's functionality with things like contact forms, ecommerce and much more. That means they have deep access to your site, so it's vital to keep them up to date.</p>
                    <p class="mb-3">Your site has 2 inactive plugins, it is recommended to remove any unused plugins to enhance your site security.</p>
                    <a href="plugins-list.html" class="btn btn-outline-secondary btn-sm">Manage your plugins</a>
                  </div>
                </div>
              </div>
            </div>

            <h5 class="fw-bold mb-3">Passed Tests</h5>

            <div class="card border-0 shadow-sm mb-4">
              <ul class="list-group list-group-flush rounded">
                <li class="list-group-item py-3 d-flex align-items-center gap-3">
                  <i class="fi fi-rr-check-circle text-success"></i>
                  <span class="text-dark fw-medium">Your version of LaravelCMS is up to date</span>
                </li>
                <li class="list-group-item py-3 d-flex align-items-center gap-3">
                  <i class="fi fi-rr-check-circle text-success"></i>
                  <span class="text-dark fw-medium">Your server is running a supported version of PHP</span>
                </li>
                <li class="list-group-item py-3 d-flex align-items-center gap-3">
                  <i class="fi fi-rr-check-circle text-success"></i>
                  <span class="text-dark fw-medium">SQL server is up to date</span>
                </li>
                <li class="list-group-item py-3 d-flex align-items-center gap-3">
                  <i class="fi fi-rr-check-circle text-success"></i>
                  <span class="text-dark fw-medium">REST API is available</span>
                </li>
                <li class="list-group-item py-3 d-flex align-items-center gap-3">
                  <i class="fi fi-rr-check-circle text-success"></i>
                  <span class="text-dark fw-medium">Your site can communicate securely with other services</span>
                </li>
              </ul>
            </div>

          </div>
        </div>

      </div>
    </main>
    <!-- end::Main Content Area -->'''

pattern = r'<!-- begin::Main Content Area -->.*?<!-- end::Main Content Area -->'
new_html = re.sub(pattern, main_content, html, flags=re.DOTALL)

with open('c:/laragon/www/LaravelCMShtml/tools-health.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created tools-health.html")
