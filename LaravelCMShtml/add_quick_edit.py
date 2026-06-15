import re

with open('c:/laragon/www/LaravelCMShtml/pages-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to replace the first page row to add the ID and the javascript toggle, and then insert the quick edit row right after it.

row_1_old = '''                <!-- Page Row 1 -->
                <tr>
                  <td class="ps-3 align-top pt-3">
                    <input class="form-check-input" type="checkbox">
                  </td>
                  <td class="align-top pt-3" style="width: 35%;">
                    <a href="pages-edit.html" class="fw-bold text-dark text-decoration-none">About Daily Life Pulse</a>
                    <div class="small mt-1 text-muted" style="font-size: 0.8rem;">
                      <a href="pages-edit.html" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                      <a href="#" class="text-decoration-none text-primary hover-primary">Quick Edit</a> <span class="text-light">|</span>'''

row_1_new = '''                <!-- Page Row 1 -->
                <tr id="row1">
                  <td class="ps-3 align-top pt-3">
                    <input class="form-check-input" type="checkbox">
                  </td>
                  <td class="align-top pt-3" style="width: 35%;">
                    <a href="pages-edit.html" class="fw-bold text-dark text-decoration-none">About Daily Life Pulse</a>
                    <div class="small mt-1 text-muted" style="font-size: 0.8rem;">
                      <a href="pages-edit.html" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                      <a href="javascript:void(0);" onclick="document.getElementById('row1').classList.add('d-none'); document.getElementById('quickEditRow1').classList.remove('d-none');" class="text-decoration-none text-primary hover-primary">Quick Edit</a> <span class="text-light">|</span>'''

html = html.replace(row_1_old, row_1_new)


# Now insert the Quick Edit Row right after the end of row 1
# Row 1 ends with:
row_1_end = '''                  </td>
                </tr>'''

quick_edit_row = '''                  </td>
                </tr>
                
                <!-- Quick Edit Row 1 -->
                <tr id="quickEditRow1" class="d-none bg-light">
                  <td colspan="6" class="p-4 border-bottom">
                    <div class="mb-3">
                      <h6 class="fw-bold small text-uppercase text-muted mb-0">Quick Edit</h6>
                    </div>
                    
                    <div class="row">
                      
                      <!-- Left Column -->
                      <div class="col-md-6 mb-3 mb-md-0">
                        
                        <div class="row mb-2 align-items-center">
                          <label class="col-sm-3 col-form-label small text-dark">Title</label>
                          <div class="col-sm-9">
                            <input type="text" class="form-control form-control-sm" value="About Daily Life Pulse">
                          </div>
                        </div>

                        <div class="row mb-2 align-items-center">
                          <label class="col-sm-3 col-form-label small text-dark">Slug</label>
                          <div class="col-sm-9">
                            <input type="text" class="form-control form-control-sm" value="about">
                          </div>
                        </div>

                        <div class="row mb-2 align-items-center">
                          <label class="col-sm-3 col-form-label small text-dark">Date</label>
                          <div class="col-sm-9">
                            <div class="d-flex align-items-center gap-1">
                              <select class="form-select form-select-sm px-1" style="width: auto;">
                                <option>01-Jan</option><option>02-Feb</option><option>03-Mar</option><option>04-Apr</option><option selected>05-May</option>
                              </select>
                              <input type="text" class="form-control form-control-sm text-center px-1" value="21" style="width: 40px;"> , 
                              <input type="text" class="form-control form-control-sm text-center px-1" value="2019" style="width: 50px;"> at 
                              <input type="text" class="form-control form-control-sm text-center px-1" value="07" style="width: 35px;"> : 
                              <input type="text" class="form-control form-control-sm text-center px-1" value="06" style="width: 35px;">
                            </div>
                          </div>
                        </div>

                        <div class="row align-items-center">
                          <label class="col-sm-3 col-form-label small text-dark">Password</label>
                          <div class="col-sm-9 d-flex align-items-center gap-2">
                            <input type="text" class="form-control form-control-sm" style="width: 120px;">
                            <span class="small text-muted">&ndash;OR&ndash;</span>
                            <div class="form-check mb-0">
                              <input class="form-check-input" type="checkbox" id="privateCheck">
                              <label class="form-check-label small text-dark" for="privateCheck">Private</label>
                            </div>
                          </div>
                        </div>

                      </div>

                      <!-- Right Column -->
                      <div class="col-md-6">
                        
                        <div class="row mb-2 align-items-center">
                          <label class="col-sm-3 col-form-label small text-dark">Parent</label>
                          <div class="col-sm-9">
                            <select class="form-select form-select-sm">
                              <option>Main Page (no parent)</option>
                              <option>&nbsp;&nbsp;&nbsp;Blog</option>
                            </select>
                          </div>
                        </div>

                        <div class="row mb-2 align-items-center">
                          <label class="col-sm-3 col-form-label small text-dark">Order</label>
                          <div class="col-sm-9">
                            <input type="number" class="form-control form-control-sm" value="0" style="width: 80px;">
                          </div>
                        </div>

                        <div class="row mb-3 align-items-center">
                          <label class="col-sm-3 col-form-label small text-dark">Template</label>
                          <div class="col-sm-9">
                            <select class="form-select form-select-sm">
                              <option>Default Template</option>
                              <option selected>About Us New</option>
                              <option>Contact Page</option>
                            </select>
                          </div>
                        </div>

                        <div class="row mb-3 align-items-center">
                          <div class="col-sm-9 offset-sm-3">
                            <div class="form-check mb-0">
                              <input class="form-check-input" type="checkbox" id="allowCommentsCheck">
                              <label class="form-check-label small text-dark" for="allowCommentsCheck">Allow Comments</label>
                            </div>
                          </div>
                        </div>

                        <div class="row align-items-center">
                          <label class="col-sm-3 col-form-label small text-dark">Status</label>
                          <div class="col-sm-9">
                            <select class="form-select form-select-sm" style="width: auto;">
                              <option selected>Published</option>
                              <option>Pending Review</option>
                              <option>Draft</option>
                            </select>
                          </div>
                        </div>

                      </div>

                    </div>
                    
                    <div class="mt-4 pt-3 border-top">
                      <button type="button" class="btn btn-sm btn-primary px-3 me-1" onclick="document.getElementById('quickEditRow1').classList.add('d-none'); document.getElementById('row1').classList.remove('d-none');">Update</button>
                      <button type="button" class="btn btn-sm btn-outline-secondary px-3" onclick="document.getElementById('quickEditRow1').classList.add('d-none'); document.getElementById('row1').classList.remove('d-none');">Cancel</button>
                    </div>

                  </td>
                </tr>'''

html = html.replace(row_1_end, quick_edit_row, 1)

with open('c:/laragon/www/LaravelCMShtml/pages-list.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added Quick Edit row functionality")
