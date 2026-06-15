import re

with open('c:/laragon/www/LaravelCMShtml/tools-index.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Import</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item"><a href="tools-index.html">Tools</a></li>
                <li class="breadcrumb-item active" aria-current="page">Import</li>
              </ol>
            </nav>
          </div>
        </div>

        <div class="row">
          <div class="col-lg-10 col-xl-8">
            <div class="card border-0 shadow-sm mb-4">
              <div class="card-body p-4">
                
                <p class="text-muted mb-4">If you have posts or comments in another system, LaravelCMS can import those into this site. To get started, choose a system to import from below:</p>

                <div class="table-responsive">
                  <table class="table align-middle">
                    <tbody>
                      
                      <tr>
                        <td class="fw-bold" style="width: 200px;">Blogger</td>
                        <td><span class="text-muted small">Install the Blogger importer to import posts, comments, and users from a Blogger blog.</span></td>
                        <td class="text-end"><button class="btn btn-sm btn-outline-secondary">Install Now</button></td>
                      </tr>

                      <tr>
                        <td class="fw-bold">Categories and Tags Converter</td>
                        <td><span class="text-muted small">Install the category/tag converter to convert existing categories to tags or tags to categories, selectively.</span></td>
                        <td class="text-end"><button class="btn btn-sm btn-outline-secondary">Install Now</button></td>
                      </tr>

                      <tr>
                        <td class="fw-bold">LiveJournal</td>
                        <td><span class="text-muted small">Install the LiveJournal importer to import posts from LiveJournal using their API.</span></td>
                        <td class="text-end"><button class="btn btn-sm btn-outline-secondary">Install Now</button></td>
                      </tr>

                      <tr>
                        <td class="fw-bold">Movable Type and TypePad</td>
                        <td><span class="text-muted small">Install the Movable Type importer to import posts and comments from a Movable Type or TypePad blog.</span></td>
                        <td class="text-end"><button class="btn btn-sm btn-outline-secondary">Install Now</button></td>
                      </tr>

                      <tr>
                        <td class="fw-bold">RSS</td>
                        <td><span class="text-muted small">Install the RSS importer to import posts from an RSS feed.</span></td>
                        <td class="text-end"><button class="btn btn-sm btn-outline-secondary">Install Now</button></td>
                      </tr>

                      <tr>
                        <td class="fw-bold">Tumblr</td>
                        <td><span class="text-muted small">Install the Tumblr importer to import posts & media from Tumblr using their API.</span></td>
                        <td class="text-end"><button class="btn btn-sm btn-outline-secondary">Install Now</button></td>
                      </tr>

                      <tr class="table-active bg-light">
                        <td class="fw-bold text-primary">WordPress</td>
                        <td><span class="text-muted small">Import posts, pages, comments, custom fields, categories, and tags from a WordPress export file.</span></td>
                        <td class="text-end"><button class="btn btn-sm btn-primary">Run Importer</button></td>
                      </tr>

                    </tbody>
                  </table>
                </div>

                <div class="mt-4 pt-3 border-top">
                  <p class="mb-0 text-muted small">If the importer you need is not listed, <a href="#" class="text-decoration-none">search the plugin directory</a> to see if an importer is available.</p>
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

with open('c:/laragon/www/LaravelCMShtml/tools-import.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created tools-import.html")
