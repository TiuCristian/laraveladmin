with open('c:/laragon/www/LaravelCMShtml/pages-add.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of row g-4
row_start = content.find('<div class="row g-4">')

# Find the end of row g-4 (before </main>)
main_end = content.find('</main>')
# Find the </div> right before </main> that belongs to container-fluid
# And the </div> before that which belongs to row g-4
# Let's just use slicing up to row_start, and after main_end - 16
# Actually just split by <main class="app-wrapper"> and </main>

main_start = content.find('<main class="app-wrapper">')

top_part = content[:row_start]
bottom_part = content[main_end - 14:] # This is '      </div>\n    </main>'

clean_middle = '''<div class="row g-4">
          
          <!-- Editor Area (Left Column) -->
          <div class="col-lg-8">
            <div class="card border-0 shadow-sm mb-4">
              <div class="card-body p-4">
                
                <div class="mb-4">
                  <input type="text" class="form-control form-control-lg border-0 bg-light fs-4 fw-bold" placeholder="Add title" id="pageTitle">
                  <div class="mt-2 ms-2 small text-muted">
                    Permalink: <a href="#" class="text-decoration-none">http://localhost/new-page/</a> <button class="btn btn-sm btn-link p-0 ms-1 text-decoration-none">Edit</button>
                  </div>
                </div>

                <div class="mb-3 d-flex align-items-center gap-2">
                  <a href="media-add.html" class="btn btn-sm btn-light border"><i class="fi fi-rr-picture"></i> Add Media</a>
                </div>

                <!-- Mock Rich Text Editor -->
                <div class="border rounded bg-white">
                  <div class="bg-light border-bottom p-2 d-flex flex-wrap gap-1 align-items-center">
                    <button class="btn btn-sm btn-light border"><i class="fi fi-rr-bold"></i></button>
                    <button class="btn btn-sm btn-light border"><i class="fi fi-rr-italic"></i></button>
                    <button class="btn btn-sm btn-light border"><i class="fi fi-rr-list"></i></button>
                    <button class="btn btn-sm btn-light border"><i class="fi fi-rr-quote-right"></i></button>
                    <span class="border-start mx-1 h-100"></span>
                    <button class="btn btn-sm btn-light border"><i class="fi fi-rr-align-left"></i></button>
                    <button class="btn btn-sm btn-light border"><i class="fi fi-rr-align-center"></i></button>
                    <button class="btn btn-sm btn-light border"><i class="fi fi-rr-align-right"></i></button>
                    <span class="border-start mx-1 h-100"></span>
                    <button class="btn btn-sm btn-light border"><i class="fi fi-rr-link"></i></button>
                  </div>
                  <textarea class="form-control border-0 rounded-0" rows="15" placeholder="Start writing or type / to choose a block"></textarea>
                  <div class="bg-light border-top p-1 text-end small text-muted">
                    Word count: 0
                  </div>
                </div>

              </div>
            </div>
          </div>

          <!-- Sidebar Meta Boxes (Right Column) -->
          <div class="col-lg-4">
            
            <div class="card border-0 shadow-sm rounded-0 h-100 bg-body border-start">
              
              <!-- Tabs -->
              <ul class="nav nav-tabs border-bottom bg-body px-2 pt-2 d-flex flex-nowrap" id="sidebarTabs" role="tablist" style="border-bottom-width: 1px;">
                <li class="nav-item" role="presentation">
                  <button class="nav-link active text-body fw-medium py-2 px-3 fs-6 rounded-0 border-0 bg-transparent" id="page-tab" data-bs-toggle="tab" data-bs-target="#page-pane" type="button" role="tab" style="box-shadow: inset 0 -2px 0 0 var(--bs-dark); margin-bottom: -1px;">Page</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link text-muted py-2 px-3 fs-6 rounded-0 border-0 bg-transparent hover-dark" id="block-tab" data-bs-toggle="tab" data-bs-target="#block-pane" type="button" role="tab" style="margin-bottom: -1px;">Block</button>
                </li>
                <li class="nav-item ms-auto" role="presentation">
                  <button class="nav-link text-muted px-2 hover-dark bg-transparent border-0"><i class="fi fi-rr-cross-small"></i></button>
                </li>
              </ul>

              <div class="tab-content" id="sidebarTabsContent">
                
                <!-- Page Pane -->
                <div class="tab-pane fade show active" id="page-pane" role="tabpanel" aria-labelledby="page-tab">
                  <div class="card-body p-4">
                    
                    <div class="d-flex align-items-center justify-content-between mb-3">
                      <div class="fw-bold d-flex align-items-center gap-2 text-body">
                        <i class="fi fi-rr-document"></i> No title
                      </div>
                      <button class="btn btn-sm btn-link text-muted p-0 hover-dark"><i class="fi fi-rr-menu-dots-vertical"></i></button>
                    </div>

                    <div class="mb-3">
                      <button class="btn w-100 py-2 text-body bg-body border border-secondary-subtle" style="font-size: 0.9rem;">Set featured image</button>
                    </div>

                    <p class="text-muted small mb-4">Last edited a second ago.</p>

                    <!-- Status & Publish Properties -->
                    <div class="mb-4">
                      <div class="d-flex justify-content-between align-items-start mb-3">
                        <span class="text-body small">Status</span>
                        <a href="#" class="text-decoration-none small d-flex align-items-center gap-1"><i class="fi fi-rr-circle-small text-primary"></i> Draft</a>
                      </div>
                      <div class="d-flex justify-content-between align-items-start mb-3">
                        <span class="text-body small">Publish</span>
                        <a href="#" class="text-decoration-none small">Immediately</a>
                      </div>
                      <div class="d-flex justify-content-between align-items-start mb-3">
                        <span class="text-body small">Slug</span>
                        <a href="#" class="text-decoration-none small">404605</a>
                      </div>
                      <div class="d-flex justify-content-between align-items-start mb-3">
                        <span class="text-body small">Author</span>
                        <a href="#" class="text-decoration-none small text-end" style="max-width: 150px; line-height: 1.2;">Editorial team -<br>Daily Life Pulse</a>
                      </div>
                      <div class="d-flex justify-content-between align-items-start mb-3">
                        <span class="text-body small">Template</span>
                        <a href="#" class="text-decoration-none small">Default template</a>
                      </div>
                      <div class="d-flex justify-content-between align-items-start mb-3">
                        <span class="text-body small">Discussion</span>
                        <a href="#" class="text-decoration-none small">Closed</a>
                      </div>
                      <div class="d-flex justify-content-between align-items-start mb-4">
                        <span class="text-body small">Parent</span>
                        <a href="#" class="text-decoration-none small">None</a>
                      </div>

                      <div class="form-check form-switch d-flex align-items-center gap-2 mb-0">
                        <input class="form-check-input mt-0" type="checkbox" role="switch" id="lockModifiedDate">
                        <label class="form-check-label small text-body" for="lockModifiedDate">Lock Modified Date</label>
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
        </div>\n'''

with open('c:/laragon/www/LaravelCMShtml/pages-add.html', 'w', encoding='utf-8') as f:
    f.write(top_part + clean_middle + bottom_part)

print("Layout fixed.")
