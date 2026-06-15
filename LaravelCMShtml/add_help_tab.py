import re

with open('c:/laragon/www/LaravelCMShtml/pages-list.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will find the Screen Options tab and append the Help tab right next to it.
screen_options_btn = '''<button class="btn btn-light btn-sm shadow-sm text-muted bg-white border border-top-0 px-3" type="button" data-bs-toggle="collapse" data-bs-target="#screenOptions" aria-expanded="false" aria-controls="screenOptions" style="border-radius: 0 0 4px 4px; font-size: 0.8rem;">
            Screen Options <i class="fi fi-rr-caret-down ms-1"></i>
          </button>'''

replacement = screen_options_btn + '''
          <button class="btn btn-light btn-sm shadow-sm text-muted bg-white border border-top-0 px-3 ms-2" type="button" style="border-radius: 0 0 4px 4px; font-size: 0.8rem;">
            Help <i class="fi fi-rr-caret-down ms-1"></i>
          </button>'''

content = content.replace(screen_options_btn, replacement)

with open('c:/laragon/www/LaravelCMShtml/pages-list.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added Help tab.")
