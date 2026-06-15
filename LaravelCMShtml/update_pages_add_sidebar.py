import re

with open('c:/laragon/www/LaravelCMShtml/pages-add.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the exact start of the sidebar and end of the row
sidebar_start = content.find('<!-- Sidebar Meta Boxes (Right Column) -->')
# Find the closing tag of the .row g-4. 
# It is located just before:
#       </div>
#     </main>
#     <!-- end::Main Content Area -->

end_marker = '      </div>\n    </main>'
end_idx = content.find(end_marker)

if sidebar_start != -1 and end_idx != -1:
    # the closing div for the row is right before end_marker.
    # Let's just find the last </div> before end_marker.
    
    new_sidebar = '''<!-- Sidebar Meta Boxes (Right Column) -->
          <div class="col-lg-4">
            
            <div class="card border-0 shadow-sm rounded-0 h-100 bg-body border-start">
              
              <!-- Tabs -->
              <div class="d-flex border-bottom bg-body px-2 pt-2">
                <button class="btn btn-link text-decoration-none text-body fw-medium py-2 border-bottom border-2 border-dark rounded-0 px-3 fs-6">Page</button>
                <button class="btn btn-link text-decoration-none text-muted py-2 px-3 fs-6 hover-dark">Block</button>
                <button class="btn btn-link text-muted ms-auto px-2 hover-dark"><i class="fi fi-rr-cross-small"></i></button>
              </div>

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

          </div>
        </div>
'''
    # Wait, the closing </div> for the row is needed.
    # The current string has sidebar_start at '<!-- Sidebar Meta Boxes (Right Column) -->'
    # I should replace from sidebar_start up to the last </div> before end_marker.
    # Actually, I can just replace everything from sidebar_start to the end_marker with my new sidebar + '</div>\n\n' + end_marker.
    
    content = content[:sidebar_start] + new_sidebar + '\n' + end_marker + content[end_idx + len(end_marker):]
    
    with open('c:/laragon/www/LaravelCMShtml/pages-add.html', 'w', encoding='utf-8') as f:
        f.write(content)

print("Sidebar updated.")
