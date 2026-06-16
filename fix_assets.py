import re

with open('resources/views/admin/menus/index.blade.php', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('href="assets/', 'href="{{ asset(\'assets/')
content = content.replace('src="assets/', 'src="{{ asset(\'assets/')
content = content.replace('.css">', '.css\') }}">')
content = content.replace('.js"></script>', '.js\') }}"></script>')
content = content.replace('.png">', '.png\') }}">')
content = content.replace('.webp">', '.webp\') }}">')

with open('resources/views/admin/menus/index.blade.php', 'w', encoding='utf-8') as f:
    f.write(content)
