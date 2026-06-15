import os
import glob

def fix_sidebar_links():
    files = glob.glob('resources/views/admin/**/*.blade.php', recursive=True)
    
    replacements = {
        '"users-list.html"': '"{{ route(\'users.index\') }}"',
        "'users-list.html'": '"{{ route(\'users.index\') }}"',
        '"users-add.html"': '"{{ route(\'users.create\') }}"',
        "'users-add.html'": '"{{ route(\'users.create\') }}"',
        '"users-profile.html"': '"{{ route(\'profile.edit\') }}"',
        "'users-profile.html'": '"{{ route(\'profile.edit\') }}"',
        '"dashboard.html"': '"{{ route(\'admin.dashboard\') }}"',
        "'dashboard.html'": '"{{ route(\'admin.dashboard\') }}"'
    }

    count = 0
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        if content != original_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            print(f"Fixed links in {file}")
            
    print(f"Updated {count} files.")

fix_sidebar_links()
