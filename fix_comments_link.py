import os, glob

for f in glob.glob('resources/views/admin/**/*.blade.php', recursive=True):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '"comments-list.html"' in content:
        content = content.replace('"comments-list.html"', '"{{ route(\'comments.index\') }}"')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
