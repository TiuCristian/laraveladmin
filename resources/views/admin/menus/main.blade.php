    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4 mt-3">
          <div class="d-flex align-items-center gap-2">
            <h3 class="mb-0 fw-normal">Menus</h3>
          </div>
        </div>

        @if(session('success'))
            <div class="alert alert-success alert-dismissible fade show mb-4" role="alert">
                {{ session('success') }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        @endif

        <div class="row">
          <div class="col-12">
            
            <ul class="nav nav-tabs border-bottom-0 mb-0" id="menuTabs" role="tablist">
              <li class="nav-item" role="presentation">
                <button class="nav-link {{ request('tab') != 'manage-locations' ? 'active bg-body text-body fw-bold' : 'bg-body-tertiary text-muted' }} border border-bottom-0 px-4" id="edit-menus-tab" data-bs-toggle="tab" data-bs-target="#edit-menus" type="button" role="tab">Edit Menus</button>
              </li>
              <li class="nav-item ms-1" role="presentation">
                <button class="nav-link {{ request('tab') == 'manage-locations' ? 'active bg-body text-body fw-bold' : 'bg-body-tertiary text-muted' }} border border-bottom-0 px-4" id="manage-locations-tab" data-bs-toggle="tab" data-bs-target="#manage-locations" type="button" role="tab">Manage Locations</button>
              </li>
            </ul>

            <div class="tab-content" id="menuTabsContent">
              <!-- Edit Menus Tab -->
              <div class="tab-pane fade {{ request('tab') != 'manage-locations' ? 'show active' : '' }}" id="edit-menus" role="tabpanel">
                
                <div class="card border border-top-0 bg-body shadow-sm mb-0 rounded-0 rounded-bottom">
                  <div class="card-body py-2 px-3 d-flex flex-wrap align-items-center gap-3">
                    <form action="{{ route('menus.index') }}" method="GET" class="d-flex align-items-center gap-3 m-0">
                        <label for="selectMenu" class="fw-medium text-body small">Select a menu to edit:</label>
                        <select class="form-select form-select-sm w-auto" name="menu" id="selectMenu" onchange="this.form.submit()">
                          @foreach($menus as $m)
                            <option value="{{ $m->id }}" {{ ($activeMenu && $activeMenu->id == $m->id) ? 'selected' : '' }}>{{ $m->name }}</option>
                          @endforeach
                        </select>
                        <button type="submit" class="btn btn-sm btn-outline-secondary px-3">Select</button>
                    </form>
                    <span class="text-body small ms-2">or <a href="#" onclick="document.getElementById('createMenuDiv').classList.remove('d-none'); document.getElementById('editMenuDiv').classList.add('d-none'); return false;" class="text-primary text-decoration-none">create a new menu</a>.</span>
                  </div>
                </div>

                <!-- Create New Menu Section -->
                <div id="createMenuDiv" class="row mt-4 d-none">
                    <div class="col-12">
                        <div class="card bg-body border shadow-sm">
                            <div class="card-body p-4">
                                <h5 class="fw-bold text-body mb-3">Create New Menu</h5>
                                <form action="{{ route('menus.store') }}" method="POST">
                                    @csrf
                                    <div class="mb-3">
                                        <label class="form-label text-body small fw-bold">Menu Name</label>
                                        <input type="text" name="name" class="form-control w-50" required>
                                    </div>
                                    <button type="submit" class="btn btn-primary btn-sm px-4">Create Menu</button>
                                    <button type="button" onclick="document.getElementById('createMenuDiv').classList.add('d-none'); document.getElementById('editMenuDiv').classList.remove('d-none');" class="btn btn-light btn-sm px-4 ms-2 border">Cancel</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>

                @if($activeMenu)
                <!-- Edit Existing Menu Section -->
                <div id="editMenuDiv" class="row mt-4">
                  <!-- Left Sidebar: Add Menu Items -->
                  <div class="col-lg-4 col-xl-3">
                    <h6 class="fw-bold mb-3 text-body">Add menu items</h6>
                    
                    <div class="accordion" id="addMenuAccordion">
                      
                      <!-- Pages Accordion -->
                      <div class="accordion-item border mb-2 bg-body">
                        <h2 class="accordion-header">
                          <button class="accordion-button bg-transparent shadow-none px-3 py-3 fw-bold text-body border-bottom" type="button" data-bs-toggle="collapse" data-bs-target="#collapsePages" aria-expanded="true">
                            Pages
                          </button>
                        </h2>
                        <div id="collapsePages" class="accordion-collapse collapse show" data-bs-parent="#addMenuAccordion">
                          <div class="accordion-body p-3">
                            <div class="border rounded p-2 mb-3 bg-body" style="max-height: 150px; overflow-y: auto;">
                              @foreach($pages as $page)
                              <div class="form-check mb-2">
                                <input class="form-check-input page-checkbox" type="checkbox" id="page_{{ $page->id }}" value="{{ $page->id }}" data-title="{{ $page->title }}" data-url="/{{ $page->slug }}">
                                <label class="form-check-label small text-body" for="page_{{ $page->id }}">{{ $page->title }}</label>
                              </div>
                              @endforeach
                            </div>
                            <div class="d-flex justify-content-between align-items-center pt-2">
                              <div class="form-check mb-0">
                                <input class="form-check-input" type="checkbox" onchange="document.querySelectorAll('.page-checkbox').forEach(cb => cb.checked = this.checked)">
                                <label class="form-check-label small text-body">Select All</label>
                              </div>
                              <button type="button" onclick="addItemsToMenu('page')" class="btn btn-sm btn-outline-secondary px-3">Add to Menu</button>
                            </div>
                          </div>
                        </div>
                      </div>

                      <!-- Posts Accordion -->
                      <div class="accordion-item border mb-2 bg-body">
                        <h2 class="accordion-header">
                          <button class="accordion-button collapsed bg-transparent shadow-none px-3 py-3 fw-bold text-body" type="button" data-bs-toggle="collapse" data-bs-target="#collapsePosts">
                            Posts
                          </button>
                        </h2>
                        <div id="collapsePosts" class="accordion-collapse collapse" data-bs-parent="#addMenuAccordion">
                          <div class="accordion-body p-3">
                            <div class="border rounded p-2 mb-3 bg-body" style="max-height: 150px; overflow-y: auto;">
                              @foreach($posts as $post)
                              <div class="form-check mb-2">
                                <input class="form-check-input post-checkbox" type="checkbox" id="post_{{ $post->id }}" value="{{ $post->id }}" data-title="{{ $post->title }}" data-url="/post/{{ $post->slug }}">
                                <label class="form-check-label small text-body" for="post_{{ $post->id }}">{{ $post->title }}</label>
                              </div>
                              @endforeach
                            </div>
                            <div class="d-flex justify-content-between align-items-center pt-2">
                              <div class="form-check mb-0">
                                <input class="form-check-input" type="checkbox" onchange="document.querySelectorAll('.post-checkbox').forEach(cb => cb.checked = this.checked)">
                                <label class="form-check-label small text-body">Select All</label>
                              </div>
                              <button type="button" onclick="addItemsToMenu('post')" class="btn btn-sm btn-outline-secondary px-3">Add to Menu</button>
                            </div>
                          </div>
                        </div>
                      </div>
                      
                      <!-- Categories Accordion -->
                      <div class="accordion-item border mb-2 bg-body">
                        <h2 class="accordion-header">
                          <button class="accordion-button collapsed bg-transparent shadow-none px-3 py-3 fw-bold text-body" type="button" data-bs-toggle="collapse" data-bs-target="#collapseCats">
                            Categories
                          </button>
                        </h2>
                        <div id="collapseCats" class="accordion-collapse collapse" data-bs-parent="#addMenuAccordion">
                          <div class="accordion-body p-3">
                            <div class="border rounded p-2 mb-3 bg-body" style="max-height: 150px; overflow-y: auto;">
                              @foreach($categories as $category)
                              <div class="form-check mb-2">
                                <input class="form-check-input category-checkbox" type="checkbox" id="cat_{{ $category->id }}" value="{{ $category->id }}" data-title="{{ $category->name }}" data-url="/category/{{ $category->slug }}">
                                <label class="form-check-label small text-body" for="cat_{{ $category->id }}">{{ $category->name }}</label>
                              </div>
                              @endforeach
                            </div>
                            <div class="d-flex justify-content-between align-items-center pt-2">
                              <div class="form-check mb-0">
                                <input class="form-check-input" type="checkbox" onchange="document.querySelectorAll('.category-checkbox').forEach(cb => cb.checked = this.checked)">
                                <label class="form-check-label small text-body">Select All</label>
                              </div>
                              <button type="button" onclick="addItemsToMenu('category')" class="btn btn-sm btn-outline-secondary px-3">Add to Menu</button>
                            </div>
                          </div>
                        </div>
                      </div>

                      <!-- Custom Links Accordion -->
                      <div class="accordion-item border mb-2 bg-body">
                        <h2 class="accordion-header">
                          <button class="accordion-button collapsed bg-transparent shadow-none px-3 py-3 fw-bold text-body" type="button" data-bs-toggle="collapse" data-bs-target="#collapseCustom">
                            Custom Links
                          </button>
                        </h2>
                        <div id="collapseCustom" class="accordion-collapse collapse" data-bs-parent="#addMenuAccordion">
                          <div class="accordion-body px-3 py-3">
                            <div class="mb-2">
                              <label class="form-label small text-muted mb-1">URL</label>
                              <input type="url" id="customLinkUrl" class="form-control form-control-sm" value="http://">
                            </div>
                            <div class="mb-3">
                              <label class="form-label small text-muted mb-1">Link Text</label>
                              <input type="text" id="customLinkText" class="form-control form-control-sm">
                            </div>
                            <div class="text-end">
                              <button type="button" onclick="addCustomLinkToMenu()" class="btn btn-sm btn-outline-secondary">Add to Menu</button>
                            </div>
                          </div>
                        </div>
                      </div>

                    </div>
                  </div>

                  <!-- Right Area: Menu Structure -->
                  <div class="col-lg-8 col-xl-9">
                    <h6 class="fw-bold mb-3 text-body">Menu structure</h6>
                    
                    <form id="menuForm" action="{{ route('menus.update', $activeMenu->id) }}" method="POST">
                        @csrf
                        @method('PUT')
                        <input type="hidden" name="items" id="menuItemsInput">
                        
                        <div class="border bg-body mb-4">
                          <div class="p-3 border-bottom d-flex align-items-center bg-body-tertiary">
                            <label class="fw-bold text-body mb-0 me-3">Menu Name</label>
                            <input type="text" name="name" class="form-control form-control-sm" value="{{ $activeMenu->name }}" style="max-width: 300px;">
                          </div>

                          <div class="p-4 bg-body border-bottom">
                            <p class="text-body small mb-3">Drag the items into the order you prefer. Click the trash icon to remove an item.</p>

                            <!-- Sortable Menu Items Container -->
                            <div id="menuSortable" class="mb-3">
                              @if($activeMenu->items)
                                  @foreach($activeMenu->items as $item)
                                  <div class="menu-item-bar mb-2" style="max-width: 450px;" data-title="{{ $item['title'] }}" data-url="{{ $item['url'] }}" data-type="{{ $item['type'] ?? 'custom' }}">
                                    <div class="menu-item-handle bg-body-tertiary border p-2 d-flex align-items-center justify-content-between">
                                      <div class="fw-bold text-body small item-title">{{ $item['title'] }}</div>
                                      <div class="d-flex align-items-center gap-3">
                                        <span class="text-muted small item-type" style="text-transform: capitalize;">{{ $item['type'] ?? 'Custom Link' }}</span>
                                        <button class="btn btn-sm btn-link p-0 text-danger shadow-none" type="button" onclick="this.closest('.menu-item-bar').remove()"><i class="fas fa-trash"></i></button>
                                      </div>
                                    </div>
                                  </div>
                                  @endforeach
                              @endif
                            </div>
                            
                            <!-- Menu Settings -->
                            <h6 class="fw-bold text-body mt-4 mb-3 pt-2">Menu Settings</h6>
                            
                            <div class="row mb-2">
                              <div class="col-sm-3 col-md-4 col-lg-3">
                                <span class="text-body small">Auto add pages</span>
                              </div>
                              <div class="col-sm-9 col-md-8 col-lg-9">
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" name="auto_add_pages" value="1" id="autoAdd" {{ $activeMenu->auto_add_pages ? 'checked' : '' }}>
                                  <label class="form-check-label text-body small" for="autoAdd">
                                    Automatically add new top-level pages to this menu
                                  </label>
                                </div>
                              </div>
                            </div>
                            
                            <div class="row">
                              <div class="col-sm-3 col-md-4 col-lg-3">
                                <span class="text-body small">Display location</span>
                              </div>
                              <div class="col-sm-9 col-md-8 col-lg-9">
                                <div class="form-check mb-1">
                                  <input class="form-check-input" type="checkbox" name="locations[]" value="primary" id="locPrimary" {{ isset($locations['primary']) && $locations['primary'] == $activeMenu->id ? 'checked' : '' }}>
                                  <label class="form-check-label text-body small" for="locPrimary">Primary Menu</label>
                                </div>
                                <div class="form-check mb-1">
                                  <input class="form-check-input" type="checkbox" name="locations[]" value="footer" id="locFooter" {{ isset($locations['footer']) && $locations['footer'] == $activeMenu->id ? 'checked' : '' }}>
                                  <label class="form-check-label text-body small" for="locFooter">Footer Menu</label>
                                </div>
                                <div class="form-check mb-1">
                                  <input class="form-check-input" type="checkbox" name="locations[]" value="mobile" id="locMobile" {{ isset($locations['mobile']) && $locations['mobile'] == $activeMenu->id ? 'checked' : '' }}>
                                  <label class="form-check-label text-body small" for="locMobile">Mobile Menu</label>
                                </div>
                              </div>
                            </div>

                          </div>
                          
                          <div class="p-3 bg-body-tertiary d-flex justify-content-between align-items-center">
                            <button type="button" onclick="if(confirm('Are you sure you want to delete this menu?')) document.getElementById('deleteMenuForm').submit();" class="btn btn-link text-danger small text-decoration-none hover-danger p-0">Delete Menu</button>
                            <button type="button" onclick="saveMenu()" class="btn btn-primary btn-sm px-4 waves-effect">Save Menu</button>
                          </div>

                        </div>
                    </form>
                    
                    <form id="deleteMenuForm" action="{{ route('menus.destroy', $activeMenu->id) }}" method="POST" class="d-none">
                        @csrf
                        @method('DELETE')
                    </form>

                  </div>
                </div>
                @endif

              </div>

              <!-- Manage Locations Tab -->
              <div class="tab-pane fade {{ request('tab') == 'manage-locations' ? 'show active' : '' }}" id="manage-locations" role="tabpanel">
                <div class="card border border-top-0 bg-body shadow-sm mb-4 rounded-0 rounded-bottom">
                  <div class="card-body p-4">
                    <p class="text-body small mb-4">Your theme supports 3 menus. Select which menu appears in each location.</p>
                    
                    <form action="{{ route('menus.locations') }}" method="POST">
                        @csrf
                        <div class="table-responsive" style="max-width: 800px;">
                          <table class="table table-bordered align-middle">
                            <thead class="table-light">
                              <tr>
                                <th class="fw-medium text-body small" style="width: 30%;">Theme Location</th>
                                <th class="fw-medium text-body small">Assigned Menu</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr>
                                <td class="text-body small fw-medium">Primary Menu</td>
                                <td>
                                    <select name="locations[primary]" class="form-select form-select-sm w-auto">
                                      <option value="">- Select a Menu -</option>
                                      @foreach($menus as $m)
                                        <option value="{{ $m->id }}" {{ isset($locations['primary']) && $locations['primary'] == $m->id ? 'selected' : '' }}>{{ $m->name }}</option>
                                      @endforeach
                                    </select>
                                </td>
                              </tr>
                              <tr>
                                <td class="text-body small fw-medium">Footer Menu</td>
                                <td>
                                    <select name="locations[footer]" class="form-select form-select-sm w-auto">
                                      <option value="">- Select a Menu -</option>
                                      @foreach($menus as $m)
                                        <option value="{{ $m->id }}" {{ isset($locations['footer']) && $locations['footer'] == $m->id ? 'selected' : '' }}>{{ $m->name }}</option>
                                      @endforeach
                                    </select>
                                </td>
                              </tr>
                              <tr>
                                <td class="text-body small fw-medium">Mobile Menu</td>
                                <td>
                                    <select name="locations[mobile]" class="form-select form-select-sm w-auto">
                                      <option value="">- Select a Menu -</option>
                                      @foreach($menus as $m)
                                        <option value="{{ $m->id }}" {{ isset($locations['mobile']) && $locations['mobile'] == $m->id ? 'selected' : '' }}>{{ $m->name }}</option>
                                      @endforeach
                                    </select>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                        
                        <div class="mt-3">
                          <button type="submit" class="btn btn-primary btn-sm px-4">Save Changes</button>
                        </div>
                    </form>

                  </div>
                </div>
              </div>

            </div>

          </div>
        </div>

      </div>
    </main>
    <!-- end::Main Content Area -->
