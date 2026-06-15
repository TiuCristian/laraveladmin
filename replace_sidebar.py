import os

file_path = r'c:\laragon\www\LaravelAdmin\resources\views\admin\posts\create.blade.php'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the part to replace
start_marker = "          <!-- Sidebar Meta Boxes -->\n          <div class=\"col-lg-4\">"
end_marker = "          </div>\n        </div>\n        </form>"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx) + len(end_marker)

if start_idx != -1 and end_idx != -1:
    new_sidebar = """          <!-- Sidebar Meta Boxes (Right Column) -->
          <div class="col-lg-4">
            
            <div class="card border-0 shadow-sm rounded-0 h-100 bg-body border-start">
              
              <!-- Tabs -->
              <ul class="nav nav-tabs border-bottom bg-body px-2 pt-2 d-flex flex-nowrap" id="sidebarTabs" role="tablist" style="border-bottom-width: 1px;">
                <li class="nav-item" role="presentation">
                  <button class="nav-link active text-body fw-medium py-2 px-3 fs-6 rounded-0 border-0 bg-transparent" id="post-tab" data-bs-toggle="tab" data-bs-target="#post-pane" type="button" role="tab" style="box-shadow: inset 0 -2px 0 0 var(--bs-dark); margin-bottom: -1px;">Post</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link text-muted py-2 px-3 fs-6 rounded-0 border-0 bg-transparent hover-dark" id="block-tab" data-bs-toggle="tab" data-bs-target="#block-pane" type="button" role="tab" style="margin-bottom: -1px;">Block</button>
                </li>
                <li class="nav-item ms-auto" role="presentation">
                  <button class="nav-link text-muted px-2 hover-dark bg-transparent border-0"><i class="fi fi-rr-cross-small"></i></button>
                </li>
              </ul>

              <div class="tab-content" id="sidebarTabsContent">
                
                <!-- Post Pane -->
                <div class="tab-pane fade show active" id="post-pane" role="tabpanel" aria-labelledby="post-tab">
                  <div class="card-body p-4">
                    
                    <div class="d-flex align-items-center justify-content-between mb-3">
                      <div class="fw-bold d-flex align-items-center gap-2 text-body">
                        <i class="fi fi-rr-thumbtack"></i> No title
                      </div>
                      <button class="btn btn-sm btn-link text-muted p-0 hover-dark"><i class="fi fi-rr-menu-dots-vertical"></i></button>
                    </div>

                    <div class="mb-3">
                      <button type="button" class="btn w-100 py-2 text-body bg-body border border-secondary-subtle" style="font-size: 0.9rem;">Set featured image</button>
                    </div>

                    <p class="text-muted small mb-4">Last edited a second ago.</p>

                    <!-- Status & Publish Properties -->
                    <div class="mb-4">
                      <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body small">Status</span>
                        <select form="editForm" name="status" class="form-select form-select-sm w-auto" style="max-width: 120px;">
                            <option value="draft">Draft</option>
                            <option value="published">Published</option>
                        </select>
                      </div>
                      <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body small">Publish</span>
                        <input type="datetime-local" form="editForm" name="published_at" class="form-control form-control-sm w-auto" value="" style="max-width: 150px;">
                      </div>
                      <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body small">Slug</span>
                        <input type="text" form="editForm" name="slug" class="form-control form-control-sm w-auto" value="" placeholder="auto-generated" style="max-width: 120px;">
                      </div>
                      <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body small">Author</span>
                        <select form="editForm" name="author_id" class="form-select form-select-sm w-auto" style="max-width: 120px;">
                            <option value="1">Admin User</option>
                        </select>
                      </div>
                      <div class="d-flex justify-content-between align-items-start mb-3">
                        <span class="text-body small">Discussion</span>
                        <a href="#" class="text-decoration-none small">Open</a>
                      </div>

                      <div class="form-check form-switch d-flex align-items-center gap-2 mb-0 mt-3">
                        <input class="form-check-input mt-0" type="checkbox" role="switch" id="lockModifiedDate">
                        <label class="form-check-label small text-body" for="lockModifiedDate">Lock Modified Date</label>
                      </div>
                    </div>

                    <hr class="my-4 border-secondary-subtle">
                    
                    <!-- Categories Accordion -->
                    <div class="accordion accordion-flush" id="categoriesAccordion">
                      <div class="accordion-item bg-transparent border-0">
                        <h2 class="accordion-header">
                          <button class="accordion-button collapsed bg-transparent px-0 py-2 shadow-none text-body fw-medium" type="button" data-bs-toggle="collapse" data-bs-target="#categoriesCollapse">
                            Categories
                          </button>
                        </h2>
                        <div id="categoriesCollapse" class="accordion-collapse collapse" data-bs-parent="#categoriesAccordion">
                          <div class="accordion-body px-0 pt-3 pb-0">
                            <div class="mb-3" style="max-height: 150px; overflow-y: auto;" data-simplebar>
                              @foreach(\\App\\Models\\Category::all() as $category)
                              <div class="form-check mb-1">
                                <input class="form-check-input" type="checkbox" id="cat{{ $category->id }}" name="categories[]" value="{{ $category->id }}">
                                <label class="form-check-label small text-body" for="cat{{ $category->id }}">{{ $category->name }}</label>
                              </div>
                              @endforeach
                            </div>
                            <a href="#" class="text-decoration-none text-primary small d-flex align-items-center"><i class="fi fi-rr-add me-1"></i> Add New Category</a>
                          </div>
                        </div>
                      </div>
                    </div>

                    <hr class="my-4 border-secondary-subtle">

                    <!-- Tags Accordion -->
                    <div class="accordion accordion-flush" id="tagsAccordion">
                      <div class="accordion-item bg-transparent border-0">
                        <h2 class="accordion-header">
                          <button class="accordion-button collapsed bg-transparent px-0 py-2 shadow-none text-body fw-medium" type="button" data-bs-toggle="collapse" data-bs-target="#tagsCollapse">
                            Tags
                          </button>
                        </h2>
                        <div id="tagsCollapse" class="accordion-collapse collapse" data-bs-parent="#tagsAccordion">
                          <div class="accordion-body px-0 pt-3 pb-0">
                            <div class="input-group mb-2">
                              <input type="text" class="form-control form-control-sm" placeholder="Add new tag">
                              <button class="btn btn-sm btn-outline-secondary" type="button">Add</button>
                            </div>
                            <small class="text-muted d-block mb-3">Separate tags with commas</small>
                            <div class="d-flex flex-wrap gap-2">
                              <!-- tag badges will go here -->
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <hr class="my-4 border-secondary-subtle">

                    <!-- Excerpt Accordion -->
                    <div class="accordion accordion-flush" id="excerptAccordion">
                      <div class="accordion-item bg-transparent border-0">
                        <h2 class="accordion-header">
                          <button class="accordion-button collapsed bg-transparent px-0 py-2 shadow-none text-body fw-medium" type="button" data-bs-toggle="collapse" data-bs-target="#excerptCollapse">
                            Excerpt
                          </button>
                        </h2>
                        <div id="excerptCollapse" class="accordion-collapse collapse" data-bs-parent="#excerptAccordion">
                          <div class="accordion-body px-0 pt-3 pb-0">
                            <textarea class="form-control" rows="3" placeholder="Write an excerpt (optional)"></textarea>
                            <small class="text-muted d-block mt-2">Excerpts are optional hand-crafted summaries of your content that can be used in your theme.</small>
                          </div>
                        </div>
                      </div>
                    </div>

                  </div>
                </div>

                <!-- Block Pane -->
                <div class="tab-pane fade" id="block-pane" role="tabpanel" aria-labelledby="block-tab">
                  <div class="card-body p-4">
                    
                    <!-- Block Header -->
                    <div class="d-flex align-items-start gap-3 mb-4">
                      <i class="fi fi-rr-paragraph fs-3 text-body mt-1"></i>
                      <div>
                        <h6 class="fw-bold mb-1 text-body">Paragraph</h6>
                        <p class="small text-muted mb-0">Start with the basic building block of all narrative.</p>
                      </div>
                    </div>
                    
                    <hr class="my-4 border-secondary-subtle">

                    <!-- Color Section -->
                    <div class="mb-4">
                      <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body fw-medium">Color</span>
                        <button class="btn btn-sm btn-link text-muted p-0 hover-dark"><i class="fi fi-rr-menu-dots-vertical"></i></button>
                      </div>
                      
                      <div class="border rounded bg-body">
                        <button class="btn w-100 text-start px-3 py-2 border-0 border-bottom d-flex align-items-center gap-3 rounded-0 bg-transparent text-body">
                          <div class="rounded-circle border" style="width: 20px; height: 20px; background: linear-gradient(135deg, transparent 45%, var(--bs-border-color) 45%, var(--bs-border-color) 55%, transparent 55%);"></div> Text
                        </button>
                        <button class="btn w-100 text-start px-3 py-2 border-0 d-flex align-items-center gap-3 rounded-0 bg-transparent text-primary fw-medium">
                          <div class="rounded-circle border border-primary" style="width: 20px; height: 20px; background: linear-gradient(135deg, transparent 45%, var(--bs-primary) 45%, var(--bs-primary) 55%, transparent 55%);"></div> Background
                        </button>
                      </div>
                    </div>

                    <hr class="my-4 border-secondary-subtle">

                    <!-- Typography Section -->
                    <div class="mb-4">
                      <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body fw-medium">Typography</span>
                        <button class="btn btn-sm btn-link text-muted p-0 hover-dark"><i class="fi fi-rr-menu-dots-vertical"></i></button>
                      </div>
                      
                      <div class="d-flex justify-content-between align-items-center mb-2">
                        <span class="text-muted small fw-medium" style="font-size: 0.75rem; letter-spacing: 0.5px;">FONT SIZE</span>
                        <button class="btn btn-sm btn-link text-body p-0 hover-dark"><i class="fi fi-rr-settings-sliders"></i></button>
                      </div>

                      <div class="btn-group w-100 border rounded" role="group">
                        <button type="button" class="btn btn-light bg-body border-0 border-end text-muted py-2 hover-dark" style="font-size: 0.85rem;">S</button>
                        <button type="button" class="btn btn-light bg-body border-0 border-end text-muted py-2 hover-dark" style="font-size: 0.85rem;">M</button>
                        <button type="button" class="btn btn-light bg-body border-0 border-end text-muted py-2 hover-dark" style="font-size: 0.85rem;">L</button>
                        <button type="button" class="btn btn-light bg-body border-0 text-muted py-2 hover-dark" style="font-size: 0.85rem;">XL</button>
                      </div>
                    </div>
                    
                    <hr class="my-4 border-secondary-subtle">
                    
                    <!-- Advanced Section -->
                    <div class="accordion accordion-flush" id="advancedAccordion">
                      <div class="accordion-item bg-transparent border-0">
                        <h2 class="accordion-header">
                          <button class="accordion-button collapsed bg-transparent px-0 py-2 shadow-none text-body fw-medium" type="button" data-bs-toggle="collapse" data-bs-target="#advancedCollapse">
                            Advanced
                          </button>
                        </h2>
                        <div id="advancedCollapse" class="accordion-collapse collapse" data-bs-parent="#advancedAccordion">
                          <div class="accordion-body px-0 pt-3 pb-0">
                            <label class="form-label text-muted small fw-medium mb-2" style="font-size: 0.75rem; letter-spacing: 0.5px;">HTML ANCHOR</label>
                            <input type="text" class="form-control mb-3">
                            <p class="small text-muted mb-4" style="font-size: 0.8rem; line-height: 1.5;">Enter a word or two &mdash; without spaces &mdash; to make a unique web address just for this block, called an "anchor". Then, you'll be able to link directly to this section of your page. <a href="#" class="text-decoration-none">Learn more about anchors <i class="fi fi-rr-arrow-up-right small"></i></a></p>
                            
                            <label class="form-label text-muted small fw-medium mb-2" style="font-size: 0.75rem; letter-spacing: 0.5px;">ADDITIONAL CSS CLASS(ES)</label>
                            <input type="text" class="form-control">
                          </div>
                        </div>
                      </div>
                    </div>

                  </div>
                </div>

              </div>
            </div>
          </div>
        </div>
        </form>"""

    new_content = content[:start_idx] + new_sidebar + content[end_idx:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Sidebar replaced successfully.")
else:
    print("Could not find start or end markers.")
