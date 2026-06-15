# -*- coding: utf-8 -*-
css_path = 'c:/laragon/www/LaravelCMShtml/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace left: var(--app-menubar-tabs); with left: 100%;
css_content = css_content.replace('left: var(--app-menubar-tabs); /* Width of the sidebar */', 'left: 100%;')

# Replace left: 80px !important; with left: 100% !important;
css_content = css_content.replace('left: 80px !important;', 'left: 100% !important;')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print('Hover gap fixed.')
