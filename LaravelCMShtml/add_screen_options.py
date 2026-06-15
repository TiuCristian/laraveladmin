import re

screen_options_html = '''
        <!-- Screen Options Collapse Panel -->
        <div class="collapse bg-white border border-top-0 shadow-sm mb-0 position-relative" id="screenOptions" style="z-index: 5;">
          <div class="p-4">
            <div class="row">
              <div class="col-md-5 mb-3 mb-md-0">
                <h6 class="fw-bold mb-3 small text-uppercase text-muted">Columns</h6>
                <div class="d-flex flex-wrap gap-3 small">
                  <div class="form-check"><input class="form-check-input" type="checkbox" id="colAuthor" checked><label class="form-check-label" for="colAuthor">Author</label></div>
                  <div class="form-check"><input class="form-check-input" type="checkbox" id="colComments" checked><label class="form-check-label" for="colComments">Comments</label></div>
                  <div class="form-check"><input class="form-check-input" type="checkbox" id="colDate" checked><label class="form-check-label" for="colDate">Date</label></div>
                  <div class="form-check"><input class="form-check-input" type="checkbox" id="colSeoDetails" checked><label class="form-check-label" for="colSeoDetails">SEO Details</label></div>
                  <div class="form-check"><input class="form-check-input" type="checkbox" id="colSeoTitle"><label class="form-check-label" for="colSeoTitle">SEO Title</label></div>
                  <div class="form-check"><input class="form-check-input" type="checkbox" id="colSeoDesc"><label class="form-check-label" for="colSeoDesc">SEO Desc</label></div>
                </div>
              </div>
              <div class="col-md-3 mb-3 mb-md-0">
                <h6 class="fw-bold mb-3 small text-uppercase text-muted">Pagination</h6>
                <div class="d-flex align-items-center gap-2 small">
                  <label for="perPage">Number of items per page:</label>
                  <input type="number" class="form-control form-control-sm" id="perPage" value="20" style="width: 60px;">
                </div>
              </div>
              <div class="col-md-4">
                <h6 class="fw-bold mb-3 small text-uppercase text-muted">View mode</h6>
                <div class="d-flex flex-wrap gap-3 small">
                  <div class="form-check"><input class="form-check-input" type="radio" name="viewMode" id="viewCompact" checked><label class="form-check-label" for="viewCompact">Compact view</label></div>
                  <div class="form-check"><input class="form-check-input" type="radio" name="viewMode" id="viewExtended"><label class="form-check-label" for="viewExtended">Extended view</label></div>
                </div>
              </div>
            </div>
            <div class="mt-4">
              <button class="btn btn-outline-primary btn-sm px-4">Apply</button>
            </div>
          </div>
        </div>

        <!-- Screen Options Tab Button -->
        <div class="d-flex justify-content-end mb-4 position-relative" style="margin-top: -1px; z-index: 4;">
          <button class="btn btn-light btn-sm shadow-sm text-muted bg-white border border-top-0 px-3" type="button" data-bs-toggle="collapse" data-bs-target="#screenOptions" aria-expanded="false" aria-controls="screenOptions" style="border-radius: 0 0 4px 4px; font-size: 0.8rem;">
            Screen Options <i class="fi fi-rr-caret-down ms-1"></i>
          </button>
        </div>

        <!-- Update Notice -->
        <div class="alert bg-white border border-start-0 border-end-0 border-bottom-0 shadow-sm p-3 mb-4" style="border-left: 4px solid #ffb900 !important;">
          <span class="text-dark">LaravelCMS 1.1 is available! <a href="dashboard-updates.html" class="text-decoration-none">Please update now.</a></span>
        </div>
'''

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already added
    if 'id="screenOptions"' in content:
        return

    # Insert right after <div class="container-fluid">
    insert_point = '<div class="container-fluid">'
    if insert_point in content:
        content = content.replace(insert_point, insert_point + screen_options_html)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

process_file('c:/laragon/www/LaravelCMShtml/posts-list.html')
process_file('c:/laragon/www/LaravelCMShtml/pages-list.html')

print("Screen Options added to posts and pages list.")
