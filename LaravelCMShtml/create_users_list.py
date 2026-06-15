import re

with open('c:/laragon/www/LaravelCMShtml/plugins-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0 d-inline-block me-2">Users</h3>
            <a href="users-add.html" class="btn btn-outline-primary btn-sm mb-1">Add New</a>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item active" aria-current="page">Users</li>
              </ol>
            </nav>
          </div>
        </div>

        <ul class="nav nav-pills nav-sm mb-3" style="font-size: 0.9rem;">
          <li class="nav-item"><a class="nav-link active fw-medium px-3 py-1" href="#">All <span class="badge bg-white text-primary ms-1">4</span></a></li>
          <li class="nav-item"><a class="nav-link text-muted px-3 py-1" href="#">Administrator <span class="badge bg-light text-dark ms-1">1</span></a></li>
          <li class="nav-item"><a class="nav-link text-muted px-3 py-1" href="#">Editor <span class="badge bg-light text-dark ms-1">1</span></a></li>
          <li class="nav-item"><a class="nav-link text-muted px-3 py-1" href="#">Subscriber <span class="badge bg-light text-dark ms-1">2</span></a></li>
        </ul>

        <!-- Filters & Bulk Actions -->
        <div class="row mb-3">
          <div class="col-12 d-flex flex-wrap align-items-center justify-content-between gap-2">
            
            <div class="d-flex flex-wrap align-items-center gap-2">
              <select class="form-select form-select-sm" style="width: auto;">
                <option>Bulk actions</option>
                <option>Delete</option>
              </select>
              <button class="btn btn-sm btn-outline-secondary">Apply</button>
              
              <select class="form-select form-select-sm ms-md-2" style="width: auto;">
                <option>Change role to...</option>
                <option>Administrator</option>
                <option>Editor</option>
                <option>Author</option>
                <option>Contributor</option>
                <option>Subscriber</option>
              </select>
              <button class="btn btn-sm btn-outline-secondary">Change</button>
            </div>
            
            <div class="d-flex align-items-center gap-2">
              <input type="text" class="form-control form-control-sm" placeholder="Search users">
              <button class="btn btn-sm btn-primary">Search</button>
            </div>
            
          </div>
        </div>

        <!-- Users Table -->
        <div class="card border-0 shadow-sm mb-4">
          <div class="table-responsive">
            <table class="table align-middle table-hover mb-0">
              <thead class="table-light">
                <tr>
                  <th scope="col" style="width: 40px;" class="ps-4">
                    <input class="form-check-input" type="checkbox" id="selectAll">
                  </th>
                  <th scope="col">Username</th>
                  <th scope="col">Name</th>
                  <th scope="col">Email</th>
                  <th scope="col">Role</th>
                  <th scope="col" class="text-center pe-4">Posts</th>
                </tr>
              </thead>
              <tbody>
                
                <!-- Admin User Row -->
                <tr>
                  <td class="ps-4">
                    <input class="form-check-input" type="checkbox">
                  </td>
                  <td>
                    <div class="d-flex align-items-center gap-3">
                      <img src="assets/images/avatar/avatar1.webp" class="rounded-circle" width="32" height="32" alt="Avatar">
                      <div>
                        <a href="users-profile.html" class="fw-bold text-dark text-decoration-none">admin</a>
                        <div class="small mt-1 text-muted">
                          <a href="users-profile.html" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                          <a href="#" class="text-decoration-none text-secondary hover-dark">View</a>
                        </div>
                      </div>
                    </div>
                  </td>
                  <td>Admin User</td>
                  <td><a href="mailto:admin@example.com" class="text-decoration-none">admin@example.com</a></td>
                  <td>Administrator</td>
                  <td class="text-center pe-4"><a href="#" class="fw-bold text-decoration-none">12</a></td>
                </tr>

                <!-- Editor User Row -->
                <tr>
                  <td class="ps-4">
                    <input class="form-check-input" type="checkbox">
                  </td>
                  <td>
                    <div class="d-flex align-items-center gap-3">
                      <div class="avatar avatar-sm rounded-circle bg-primary text-white d-flex align-items-center justify-content-center">JS</div>
                      <div>
                        <a href="#" class="fw-bold text-dark text-decoration-none">jsmith</a>
                        <div class="small mt-1 text-muted">
                          <a href="#" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                          <a href="#" class="text-decoration-none text-danger hover-danger">Delete</a> <span class="text-light">|</span> 
                          <a href="#" class="text-decoration-none text-secondary hover-dark">View</a>
                        </div>
                      </div>
                    </div>
                  </td>
                  <td>John Smith</td>
                  <td><a href="mailto:john@example.com" class="text-decoration-none">john@example.com</a></td>
                  <td>Editor</td>
                  <td class="text-center pe-4"><a href="#" class="fw-bold text-decoration-none">4</a></td>
                </tr>

                <!-- Subscriber User Row -->
                <tr>
                  <td class="ps-4">
                    <input class="form-check-input" type="checkbox">
                  </td>
                  <td>
                    <div class="d-flex align-items-center gap-3">
                      <div class="avatar avatar-sm rounded-circle bg-success text-white d-flex align-items-center justify-content-center">ED</div>
                      <div>
                        <a href="#" class="fw-bold text-dark text-decoration-none">emily_d</a>
                        <div class="small mt-1 text-muted">
                          <a href="#" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                          <a href="#" class="text-decoration-none text-danger hover-danger">Delete</a> <span class="text-light">|</span> 
                          <a href="#" class="text-decoration-none text-secondary hover-dark">View</a>
                        </div>
                      </div>
                    </div>
                  </td>
                  <td>Emily Davis</td>
                  <td><a href="mailto:emily.davis@example.com" class="text-decoration-none">emily.davis@example.com</a></td>
                  <td>Subscriber</td>
                  <td class="text-center pe-4">0</td>
                </tr>

                <!-- Subscriber User Row -->
                <tr>
                  <td class="ps-4">
                    <input class="form-check-input" type="checkbox">
                  </td>
                  <td>
                    <div class="d-flex align-items-center gap-3">
                      <div class="avatar avatar-sm rounded-circle bg-info text-white d-flex align-items-center justify-content-center">MR</div>
                      <div>
                        <a href="#" class="fw-bold text-dark text-decoration-none">markr</a>
                        <div class="small mt-1 text-muted">
                          <a href="#" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                          <a href="#" class="text-decoration-none text-danger hover-danger">Delete</a> <span class="text-light">|</span> 
                          <a href="#" class="text-decoration-none text-secondary hover-dark">View</a>
                        </div>
                      </div>
                    </div>
                  </td>
                  <td>Mark Robinson</td>
                  <td><a href="mailto:mark.r@example.com" class="text-decoration-none">mark.r@example.com</a></td>
                  <td>Subscriber</td>
                  <td class="text-center pe-4">0</td>
                </tr>

              </tbody>
            </table>
          </div>
          
          <!-- Pagination -->
          <div class="card-footer bg-transparent py-3 d-flex align-items-center justify-content-between border-top">
            <span class="text-muted small">4 items</span>
          </div>
        </div>

      </div>
    </main>
    <!-- end::Main Content Area -->'''

pattern = r'<!-- begin::Main Content Area -->.*?<!-- end::Main Content Area -->'
new_html = re.sub(pattern, main_content, html, flags=re.DOTALL)

# Also ensure active link is users-list
new_html = new_html.replace('class="menu-link active" href="plugins-list.html"', 'class="menu-link" href="plugins-list.html"')
new_html = new_html.replace('class="menu-link" href="users-list.html"', 'class="menu-link active" href="users-list.html"')

with open('c:/laragon/www/LaravelCMShtml/users-list.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created users-list.html")
