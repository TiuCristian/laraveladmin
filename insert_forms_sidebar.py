import os
import glob
import re

def insert_forms_sidebar(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # If it already has Forms, skip
    if '>Forms</span>' in content or '>Forms<' in content:
        return

    # Find the Media block
    media_pattern = r'(<li class="menu-item[^>]*>.*?<span class="menu-label">Media</span>.*?</ul>\s*</li>)'
    
    forms_block = '''
                  <li class="menu-item wp-has-submenu">
                    <a class="menu-link" href="{{ route('forms.index') }}">
                      <i class="fi fi-rr-document"></i><span class="menu-label">Forms</span>
                    </a>
                    <ul class="wp-submenu wp-submenu-wrap">
                      <li class="wp-submenu-head" aria-hidden="true">Forms</li>
                      <li class="wp-first-item"><a href="{{ route('forms.index') }}" class="wp-first-item">All Forms</a></li>
                      <li><a href="{{ route('forms.create') }}">Add New</a></li>
                    </ul>
                  </li>'''

    if re.search(media_pattern, content, flags=re.DOTALL):
        # We need to use a function or careful replacement to insert after the match
        match = re.search(media_pattern, content, flags=re.DOTALL)
        if match:
            new_content = content[:match.end()] + "\n" + forms_block + content[match.end():]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")

for root, dirs, files in os.walk('resources/views/admin'):
    for file in files:
        if file.endswith('.blade.php'):
            insert_forms_sidebar(os.path.join(root, file))
