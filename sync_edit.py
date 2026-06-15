import os

create_path = r'c:\laragon\www\LaravelAdmin\resources\views\admin\posts\create.blade.php'
edit_path = r'c:\laragon\www\LaravelAdmin\resources\views\admin\posts\edit.blade.php'

with open(create_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace breadcrumb and titles
content = content.replace('>Add New Post<', '>Edit Post<')
content = content.replace('Add New</li>', 'Edit Post</li>')

# Replace form action and method
content = content.replace('action="{{ route(\'posts.store\') }}" method="POST"', 'action="{{ route(\'posts.update\', $post) }}" method="POST"')
content = content.replace('@csrf\n', '@csrf\n        @method(\'PUT\')\n')

# Populate Title
content = content.replace('name="title" placeholder="Add title" value=""', 'name="title" placeholder="Add title" value="{{ $post->title }}"')

# Status
content = content.replace('<option value="draft">Draft</option>', '<option value="draft" {{ $post->status == \'draft\' ? \'selected\' : \'\' }}>Draft</option>')
content = content.replace('<option value="published">Published</option>', '<option value="published" {{ $post->status == \'published\' ? \'selected\' : \'\' }}>Published</option>')

# Slug
content = content.replace('name="slug" class="form-control form-control-sm w-auto" value=""', 'name="slug" class="form-control form-control-sm w-auto" value="{{ $post->slug }}"')

# Excerpt
content = content.replace('name="excerpt" class="form-control" rows="3" placeholder="Write an excerpt (optional)"></textarea>', 'name="excerpt" class="form-control" rows="3" placeholder="Write an excerpt (optional)">{{ $post->excerpt }}</textarea>')

# Categories check
content = content.replace('value="{{ $category->id }}">', 'value="{{ $category->id }}" {{ $post->categories->contains($category->id) ? \'checked\' : \'\' }}>')

# Populate content into input
content = content.replace('<input type="hidden" name="content" id="contentInput">', '<input type="hidden" name="content" id="contentInput" value="{{ $post->content }}">')

with open(edit_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
