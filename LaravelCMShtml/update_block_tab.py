import re

with open('c:/laragon/www/LaravelCMShtml/pages-add.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the tabs div
tabs_start_marker = '<!-- Tabs -->'
tabs_end_marker = '<div class="card-body p-4">'

tabs_start = content.find(tabs_start_marker)
tabs_end = content.find(tabs_end_marker)

if tabs_start != -1 and tabs_end != -1:
    
    new_tabs = '''<!-- Tabs -->
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
'''
    
    # We replace from tabs_start to tabs_end + len(tabs_end_marker)
    content = content[:tabs_start] + new_tabs + content[tabs_end + len(tabs_end_marker):]
    
    # Now we need to close the card-body, close the tab-pane, and add the Block pane.
    # The end of the sidebar card is right before </div>\n\n          </div>\n        </div>
    
    end_sidebar_marker = '</div>\n            </div>\n\n          </div>'
    end_sidebar_idx = content.find(end_sidebar_marker)
    
    if end_sidebar_idx != -1:
        
        block_pane = '''</div>
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
'''
        content = content[:end_sidebar_idx] + block_pane + content[end_sidebar_idx:]

    # Add a little script to toggle the active tab styling to mimic Gutenberg
    js_script = '''
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const pageTab = document.getElementById('page-tab');
      const blockTab = document.getElementById('block-tab');
      
      if(pageTab && blockTab) {
        pageTab.addEventListener('shown.bs.tab', function (event) {
          pageTab.classList.add('text-body');
          pageTab.classList.remove('text-muted');
          pageTab.style.boxShadow = 'inset 0 -2px 0 0 var(--bs-dark)';
          
          blockTab.classList.remove('text-body');
          blockTab.classList.add('text-muted');
          blockTab.style.boxShadow = 'none';
        });
        
        blockTab.addEventListener('shown.bs.tab', function (event) {
          blockTab.classList.add('text-body');
          blockTab.classList.remove('text-muted');
          blockTab.style.boxShadow = 'inset 0 -2px 0 0 var(--bs-dark)';
          
          pageTab.classList.remove('text-body');
          pageTab.classList.add('text-muted');
          pageTab.style.boxShadow = 'none';
        });
      }
    });
  </script>
</body>'''
    
    content = content.replace('</body>', js_script)

with open('c:/laragon/www/LaravelCMShtml/pages-add.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Block tab added.")
