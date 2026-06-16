import os
import re

shortcode_class = '''
  <script>
    class ShortcodeTool {
      static get toolbox() {
        return {
          title: 'Shortcode',
          icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M10 8l-4 4 4 4M14 8l4 4-4 4"></path></svg>'
        };
      }

      constructor({data}){
        this.data = data;
      }

      render(){
        this.wrapper = document.createElement('div');
        this.wrapper.classList.add('shortcode-wrapper', 'p-3', 'bg-light', 'border', 'border-dashed', 'rounded', 'text-center', 'my-2');
        this.input = document.createElement('input');
        this.input.classList.add('form-control', 'text-center', 'font-monospace', 'bg-transparent', 'border-0', 'shadow-none');
        this.input.style.fontSize = '1.1rem';
        this.input.placeholder = 'Write shortcode here... e.g. [form id="1"]';
        this.input.value = this.data && this.data.code ? this.data.code : '';
        this.wrapper.appendChild(this.input);
        return this.wrapper;
      }

      save(blockContent){
        return {
          code: this.input.value
        }
      }
    }
  </script>
'''

def inject_shortcode_tool(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'ShortcodeTool' in content:
        return

    content = content.replace("document.addEventListener('DOMContentLoaded', function() {", shortcode_class + "\n  <script>\n    document.addEventListener('DOMContentLoaded', function() {")
    
    content = re.sub(r'(paragraph:\s*\{[^}]+\},?)', r'\1\n          shortcode: ShortcodeTool,', content)
    
    if 'paragraph: Paragraph' in content:
        content = re.sub(r'(paragraph:\s*Paragraph,?)', r'\1\n          shortcode: ShortcodeTool,', content)

    content = content.replace('</script>\n  <script>\n  <script>', '</script>\n  <script>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

inject_shortcode_tool('resources/views/admin/posts/create.blade.php')
inject_shortcode_tool('resources/views/admin/posts/edit.blade.php')
inject_shortcode_tool('resources/views/admin/pages/create.blade.php')
inject_shortcode_tool('resources/views/admin/pages/edit.blade.php')

def update_frontend(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    js_form_logic = '''
                    case 'shortcode':
                        let codeText = block.data.code || '';
                        let sFormMatch = codeText.match(/\\[form id=["']?(\\d+)["']?\\]/);
                        if (sFormMatch) {
                            let formId = parseInt(sFormMatch[1]);
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
                                codeText = codeText.replace(sFormMatch[0], formHtml);
                            }
                        }
                        html += `<div>${codeText}</div>`;
                        break;
'''
    if "case 'shortcode':" not in content:
        content = content.replace("case 'paragraph':", js_form_logic + "\n                    case 'paragraph':")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

update_frontend('resources/views/frontend/post.blade.php')
try:
    update_frontend('resources/views/frontend/page.blade.php')
except FileNotFoundError:
    pass
