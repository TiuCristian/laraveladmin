import re

with open('c:/laragon/www/LaravelCMShtml/settings-general.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_content = '''    <!-- begin::Main Content Area -->
    <main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Discussion Settings</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item"><a href="settings-general.html">Settings</a></li>
                <li class="breadcrumb-item active" aria-current="page">Discussion</li>
              </ol>
            </nav>
          </div>
        </div>

        <div class="row">
          <div class="col-lg-10 col-xl-8">
            <form>
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-body p-4">
                  
                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Default post settings</label>
                    <div class="col-sm-8 pt-2">
                      <div class="form-check mb-2">
                        <input class="form-check-input" type="checkbox" id="attemptPing" checked>
                        <label class="form-check-label text-dark" for="attemptPing">Attempt to notify any blogs linked to from the post</label>
                      </div>
                      <div class="form-check mb-2">
                        <input class="form-check-input" type="checkbox" id="allowPing" checked>
                        <label class="form-check-label text-dark" for="allowPing">Allow link notifications from other blogs (pingbacks and trackbacks) on new posts</label>
                      </div>
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="allowComments" checked>
                        <label class="form-check-label text-dark" for="allowComments">Allow people to submit comments on new posts</label>
                      </div>
                      <div class="form-text mt-2">(These settings may be overridden for individual posts.)</div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Other comment settings</label>
                    <div class="col-sm-8 pt-2">
                      <div class="form-check mb-2">
                        <input class="form-check-input" type="checkbox" id="requireNameEmail" checked>
                        <label class="form-check-label text-dark" for="requireNameEmail">Comment author must fill out name and email</label>
                      </div>
                      <div class="form-check mb-2">
                        <input class="form-check-input" type="checkbox" id="requireLogin">
                        <label class="form-check-label text-dark" for="requireLogin">Users must be registered and logged in to comment</label>
                      </div>
                      <div class="form-check mb-2 d-flex align-items-center gap-2">
                        <input class="form-check-input" type="checkbox" id="closeComments" checked>
                        <label class="form-check-label text-dark" for="closeComments">Automatically close comments on posts older than</label>
                        <input type="number" class="form-control form-control-sm" style="width: 60px;" value="14">
                        <span class="text-dark small">days</span>
                      </div>
                      <div class="form-check mb-2 d-flex align-items-center gap-2">
                        <input class="form-check-input" type="checkbox" id="threadComments" checked>
                        <label class="form-check-label text-dark" for="threadComments">Enable threaded (nested) comments</label>
                        <input type="number" class="form-control form-control-sm" style="width: 60px;" value="5">
                        <span class="text-dark small">levels deep</span>
                      </div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Email me whenever</label>
                    <div class="col-sm-8 pt-2">
                      <div class="form-check mb-2">
                        <input class="form-check-input" type="checkbox" id="emailAnyonePosts" checked>
                        <label class="form-check-label text-dark" for="emailAnyonePosts">Anyone posts a comment</label>
                      </div>
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="emailModeration" checked>
                        <label class="form-check-label text-dark" for="emailModeration">A comment is held for moderation</label>
                      </div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Before a comment appears</label>
                    <div class="col-sm-8 pt-2">
                      <div class="form-check mb-2">
                        <input class="form-check-input" type="checkbox" id="approveManually">
                        <label class="form-check-label text-dark" for="approveManually">Comment must be manually approved</label>
                      </div>
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="previouslyApproved" checked>
                        <label class="form-check-label text-dark" for="previouslyApproved">Comment author must have a previously approved comment</label>
                      </div>
                    </div>
                  </div>

                  <hr class="my-4">

                  <h5 class="fw-bold mb-4">Avatars</h5>
                  <p class="text-muted small mb-4">An avatar is an image that follows you from weblog to weblog appearing beside your name when you comment on avatar enabled sites. Here you can enable the display of avatars for people who comment on your site.</p>

                  <div class="row mb-4 align-items-center">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Avatar Display</label>
                    <div class="col-sm-8 pt-2">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="showAvatars" checked>
                        <label class="form-check-label text-dark" for="showAvatars">Show Avatars</label>
                      </div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Maximum Rating</label>
                    <div class="col-sm-8 pt-2">
                      <div class="form-check mb-2">
                        <input class="form-check-input" type="radio" name="maxRating" id="ratingG" checked>
                        <label class="form-check-label text-dark" for="ratingG">G &mdash; Suitable for all audiences</label>
                      </div>
                      <div class="form-check mb-2">
                        <input class="form-check-input" type="radio" name="maxRating" id="ratingPG">
                        <label class="form-check-label text-dark" for="ratingPG">PG &mdash; Possibly offensive, usually for audiences 13 and above</label>
                      </div>
                      <div class="form-check mb-2">
                        <input class="form-check-input" type="radio" name="maxRating" id="ratingR">
                        <label class="form-check-label text-dark" for="ratingR">R &mdash; Intended for adult audiences above 17</label>
                      </div>
                      <div class="form-check">
                        <input class="form-check-input" type="radio" name="maxRating" id="ratingX">
                        <label class="form-check-label text-dark" for="ratingX">X &mdash; Even more mature than above</label>
                      </div>
                    </div>
                  </div>

                  <div class="row mb-4 align-items-start">
                    <label class="col-sm-4 col-form-label fw-medium text-dark">Default Avatar</label>
                    <div class="col-sm-8 pt-2">
                      <p class="text-muted small mb-2">For users without a custom avatar of their own, you can either display a generic logo or a generated one based on their email address.</p>
                      
                      <div class="form-check mb-2 d-flex align-items-center gap-2">
                        <input class="form-check-input" type="radio" name="defaultAvatar" id="avatarMystery" checked>
                        <div class="avatar avatar-sm rounded bg-light border"><i class="fi fi-rr-user text-secondary"></i></div>
                        <label class="form-check-label text-dark" for="avatarMystery">Mystery Person</label>
                      </div>
                      
                      <div class="form-check mb-2 d-flex align-items-center gap-2">
                        <input class="form-check-input" type="radio" name="defaultAvatar" id="avatarBlank">
                        <div class="avatar avatar-sm rounded bg-light border"></div>
                        <label class="form-check-label text-dark" for="avatarBlank">Blank</label>
                      </div>

                      <div class="form-check d-flex align-items-center gap-2">
                        <input class="form-check-input" type="radio" name="defaultAvatar" id="avatarGravatar">
                        <div class="avatar avatar-sm rounded bg-primary text-white d-flex align-items-center justify-content-center">G</div>
                        <label class="form-check-label text-dark" for="avatarGravatar">Gravatar Logo</label>
                      </div>
                      
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

with open('c:/laragon/www/LaravelCMShtml/settings-discussion.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created settings-discussion.html")
