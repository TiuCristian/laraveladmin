import re

with open('c:/laragon/www/LaravelCMShtml/users-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Add New User</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item"><a href="users-list.html">Users</a></li>
                <li class="breadcrumb-item active" aria-current="page">Add New</li>
              </ol>
            </nav>
          </div>
        </div>

        <div class="row">
          <div class="col-lg-8 col-xl-6">
            <div class="card border-0 shadow-sm mb-4">
              <div class="card-body p-4">
                
                <p class="text-muted mb-4">Create a brand new user and add them to this site.</p>

                <form>
                  <div class="row mb-3 align-items-center">
                    <label for="username" class="col-sm-4 col-form-label fw-medium text-dark">Username (required)</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" id="username" required>
                    </div>
                  </div>
                  
                  <div class="row mb-3 align-items-center">
                    <label for="email" class="col-sm-4 col-form-label fw-medium text-dark">Email (required)</label>
                    <div class="col-sm-8">
                      <input type="email" class="form-control" id="email" required>
                    </div>
                  </div>

                  <div class="row mb-3 align-items-center">
                    <label for="firstName" class="col-sm-4 col-form-label fw-medium text-dark">First Name</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" id="firstName">
                    </div>
                  </div>

                  <div class="row mb-3 align-items-center">
                    <label for="lastName" class="col-sm-4 col-form-label fw-medium text-dark">Last Name</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" id="lastName">
                    </div>
                  </div>

                  <div class="row mb-3 align-items-center">
                    <label for="website" class="col-sm-4 col-form-label fw-medium text-dark">Website</label>
                    <div class="col-sm-8">
                      <input type="url" class="form-control" id="website">
                    </div>
                  </div>

                  <div class="row mb-3 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Password</label>
                    <div class="col-sm-8">
                      <button type="button" class="btn btn-outline-secondary btn-sm mb-2">Generate password</button>
                      <div class="input-group">
                        <input type="text" class="form-control font-monospace" value="e@!%2&T*HqM9Lp" id="passwordInput">
                        <button class="btn btn-outline-secondary" type="button"><i class="fi fi-rr-eye"></i></button>
                      </div>
                      <div class="form-check mt-2">
                        <input class="form-check-input" type="checkbox" id="weakPassword">
                        <label class="form-check-label small" for="weakPassword">Confirm use of weak password</label>
                      </div>
                    </div>
                  </div>

                  <div class="row mb-3 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Send User Notification</label>
                    <div class="col-sm-8 pt-2">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="sendNotification" checked>
                        <label class="form-check-label" for="sendNotification">Send the new user an email about their account.</label>
                      </div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-center">
                    <label for="userRole" class="col-sm-4 col-form-label fw-medium text-dark">Role</label>
                    <div class="col-sm-8">
                      <select class="form-select" id="userRole">
                        <option value="subscriber" selected>Subscriber</option>
                        <option value="contributor">Contributor</option>
                        <option value="author">Author</option>
                        <option value="editor">Editor</option>
                        <option value="administrator">Administrator</option>
                      </select>
                    </div>
                  </div>

                  <div class="row">
                    <div class="col-sm-8 offset-sm-4">
                      <button type="submit" class="btn btn-primary px-4 waves-effect">Add New User</button>
                    </div>
                  </div>
                </form>

              </div>
            </div>
          </div>
        </div>

      </div>
    </main>
    <!-- end::Main Content Area -->'''

pattern = r'<!-- begin::Main Content Area -->.*?<!-- end::Main Content Area -->'
new_html = re.sub(pattern, main_content, html, flags=re.DOTALL)

with open('c:/laragon/www/LaravelCMShtml/users-add.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created users-add.html")
