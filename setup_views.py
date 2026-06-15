import os
import shutil

html_dir = 'LaravelCMShtml'
views_dir = 'resources/views/admin'

# Define the mappings
mappings = {
    'posts-list.html': 'posts/index.blade.php',
    'posts-add.html': 'posts/create.blade.php',
    'posts-edit.html': 'posts/edit.blade.php',
    'posts-categories.html': 'categories/index.blade.php',
    'posts-categories-edit.html': 'categories/edit.blade.php',
    'posts-tags.html': 'tags/index.blade.php',
    'posts-tags-edit.html': 'tags/edit.blade.php',
    'pages-list.html': 'pages/index.blade.php',
    'pages-add.html': 'pages/create.blade.php',
    'pages-edit.html': 'pages/edit.blade.php',
}

for src, dest in mappings.items():
    src_path = os.path.join(html_dir, src)
    dest_path = os.path.join(views_dir, dest)
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Copy file
    shutil.copy2(src_path, dest_path)
    print(f"Copied {src} to {dest}")
