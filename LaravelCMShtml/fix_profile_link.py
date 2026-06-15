import os
import glob

# Find all html files in the directory
html_files = glob.glob('c:/laragon/www/LaravelCMShtml/*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We are looking for: href="#"><i class="fi fi-rr-user"></i> Edit Profile</a>
    # We will replace href="#" with href="users-profile.html"
    old_string = 'href="#"><i class="fi fi-rr-user"></i> Edit Profile</a>'
    new_string = 'href="users-profile.html"><i class="fi fi-rr-user"></i> Edit Profile</a>'
    
    if old_string in content:
        content = content.replace(old_string, new_string)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Fixed Edit Profile links in all HTML files.")
