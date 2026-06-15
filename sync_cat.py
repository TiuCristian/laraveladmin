import os
import re

filepath = r'c:\laragon\www\LaravelAdmin\resources\views\admin\categories\index.blade.php'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Add form
form_start = '''<form action="{{ route('categories.store') }}" method="POST">
                  @csrf'''
content = content.replace('<form>', form_start)
content = content.replace('id="catName"', 'id="catName" name="name" required')
content = content.replace('id="catSlug"', 'id="catSlug" name="slug"')
content = content.replace('id="catDesc"', 'id="catDesc" name="description"')

parent_select = '''<select class="form-select" id="catParent" name="parent_id">
                      <option value="">None</option>
                      @foreach(\App\Models\Category::all() as $cat)
                          <option value="{{ $cat->id }}">{{ $cat->name }}</option>
                      @endforeach
                    </select>'''
content = content.replace('''<select class="form-select" id="catParent">
                      <option selected>None</option>
                      <option>News</option>
                      <option>Updates</option>
                    </select>''', parent_select)

content = content.replace('<button type="button" class="btn btn-primary px-4 waves-effect">Add New Category</button>', '<button type="submit" class="btn btn-primary px-4 waves-effect">Add New Category</button>')

# Replace Bulk actions select
bulk_form = '''<form action="{{ route('categories.bulk') }}" method="POST" id="bulkForm">
              @csrf
              <input type="hidden" name="action" id="bulkActionInput">
              <div class="d-flex align-items-center gap-2">
                <select class="form-select form-select-sm" style="width: auto;" id="bulkActionSelect">
                  <option value="">Bulk actions</option>
                  <option value="delete">Delete</option>
                </select>
                <button type="button" class="btn btn-sm btn-outline-secondary" onclick="applyBulkAction()">Apply</button>
              </div>
            </form>'''

# Replace bulk action section
content = re.sub(r'<div class="d-flex align-items-center gap-2">\s*<select class="form-select form-select-sm" style="width: auto;">\s*<option>Bulk actions</option>\s*<option>Delete</option>\s*</select>\s*<button class="btn btn-sm btn-outline-secondary">Apply</button>\s*</div>', bulk_form, content)

# Table body loop
table_body = '''<tbody>
                  @foreach($categories as $category)
                    <tr>
                      <td class="ps-4">
                        <input class="form-check-input" type="checkbox" name="category_ids[]" value="{{ $category->id }}" form="bulkForm">
                      </td>
                      <td>
                        <a href="#" class="fw-bold text-dark text-decoration-none">{{ $category->name }}</a>
                        <div class="small mt-1 text-muted">
                          <a href="{{ route('categories.edit', $category) }}" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                          <a href="#" class="text-decoration-none text-secondary hover-dark quick-edit-btn">Quick Edit</a> <span class="text-light">|</span> 
                          <form action="{{ route('categories.destroy', $category) }}" method="POST" class="d-inline">
                            @csrf
                            @method('DELETE')
                            <button type="submit" class="btn btn-link p-0 m-0 align-baseline text-decoration-none text-danger hover-danger" style="font-size: 0.8rem;" onclick="return confirm('Are you sure?')">Delete</button>
                          </form>
                        </div>
                      </td>
                      <td class="text-muted small">{{ $category->description }}</td>
                      <td>{{ $category->slug }}</td>
                      <td class="text-center pe-4">
                        <a href="{{ route('posts.index', ['category' => $category->id]) }}" class="text-decoration-none text-primary fw-medium">{{ $category->posts()->count() }}</a>
                      </td>
                    </tr>

                    <!-- Quick Edit Form -->
                    <tr class="quick-edit-row d-none bg-body-tertiary border-bottom">
                      <td colspan="5" class="p-4">
                        <form action="{{ route('categories.update', $category) }}" method="POST">
                          @csrf
                          @method('PUT')
                          <fieldset class="border p-3 rounded bg-body">
                            <legend class="float-none w-auto px-2 fs-6 fw-bold mb-0">Quick Edit</legend>
                            <div class="row g-3">
                              <div class="col-md-6">
                                <label class="form-label small fw-medium text-body mb-1">Name</label>
                                <input type="text" name="name" class="form-control form-control-sm" value="{{ $category->name }}" required>
                              </div>
                              <div class="col-md-6">
                                <label class="form-label small fw-medium text-body mb-1">Slug</label>
                                <input type="text" name="slug" class="form-control form-control-sm" value="{{ $category->slug }}">
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
content = content.replace('id="selectAll"', 'id="selectAll" onclick="document.querySelectorAll(\'input[name=\\\'category_ids[]\\\']\').forEach(cb => cb.checked = this.checked)"')

# Add bulk action script
script = '''<script>
    function applyBulkAction() {
        const action = document.getElementById('bulkActionSelect').value;
        if (!action) return;
        
        const selected = document.querySelectorAll('input[name="category_ids[]"]:checked');
        if (selected.length === 0) {
            alert('Please select at least one item.');
            return;
        }
        
        if (confirm('Are you sure you want to delete the selected categories?')) {
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
