import re

with open('c:/laragon/www/LaravelCMShtml/settings-general.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Reading Settings</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item"><a href="settings-general.html">Settings</a></li>
                <li class="breadcrumb-item active" aria-current="page">Reading</li>
              </ol>
            </nav>
          </div>
        </div>

        <div class="row">
          <div class="col-lg-10 col-xl-8">
            <form>
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-body p-4">
                  
                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Your homepage displays</label>
                    <div class="col-sm-8 pt-2">
                      <div class="form-check mb-2">
                        <input class="form-check-input" type="radio" name="homepageDisplay" id="latestPosts" checked>
                        <label class="form-check-label text-dark" for="latestPosts">Your latest posts</label>
                      </div>
                      <div class="form-check">
                        <input class="form-check-input" type="radio" name="homepageDisplay" id="staticPage">
                        <label class="form-check-label text-dark" for="staticPage">A static page (select below)</label>
                      </div>
                      
                      <div class="ps-4 mt-3">
                        <div class="row mb-2 align-items-center">
                          <label for="homepage" class="col-sm-4 col-form-label small">Homepage:</label>
                          <div class="col-sm-8">
                            <select class="form-select form-select-sm" id="homepage" disabled>
                              <option value="">&mdash; Select &mdash;</option>
                              <option value="1">Home</option>
                              <option value="2">About Us</option>
                              <option value="3">Contact</option>
                            </select>
                          </div>
                        </div>
                        <div class="row align-items-center">
                          <label for="postsPage" class="col-sm-4 col-form-label small">Posts page:</label>
                          <div class="col-sm-8">
                            <select class="form-select form-select-sm" id="postsPage" disabled>
                              <option value="">&mdash; Select &mdash;</option>
                              <option value="4">Blog</option>
                              <option value="5">News</option>
                            </select>
                          </div>
                        </div>
                      </div>

                    </div>
                  </div>

                  <div class="row mb-4 align-items-center">
                    <label for="postsPerPage" class="col-sm-4 col-form-label fw-medium text-dark">Blog pages show at most</label>
                    <div class="col-sm-3 d-flex align-items-center gap-2">
                      <input type="number" class="form-control" id="postsPerPage" value="10">
                      <span class="small text-muted">posts</span>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-center">
                    <label for="syndicationFeed" class="col-sm-4 col-form-label fw-medium text-dark">Syndication feeds show the most recent</label>
                    <div class="col-sm-3 d-flex align-items-center gap-2">
                      <input type="number" class="form-control" id="syndicationFeed" value="10">
                      <span class="small text-muted">items</span>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">For each post in a feed, include</label>
                    <div class="col-sm-8 pt-2">
                      <div class="form-check mb-2">
                        <input class="form-check-input" type="radio" name="feedInclude" id="fullText" checked>
                        <label class="form-check-label text-dark" for="fullText">Full text</label>
                      </div>
                      <div class="form-check">
                        <input class="form-check-input" type="radio" name="feedInclude" id="excerpt">
                        <label class="form-check-label text-dark" for="excerpt">Excerpt</label>
                      </div>
                    </div>
                  </div>

                  <div class="row mb-3 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Search engine visibility</label>
                    <div class="col-sm-8 pt-2">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="discourageSearchEngines">
                        <label class="form-check-label text-dark" for="discourageSearchEngines">Discourage search engines from indexing this site</label>
                      </div>
                      <div class="form-text mt-2">It is up to search engines to honor this request.</div>
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

with open('c:/laragon/www/LaravelCMShtml/settings-reading.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created settings-reading.html")
