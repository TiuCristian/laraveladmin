import re

with open('c:/laragon/www/LaravelCMShtml/posts-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_content = '''
        <!-- Navigation Links -->
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-2">
          <ul class="list-inline mb-2 mb-md-0 small">
            <li class="list-inline-item"><a href="#" class="fw-bold text-dark text-decoration-none">All <span class="text-muted fw-normal">(3)</span></a> <span class="text-muted mx-1">|</span></li>
            <li class="list-inline-item"><a href="#" class="text-primary text-decoration-none hover-primary">Published <span class="text-muted">(2)</span></a> <span class="text-muted mx-1">|</span></li>
            <li class="list-inline-item"><a href="#" class="text-primary text-decoration-none hover-primary">Draft <span class="text-muted">(1)</span></a> <span class="text-muted mx-1">|</span></li>
            <li class="list-inline-item"><a href="#" class="text-primary text-decoration-none hover-primary">Pillar Content <span class="text-muted">(0)</span></a></li>
          </ul>
          
          <div class="d-flex align-items-center gap-2">
            <input type="text" class="form-control form-control-sm" style="width: 200px;" placeholder="">
            <button class="btn btn-sm btn-outline-secondary bg-white text-dark">Search Posts</button>
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
              <option>All categories</option>
              <option>Tech</option>
              <option>News</option>
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
            3 items
          </div>
          
        </div>

        <!-- Posts Table Card -->
        <div class="card border-0 shadow-sm mb-4">
          <div class="table-responsive">
            <table class="table table-hover align-middle mb-0" style="font-size: 0.9rem;">
              <thead class="table-light">
                <tr>
                  <th scope="col" style="width: 40px;" class="ps-3 border-bottom-0">
                    <input class="form-check-input" type="checkbox" id="selectAll">
                  </th>
                  <th scope="col" class="border-bottom-0 text-primary fw-medium">Title <i class="fi fi-rr-caret-up ms-1 small"></i></th>
                  <th scope="col" class="border-bottom-0 text-dark fw-medium">Categories</th>
                  <th scope="col" class="border-bottom-0 text-dark fw-medium">Tags</th>
                  <th scope="col" class="text-center border-bottom-0 text-dark fw-medium">
                    <i class="fi fi-rr-comment-alt"></i> <i class="fi fi-rr-caret-up ms-1 small"></i>
                  </th>
                  <th scope="col" class="border-bottom-0 text-primary fw-medium">Date <i class="fi fi-rr-caret-up ms-1 small"></i></th>
                  <th scope="col" class="pe-3 border-bottom-0 text-primary fw-medium">SEO Details <i class="fi fi-rr-pencil ms-1 small"></i></th>
                </tr>
              </thead>
              <tbody>
                
                <!-- Post Row 1 -->
                <tr id="postRow1">
                  <td class="ps-3 align-top pt-3">
                    <input class="form-check-input" type="checkbox">
                  </td>
                  <td class="align-top pt-3" style="width: 35%;">
                    <a href="posts-edit.html" class="fw-bold text-dark text-decoration-none">The Total Cost of Owning Tech Over 5 Years: 17 Hidden Expenses That Quietly Drain Your Budget <span class="fw-normal text-muted">&mdash; Pending</span></a>
                    <div class="small mt-1 text-muted" style="font-size: 0.8rem;">
                      <a href="posts-edit.html" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                      <a href="javascript:void(0);" onclick="document.getElementById('postRow1').classList.add('d-none'); document.getElementById('quickEditPost1').classList.remove('d-none');" class="text-decoration-none text-primary hover-primary">Quick Edit</a> <span class="text-light">|</span> 
                      <a href="#" class="text-decoration-none text-danger hover-danger">Trash</a> <span class="text-light">|</span> 
                      <a href="#" class="text-decoration-none text-secondary hover-dark">Preview</a>
                    </div>
                  </td>
                  <td class="align-top pt-3"><a href="#" class="text-decoration-none text-primary small">Tech</a></td>
                  <td class="align-top pt-3"><a href="#" class="text-decoration-none text-primary small">tech</a></td>
                  <td class="text-center align-top pt-3">
                    <span class="text-muted">&mdash;</span>
                  </td>
                  <td class="align-top pt-3" style="width: 15%;">
                    <span class="d-block text-dark small">Last Modified</span>
                    <span class="text-muted small">2026/05/06 at 4:13 pm</span>
                  </td>
                  <td class="pe-3 align-top pt-3" style="width: 25%;">
                    <div class="d-inline-block bg-warning bg-opacity-25 text-dark fw-bold px-2 py-1 rounded small mb-2">79 / 100</div>
                    <div class="small text-dark mb-1"><strong>Keyword:</strong> The Total Cost of Owning Tech Over 5 Years</div>
                    <div class="small text-dark mb-2"><strong>Schema:</strong> Article (BlogPosting)</div>
                    <div class="small text-muted d-flex align-items-center gap-3">
                      <span><strong>Links:</strong> <i class="fi fi-rr-link ms-1"></i> 5</span>
                      <span><i class="fi fi-rr-arrow-up-right-from-square"></i> 1</span>
                      <span><i class="fi fi-rr-comment-alt"></i> 5</span>
                    </div>
                  </td>
                </tr>

                <!-- Quick Edit Row 1 -->
                <tr id="quickEditPost1" class="d-none bg-light">
                  <td colspan="7" class="p-4 border-bottom">
                    <div class="mb-3">
                      <h6 class="fw-bold small text-uppercase text-muted mb-0">Quick Edit</h6>
                    </div>
                    
                    <div class="row">
                      
                      <!-- Left Column -->
                      <div class="col-md-6 mb-3 mb-md-0">
                        
                        <div class="row mb-2 align-items-center">
                          <label class="col-sm-3 col-form-label small text-dark">Title</label>
                          <div class="col-sm-9">
                            <input type="text" class="form-control form-control-sm" value="The Total Cost of Owning Tech Over 5 Years">
                          </div>
                        </div>

                        <div class="row mb-2 align-items-center">
                          <label class="col-sm-3 col-form-label small text-dark">Slug</label>
                          <div class="col-sm-9">
                            <input type="text" class="form-control form-control-sm" value="total-cost-tech-5-years">
                          </div>
                        </div>

                        <div class="row mb-2 align-items-center">
                          <label class="col-sm-3 col-form-label small text-dark">Date</label>
                          <div class="col-sm-9">
                            <div class="d-flex align-items-center gap-1">
                              <select class="form-select form-select-sm px-1" style="width: auto;">
                                <option>01-Jan</option><option>02-Feb</option><option>03-Mar</option><option>04-Apr</option><option selected>05-May</option>
                              </select>
                              <input type="text" class="form-control form-control-sm text-center px-1" value="06" style="width: 40px;"> , 
                              <input type="text" class="form-control form-control-sm text-center px-1" value="2026" style="width: 50px;"> at 
                              <input type="text" class="form-control form-control-sm text-center px-1" value="16" style="width: 35px;"> : 
                              <input type="text" class="form-control form-control-sm text-center px-1" value="13" style="width: 35px;">
                            </div>
                          </div>
                        </div>

                        <div class="row align-items-center">
                          <label class="col-sm-3 col-form-label small text-dark">Password</label>
                          <div class="col-sm-9 d-flex align-items-center gap-2">
                            <input type="text" class="form-control form-control-sm" style="width: 120px;">
                            <span class="small text-muted">&ndash;OR&ndash;</span>
                            <div class="form-check mb-0">
                              <input class="form-check-input" type="checkbox" id="privatePostCheck">
                              <label class="form-check-label small text-dark" for="privatePostCheck">Private</label>
                            </div>
                          </div>
                        </div>

                      </div>

                      <!-- Right Column -->
                      <div class="col-md-6">
                        
                        <div class="row mb-2">
                          <label class="col-sm-3 col-form-label small text-dark">Categories</label>
                          <div class="col-sm-9">
                            <div class="border bg-white p-2 rounded" style="max-height: 100px; overflow-y: auto;">
                              <div class="form-check mb-1">
                                <input class="form-check-input" type="checkbox" id="catFinance">
                                <label class="form-check-label small" for="catFinance">Finance</label>
                              </div>
                              <div class="form-check mb-1">
                                <input class="form-check-input" type="checkbox" id="catMarketing">
                                <label class="form-check-label small" for="catMarketing">Marketing</label>
                              </div>
                              <div class="form-check mb-1">
                                <input class="form-check-input" type="checkbox" id="catTech" checked>
                                <label class="form-check-label small" for="catTech">Tech</label>
                              </div>
                              <div class="form-check mb-0">
                                <input class="form-check-input" type="checkbox" id="catUncategorized">
                                <label class="form-check-label small" for="catUncategorized">Uncategorized</label>
                              </div>
                            </div>
                          </div>
                        </div>

                        <div class="row mb-2 align-items-center">
                          <label class="col-sm-3 col-form-label small text-dark">Tags</label>
                          <div class="col-sm-9">
                            <textarea class="form-control form-control-sm" rows="1">tech</textarea>
                          </div>
                        </div>

                        <div class="row mb-3 align-items-center">
                          <div class="col-sm-9 offset-sm-3 d-flex gap-3">
                            <div class="form-check mb-0">
                              <input class="form-check-input" type="checkbox" id="allowCommentsPost" checked>
                              <label class="form-check-label small text-dark" for="allowCommentsPost">Allow Comments</label>
                            </div>
                            <div class="form-check mb-0">
                              <input class="form-check-input" type="checkbox" id="allowPingsPost" checked>
                              <label class="form-check-label small text-dark" for="allowPingsPost">Allow Pings</label>
                            </div>
                          </div>
                        </div>

                        <div class="row align-items-center mb-2">
                          <label class="col-sm-3 col-form-label small text-dark">Status</label>
                          <div class="col-sm-9">
                            <select class="form-select form-select-sm" style="width: auto;">
                              <option>Published</option>
                              <option selected>Pending Review</option>
                              <option>Draft</option>
                            </select>
                          </div>
                        </div>
                        
                        <div class="row align-items-center">
                          <div class="col-sm-9 offset-sm-3">
                            <div class="form-check mb-0">
                              <input class="form-check-input" type="checkbox" id="stickyPost">
                              <label class="form-check-label small text-dark" for="stickyPost">Make this post sticky</label>
                            </div>
                          </div>
                        </div>

                      </div>

                    </div>
                    
                    <div class="mt-4 pt-3 border-top">
                      <button type="button" class="btn btn-sm btn-primary px-3 me-1" onclick="document.getElementById('quickEditPost1').classList.add('d-none'); document.getElementById('postRow1').classList.remove('d-none');">Update</button>
                      <button type="button" class="btn btn-sm btn-outline-secondary px-3" onclick="document.getElementById('quickEditPost1').classList.add('d-none'); document.getElementById('postRow1').classList.remove('d-none');">Cancel</button>
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
              <span class="text-muted small">3 items</span>
              <nav aria-label="Page navigation">
                <ul class="pagination pagination-sm mb-0">
                  <li class="page-item disabled"><a class="page-link" href="#">&laquo;</a></li>
                  <li class="page-item active"><a class="page-link" href="#">1</a></li>
                  <li class="page-item"><a class="page-link" href="#">&raquo;</a></li>
                </ul>
              </nav>
            </div>
          </div>
        </div>
'''

pattern = r'<!-- Filters & Bulk Actions -->.*?</div>\s*</div>\s*</div>\s*</main>'
replacement = new_content + '\n      </div>\n    </main>'

new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open('c:/laragon/www/LaravelCMShtml/posts-list.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated posts-list.html with Quick Edit")
