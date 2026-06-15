import re

# We will modify posts-tags.html and posts-categories.html to support inline Quick Edit

def add_quick_edit(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add class to Quick Edit links
    content = re.sub(r'(<a href="#" class="[^"]*text-secondary hover-dark)(">Quick Edit</a>)', r'\1 quick-edit-btn\2', content)

    # 2. Inject Quick Edit row after every <tr> inside <tbody>
    # We have to be careful. The <tr> starts and ends. We want to insert right after </tr>
    # But only for rows inside <tbody>.
    
    tbody_match = re.search(r'<tbody>(.*?)</tbody>', content, re.DOTALL)
    if not tbody_match:
        return
    
    tbody_content = tbody_match.group(1)
    
    # We will split by </tr> and insert the hidden row.
    rows = tbody_content.split('</tr>')
    new_tbody = ''
    for row in rows:
        row = row.strip()
        if not row:
            continue
        
        # Determine current name to put in input value (heuristic)
        name_match = re.search(r'<a href="#" class="fw-bold[^>]*>([^<]+)</a>', row)
        name = name_match.group(1) if name_match else ''
        # Strip any entities like &mdash;
        name_clean = re.sub(r'&[^;]+;', '', name).strip()
        
        slug_match = re.search(r'<td>([a-z0-9-]+)</td>', row)
        slug = slug_match.group(1) if slug_match else name_clean.lower()
        
        new_tbody += row + '\n</tr>\n'
        
        if not "quick-edit-row" in row:
            quick_edit_html = f'''
                    <!-- Quick Edit Form (Hidden by default) -->
                    <tr class="quick-edit-row d-none bg-body-tertiary border-bottom">
                      <td colspan="5" class="p-4">
                        <fieldset class="border p-3 rounded bg-body">
                          <legend class="float-none w-auto px-2 fs-6 fw-bold mb-0">Quick Edit</legend>
                          <div class="row g-3">
                            <div class="col-md-6">
                              <label class="form-label small fw-medium text-body mb-1">Name</label>
                              <input type="text" class="form-control form-control-sm" value="{name_clean}">
                            </div>
                            <div class="col-md-6">
                              <label class="form-label small fw-medium text-body mb-1">Slug</label>
                              <input type="text" class="form-control form-control-sm" value="{slug}">
                            </div>
                            <div class="col-12 mt-3 d-flex gap-2">
                              <button type="button" class="btn btn-sm btn-outline-secondary cancel-quick-edit">Cancel</button>
                              <button type="button" class="btn btn-sm btn-primary save-quick-edit">Update</button>
                            </div>
                          </div>
                        </fieldset>
                      </td>
                    </tr>
'''
            new_tbody += quick_edit_html

    content = content.replace(tbody_match.group(1), '\n' + new_tbody + '\n')
    
    # 3. Add JS script at the bottom before </body>
    if 'document.querySelectorAll(".quick-edit-btn")' not in content:
        js_script = '''
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // Quick Edit Toggle Logic
      const quickEditBtns = document.querySelectorAll('.quick-edit-btn');
      quickEditBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
          e.preventDefault();
          
          // Hide any currently open quick edit rows
          document.querySelectorAll('.quick-edit-row').forEach(row => {
            row.classList.add('d-none');
            row.previousElementSibling.classList.remove('d-none');
          });

          const tr = this.closest('tr');
          const quickEditRow = tr.nextElementSibling;
          
          if (quickEditRow && quickEditRow.classList.contains('quick-edit-row')) {
            tr.classList.add('d-none');
            quickEditRow.classList.remove('d-none');
          }
        });
      });

      // Cancel Quick Edit
      const cancelBtns = document.querySelectorAll('.cancel-quick-edit');
      cancelBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
          e.preventDefault();
          const quickEditRow = this.closest('.quick-edit-row');
          const originalTr = quickEditRow.previousElementSibling;
          
          quickEditRow.classList.add('d-none');
          originalTr.classList.remove('d-none');
        });
      });

      // Update Quick Edit (Simulated)
      const saveBtns = document.querySelectorAll('.save-quick-edit');
      saveBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
          e.preventDefault();
          const quickEditRow = this.closest('.quick-edit-row');
          const originalTr = quickEditRow.previousElementSibling;
          
          // Just close it for now as a mock
          quickEditRow.classList.add('d-none');
          originalTr.classList.remove('d-none');
        });
      });
    });
  </script>
'''
        content = content.replace('</body>', js_script + '</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

add_quick_edit('c:/laragon/www/LaravelCMShtml/posts-tags.html')
add_quick_edit('c:/laragon/www/LaravelCMShtml/posts-categories.html')

print("Quick Edit functionality injected.")
