import re

def update_frontend(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    js_form_logic = '''
                    case 'paragraph':
                        let text = block.data.text;
                        let formMatch = text.match(/\\[form id=["']?(\\d+)["']?\\]/);
                        if (formMatch) {
                            let formId = parseInt(formMatch[1]);
                            @php
                                $allForms = \\App\\Models\\Form::all();
                            @endphp
                            let preloadedForms = {!! json_encode($allForms) !!};
                            let form = preloadedForms.find(f => f.id === formId);
                            if (form) {
                                let formHtml = `<form action="/forms/${form.id}/submit" method="POST" class="mt-4 mb-4 border p-4 rounded bg-light">`;
                                formHtml += `<input type="hidden" name="_token" value="{{ csrf_token() }}">`;
                                if(form.fields) {
                                    form.fields.forEach(field => {
                                        let req = field.required ? 'required' : '';
                                        let reqStar = field.required ? '<span class="text-danger">*</span>' : '';
                                        formHtml += `<div class="mb-3"><label class="form-label fw-bold">${field.label} ${reqStar}</label>`;
                                        if (field.type === 'textarea') {
                                            formHtml += `<textarea name="fields[${field.label}]" class="form-control" ${req}></textarea>`;
                                        } else if (field.type === 'select') {
                                            formHtml += `<select name="fields[${field.label}]" class="form-select" ${req}>`;
                                            if(field.options) {
                                                field.options.split(',').forEach(opt => {
                                                    formHtml += `<option value="${opt.trim()}">${opt.trim()}</option>`;
                                                });
                                            }
                                            formHtml += `</select>`;
                                        } else {
                                            formHtml += `<input type="${field.type}" name="fields[${field.label}]" class="form-control" ${req}>`;
                                        }
                                        formHtml += `</div>`;
                                    });
                                }
                                formHtml += `<button type="submit" class="btn btn-primary">${form.submit_text || 'Submit'}</button>`;
                                formHtml += `</form>`;
                                text = text.replace(formMatch[0], formHtml);
                            }
                        }
                        html += `<p>${text}</p>`;
                        break;
'''
    
    content = re.sub(r"case 'paragraph':\s*html \+= `<p>\$\{block\.data\.text\}</p>`;\s*break;", js_form_logic, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_frontend('resources/views/frontend/post.blade.php')
try:
    update_frontend('resources/views/frontend/page.blade.php')
except FileNotFoundError:
    pass
