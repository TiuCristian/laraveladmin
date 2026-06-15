import os
import re

filepath = r'c:\laragon\www\LaravelAdmin\resources\views\admin\tags\index.blade.php'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Add form
form_start = '''<form action="{{ route('tags.store') }}" method="POST">
                  @csrf'''
content = content.replace('<form>', form_start)
content = content.replace('id="tagName"', 'id="tagName" name="name" required')
content = content.replace('id="tagSlug"', 'id="tagSlug" name="slug"')
content = content.replace('id="tagDesc"', 'id="tagDesc" name="description"')

content = content.replace('<button type="button" class="btn btn-primary px-4 waves-effect">Add New Tag</button>', '<button type="submit" class="btn btn-primary px-4 waves-effect">Add New Tag</button>')

# Replace Bulk actions select
bulk_form = '''<form action="{{ route('tags.bulk') }}" method="POST" id="bulkForm">
              @csrf
              <input type="hidden" name="action" id="bulkActionInput">
              <div class="d-flex align-items-center gap-2">
                <select class="form-select form-select-sm" style="width: auto;" id="bulkActionSelect">
                  <option value="">Bulk actions</option>
                  <option value="delete">Delete</option>
                </select>
                <button type="button" class="btn btn-sm btn-outline-secondary" onclick="applyBulkAction()">Apply</button>
              </div>
            </form>
              <form action="{{ route('tags.index') }}" method="GET" class="d-flex align-items-center gap-2">
                <input type="text" name="search" class="form-control form-control-sm" placeholder="Search tags" value="{{ request('search') }}">
                <button type="submit" class="btn btn-sm btn-primary">Search</button>
              </form>'''

# Replace bulk action section and search
content = re.sub(r'<div class="d-flex flex-wrap align-items-center justify-content-between mb-3 gap-2">.*?</div>\s*</div>', '<div class="d-flex flex-wrap align-items-center justify-content-between mb-3 gap-2">' + bulk_form + '</div>', content, flags=re.DOTALL)

# Table body loop
table_body = '''<tbody>
                  @foreach($tags as $tag)
                    <tr>
                      <td class="ps-4">
                        <input class="form-check-input" type="checkbox" name="tag_ids[]" value="{{ $tag->id }}" form="bulkForm">
                      </td>
                      <td>
                        <a href="#" class="fw-bold text-dark text-decoration-none">{{ $tag->name }}</a>
                        <div class="small mt-1 text-muted">
                          <a href="{{ route('tags.edit', $tag) }}" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                          <a href="#" class="text-decoration-none text-secondary hover-dark quick-edit-btn">Quick Edit</a> <span class="text-light">|</span> 
                          <form action="{{ route('tags.destroy', $tag) }}" method="POST" class="d-inline">
                            @csrf
                            @method('DELETE')
                            <button type="submit" class="btn btn-link p-0 m-0 align-baseline text-decoration-none text-danger hover-danger" style="font-size: 0.8rem;" onclick="return confirm('Are you sure?')">Delete</button>
                          </form>
                        </div>
                      </td>
                      <td class="text-muted small">{{ $tag->description }}</td>
                      <td>{{ $tag->slug }}</td>
                      <td class="text-center pe-4">
                        <a href="{{ route('posts.index', ['tag' => $tag->id]) }}" class="text-decoration-none text-primary fw-medium">{{ $tag->posts()->count() }}</a>
                      </td>
                    </tr>

                    <!-- Quick Edit Form -->
                    <tr class="quick-edit-row d-none bg-body-tertiary border-bottom">
                      <td colspan="5" class="p-4">
                        <form action="{{ route('tags.update', $tag) }}" method="POST">
                          @csrf
                          @method('PUT')
                          <fieldset class="border p-3 rounded bg-body">
                            <legend class="float-none w-auto px-2 fs-6 fw-bold mb-0">Quick Edit</legend>
                            <div class="row g-3">
                              <div class="col-md-6">
                                <label class="form-label small fw-medium text-body mb-1">Name</label>
                                <input type="text" name="name" class="form-control form-control-sm" value="{{ $tag->name }}" required>
                              </div>
                              <div class="col-md-6">
                                <label class="form-label small fw-medium text-body mb-1">Slug</label>
                                <input type="text" name="slug" class="form-control form-control-sm" value="{{ $tag->slug }}">
                              </div>
                              <div class="col-12 mt-3 d-flex gap-2">
                                <button type="button" class="btn btn-sm btn-outline-secondary cancel-quick-edit">Cancel</button>
                                <button type="submit" class="btn btn-sm btn-primary">Update</button>
                              </div>
                            </div>
                          </fieldset>
                        </form>
                      </td>
                    </tr>
                  @endforeach
                  </tbody>'''

# Replace everything from <tbody> to </tbody>
content = re.sub(r'<tbody>.*?</tbody>', table_body, content, flags=re.DOTALL)

# Select all
content = content.replace('id="selectAll"', 'id="selectAll" onclick="document.querySelectorAll(\'input[name=\\\'tag_ids[]\\\']\').forEach(cb => cb.checked = this.checked)"')

# Pagination
pagination = '''              <div class="card-footer bg-transparent py-3 d-flex align-items-center justify-content-between border-top">
                <span class="text-muted small">{{ $tags->total() }} items</span>
                <nav aria-label="Page navigation">
                  {{ $tags->links('pagination::bootstrap-5') }}
                </nav>
              </div>'''
content = re.sub(r'<div class="card-footer bg-transparent py-3 d-flex align-items-center justify-content-between border-top">.*?</div>', pagination, content, flags=re.DOTALL)

# Add bulk action script
script = '''<script>
    function applyBulkAction() {
        const action = document.getElementById('bulkActionSelect').value;
        if (!action) return;
        
        const selected = document.querySelectorAll('input[name="tag_ids[]"]:checked');
        if (selected.length === 0) {
            alert('Please select at least one item.');
            return;
        }
        
        if (confirm('Are you sure you want to delete the selected tags?')) {
            document.getElementById('bulkActionInput').value = action;
            document.getElementById('bulkForm').submit();
        }
    }
  </script>
</body>'''
content = content.replace('</body>', script)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
