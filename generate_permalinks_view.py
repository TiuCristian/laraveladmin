import sys

with open('resources/views/admin/settings/discussion.blade.php', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace active classes in sidebar
content = content.replace('<li class="current"><a href="{{ route(\'settings.discussion\') }}" class="current">Discussion</a></li>', '<li><a href="{{ route(\'settings.discussion\') }}">Discussion</a></li>')
content = content.replace('<li><a href="settings-permalinks.html">Permalinks</a></li>', '<li class="current"><a href="{{ route(\'settings.permalinks\') }}" class="current">Permalinks</a></li>')

main_start = content.find('<main class="app-wrapper">')
main_end = content.find('</main>') + len('</main>')

before_main = content[:main_start]
after_main = content[main_end:]

permalink_main = """<main class="app-wrapper">
      <div class="container-fluid">
        
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">Permalink Settings</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="{{ route('admin.dashboard') }}">Home</a></li>
                <li class="breadcrumb-item"><a href="{{ route('settings.general') }}">Settings</a></li>
                <li class="breadcrumb-item active" aria-current="page">Permalinks</li>
              </ol>
            </nav>
          </div>
        </div>

        @if(session('success'))
            <div class="alert alert-success alert-dismissible fade show mb-4" role="alert">
                {{ session('success') }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        @endif

        <div class="row">
          <div class="col-lg-10 col-xl-8">
            <form action="{{ route('settings.permalinks.update') }}" method="POST">
              @csrf
              <div class="card border-0 shadow-sm mb-4">
                <div class="card-body p-4">
                  
                  <p class="text-muted mb-4">WordPress offers you the ability to create a custom URL structure for your permalinks and archives. Custom URL structures can improve the aesthetics, usability, and forward-compatibility of your links.</p>

                  <h5 class="fw-bold mb-4">Common Settings</h5>

                  <div class="row mb-4 align-items-start">
                    <div class="col-12">
                      @php $p_struct = old('permalink_structure', $settings['permalink_structure'] ?? '/%postname%/'); @endphp
                      
                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalink_structure" id="plain" value="plain" {{ $p_struct == 'plain' ? 'checked' : '' }}>
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="plain">Plain</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">{{ url('/') }}/?p=123</code>
                      </div>

                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalink_structure" id="dayName" value="/%year%/%monthnum%/%day%/%postname%/" {{ $p_struct == '/%year%/%monthnum%/%day%/%postname%/' ? 'checked' : '' }}>
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="dayName">Day and name</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">{{ url('/') }}/{{ date('Y/m/d') }}/sample-post/</code>
                      </div>

                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalink_structure" id="monthName" value="/%year%/%monthnum%/%postname%/" {{ $p_struct == '/%year%/%monthnum%/%postname%/' ? 'checked' : '' }}>
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="monthName">Month and name</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">{{ url('/') }}/{{ date('Y/m') }}/sample-post/</code>
                      </div>

                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalink_structure" id="numeric" value="/archives/%post_id%" {{ $p_struct == '/archives/%post_id%' ? 'checked' : '' }}>
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="numeric">Numeric</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">{{ url('/') }}/archives/123</code>
                      </div>

                      <div class="form-check mb-3 d-flex align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalink_structure" id="postName" value="/%postname%/" {{ $p_struct == '/%postname%/' ? 'checked' : '' }}>
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="postName">Post name</label>
                        <code class="bg-light px-2 py-1 rounded text-muted">{{ url('/') }}/sample-post/</code>
                      </div>

                      <div class="form-check mb-3 d-flex flex-wrap align-items-center gap-3">
                        <input class="form-check-input mt-0" type="radio" name="permalink_structure" id="custom" value="custom" {{ !in_array($p_struct, ['plain', '/%year%/%monthnum%/%day%/%postname%/', '/%year%/%monthnum%/%postname%/', '/archives/%post_id%', '/%postname%/']) ? 'checked' : '' }}>
                        <label class="form-check-label fw-medium text-dark" style="min-width: 150px;" for="custom">Custom Structure</label>
                        <div class="d-flex align-items-center gap-1">
                          <code class="text-muted">{{ url('/') }}</code>
                          <input type="text" name="custom_permalink_structure" class="form-control form-control-sm font-monospace" style="width: 300px;" value="{{ old('custom_permalink_structure', (!in_array($p_struct, ['plain', '/%year%/%monthnum%/%day%/%postname%/', '/%year%/%monthnum%/%postname%/', '/archives/%post_id%', '/%postname%/']) ? $p_struct : '/%postname%/')) }}">
                        </div>
                      </div>

                      <div class="ps-4 mt-2">
                        <p class="small text-muted mb-2">Available tags:</p>
                        <div class="d-flex flex-wrap gap-2">
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%year%')">%year%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%monthnum%')">%monthnum%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%day%')">%day%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%hour%')">%hour%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%minute%')">%minute%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%second%')">%second%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%post_id%')">%post_id%</button>
                          <button type="button" class="btn btn-sm btn-primary" onclick="appendTag('%postname%')">%postname%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%category%')">%category%</button>
                          <button type="button" class="btn btn-sm btn-light border" onclick="appendTag('%author%')">%author%</button>
                        </div>
                      </div>

                    </div>
                  </div>

                  <hr class="my-4">

                  <h5 class="fw-bold mb-4">Optional</h5>
                  <p class="text-muted small mb-4">If you like, you may enter custom structures for your category and tag URLs here. For example, using <code>topics</code> as your category base would make your category links like <code>{{ url('/') }}/topics/uncategorized/</code>. If you leave these blank the defaults will be used.</p>

                  <div class="row mb-3 align-items-center">
                    <label for="category_base" class="col-sm-4 col-form-label fw-medium text-dark">Category base</label>
                    <div class="col-sm-8">
                      <input type="text" name="category_base" class="form-control" id="category_base" value="{{ old('category_base', $settings['category_base'] ?? '') }}">
                    </div>
                  </div>

                  <div class="row align-items-center">
                    <label for="tag_base" class="col-sm-4 col-form-label fw-medium text-dark">Tag base</label>
                    <div class="col-sm-8">
                      <input type="text" name="tag_base" class="form-control" id="tag_base" value="{{ old('tag_base', $settings['tag_base'] ?? '') }}">
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
    <script>
        function appendTag(tag) {
            document.getElementById('custom').checked = true;
            let input = document.querySelector('input[name="custom_permalink_structure"]');
            if (input.value && !input.value.endsWith('/')) {
                input.value += '/';
            }
            input.value += tag + '/';
        }
    </script>
    """

with open('resources/views/admin/settings/permalinks.blade.php', 'w', encoding='utf-8') as f:
    f.write(before_main + permalink_main + after_main)
print('Done!')
