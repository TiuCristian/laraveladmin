# -*- coding: utf-8 -*-
css_path = 'c:/laragon/www/LaravelCMShtml/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Make the sidebar respect theme colors
css_content = css_content.replace('background: #1e2225;', 'background: var(--bs-body-bg); border-right: 1px solid var(--bs-border-color);')

css_content = css_content.replace('background-color: #2c3338;', 'background-color: var(--bs-tertiary-bg); border: 1px solid var(--bs-border-color);')

css_content = css_content.replace('background-color: #1e2225;\n  color: #fff;', 'background-color: var(--bs-secondary-bg);\n  color: var(--bs-heading-color);')

css_content = css_content.replace('border-bottom: 1px solid rgba(255,255,255,0.05);', 'border-bottom: 1px solid var(--bs-border-color);')

css_content = css_content.replace('color: rgba(255,255,255,0.8);', 'color: var(--bs-body-color);')

css_content = css_content.replace('background-color: rgba(255,255,255,0.1);\n  color: #fff;', 'background-color: var(--bs-secondary-bg);\n  color: var(--bs-heading-color);')


with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print('Colors fixed for light/dark mode.')
