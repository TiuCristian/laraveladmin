import glob

files = glob.glob('resources/views/admin/**/*.blade.php', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the top right dropdown avatar
    content = content.replace(
        '<img src="/assets/images/avatar/avatar1.webp" alt="User Avatar">',
        '<img src="{{ auth()->user()->avatar_url }}" alt="User Avatar" style="object-fit: cover; width: 100%; height: 100%;">'
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
