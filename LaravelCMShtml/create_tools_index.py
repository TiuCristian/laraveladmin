import re

with open('c:/laragon/www/LaravelCMShtml/users-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Tools</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item active" aria-current="page">Tools</li>
              </ol>
            </nav>
          </div>
        </div>

        <div class="row">
          <div class="col-lg-8 col-xl-6">
            <div class="card border-0 shadow-sm mb-4">
              <div class="card-header bg-transparent border-bottom">
                <h5 class="mb-0">Available Tools</h5>
              </div>
              <div class="card-body p-4">
                
                <div class="mb-4">
                  <h6 class="fw-bold mb-2">Categories and Tags Converter</h6>
                  <p class="text-muted small mb-2">If you want to convert your categories to tags (or vice versa), use the Categories and Tags Converter available from the Import screen.</p>
                  <a href="tools-import.html" class="btn btn-outline-primary btn-sm">Go to Importer</a>
                </div>

                <div class="mb-4">
                  <h6 class="fw-bold mb-2">Export Personal Data</h6>
                  <p class="text-muted small mb-2">Generate a file containing all of the personal data for a given user. This is helpful for GDPR compliance and data portability requests.</p>
                  <a href="tools-export.html" class="btn btn-outline-primary btn-sm">Export Data</a>
                </div>

                <div>
                  <h6 class="fw-bold mb-2">Erase Personal Data</h6>
                  <p class="text-muted small mb-2">Anonymize or remove the personal data associated with a user's email address. This is required for right-to-be-forgotten requests.</p>
                  <a href="#" class="btn btn-outline-danger btn-sm">Erase Data</a>
                </div>

              </div>
            </div>
          </div>
        </div>

      </div>
    </main>
    <!-- end::Main Content Area -->'''

pattern = r'<!-- begin::Main Content Area -->.*?<!-- end::Main Content Area -->'
new_html = re.sub(pattern, main_content, html, flags=re.DOTALL)

# Fix active menu link
new_html = new_html.replace('class="menu-link active" href="users-list.html"', 'class="menu-link" href="users-list.html"')
new_html = new_html.replace('class="menu-link" href="tools-index.html"', 'class="menu-link active" href="tools-index.html"')

with open('c:/laragon/www/LaravelCMShtml/tools-index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created tools-index.html")
