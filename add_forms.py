import re
import os

files = [
    ('resources/views/admin/posts/create.blade.php', 'post', 'create'),
    ('resources/views/admin/posts/edit.blade.php', 'post', 'edit'),
    ('resources/views/admin/pages/create.blade.php', 'page', 'create'),
    ('resources/views/admin/pages/edit.blade.php', 'page', 'edit'),
]

for filepath, model_name, action in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Wrap the row inside a form
    route_action = f"{{{{ route('{model_name}s.store') }}}}" if action == 'create' else f"{{{{ route('{model_name}s.update', ${model_name}) }}}}"
    method_field = "" if action == 'create' else "@method('PUT')"
    
    # We find `<div class="row">` that wraps the editor and sidebar
    # Usually it's after `<div class="app-page-head ...">`
    row_match = re.search(r'(<div class="row">)(.*)(</main>)', content, re.DOTALL)
    
    if row_match:
        form_start = f'<form action="{route_action}" method="POST" id="editForm">\n@csrf\n{method_field}\n<div class="row">'
        content = content.replace('<div class="row">', form_start, 1)
        # Find the last closing div of the container before </main>
        content = content.replace('</main>', '</form>\n</main>', 1)

    # Change the publish button to submit the form
    content = content.replace('<button class="btn btn-primary btn-sm">Publish</button>', '<button type="submit" class="btn btn-primary btn-sm">Publish</button>')
    content = content.replace('<button class="btn btn-primary btn-sm px-4 waves-effect">Update</button>', '<button type="submit" class="btn btn-primary btn-sm px-4 waves-effect">Update</button>')

    # Replace title input value
    if action == 'edit':
        content = re.sub(r'value="Hello World!" value="Getting Started with CMS"', f'value="{{{{ ${model_name}->title }}}}"', content)
        content = re.sub(r'id="postTitle" placeholder="Add title" value="[^"]*"', f'id="postTitle" name="title" placeholder="Add title" value="{{{{ ${model_name}->title }}}}"', content)
        # Sometimes there's no double value
        content = re.sub(r'id="postTitle" placeholder="Add title" value=""', f'id="postTitle" name="title" placeholder="Add title" value="{{{{ ${model_name}->title }}}}"', content)
        
        # If it didn't match the exact placeholder, try a generic replace
        if f'name="title"' not in content:
            content = content.replace('id="postTitle"', f'id="postTitle" name="title" value="{{{{ ${model_name}->title }}}}"')
    else:
        # Create form
        content = re.sub(r'value="Hello World!" value="Getting Started with CMS"', 'value=""', content)
        content = content.replace('id="postTitle"', 'id="postTitle" name="title"')

    # Replace the editor textarea with Editor.js block
    textarea_pattern = r'<!-- Editor Textarea -->\s*<textarea[^>]*>.*?</textarea>'
    
    editor_html = f"""<!-- Editor Textarea -->
                <div id="editorjs" class="border rounded bg-white p-3 shadow-sm" style="min-height: 400px; font-family: 'Instrument Sans', sans-serif;"></div>
                <input type="hidden" name="content" id="contentInput">
                <style>
                  .ce-block__content, .ce-toolbar__content {{ max-width: 100%; }}
                  .codex-editor__redactor {{ padding-bottom: 50px !important; }}
                </style>
    """
    content = re.sub(textarea_pattern, editor_html, content, flags=re.DOTALL)
    
    # Hide the Mock Toolbar since EditorJS has its own inline toolbar
    content = content.replace('<!-- Mock Toolbar for Editor -->', '<div class="d-none">')
    content = content.replace('<!-- Editor Textarea -->', '</div><!-- Editor Textarea -->')

    # Add Editor.js scripts at the end
    script_injection = f"""
  <script src="https://cdn.jsdelivr.net/npm/@editorjs/editorjs@latest"></script>
  <script src="https://cdn.jsdelivr.net/npm/@editorjs/header@latest"></script>
  <script src="https://cdn.jsdelivr.net/npm/@editorjs/list@latest"></script>
  <script src="https://cdn.jsdelivr.net/npm/@editorjs/paragraph@latest"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      const editorData = {('{!! $' + model_name + '->content ?: \'' + '{"blocks":[]}' + '\' !!}') if action == 'edit' else '\'{"blocks":[]}\''};
      
      let parsedData = {{"blocks":[]}};
      try {{
          parsedData = typeof editorData === 'string' ? JSON.parse(editorData) : editorData;
      }} catch (e) {{ console.log(e); }}

      const editor = new EditorJS({{
        holder: 'editorjs',
        tools: {{
          header: Header,
          list: List,
          paragraph: Paragraph
        }},
        data: parsedData,
        onChange: () => {{
          editor.save().then((outputData) => {{
            document.getElementById('contentInput').value = JSON.stringify(outputData);
          }});
        }},
        onReady: () => {{
            editor.save().then((outputData) => {{
                document.getElementById('contentInput').value = JSON.stringify(outputData);
            }});
        }}
      }});
      
      // Auto save content before form submit if needed
      const editForm = document.getElementById('editForm');
      if (editForm) {{
        editForm.addEventListener('submit', function(e) {{
            // editor onChange already populates it, but just in case
        }});
      }}
    }});
  </script>
  <!-- end::NexLink Page Scripts -->
"""
    content = content.replace('<!-- end::NexLink Page Scripts -->', script_injection)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated {filepath}")
