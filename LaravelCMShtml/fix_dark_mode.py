import os

files_to_fix = [
    'c:/laragon/www/LaravelCMShtml/appearance-menus.html',
    'c:/laragon/www/LaravelCMShtml/pages-list.html',
    'c:/laragon/www/LaravelCMShtml/posts-list.html',
    'c:/laragon/www/LaravelCMShtml/media-edit.html'
]

for filepath in files_to_fix:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We don't want to replace standard bootstrap classes that might be needed,
        # but bg-white, bg-light, text-dark are the main culprits.
        content = content.replace('bg-white', 'bg-body')
        content = content.replace('bg-light', 'bg-body-tertiary')
        content = content.replace('text-dark', 'text-body')
        
        # Also fix the accordion button text colors which might be hardcoded
        # Actually text-body is fine.

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Fixed dark mode classes.")
