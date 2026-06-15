import re

with open('c:/laragon/www/LaravelCMShtml/settings-general.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Writing Settings</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item"><a href="settings-general.html">Settings</a></li>
                <li class="breadcrumb-item active" aria-current="page">Writing</li>
              </ol>
            </nav>
          </div>
        </div>

        <div class="row">
          <div class="col-lg-10 col-xl-8">
            <form>
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-body p-4">
                  
                  <div class="row mb-4 align-items-center">
                    <label for="defaultCategory" class="col-sm-4 col-form-label fw-medium text-dark">Default Post Category</label>
                    <div class="col-sm-6">
                      <select class="form-select" id="defaultCategory">
                        <option value="1" selected>Uncategorized</option>
                        <option value="2">News</option>
                        <option value="3">Updates</option>
                      </select>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-center">
                    <label for="defaultPostFormat" class="col-sm-4 col-form-label fw-medium text-dark">Default Post Format</label>
                    <div class="col-sm-6">
                      <select class="form-select" id="defaultPostFormat">
                        <option value="standard" selected>Standard</option>
                        <option value="aside">Aside</option>
                        <option value="chat">Chat</option>
                        <option value="gallery">Gallery</option>
                        <option value="link">Link</option>
                        <option value="image">Image</option>
                        <option value="quote">Quote</option>
                        <option value="status">Status</option>
                        <option value="video">Video</option>
                        <option value="audio">Audio</option>
                      </select>
                    </div>
                  </div>

                  <hr class="my-4">

                  <h5 class="fw-bold mb-4">Post via email</h5>
                  <p class="text-muted small mb-4">To post to WordPress by email you must set up a secret email account with POP3 access. Any mail received at this address will be posted, so it's a good idea to keep this address very secret.</p>

                  <div class="row mb-3 align-items-center">
                    <label for="mailServer" class="col-sm-4 col-form-label fw-medium text-dark">Mail Server</label>
                    <div class="col-sm-6">
                      <input type="text" class="form-control" id="mailServer" value="mail.example.com">
                    </div>
                    <div class="col-sm-2 text-sm-end mt-2 mt-sm-0">
                      <label class="col-form-label fw-medium text-dark me-2">Port</label>
                      <input type="text" class="form-control d-inline-block text-center" style="width: 70px;" value="110">
                    </div>
                  </div>

                  <div class="row mb-3 align-items-center">
                    <label for="loginName" class="col-sm-4 col-form-label fw-medium text-dark">Login Name</label>
                    <div class="col-sm-6">
                      <input type="text" class="form-control" id="loginName" value="login@example.com">
                    </div>
                  </div>

                  <div class="row mb-3 align-items-center">
                    <label for="mailPassword" class="col-sm-4 col-form-label fw-medium text-dark">Password</label>
                    <div class="col-sm-6">
                      <input type="password" class="form-control" id="mailPassword" value="password123">
                    </div>
                  </div>

                  <div class="row mb-4 align-items-center">
                    <label for="mailCategory" class="col-sm-4 col-form-label fw-medium text-dark">Default Mail Category</label>
                    <div class="col-sm-6">
                      <select class="form-select" id="mailCategory">
                        <option value="1" selected>Uncategorized</option>
                        <option value="2">News</option>
                        <option value="3">Updates</option>
                      </select>
                    </div>
                  </div>

                  <hr class="my-4">

                  <h5 class="fw-bold mb-4">Update Services</h5>
                  <p class="text-muted small mb-2">When you publish a new post, WordPress automatically notifies the following site update services.</p>
                  
                  <div class="row mb-4">
                    <div class="col-12">
                      <textarea class="form-control" rows="4">http://rpc.pingomatic.com/</textarea>
                      <div class="form-text mt-2">Separate multiple service URLs with line breaks.</div>
                    </div>
                  </div>

                </div>
              </div>
              
              <div class="mb-5 pb-5">
                <button type="submit" class="btn btn-primary px-4 py-2 fw-bold shadow-sm waves-effect">Save Changes</button>
              </div>

            </form>
          </div>
        </div>

      </div>
    </main>
    <!-- end::Main Content Area -->'''

pattern = r'<!-- begin::Main Content Area -->.*?<!-- end::Main Content Area -->'
new_html = re.sub(pattern, main_content, html, flags=re.DOTALL)

with open('c:/laragon/www/LaravelCMShtml/settings-writing.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created settings-writing.html")
