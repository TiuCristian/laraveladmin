import os, glob

for f in glob.glob('resources/views/admin/**/*.blade.php', recursive=True):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '"settings-reading.html"' in content:
        content = content.replace('"settings-reading.html"', '"{{ route(\'settings.reading\') }}"')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
