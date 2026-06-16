import os
import glob

files = glob.glob('resources/views/admin/**/*.blade.php', recursive=True)

target_str = "<li><a href=\"{{ route('forms.create') }}\">Add New</a></li>"
replacement_str = "<li><a href=\"{{ route('forms.create') }}\">Add New</a></li>\n                      <li><a href=\"{{ route('forms.messages') }}\">Messages</a></li>"

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "route('forms.messages')" not in content and target_str in content:
        content = content.replace(target_str, replacement_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
