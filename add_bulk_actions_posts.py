import os
import re

file_path = r'c:\laragon\www\LaravelAdmin\resources\views\admin\posts\index.blade.php'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add the hidden bulk form right above the Posts Table Card
hidden_form = """        <!-- Bulk Form -->
        <form id="bulkForm" action="{{ route('posts.bulk') }}" method="POST" class="d-none">
            @csrf
            <input type="hidden" name="action" id="bulkActionInput">
        </form>

        <!-- Posts Table Card -->"""
content = content.replace('        <!-- Posts Table Card -->', hidden_form)
content = content.replace('        <!-- Pages Table Card -->', hidden_form) # In case it was copied and still says Pages

# Add form="bulkForm" to post_ids checkboxes
content = content.replace('name="post_ids[]" value="{{ $post->id }}"', 'name="post_ids[]" value="{{ $post->id }}" form="bulkForm"')

# Update top bulk actions dropdown and apply button
top_bulk_orig = """          <div class="d-flex align-items-center gap-2">
            <select class="form-select form-select-sm" style="width: auto;">
              <option>Bulk actions</option>
              <option>Edit</option>
              <option>Move to Trash</option>
            </select>
            <button class="btn btn-sm btn-outline-primary bg-body text-primary">Apply</button>"""

top_bulk_new = """          <div class="d-flex align-items-center gap-2">
            <select id="bulkActionTop" class="form-select form-select-sm" style="width: auto;">
              <option value="">Bulk actions</option>
              @if(isset($filter) && $filter === 'trash')
                <option value="restore">Restore</option>
                <option value="force_delete">Delete Permanently</option>
              @else
                <option value="trash">Move to Trash</option>
              @endif
            </select>
            <button class="btn btn-sm btn-outline-primary bg-body text-primary" onclick="applyBulkAction('bulkActionTop')">Apply</button>"""
content = content.replace(top_bulk_orig, top_bulk_new)

# Update bottom bulk actions
bottom_bulk_orig = """            <div class="d-flex align-items-center gap-2">
              <select class="form-select form-select-sm" style="width: auto;">
                <option>Bulk actions</option>
                <option>Edit</option>
                <option>Move to Trash</option>
              </select>
              <button class="btn btn-sm btn-outline-primary bg-body text-primary">Apply</button>
            </div>"""
            
bottom_bulk_new = """            <div class="d-flex align-items-center gap-2">
              <select id="bulkActionBottom" class="form-select form-select-sm" style="width: auto;">
                <option value="">Bulk actions</option>
                @if(isset($filter) && $filter === 'trash')
                  <option value="restore">Restore</option>
                  <option value="force_delete">Delete Permanently</option>
                @else
                  <option value="trash">Move to Trash</option>
                @endif
              </select>
              <button class="btn btn-sm btn-outline-primary bg-body text-primary" onclick="applyBulkAction('bulkActionBottom')">Apply</button>
            </div>"""
content = content.replace(bottom_bulk_orig, bottom_bulk_new)

# Add the JS script before </body>
script = """  <script>
    function applyBulkAction(selectId) {
        const action = document.getElementById(selectId).value;
        if (!action) return;
        
        const selected = document.querySelectorAll('input[name="post_ids[]"]:checked');
        if (selected.length === 0) {
            alert('Please select at least one item.');
            return;
        }
        
        if (action === 'force_delete' || action === 'trash') {
            if (!confirm('Are you sure you want to ' + (action === 'trash' ? 'trash' : 'permanently delete') + ' the selected items?')) return;
        }
        
        document.getElementById('bulkActionInput').value = action;
        document.getElementById('bulkForm').submit();
    }
  </script>
</body>"""
content = content.replace('</body>', script)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Bulk action logic added to posts/index.blade.php")
