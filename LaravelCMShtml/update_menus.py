import re

with open('c:/laragon/www/LaravelCMShtml/appearance-menus.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_content = '''
        <!-- Screen Options & Help Tabs -->
        <div class="d-flex justify-content-end mb-4 position-relative" style="margin-top: -1px; z-index: 4;">
          <button class="btn btn-light btn-sm shadow-sm text-muted bg-white border border-top-0 px-3" type="button" style="border-radius: 0 0 4px 4px; font-size: 0.8rem;">
            Screen Options <i class="fi fi-rr-caret-down ms-1"></i>
          </button>
          <button class="btn btn-light btn-sm shadow-sm text-muted bg-white border border-top-0 px-3 ms-2" type="button" style="border-radius: 0 0 4px 4px; font-size: 0.8rem;">
            Help <i class="fi fi-rr-caret-down ms-1"></i>
          </button>
        </div>

        <!-- Update Notice -->
        <div class="alert bg-white border border-start-0 border-end-0 border-bottom-0 shadow-sm p-3 mb-4" style="border-left: 4px solid #ffb900 !important;">
          <span class="text-dark">WordPress 7.0 is available! <a href="dashboard-updates.html" class="text-decoration-none">Please update now.</a></span>
        </div>

        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div class="d-flex align-items-center gap-2">
            <h3 class="mb-0 fw-normal">Menus</h3>
            <button class="btn btn-outline-primary bg-white btn-sm mt-1">Manage with Live Preview</button>
          </div>
        </div>

        <div class="row">
          <div class="col-12">
            
            <ul class="nav nav-tabs border-bottom-0 mb-0" id="menuTabs" role="tablist">
              <li class="nav-item" role="presentation">
                <button class="nav-link active bg-white border border-bottom-0 text-dark fw-bold px-4" id="edit-menus-tab" data-bs-toggle="tab" data-bs-target="#edit-menus" type="button" role="tab">Edit Menus</button>
              </li>
              <li class="nav-item ms-1" role="presentation">
                <button class="nav-link bg-light border border-bottom-0 text-muted px-4" id="manage-locations-tab" data-bs-toggle="tab" data-bs-target="#manage-locations" type="button" role="tab">Manage Locations</button>
              </li>
            </ul>

            <div class="tab-content" id="menuTabsContent">
              <!-- Edit Menus Tab -->
              <div class="tab-pane fade show active" id="edit-menus" role="tabpanel">
                
                <div class="card border border-top-0 bg-white shadow-sm mb-0 rounded-0 rounded-bottom">
                  <div class="card-body py-2 px-3 d-flex flex-wrap align-items-center gap-3">
                    <label for="selectMenu" class="fw-medium text-dark small">Select a menu to edit:</label>
                    <select class="form-select form-select-sm w-auto" id="selectMenu">
                      <option>Footer Menu (Footer Menu)</option>
                    </select>
                    <button class="btn btn-sm btn-outline-secondary px-3">Select</button>
                    <span class="text-dark small ms-2">or <a href="#" class="text-primary text-decoration-none">create a new menu</a>. Do not forget to save your changes!</span>
                  </div>
                </div>

                <div class="row mt-4">
                  
                  <!-- Left Sidebar: Add Menu Items -->
                  <div class="col-lg-4 col-xl-3">
                    <h6 class="fw-bold mb-3 text-dark">Add menu items</h6>
                    
                    <div class="accordion" id="addMenuAccordion">
                      
                      <!-- Pages Accordion -->
                      <div class="accordion-item border mb-2 bg-white">
                        <h2 class="accordion-header">
                          <button class="accordion-button bg-transparent shadow-none px-3 py-3 fw-bold text-dark border-bottom" type="button" data-bs-toggle="collapse" data-bs-target="#collapsePages" aria-expanded="true">
                            Pages
                          </button>
                        </h2>
                        <div id="collapsePages" class="accordion-collapse collapse show" data-bs-parent="#addMenuAccordion">
                          <div class="accordion-body p-3">
                            <ul class="nav nav-tabs nav-sm mb-3 border-bottom" style="font-size: 0.8rem;">
                              <li class="nav-item"><a class="nav-link active px-2 py-1 border-bottom-0 text-dark fw-medium" href="#">Most Recent</a></li>
                              <li class="nav-item"><a class="nav-link text-primary px-2 py-1 border-0" href="#">View All</a></li>
                              <li class="nav-item"><a class="nav-link text-primary px-2 py-1 border-0" href="#">Search</a></li>
                            </ul>
                            <div class="border rounded p-2 mb-3 bg-white" style="max-height: 150px; overflow-y: auto;">
                              <div class="form-check mb-2">
                                <input class="form-check-input" type="checkbox" id="pageTopics">
                                <label class="form-check-label small text-dark" for="pageTopics">Topics</label>
                              </div>
                              <div class="form-check mb-2">
                                <input class="form-check-input" type="checkbox" id="pageTerms">
                                <label class="form-check-label small text-dark" for="pageTerms">Terms and Conditions</label>
                              </div>
                              <div class="form-check mb-2">
                                <input class="form-check-input" type="checkbox" id="pageContact">
                                <label class="form-check-label small text-dark" for="pageContact">Contact Daily Life Pulse</label>
                              </div>
                              <div class="form-check mb-0">
                                <input class="form-check-input" type="checkbox" id="pageAbout">
                                <label class="form-check-label small text-dark" for="pageAbout">About Daily Life Pulse</label>
                              </div>
                            </div>
                            <div class="d-flex justify-content-between align-items-center pt-2">
                              <div class="form-check mb-0">
                                <input class="form-check-input" type="checkbox" id="selectAllPages">
                                <label class="form-check-label small text-dark" for="selectAllPages">Select All</label>
                              </div>
                              <button class="btn btn-sm btn-outline-secondary px-3">Add to Menu</button>
                            </div>
                          </div>
                        </div>
                      </div>

                      <!-- Posts Accordion -->
                      <div class="accordion-item border mb-2 bg-white">
                        <h2 class="accordion-header">
                          <button class="accordion-button collapsed bg-transparent shadow-none px-3 py-3 fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#collapsePosts">
                            Posts
                          </button>
                        </h2>
                        <div id="collapsePosts" class="accordion-collapse collapse" data-bs-parent="#addMenuAccordion">
                          <div class="accordion-body px-3 py-3 text-muted small">
                            Search and add posts.
                          </div>
                        </div>
                      </div>

                      <!-- Custom Links Accordion -->
                      <div class="accordion-item border mb-2 bg-white">
                        <h2 class="accordion-header">
                          <button class="accordion-button collapsed bg-transparent shadow-none px-3 py-3 fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#collapseCustom">
                            Custom Links
                          </button>
                        </h2>
                        <div id="collapseCustom" class="accordion-collapse collapse" data-bs-parent="#addMenuAccordion">
                          <div class="accordion-body px-3 py-3">
                            <div class="mb-2">
                              <label class="form-label small text-muted mb-1">URL</label>
                              <input type="url" class="form-control form-control-sm" value="http://">
                            </div>
                            <div class="mb-3">
                              <label class="form-label small text-muted mb-1">Link Text</label>
                              <input type="text" class="form-control form-control-sm">
                            </div>
                            <div class="text-end">
                              <button class="btn btn-sm btn-outline-secondary">Add to Menu</button>
                            </div>
                          </div>
                        </div>
                      </div>

                      <!-- Categories Accordion -->
                      <div class="accordion-item border mb-2 bg-white">
                        <h2 class="accordion-header">
                          <button class="accordion-button collapsed bg-transparent shadow-none px-3 py-3 fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#collapseCats">
                            Categories
                          </button>
                        </h2>
                        <div id="collapseCats" class="accordion-collapse collapse" data-bs-parent="#addMenuAccordion">
                          <div class="accordion-body px-3 py-3 text-muted small">
                            Select categories.
                          </div>
                        </div>
                      </div>

                    </div>

                  </div>

                  <!-- Right Area: Menu Structure -->
                  <div class="col-lg-8 col-xl-9">
                    
                    <h6 class="fw-bold mb-3 text-dark">Menu structure</h6>
                    
                    <div class="border bg-white mb-4">
                      <div class="p-3 border-bottom d-flex align-items-center bg-light">
                        <label class="fw-bold text-dark mb-0 me-3">Menu Name</label>
                        <input type="text" class="form-control form-control-sm" value="Footer Menu" style="max-width: 300px;">
                      </div>

                      <div class="p-4 bg-white border-bottom">
                        <p class="text-dark small mb-3">Drag the items into the order you prefer. Click the arrow on the right of the item to reveal additional configuration options.</p>

                        <div class="mb-3">
                          <button class="btn btn-sm btn-outline-secondary px-3 bg-light text-dark"><input type="checkbox" class="me-2"> Bulk Select</button>
                        </div>

                        <!-- Sortable Menu Items Container -->
                        <div id="menuSortable" class="mb-3">
                          
                          <!-- Item 1 -->
                          <div class="menu-item-bar mb-2" style="max-width: 450px;">
                            <div class="menu-item-handle bg-light border p-2 d-flex align-items-center justify-content-between">
                              <div class="fw-bold text-dark small">Privacy Policy</div>
                              <div class="d-flex align-items-center gap-3">
                                <span class="text-muted small">Privacy Policy Page</span>
                                <button class="btn btn-sm btn-link p-0 text-muted shadow-none" type="button"><i class="fi fi-rr-caret-down"></i></button>
                              </div>
                            </div>
                          </div>

                          <!-- Item 2 -->
                          <div class="menu-item-bar mb-2" style="max-width: 450px;">
                            <div class="menu-item-handle bg-light border p-2 d-flex align-items-center justify-content-between">
                              <div class="fw-bold text-dark small">Terms and Conditions</div>
                              <div class="d-flex align-items-center gap-3">
                                <span class="text-muted small">Page</span>
                                <button class="btn btn-sm btn-link p-0 text-muted shadow-none" type="button"><i class="fi fi-rr-caret-down"></i></button>
                              </div>
                            </div>
                          </div>

                          <!-- Item 3 -->
                          <div class="menu-item-bar mb-2" style="max-width: 450px;">
                            <div class="menu-item-handle bg-light border p-2 d-flex align-items-center justify-content-between">
                              <div class="fw-bold text-dark small">Contact Daily Life Pulse</div>
                              <div class="d-flex align-items-center gap-3">
                                <span class="text-muted small">Page</span>
                                <button class="btn btn-sm btn-link p-0 text-muted shadow-none" type="button"><i class="fi fi-rr-caret-down"></i></button>
                              </div>
                            </div>
                          </div>

                        </div>
                        
                        <div class="mb-2">
                          <button class="btn btn-sm btn-outline-secondary px-3 bg-light text-dark"><input type="checkbox" class="me-2"> Bulk Select</button>
                        </div>

                        <!-- Menu Settings -->
                        <h6 class="fw-bold text-dark mt-4 mb-3 pt-2">Menu Settings</h6>
                        
                        <div class="row mb-2">
                          <div class="col-sm-3 col-md-4 col-lg-3">
                            <span class="text-dark small">Auto add pages</span>
                          </div>
                          <div class="col-sm-9 col-md-8 col-lg-9">
                            <div class="form-check">
                              <input class="form-check-input" type="checkbox" id="autoAdd">
                              <label class="form-check-label text-dark small" for="autoAdd">
                                Automatically add new top-level pages to this menu
                              </label>
                            </div>
                          </div>
                        </div>
                        
                        <div class="row">
                          <div class="col-sm-3 col-md-4 col-lg-3">
                            <span class="text-dark small">Display location</span>
                          </div>
                          <div class="col-sm-9 col-md-8 col-lg-9">
                            <div class="form-check mb-1">
                              <input class="form-check-input" type="checkbox" id="locFooter" checked>
                              <label class="form-check-label text-dark small" for="locFooter">
                                Footer Menu <span class="text-muted">(Currently set to: Footer Menu)</span>
                              </label>
                            </div>
                            <div class="form-check mb-1">
                              <input class="form-check-input" type="checkbox" id="locMobile">
                              <label class="form-check-label text-dark small" for="locMobile">
                                Mobile Menu <span class="text-muted">(Currently set to: Mobile Menu)</span>
                              </label>
                            </div>
                            <div class="form-check">
                              <input class="form-check-input" type="checkbox" id="locPrimary">
                              <label class="form-check-label text-dark small" for="locPrimary">
                                Primary <span class="text-muted">(Currently set to: Menu 1)</span>
                              </label>
                            </div>
                          </div>
                        </div>

                      </div>
                      
                      <div class="p-3 bg-light d-flex justify-content-between align-items-center">
                        <a href="#" class="text-danger small text-decoration-none hover-danger">Delete Menu</a>
                        <button class="btn btn-primary btn-sm px-4 waves-effect">Save Menu</button>
                      </div>

                    </div>
                  </div>
                </div>

              </div>

              <!-- Manage Locations Tab -->
              <div class="tab-pane fade" id="manage-locations" role="tabpanel">
                <div class="card border border-top-0 bg-white shadow-sm mb-4 rounded-0 rounded-bottom">
                  <div class="card-body p-4">
                    <p class="text-dark small mb-4">Your theme supports 3 menus. Select which menu appears in each location.</p>
                    
                    <div class="table-responsive" style="max-width: 800px;">
                      <table class="table table-bordered align-middle">
                        <thead class="table-light">
                          <tr>
                            <th class="fw-medium text-dark small" style="width: 30%;">Theme Location</th>
                            <th class="fw-medium text-dark small">Assigned Menu</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <td class="text-dark small fw-medium">Footer Menu</td>
                            <td>
                              <div class="d-flex align-items-center gap-2">
                                <select class="form-select form-select-sm w-auto">
                                  <option>Footer Menu</option>
                                  <option>Mobile Menu</option>
                                  <option>Menu 1</option>
                                </select>
                                <a href="#" class="small text-primary text-decoration-none">Edit</a>
                                <a href="#" class="small text-primary text-decoration-none">Use new menu</a>
                              </div>
                            </td>
                          </tr>
                          <tr>
                            <td class="text-dark small fw-medium">Mobile Menu</td>
                            <td>
                              <div class="d-flex align-items-center gap-2">
                                <select class="form-select form-select-sm w-auto">
                                  <option>Footer Menu</option>
                                  <option selected>Mobile Menu</option>
                                  <option>Menu 1</option>
                                </select>
                                <a href="#" class="small text-primary text-decoration-none">Edit</a>
                                <a href="#" class="small text-primary text-decoration-none">Use new menu</a>
                              </div>
                            </td>
                          </tr>
                          <tr>
                            <td class="text-dark small fw-medium">Primary</td>
                            <td>
                              <div class="d-flex align-items-center gap-2">
                                <select class="form-select form-select-sm w-auto">
                                  <option>Footer Menu</option>
                                  <option>Mobile Menu</option>
                                  <option selected>Menu 1</option>
                                </select>
                                <a href="#" class="small text-primary text-decoration-none">Edit</a>
                                <a href="#" class="small text-primary text-decoration-none">Use new menu</a>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    
                    <div class="mt-3">
                      <button class="btn btn-primary btn-sm px-4">Save Changes</button>
                    </div>

                  </div>
                </div>
              </div>

            </div>

          </div>
        </div>
'''

pattern = r'<!-- Page Title & Breadcrumbs -->.*?</div>\s*</div>\s*</div>\s*</main>'
replacement = new_content + '\n      </div>\n    </main>'

new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open('c:/laragon/www/LaravelCMShtml/appearance-menus.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated appearance-menus.html to match screenshot")
