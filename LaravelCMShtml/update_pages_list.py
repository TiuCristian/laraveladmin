import re

with open('c:/laragon/www/LaravelCMShtml/pages-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I will replace from <!-- Filters & Bulk Actions --> down to <!-- Pages Table Card -->
# and also update the table structure to include SEO details and Quick Edit.
# I'll just write the entire main content area below the Page Title & Breadcrumbs.

new_content = '''
        <!-- Navigation Links -->
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-2">
          <ul class="list-inline mb-2 mb-md-0 small">
            <li class="list-inline-item"><a href="#" class="fw-bold text-dark text-decoration-none">All <span class="text-muted fw-normal">(6)</span></a> <span class="text-muted mx-1">|</span></li>
            <li class="list-inline-item"><a href="#" class="text-primary text-decoration-none hover-primary">Published <span class="text-muted">(6)</span></a> <span class="text-muted mx-1">|</span></li>
            <li class="list-inline-item"><a href="#" class="text-primary text-decoration-none hover-primary">Pillar Content <span class="text-muted">(0)</span></a></li>
          </ul>
          
          <div class="d-flex align-items-center gap-2">
            <input type="text" class="form-control form-control-sm" style="width: 200px;" placeholder="">
            <button class="btn btn-sm btn-outline-secondary bg-white text-dark">Search Pages</button>
          </div>
        </div>

        <!-- Filters & Bulk Actions -->
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-2">
          
          <div class="d-flex align-items-center gap-2">
            <select class="form-select form-select-sm" style="width: auto;">
              <option>Bulk actions</option>
              <option>Edit</option>
              <option>Move to Trash</option>
            </select>
            <button class="btn btn-sm btn-outline-primary bg-white text-primary">Apply</button>
            
            <select class="form-select form-select-sm ms-2" style="width: auto;">
              <option>All dates</option>
              <option>June 2026</option>
              <option>May 2026</option>
            </select>

            <select class="form-select form-select-sm" style="width: auto;">
              <option>Rank Math</option>
              <option>Good</option>
              <option>Ok</option>
              <option>Bad</option>
            </select>
            <button class="btn btn-sm btn-outline-primary bg-white text-primary">Filter</button>
          </div>

          <div class="small text-muted">
            6 items
          </div>
          
        </div>

        <!-- Pages Table Card -->
        <div class="card border-0 shadow-sm mb-4">
          <div class="table-responsive">
            <table class="table table-hover align-middle mb-0" style="font-size: 0.9rem;">
              <thead class="table-light">
                <tr>
                  <th scope="col" style="width: 40px;" class="ps-3 border-bottom-0">
                    <input class="form-check-input" type="checkbox" id="selectAll">
                  </th>
                  <th scope="col" class="border-bottom-0 text-primary fw-medium">Title <i class="fi fi-rr-caret-up ms-1 small"></i></th>
                  <th scope="col" class="border-bottom-0 text-dark fw-medium">Author</th>
                  <th scope="col" class="text-center border-bottom-0 text-dark fw-medium">
                    <i class="fi fi-rr-comment-alt"></i> <i class="fi fi-rr-caret-up ms-1 small"></i>
                  </th>
                  <th scope="col" class="border-bottom-0 text-primary fw-medium">Date <i class="fi fi-rr-caret-up ms-1 small"></i></th>
                  <th scope="col" class="pe-3 border-bottom-0 text-primary fw-medium">SEO Details <i class="fi fi-rr-pencil ms-1 small"></i></th>
                </tr>
              </thead>
              <tbody>
                
                <!-- Page Row 1 -->
                <tr>
                  <td class="ps-3 align-top pt-3">
                    <input class="form-check-input" type="checkbox">
                  </td>
                  <td class="align-top pt-3" style="width: 35%;">
                    <a href="pages-edit.html" class="fw-bold text-dark text-decoration-none">About Daily Life Pulse</a>
                    <div class="small mt-1 text-muted" style="font-size: 0.8rem;">
                      <a href="pages-edit.html" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                      <a href="#" class="text-decoration-none text-primary hover-primary">Quick Edit</a> <span class="text-light">|</span> 
                      <a href="#" class="text-decoration-none text-danger hover-danger">Trash</a> <span class="text-light">|</span> 
                      <a href="#" class="text-decoration-none text-secondary hover-dark">View</a>
                    </div>
                  </td>
                  <td class="align-top pt-3"><a href="#" class="text-decoration-none text-primary small">Editorial Team &ndash; Daily Life Pulse</a></td>
                  <td class="text-center align-top pt-3">
                    <span class="text-muted">&mdash;</span>
                  </td>
                  <td class="align-top pt-3" style="width: 15%;">
                    <span class="d-block text-dark small">Published</span>
                    <span class="text-muted small">2019/05/21 at 7:06 am</span>
                  </td>
                  <td class="pe-3 align-top pt-3" style="width: 25%;">
                    <div class="d-inline-block bg-warning bg-opacity-25 text-dark fw-bold px-2 py-1 rounded small mb-2">70 / 100</div>
                    <div class="small text-dark mb-1"><strong>Keyword:</strong> about Daily Life Pulse</div>
                    <div class="small text-dark mb-2"><strong>Schema:</strong> Article</div>
                    <div class="small text-muted d-flex align-items-center gap-3">
                      <span><strong>Links:</strong> <i class="fi fi-rr-link ms-1"></i> 1</span>
                      <span><i class="fi fi-rr-arrow-up-right-from-square"></i> 2</span>
                      <span><i class="fi fi-rr-comment-alt"></i> 1</span>
                    </div>
                  </td>
                </tr>
                
                <!-- Page Row 2 -->
                <tr>
                  <td class="ps-3 align-top pt-3">
                    <input class="form-check-input" type="checkbox">
                  </td>
                  <td class="align-top pt-3">
                    <a href="pages-edit.html" class="fw-bold text-dark text-decoration-none">Contact Us</a>
                    <div class="small mt-1 text-muted" style="font-size: 0.8rem;">
                      <a href="pages-edit.html" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                      <a href="#" class="text-decoration-none text-primary hover-primary">Quick Edit</a> <span class="text-light">|</span> 
                      <a href="#" class="text-decoration-none text-danger hover-danger">Trash</a> <span class="text-light">|</span> 
                      <a href="#" class="text-decoration-none text-secondary hover-dark">View</a>
                    </div>
                  </td>
                  <td class="align-top pt-3"><a href="#" class="text-decoration-none text-primary small">Editorial Team &ndash; Daily Life Pulse</a></td>
                  <td class="text-center align-top pt-3">
                    <span class="text-muted">&mdash;</span>
                  </td>
                  <td class="align-top pt-3">
                    <span class="d-block text-dark small">Published</span>
                    <span class="text-muted small">2019/05/22 at 9:15 am</span>
                  </td>
                  <td class="pe-3 align-top pt-3">
                    <div class="d-inline-block bg-success bg-opacity-25 text-dark fw-bold px-2 py-1 rounded small mb-2">85 / 100</div>
                    <div class="small text-dark mb-1"><strong>Keyword:</strong> contact</div>
                    <div class="small text-dark mb-2"><strong>Schema:</strong> Article</div>
                    <div class="small text-muted d-flex align-items-center gap-3">
                      <span><strong>Links:</strong> <i class="fi fi-rr-link ms-1"></i> 0</span>
                      <span><i class="fi fi-rr-arrow-up-right-from-square"></i> 1</span>
                      <span><i class="fi fi-rr-comment-alt"></i> 0</span>
                    </div>
                  </td>
                </tr>

              </tbody>
            </table>
          </div>
          
          <!-- Pagination -->
          <div class="card-footer bg-transparent py-2 d-flex align-items-center justify-content-between border-top">
            <div class="d-flex align-items-center gap-2">
              <select class="form-select form-select-sm" style="width: auto;">
                <option>Bulk actions</option>
                <option>Edit</option>
                <option>Move to Trash</option>
              </select>
              <button class="btn btn-sm btn-outline-primary bg-white text-primary">Apply</button>
            </div>
            <div class="d-flex align-items-center gap-3">
              <span class="text-muted small">6 items</span>
              <nav aria-label="Page navigation">
                <ul class="pagination pagination-sm mb-0">
                  <li class="page-item disabled"><a class="page-link" href="#">&laquo;</a></li>
                  <li class="page-item active"><a class="page-link" href="#">1</a></li>
                  <li class="page-item"><a class="page-link" href="#">2</a></li>
                  <li class="page-item"><a class="page-link" href="#">&raquo;</a></li>
                </ul>
              </nav>
            </div>
          </div>
        </div>
'''

# Find the start of <!-- Filters & Bulk Actions --> and replace everything down to the bottom
pattern = r'<!-- Filters & Bulk Actions -->.*?</div>\s*</div>\s*</div>\s*</main>'
replacement = new_content + '\n      </div>\n    </main>'

# But wait, there is also the navigation links All (6) | Published (6) above it.
# We will just replace everything from <!-- Filters & Bulk Actions --> down to the end of <main>
new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open('c:/laragon/www/LaravelCMShtml/pages-list.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated pages-list.html to match the screenshot")
