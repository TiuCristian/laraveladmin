import re

def create_edit_page(source_file, target_file, title_find, title_replace, type_name):
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update page title
    content = content.replace(f'<title>{title_find} | CMS Admin Panel</title>', f'<title>{title_replace} | CMS Admin Panel</title>')
    
    # Update Breadcrumbs and main h3
    content = content.replace(f'<h3 class="mb-0">{title_find}</h3>', f'<h3 class="mb-0">{title_replace}</h3>')
    
    # Modify the grid layout
    # The current layout is <div class="col-lg-4"> for the form and <div class="col-lg-8"> for the table.
    # We want to remove the table (col-lg-8) and expand the form to something like col-lg-8 or col-lg-6
    
    # Find the form block
    form_start = content.find(f'<div class="col-lg-4">')
    # Actually let's just do a regex replace to expand the left column and remove the right column
    
    table_start = content.find('<!-- ' + title_find + ' Data Table (Right Column) -->')
    if table_start == -1:
        table_start = content.find('<!-- Tags Data Table (Right Column) -->')
        if table_start == -1:
            table_start = content.find('<!-- Categories Data Table (Right Column) -->')

    if form_start != -1 and table_start != -1:
        # replace col-lg-4 with col-lg-8
        content = content[:form_start] + content[form_start:].replace('<div class="col-lg-4">', '<div class="col-lg-8 col-xl-6">', 1)
        
        # update title "Add New x" to "Edit x"
        content = content.replace(f'Add New {type_name}', f'Edit {type_name}')
        
        # Find the end of the form column which is just before the table column
        # actually, the easiest way is to cut from table_start to the end of the row
        end_of_row = content.find('</div>\n\n      </div>\n    </main>', table_start)
        if end_of_row != -1:
            content = content[:table_start] + content[end_of_row:]

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)

# Create posts-categories-edit.html
create_edit_page('c:/laragon/www/LaravelCMShtml/posts-categories.html', 'c:/laragon/www/LaravelCMShtml/posts-categories-edit.html', 'Categories', 'Edit Category', 'Category')

# Create posts-tags-edit.html
create_edit_page('c:/laragon/www/LaravelCMShtml/posts-tags.html', 'c:/laragon/www/LaravelCMShtml/posts-tags-edit.html', 'Tags', 'Edit Tag', 'Tag')

# Update links in posts-categories.html
with open('c:/laragon/www/LaravelCMShtml/posts-categories.html', 'r', encoding='utf-8') as f:
    cat_content = f.read()
cat_content = re.sub(r'<a href="#" class="[^"]*text-primary hover-primary">Edit</a>', r'<a href="posts-categories-edit.html" class="text-decoration-none text-primary hover-primary">Edit</a>', cat_content)
with open('c:/laragon/www/LaravelCMShtml/posts-categories.html', 'w', encoding='utf-8') as f:
    f.write(cat_content)

# Update links in posts-tags.html
with open('c:/laragon/www/LaravelCMShtml/posts-tags.html', 'r', encoding='utf-8') as f:
    tag_content = f.read()
tag_content = re.sub(r'<a href="#" class="[^"]*text-primary hover-primary">Edit</a>', r'<a href="posts-tags-edit.html" class="text-decoration-none text-primary hover-primary">Edit</a>', tag_content)
with open('c:/laragon/www/LaravelCMShtml/posts-tags.html', 'w', encoding='utf-8') as f:
    f.write(tag_content)

print("Created edit pages and updated links.")
