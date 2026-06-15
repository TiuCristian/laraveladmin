import os
import glob
import re

html_files = glob.glob('c:/laragon/www/LaravelCMShtml/*.html')

for file_path in html_files:
    filename = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix the sidebar 'active' class issue
    # First, remove 'active' from all menu-link classes
    content = content.replace('class="menu-link active"', 'class="menu-link"')
    
    # Then, find the menu-link that corresponds to this file and add 'active'
    target_link = f'class="menu-link" href="{filename}"'
    replacement_link = f'class="menu-link active" href="{filename}"'
    content = content.replace(target_link, replacement_link)

    # If it's a sub-page like posts-edit.html, the menu link should probably be posts-list.html.
    # We can handle the base prefix
    if 'active' not in content.split('<!-- begin::Sidebar Menu -->')[-1].split('<!-- end::Sidebar Menu -->')[0]:
        prefix = filename.split('-')[0] + '-list.html'
        target_link = f'class="menu-link" href="{prefix}"'
        replacement_link = f'class="menu-link active" href="{prefix}"'
        content = content.replace(target_link, replacement_link)

    # 2. Fix the placeholder Edit/Add links in pages-list.html
    if filename == 'pages-list.html':
        content = content.replace('<a href="#" class="text-decoration-none text-primary hover-primary">Edit</a>', '<a href="pages-edit.html" class="text-decoration-none text-primary hover-primary">Edit</a>')
        content = content.replace('<a href="#" class="btn btn-outline-primary btn-sm mb-1">Add New</a>', '<a href="pages-add.html" class="btn btn-outline-primary btn-sm mb-1">Add New</a>')
    
    # 3. Fix the placeholder Edit/Add links in posts-list.html
    if filename == 'posts-list.html':
        content = content.replace('<a href="#" class="text-decoration-none text-primary hover-primary">Edit</a>', '<a href="posts-edit.html" class="text-decoration-none text-primary hover-primary">Edit</a>')
        content = content.replace('<a href="#" class="btn btn-outline-primary btn-sm mb-1">Add New</a>', '<a href="posts-add.html" class="btn btn-outline-primary btn-sm mb-1">Add New</a>')

    # 4. Same for media-list.html
    if filename == 'media-list.html':
        content = content.replace('<a href="#" class="text-decoration-none text-primary hover-primary">Edit</a>', '<a href="media-edit.html" class="text-decoration-none text-primary hover-primary">Edit</a>')
        content = content.replace('<a href="#" class="btn btn-outline-primary btn-sm mb-1">Add New</a>', '<a href="media-add.html" class="btn btn-outline-primary btn-sm mb-1">Add New</a>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Links and active states fixed in all files.')
