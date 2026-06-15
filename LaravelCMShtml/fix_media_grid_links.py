import re

with open('c:/laragon/www/LaravelCMShtml/media-list.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <button class="... btn-light ...">Edit</button> with <a> tag
content = re.sub(
    r'<button class="(btn btn-sm btn-light[^"]*)">Edit</button>',
    r'<a href="media-edit.html" class="\1">Edit</a>',
    content
)

# Also let's change Delete to anchor as well just so it's consistent if they want to hook it up
content = re.sub(
    r'<button class="(btn btn-sm btn-danger[^"]*)"><i class="fi fi-rr-trash me-1"></i> Delete</button>',
    r'<a href="#" class="\1"><i class="fi fi-rr-trash me-1"></i> Delete</a>',
    content
)

with open('c:/laragon/www/LaravelCMShtml/media-list.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed edit links in media-list.html grid view")
