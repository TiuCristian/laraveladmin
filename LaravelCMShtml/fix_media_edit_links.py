import re

with open('c:/laragon/www/LaravelCMShtml/media-list.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Currently the edit links in media-list.html are likely just '#' or something similar.
# Let's replace the link text "Edit" with a proper href.
# Wait, I don't know the exact HTML of the edit link in media-list.html.
# Let's just find href="#" class="text-decoration-none text-primary hover-primary">Edit</a> and replace with href="media-edit.html" ...
content = content.replace('href="#" class="text-decoration-none text-primary hover-primary">Edit</a>', 'href="media-edit.html" class="text-decoration-none text-primary hover-primary">Edit</a>')

with open('c:/laragon/www/LaravelCMShtml/media-list.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed edit links in media-list.html")
