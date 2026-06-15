import re

with open('c:/laragon/www/LaravelCMShtml/users-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Profile</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item"><a href="users-list.html">Users</a></li>
                <li class="breadcrumb-item active" aria-current="page">Profile</li>
              </ol>
            </nav>
          </div>
        </div>

        <div class="row">
          <div class="col-lg-10 col-xl-8">
            <form>
              
              <!-- Personal Options -->
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-header bg-transparent border-bottom">
                  <h5 class="mb-0">Personal Options</h5>
                </div>
                <div class="card-body p-4">
                  
                  <div class="row mb-3 align-items-start">
                    <label class="col-sm-3 col-form-label fw-medium text-dark">Visual Editor</label>
                    <div class="col-sm-9 pt-2">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="disableVisualEditor">
                        <label class="form-check-label" for="disableVisualEditor">Disable the visual editor when writing</label>
                      </div>
                    </div>
                  </div>

                  <div class="row mb-3 align-items-start">
                    <label class="col-sm-3 col-form-label fw-medium text-dark">Syntax Highlighting</label>
                    <div class="col-sm-9 pt-2">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="disableSyntaxHighlighting">
                        <label class="form-check-label" for="disableSyntaxHighlighting">Disable syntax highlighting when editing code</label>
                      </div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-3 col-form-label fw-medium text-dark">Admin Color Scheme</label>
                    <div class="col-sm-9 pt-2">
                      <div class="d-flex flex-wrap gap-4">
                        
                        <div class="form-check">
                          <input class="form-check-input" type="radio" name="colorScheme" id="colorDefault" checked>
                          <label class="form-check-label" for="colorDefault">
                            <div class="d-flex gap-1 ms-2">
                              <div style="width: 20px; height: 20px; background-color: #1e2225; border-radius: 50%;"></div>
                              <div style="width: 20px; height: 20px; background-color: #4b49ac; border-radius: 50%;"></div>
                              <div style="width: 20px; height: 20px; background-color: #5955D1; border-radius: 50%;"></div>
                            </div>
                            <div class="mt-1">Default</div>
                          </label>
                        </div>

                        <div class="form-check">
                          <input class="form-check-input" type="radio" name="colorScheme" id="colorLight">
                          <label class="form-check-label" for="colorLight">
                            <div class="d-flex gap-1 ms-2">
                              <div style="width: 20px; height: 20px; background-color: #e5e5e5; border-radius: 50%;"></div>
                              <div style="width: 20px; height: 20px; background-color: #888888; border-radius: 50%;"></div>
                              <div style="width: 20px; height: 20px; background-color: #007cba; border-radius: 50%;"></div>
                            </div>
                            <div class="mt-1">Light</div>
                          </label>
                        </div>

                        <div class="form-check">
                          <input class="form-check-input" type="radio" name="colorScheme" id="colorMidnight">
                          <label class="form-check-label" for="colorMidnight">
                            <div class="d-flex gap-1 ms-2">
                              <div style="width: 20px; height: 20px; background-color: #25282b; border-radius: 50%;"></div>
                              <div style="width: 20px; height: 20px; background-color: #363b3f; border-radius: 50%;"></div>
                              <div style="width: 20px; height: 20px; background-color: #e14d43; border-radius: 50%;"></div>
                            </div>
                            <div class="mt-1">Midnight</div>
                          </label>
                        </div>

                      </div>
                    </div>
                  </div>

                  <div class="row mb-3 align-items-start">
                    <label class="col-sm-3 col-form-label fw-medium text-dark">Keyboard Shortcuts</label>
                    <div class="col-sm-9 pt-2">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="keyboardShortcuts">
                        <label class="form-check-label" for="keyboardShortcuts">Enable keyboard shortcuts for comment moderation.</label>
                      </div>
                    </div>
                  </div>

                  <div class="row align-items-start">
                    <label class="col-sm-3 col-form-label fw-medium text-dark">Toolbar</label>
                    <div class="col-sm-9 pt-2">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="showToolbar" checked>
                        <label class="form-check-label" for="showToolbar">Show Toolbar when viewing site</label>
                      </div>
                    </div>
                  </div>

                </div>
              </div>

              <!-- Name -->
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-header bg-transparent border-bottom">
                  <h5 class="mb-0">Name</h5>
                </div>
                <div class="card-body p-4">
                  
                  <div class="row mb-3 align-items-center">
                    <label for="username" class="col-sm-3 col-form-label fw-medium text-dark">Username</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" id="username" value="admin" disabled>
                      <div class="form-text">Usernames cannot be changed.</div>
                    </div>
                  </div>

                  <div class="row mb-3 align-items-center">
                    <label for="firstName" class="col-sm-3 col-form-label fw-medium text-dark">First Name</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" id="firstName" value="Admin">
                    </div>
                  </div>

                  <div class="row mb-3 align-items-center">
                    <label for="lastName" class="col-sm-3 col-form-label fw-medium text-dark">Last Name</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" id="lastName" value="User">
                    </div>
                  </div>

                  <div class="row mb-3 align-items-center">
                    <label for="nickname" class="col-sm-3 col-form-label fw-medium text-dark">Nickname (required)</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" id="nickname" value="admin" required>
                    </div>
                  </div>

                  <div class="row align-items-center">
                    <label for="displayName" class="col-sm-3 col-form-label fw-medium text-dark">Display name publicly as</label>
                    <div class="col-sm-9">
                      <select class="form-select" id="displayName">
                        <option value="admin">admin</option>
                        <option value="Admin">Admin</option>
                        <option value="User">User</option>
                        <option value="Admin User" selected>Admin User</option>
                        <option value="User Admin">User Admin</option>
                      </select>
                    </div>
                  </div>

                </div>
              </div>

              <!-- Contact Info & About -->
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-header bg-transparent border-bottom">
                  <h5 class="mb-0">Contact Info & About Yourself</h5>
                </div>
                <div class="card-body p-4">
                  
                  <div class="row mb-3 align-items-center">
                    <label for="email" class="col-sm-3 col-form-label fw-medium text-dark">Email (required)</label>
                    <div class="col-sm-9">
                      <input type="email" class="form-control" id="email" value="admin@example.com" required>
                      <div class="form-text">If you change this we will send you an email at your new address to confirm it. <strong>The new address will not become active until confirmed.</strong></div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-center">
                    <label for="website" class="col-sm-3 col-form-label fw-medium text-dark">Website</label>
                    <div class="col-sm-9">
                      <input type="url" class="form-control" id="website" value="https://example.com">
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label for="bio" class="col-sm-3 col-form-label fw-medium text-dark">Biographical Info</label>
                    <div class="col-sm-9">
                      <textarea class="form-control" id="bio" rows="4">I am the main administrator for this website.</textarea>
                      <div class="form-text">Share a little biographical information to fill out your profile. This may be shown publicly.</div>
                    </div>
                  </div>

                  <div class="row align-items-start">
                    <label class="col-sm-3 col-form-label fw-medium text-dark">Profile Picture</label>
                    <div class="col-sm-9">
                      <div class="d-flex align-items-center gap-3">
                        <img src="assets/images/avatar/avatar1.webp" class="rounded border" width="64" height="64" alt="Avatar">
                        <a href="https://en.gravatar.com/" target="_blank" class="text-decoration-none small text-primary">You can change your profile picture on Gravatar.</a>
                      </div>
                    </div>
                  </div>

                </div>
              </div>

              <!-- Account Management -->
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-header bg-transparent border-bottom">
                  <h5 class="mb-0">Account Management</h5>
                </div>
                <div class="card-body p-4">
                  
                  <div class="row mb-4 align-items-center">
                    <label class="col-sm-3 col-form-label fw-medium text-dark">New Password</label>
                    <div class="col-sm-9">
                      <button type="button" class="btn btn-outline-secondary btn-sm">Set New Password</button>
                    </div>
                  </div>

                  <div class="row align-items-center">
                    <label class="col-sm-3 col-form-label fw-medium text-dark">Sessions</label>
                    <div class="col-sm-9">
                      <button type="button" class="btn btn-outline-danger btn-sm">Log Out Everywhere Else</button>
                      <div class="form-text mt-2">Did you lose your phone or leave your account logged in at a public computer? You can log out everywhere else, and stay logged in here.</div>
                    </div>
                  </div>

                </div>
              </div>

              <!-- Submit Button -->
              <div class="mb-5 pb-5">
                <button type="submit" class="btn btn-primary px-4 py-2 fw-bold shadow-sm waves-effect">Update Profile</button>
              </div>

            </form>
          </div>
        </div>

      </div>
    </main>
    <!-- end::Main Content Area -->'''

pattern = r'<!-- begin::Main Content Area -->.*?<!-- end::Main Content Area -->'
new_html = re.sub(pattern, main_content, html, flags=re.DOTALL)

with open('c:/laragon/www/LaravelCMShtml/users-profile.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created users-profile.html")
