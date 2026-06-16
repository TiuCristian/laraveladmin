import re

def generate_form_view(template_path, target_path, is_edit=False):
    with open(template_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # We want to replace everything inside <main class="app-wrapper">
    main_pattern = r'<main class="app-wrapper">.*?</main>'
    
    if is_edit:
        title = "Edit Form"
        action = "{{ route('forms.update', $form) }}"
        method = "@method('PUT')"
        form_name = "{{ $form->name }}"
        submit_text = "{{ $form->submit_text }}"
        shortcode_display = '''
        <div class="alert alert-info mb-4">
            <h6 class="alert-heading fw-bold mb-1"><i class="fi fi-rr-info"></i> Shortcode</h6>
            <p class="mb-0 small">Copy this shortcode and paste it into your post, page, or text widget content:</p>
            <code class="d-inline-block bg-white border p-2 mt-2 fs-6 rounded user-select-all">[form id="{{ $form->id }}"]</code>
        </div>
        '''
    else:
        title = "Add New Form"
        action = "{{ route('forms.store') }}"
        method = ""
        form_name = ""
        submit_text = "Submit"
        shortcode_display = ""

    main_content = f'''<main class="app-wrapper">
      <div class="container-fluid">
        <!-- Page Title & Breadcrumbs -->
        <div class="app-page-head d-flex align-items-center justify-content-between mb-4">
          <div>
            <h3 class="mb-0">{title}</h3>
            <nav aria-label="breadcrumb" class="mt-2">
              <ol class="breadcrumb mb-0">
                <li class="breadcrumb-item"><a href="{{{{ route('admin.dashboard') }}}}">Home</a></li>
                <li class="breadcrumb-item"><a href="{{{{ route('forms.index') }}}}">Forms</a></li>
                <li class="breadcrumb-item active" aria-current="page">{title}</li>
              </ol>
            </nav>
          </div>
          <div>
            <button type="submit" form="editForm" class="btn btn-primary btn-sm">Save Form</button>
          </div>
        </div>

        {shortcode_display}

        @if(session('success'))
            <div class="alert alert-success alert-dismissible fade show mb-4" role="alert">
                {{{{ session('success') }}}}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        @endif

        <form action="{action}" method="POST" id="editForm">
        @csrf
        {method}
        <input type="hidden" name="fields" id="fieldsInput" value="">
        
        <div class="row g-4">
          <!-- Editor Area (Left Column) -->
          <div class="col-lg-8">
            <div class="card border-0 shadow-sm mb-4">
              <div class="card-body p-4">
                <div class="mb-4">
                  <label class="form-label fw-bold">Form Name</label>
                  <input type="text" class="form-control form-control-lg border-0 bg-light fs-4 fw-bold" placeholder="e.g. Contact Form 1" value="{form_name}" name="name" required>
                </div>

                <div class="mb-4">
                  <h6 class="fw-bold mb-3 border-bottom pb-2">Form Fields Builder</h6>
                  <p class="text-muted small mb-3">Add fields to your form. You can drag and drop them to reorder.</p>
                  
                  <div id="fieldsContainer" class="mb-3">
                    <!-- Fields will be dynamically injected here -->
                  </div>
                  
                  <button type="button" class="btn btn-outline-primary btn-sm" onclick="addField()"><i class="fi fi-rr-plus"></i> Add Field</button>
                </div>

              </div>
            </div>
          </div>

          <!-- Sidebar Meta Boxes (Right Column) -->
          <div class="col-lg-4">
            
            <div class="card border-0 shadow-sm mb-4">
              <div class="card-header border-bottom bg-transparent py-3 d-flex justify-content-between align-items-center">
                <h6 class="mb-0 fw-bold">Form Settings</h6>
              </div>
              <div class="card-body">
                <div class="mb-3">
                  <label class="form-label text-muted small fw-medium">Submit Button Text</label>
                  <input type="text" name="submit_text" class="form-control form-control-sm" value="{submit_text}">
                </div>
              </div>
              <div class="card-footer bg-transparent py-3 text-end border-top">
                <button type="button" onclick="saveForm()" class="btn btn-primary btn-sm px-4 waves-effect">Save Form</button>
              </div>
            </div>

          </div>
        </div>
        </form>
      </div>
    </main>'''

    new_html = re.sub(main_pattern, main_content, html, flags=re.DOTALL)

    # Insert Javascript for Form Builder
    js_content = '''
  <script>
    let fields = [];
    
    document.addEventListener('DOMContentLoaded', function() {
        // Load existing fields
        @if(isset($form) && $form->fields)
            fields = {!! json_encode($form->fields) !!};
        @endif
        
        renderFields();

        var el = document.getElementById('fieldsContainer');
        if (el) {
            Sortable.create(el, {
                animation: 150,
                handle: '.field-drag-handle',
                onEnd: function (evt) {
                    // Update array order based on DOM
                    let newFields = [];
                    document.querySelectorAll('.form-field-row').forEach(function(row) {
                        newFields.push(fields[row.dataset.index]);
                    });
                    fields = newFields;
                    renderFields();
                }
            });
        }
    });

    function renderFields() {
        const container = document.getElementById('fieldsContainer');
        container.innerHTML = '';
        
        if (fields.length === 0) {
            container.innerHTML = '<div class="text-center text-muted small py-4 bg-light border rounded border-dashed">No fields added yet.</div>';
            return;
        }

        fields.forEach((field, index) => {
            const row = document.createElement('div');
            row.className = 'form-field-row bg-white border rounded p-3 mb-2 d-flex align-items-start gap-3';
            row.dataset.index = index;
            
            row.innerHTML = `
                <div class="field-drag-handle text-muted cursor-grab pt-1" style="cursor: grab;"><i class="fi fi-rr-menu-burger"></i></div>
                <div class="flex-grow-1">
                    <div class="row g-2">
                        <div class="col-md-4">
                            <label class="form-label small text-muted mb-1">Field Label</label>
                            <input type="text" class="form-control form-control-sm" value="${field.label || ''}" onchange="updateField(${index}, 'label', this.value)" placeholder="e.g. Your Name">
                        </div>
                        <div class="col-md-4">
                            <label class="form-label small text-muted mb-1">Field Type</label>
                            <select class="form-select form-select-sm" onchange="updateField(${index}, 'type', this.value)">
                                <option value="text" ${field.type === 'text' ? 'selected' : ''}>Text Input</option>
                                <option value="email" ${field.type === 'email' ? 'selected' : ''}>Email Input</option>
                                <option value="textarea" ${field.type === 'textarea' ? 'selected' : ''}>Textarea</option>
                                <option value="select" ${field.type === 'select' ? 'selected' : ''}>Dropdown (Select)</option>
                            </select>
                        </div>
                        <div class="col-md-2 d-flex align-items-end">
                            <div class="form-check mb-1">
                                <input class="form-check-input" type="checkbox" id="req_${index}" onchange="updateField(${index}, 'required', this.checked)" ${field.required ? 'checked' : ''}>
                                <label class="form-check-label small" for="req_${index}">Required</label>
                            </div>
                        </div>
                        <div class="col-md-2 d-flex align-items-end justify-content-end">
                            <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeField(${index})"><i class="fi fi-rr-trash"></i></button>
                        </div>
                    </div>
                    ${field.type === 'select' ? `
                    <div class="row mt-2">
                        <div class="col-12">
                            <label class="form-label small text-muted mb-1">Options (comma separated)</label>
                            <input type="text" class="form-control form-control-sm" value="${field.options || ''}" onchange="updateField(${index}, 'options', this.value)" placeholder="Option 1, Option 2, Option 3">
                        </div>
                    </div>
                    ` : ''}
                </div>
            `;
            container.appendChild(row);
        });
    }

    function addField() {
        fields.push({
            label: 'New Field',
            type: 'text',
            required: false,
            options: ''
        });
        renderFields();
    }

    function updateField(index, key, value) {
        fields[index][key] = value;
        if (key === 'type') renderFields();
    }

    function removeField(index) {
        if(confirm('Remove this field?')) {
            fields.splice(index, 1);
            renderFields();
        }
    }

    function saveForm() {
        document.getElementById('fieldsInput').value = JSON.stringify(fields);
        document.getElementById('editForm').submit();
    }
  </script>
'''
    new_html = new_html.replace('</body>', js_content + '\n</body>')

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

# Using index.blade.php as the template base to inject the new content
generate_form_view('resources/views/admin/forms/index.blade.php', 'resources/views/admin/forms/create.blade.php', is_edit=False)
generate_form_view('resources/views/admin/forms/index.blade.php', 'resources/views/admin/forms/edit.blade.php', is_edit=True)
