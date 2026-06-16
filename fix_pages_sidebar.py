import os
import re

# 1. Restore Pages sidebar in Forms
pages_block = '''
                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="{{ route('pages.index') }}">
                      <i class="fi fi-rr-document"></i><span class="menu-label">Pages</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Pages</li>
                      <li class="wp-first-item"><a href="{{ route('pages.index') }}" class="wp-first-item">All Pages</a></li>
                      <li><a href="{{ route('pages.create') }}">Add New</a></li>
                    </ul>
                  </li>'''

forms_block_pattern = r'(<li class="menu-item[^>]*>.*?<span class="menu-label">Forms</span>.*?</ul>\s*</li>)'

for filename in ['index.blade.php', 'create.blade.php', 'edit.blade.php']:
    filepath = f'resources/views/admin/forms/{filename}'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '>Pages</span>' not in content:
            match = re.search(forms_block_pattern, content, flags=re.DOTALL)
            if match:
                new_content = content[:match.end()] + '\n' + pages_block + content[match.end():]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Restored Pages sidebar in {filepath}")

# 2. Cleanup nested Shortcode scripts in Posts and Pages

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
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find ALL instances of the injected blocks
    # It might look like:
    # <script>
    #   <script>
    #     class ShortcodeTool...
    #   </script>
    #
    # We will use regex to remove everything from <script> down to </script> that contains class ShortcodeTool
    
    # Clean up broken <script> <script> tags first
    content = re.sub(r'<script>\s*<script>\s*class ShortcodeTool', r'<script>\n    class ShortcodeTool', content, flags=re.DOTALL)
    
    # Remove all shortcode definitions
    pattern = r'<script>\s*class ShortcodeTool\s*\{.*?\s*\}\s*</script>'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Clean up empty <script> blocks created by mistake
    content = re.sub(r'<script>\s*</script>', '', content)
    
    # Also clean up the random <script> tags just sitting there
    content = re.sub(r'<script>\s*<script>', '<script>', content)

    # Re-inject it EXACTLY once before the EditorJS script block
    # We look for: let editorData = document.getElementById('contentInput')
    
    if 'class ShortcodeTool' not in content:
        # insert it before let editorData =
        content = content.replace("document.addEventListener('DOMContentLoaded', function() {\n      let editorData", shortcode_class_str + "\n  <script>\n    document.addEventListener('DOMContentLoaded', function() {\n      let editorData")
        
        # for create post where it might have const tagInput = ... instead of let editorData
        content = content.replace("document.addEventListener('DOMContentLoaded', function() {\n      const tagInput", shortcode_class_str + "\n  <script>\n    document.addEventListener('DOMContentLoaded', function() {\n      const tagInput")

        # for edit post
        content = content.replace("document.addEventListener('DOMContentLoaded', function() {\n      const postTab", shortcode_class_str + "\n  <script>\n    document.addEventListener('DOMContentLoaded', function() {\n      const postTab")
        
        # also for pages create
        content = content.replace("document.addEventListener('DOMContentLoaded', function() {\n      const pageTitleInput", shortcode_class_str + "\n  <script>\n    document.addEventListener('DOMContentLoaded', function() {\n      const pageTitleInput")
        
        content = content.replace('</script>\n  <script>\n  <script>', '</script>\n  <script>')
        content = content.replace('<script>\n    \n  <script>', '<script>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned up {filepath}")
