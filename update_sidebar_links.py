import glob

replacements = {
    'href="posts-list.html"': 'href="{{ route(\'posts.index\') }}"',
    'href="posts-add.html"': 'href="{{ route(\'posts.create\') }}"',
    'href="posts-categories.html"': 'href="{{ route(\'categories.index\') }}"',
    'href="posts-tags.html"': 'href="{{ route(\'tags.index\') }}"',
    
    'href="pages-list.html"': 'href="{{ route(\'pages.index\') }}"',
    'href="pages-add.html"': 'href="{{ route(\'pages.create\') }}"',
    
    # We haven't created routes for these yet, but just in case:
    # 'href="media-list.html"': 'href="{{ route(\'media.index\') }}"',
    # 'href="media-add.html"': 'href="{{ route(\'media.create\') }}"',
    # 'href="appearance-themes.html"': 'href="{{ route(\'themes.index\') }}"',
    # 'href="plugins-list.html"': 'href="{{ route(\'plugins.index\') }}"',
}

files = glob.glob('resources/views/admin/**/*.blade.php', recursive=True)
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

print(f"Updated {count} files.")
