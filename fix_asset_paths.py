import glob

files = glob.glob('resources/views/admin/**/*.blade.php', recursive=True)
count = 0

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Replace relative asset paths with absolute asset paths
    content = content.replace('href="assets/', 'href="/assets/')
    content = content.replace('src="assets/', 'src="/assets/')
    
    # Also fix some other common paths if they exist
    content = content.replace("href='assets/", "href='/assets/")
    content = content.replace("src='assets/", "src='/assets/")
        
    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Updated {count} files.")
