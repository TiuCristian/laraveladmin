import re

with open('c:/laragon/www/LaravelCMShtml/plugins-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the Plugins -> Add New active instead of Installed Plugins
# Wait, my fix_everything.py sets "plugins-list.html" active for everything with "plugins-".
# I'll just replace the main content first.

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0 d-inline-block me-2">Add Plugins</h3>
            <a href="#" class="btn btn-outline-primary btn-sm mb-1">Upload Plugin</a>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item"><a href="plugins-list.html">Plugins</a></li>
                <li class="breadcrumb-item active" aria-current="page">Add New</li>
              </ol>
            </nav>
          </div>
        </div>

        <!-- Navigation Tabs & Search -->
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-4 pb-2 border-bottom">
          <ul class="nav nav-pills nav-sm gap-1 mb-3 mb-md-0" style="font-size: 0.95rem;">
            <li class="nav-item"><a class="nav-link text-muted px-3 py-1" href="#">Featured</a></li>
            <li class="nav-item"><a class="nav-link active fw-medium px-3 py-1" href="#">Popular</a></li>
            <li class="nav-item"><a class="nav-link text-muted px-3 py-1" href="#">Recommended</a></li>
            <li class="nav-item"><a class="nav-link text-muted px-3 py-1" href="#">Favorites</a></li>
          </ul>
          
          <div class="d-flex align-items-center">
            <div class="input-group input-group-sm">
              <input type="text" class="form-control" placeholder="Search plugins..." style="width: 250px;">
              <button class="btn btn-primary" type="button"><i class="fi fi-rr-search"></i></button>
            </div>
          </div>
        </div>

        <!-- Plugins Grid -->
        <div class="row g-4 mb-4">
          
          <!-- Plugin Card 1 -->
          <div class="col-xl-4 col-md-6">
            <div class="card h-100 border-0 shadow-sm overflow-hidden">
              <div class="card-body p-4">
                <div class="d-flex align-items-start gap-3 mb-3">
                  <div class="avatar avatar-lg rounded shadow-sm bg-light flex-shrink-0">
                    <img src="https://via.placeholder.com/128?text=SEO" class="w-100 h-100 object-fit-cover rounded" alt="Plugin icon">
                  </div>
                  <div class="flex-grow-1">
                    <h5 class="fw-bold mb-1"><a href="#" class="text-dark text-decoration-none hover-primary">Yoast SEO Alternative</a></h5>
                    <div class="small text-muted mb-2">By <a href="#" class="text-decoration-none">Team SEO</a></div>
                    <p class="mb-0 small text-body">Improve your WordPress SEO: Write better content and have a fully optimized WordPress site.</p>
                  </div>
                </div>
              </div>
              <div class="card-footer bg-transparent border-top p-3 bg-light">
                <div class="d-flex align-items-center justify-content-between mb-2">
                  <div class="text-warning small">
                    <i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i><i class="fi fi-sr-star-half"></i>
                    <span class="text-muted ms-1">(27,456)</span>
                  </div>
                  <span class="badge bg-success-subtle text-success border border-success-subtle rounded-pill">Active</span>
                </div>
                <div class="d-flex align-items-center justify-content-between">
                  <div class="small text-muted">
                    <div class="mb-1"><i class="fi fi-rr-users me-1"></i> 5+ Million active installations</div>
                    <div><i class="fi fi-rr-refresh me-1"></i> Updated 2 weeks ago</div>
                  </div>
                  <button class="btn btn-outline-secondary btn-sm disabled">Installed</button>
                </div>
              </div>
            </div>
          </div>

          <!-- Plugin Card 2 -->
          <div class="col-xl-4 col-md-6">
            <div class="card h-100 border-0 shadow-sm overflow-hidden">
              <div class="card-body p-4">
                <div class="d-flex align-items-start gap-3 mb-3">
                  <div class="avatar avatar-lg rounded shadow-sm bg-light flex-shrink-0">
                    <img src="https://via.placeholder.com/128?text=Sec" class="w-100 h-100 object-fit-cover rounded" alt="Plugin icon">
                  </div>
                  <div class="flex-grow-1">
                    <h5 class="fw-bold mb-1"><a href="#" class="text-dark text-decoration-none hover-primary">Wordfence Security</a></h5>
                    <div class="small text-muted mb-2">By <a href="#" class="text-decoration-none">Defiant</a></div>
                    <p class="mb-0 small text-body">Endpoint Firewall and Malware Scanner built from the ground up to protect WordPress.</p>
                  </div>
                </div>
              </div>
              <div class="card-footer bg-transparent border-top p-3 bg-light">
                <div class="d-flex align-items-center justify-content-between mb-2">
                  <div class="text-warning small">
                    <i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i>
                    <span class="text-muted ms-1">(3,892)</span>
                  </div>
                  <span class="badge bg-secondary-subtle text-secondary border border-secondary-subtle rounded-pill">Inactive</span>
                </div>
                <div class="d-flex align-items-center justify-content-between">
                  <div class="small text-muted">
                    <div class="mb-1"><i class="fi fi-rr-users me-1"></i> 4+ Million active installations</div>
                    <div><i class="fi fi-rr-refresh me-1"></i> Updated 3 days ago</div>
                  </div>
                  <button class="btn btn-primary btn-sm">Install Now</button>
                </div>
              </div>
            </div>
          </div>

          <!-- Plugin Card 3 -->
          <div class="col-xl-4 col-md-6">
            <div class="card h-100 border-0 shadow-sm overflow-hidden">
              <div class="card-body p-4">
                <div class="d-flex align-items-start gap-3 mb-3">
                  <div class="avatar avatar-lg rounded shadow-sm bg-light flex-shrink-0 p-2 border">
                    <i class="fi fi-rr-envelope text-primary fs-1"></i>
                  </div>
                  <div class="flex-grow-1">
                    <h5 class="fw-bold mb-1"><a href="#" class="text-dark text-decoration-none hover-primary">Contact Form Builder</a></h5>
                    <div class="small text-muted mb-2">By <a href="#" class="text-decoration-none">Forms Inc.</a></div>
                    <p class="mb-0 small text-body">Just another contact form plugin. Simple but flexible. Create highly customized contact forms easily.</p>
                  </div>
                </div>
              </div>
              <div class="card-footer bg-transparent border-top p-3 bg-light">
                <div class="d-flex align-items-center justify-content-between mb-2">
                  <div class="text-warning small">
                    <i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i><i class="fi fi-rr-star"></i>
                    <span class="text-muted ms-1">(1,204)</span>
                  </div>
                </div>
                <div class="d-flex align-items-center justify-content-between">
                  <div class="small text-muted">
                    <div class="mb-1"><i class="fi fi-rr-users me-1"></i> 1+ Million active installations</div>
                    <div class="text-danger"><i class="fi fi-rr-exclamation me-1"></i> Untested with your version</div>
                  </div>
                  <button class="btn btn-primary btn-sm">Install Now</button>
                </div>
              </div>
            </div>
          </div>

          <!-- Plugin Card 4 -->
          <div class="col-xl-4 col-md-6">
            <div class="card h-100 border-0 shadow-sm overflow-hidden">
              <div class="card-body p-4">
                <div class="d-flex align-items-start gap-3 mb-3">
                  <div class="avatar avatar-lg rounded shadow-sm bg-light flex-shrink-0 p-2 border text-center">
                    <i class="fi fi-rr-rocket-lunch text-warning fs-1"></i>
                  </div>
                  <div class="flex-grow-1">
                    <h5 class="fw-bold mb-1"><a href="#" class="text-dark text-decoration-none hover-primary">LiteSpeed Cache</a></h5>
                    <div class="small text-muted mb-2">By <a href="#" class="text-decoration-none">LiteSpeed Tech</a></div>
                    <p class="mb-0 small text-body">High-performance page caching and site optimization plugin. Speeds up your site significantly.</p>
                  </div>
                </div>
              </div>
              <div class="card-footer bg-transparent border-top p-3 bg-light">
                <div class="d-flex align-items-center justify-content-between mb-2">
                  <div class="text-warning small">
                    <i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i><i class="fi fi-sr-star"></i>
                    <span class="text-muted ms-1">(4,512)</span>
                  </div>
                </div>
                <div class="d-flex align-items-center justify-content-between">
                  <div class="small text-muted">
                    <div class="mb-1"><i class="fi fi-rr-users me-1"></i> 4+ Million active installations</div>
                    <div><i class="fi fi-rr-refresh me-1"></i> Updated 1 day ago</div>
                  </div>
                  <button class="btn btn-primary btn-sm">Install Now</button>
                </div>
              </div>
            </div>
          </div>

        </div>

        <!-- Pagination -->
        <nav aria-label="Plugin grid pagination">
          <ul class="pagination justify-content-end mb-0">
            <li class="page-item disabled">
              <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
            </li>
            <li class="page-item active"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item">
              <a class="page-link" href="#">Next</a>
            </li>
          </ul>
        </nav>

      </div>
    </main>
    <!-- end::Main Content Area -->'''

pattern = r'<!-- begin::Main Content Area -->.*?<!-- end::Main Content Area -->'
new_html = re.sub(pattern, main_content, html, flags=re.DOTALL)

with open('c:/laragon/www/LaravelCMShtml/plugins-add.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created plugins-add.html")
