import re

with open('resources/views/admin/forms/index.blade.php', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace $pages->total() to $forms->total()
content = content.replace('$pages->total()', '$forms->total()')
content = content.replace("{{ $pages->appends(request()->query())->links('pagination::bootstrap-5') }}", "{{ $forms->appends(request()->query())->links('pagination::bootstrap-5') }}")

table_content = '''
        <div class="card border-0 shadow-sm mb-4">
          <div class="table-responsive">
            <table class="table table-hover align-middle mb-0" style="font-size: 0.9rem;">
              <thead class="table-light">
                <tr>
                  <th scope="col" style="width: 40px;" class="ps-3 border-bottom-0">
                    <input class="form-check-input" type="checkbox" id="selectAll" onclick="document.querySelectorAll('input[name=\\'form_ids[]\\']').forEach(cb => cb.checked = this.checked)">
                  </th>
                  <th scope="col" class="border-bottom-0 text-primary fw-medium">Form Name</th>
                  <th scope="col" class="border-bottom-0 text-body fw-medium">Shortcode</th>
                  <th scope="col" class="border-bottom-0 text-primary fw-medium">Date Created</th>
                </tr>
              </thead>
              <tbody>
                @foreach($forms as $form)
                <tr id="row{{ $form->id }}">
                  <td class="ps-3 align-top pt-3">
                    <input class="form-check-input" type="checkbox" name="form_ids[]" value="{{ $form->id }}" form="bulkForm">
                  </td>
                  <td class="align-top pt-3" style="width: 35%;">
                    <a href="{{ route('forms.edit', $form) }}" class="fw-bold text-body text-decoration-none">{{ $form->name }}</a>
                    <div class="small mt-1 text-muted" style="font-size: 0.8rem;">
                        <a href="{{ route('forms.edit', $form) }}" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                        <form action="{{ route('forms.destroy', $form) }}" method="POST" class="d-inline">
                          @csrf
                          @method('DELETE')
                          <button type="submit" class="btn btn-link p-0 m-0 align-baseline text-decoration-none text-danger hover-danger" style="font-size: 0.8rem;" onclick="return confirm('Are you sure?')">Delete</button>
                        </form>
                    </div>
                  </td>
                  <td class="align-top pt-3">
                    <code class="bg-light border px-2 py-1 rounded text-dark">[form id="{{ $form->id }}"]</code>
                  </td>
                  <td class="align-top pt-3" style="width: 25%;">
                    <span class="text-muted small">{{ $form->created_at->format('Y/m/d g:i a') }}</span>
                  </td>
                </tr>
                @endforeach
                </tbody>
            </table>
          </div>
'''

content = re.sub(r'<div class="card border-0 shadow-sm mb-4">\s*<div class="table-responsive">.*?</div>\s*<!-- Pagination -->', table_content + '\n          <!-- Pagination -->', content, flags=re.DOTALL)

with open('resources/views/admin/forms/index.blade.php', 'w', encoding='utf-8') as f:
    f.write(content)
