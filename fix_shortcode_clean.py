import os
import re

files_to_clean = [
    'resources/views/admin/posts/create.blade.php',
    'resources/views/admin/posts/edit.blade.php',
    'resources/views/admin/pages/create.blade.php',
    'resources/views/admin/pages/edit.blade.php',
]

shortcode_class_str = '''
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

for filepath in files_to_clean:
    if not os.path.exists(filepath): continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'<script>\s*class ShortcodeTool.*?\}?\s*</script>'
    content = re.sub(pattern, '', content, flags=re.DOTALL|re.IGNORECASE)
    
    pattern2 = r'class ShortcodeTool.*?\n\s*\}\s*\}\s*\}'
    content = re.sub(pattern2, '', content, flags=re.DOTALL|re.IGNORECASE)

    content = re.sub(r'<script>\s*</script>', '', content)
    content = content.replace('<script>\n    \n  <script>', '<script>')
    content = content.replace('</script>\n  <script>\n  <script>', '</script>\n  <script>')
    
    replace_target = '<script src="https://cdn.jsdelivr.net/npm/@editorjs/image@2.3.0"></script>'
    if replace_target in content:
        content = content.replace(replace_target, replace_target + '\n' + shortcode_class_str)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned {filepath}")
