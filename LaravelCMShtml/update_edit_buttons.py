with open('c:/laragon/www/LaravelCMShtml/posts-tags-edit.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('Edit Tag</button>', 'Update</button>')
with open('c:/laragon/www/LaravelCMShtml/posts-tags-edit.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('c:/laragon/www/LaravelCMShtml/posts-categories-edit.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('Edit Category</button>', 'Update</button>')
with open('c:/laragon/www/LaravelCMShtml/posts-categories-edit.html', 'w', encoding='utf-8') as f:
    f.write(content)
