import re

def fix_page(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Mock Rich Text Editor with editorjs div
    mock_pattern = r'<!-- Mock Rich Text Editor -->.*?</div>\s*</div>\s*</div>'
    editor_div = '''<!-- Editor Textarea -->
            <div id="editorjs" class="mt-2" style="min-height: 600px; font-family: 'Instrument Sans', sans-serif;"></div>
            <input type="hidden" name="content" id="contentInput" value="{{ $page->content ?? '' }}">
            <style>
              .ce-block__content, .ce-toolbar__content { max-width: 800px; margin-left: 60px; }
            </style>
'''
    # Using a simpler string replacement since regex with multiline can be tricky
    if '<!-- Mock Rich Text Editor -->' in content:
        start_idx = content.find('<!-- Mock Rich Text Editor -->')
        # find the end of the div (just before <div class="col-lg-4">)
        # Actually let's just use re.sub with DOTALL
        content = re.sub(r'<!-- Mock Rich Text Editor -->.*?(?=</div>\s*</div>\s*</div>\s*<!-- Sidebar Meta Boxes \(Right Column\) -->)', editor_div, content, flags=re.DOTALL)

    # Replace JS script
    # It has basic EditorJS without image tool
    script_pattern = r'<script src="https://cdn.jsdelivr.net/npm/@editorjs/editorjs@latest"></script>.*?<!-- end::NexLink Page Scripts -->'
    full_script = '''<script src="https://cdn.jsdelivr.net/npm/@editorjs/editorjs@latest"></script>
  <script src="https://cdn.jsdelivr.net/npm/@editorjs/header@latest"></script>
  <script src="https://cdn.jsdelivr.net/npm/@editorjs/list@latest"></script>
  <script src="https://cdn.jsdelivr.net/npm/@editorjs/paragraph@latest"></script>
  <script src="https://cdn.jsdelivr.net/npm/@editorjs/image@2.3.0"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      let editorData = document.getElementById('contentInput').value || '{"blocks":[]}';
      
      let parsedData = {"blocks":[]};
      try {
          parsedData = typeof editorData === 'string' ? JSON.parse(editorData) : editorData;
      } catch (e) { console.log(e); }

      const editor = new EditorJS({
        holder: 'editorjs',
        tools: {
          header: { class: Header, inlineToolbar: true },
          list: { class: typeof EditorjsList !== 'undefined' ? EditorjsList : List, inlineToolbar: true },
          paragraph: { class: Paragraph, inlineToolbar: true },
          image: {
            class: ImageTool,
            config: {
              endpoints: {
                byFile: '{{ route('admin.upload.image') }}',
                byUrl: '{{ route('admin.upload.fetchUrl') }}',
              },
              additionalRequestHeaders: {
                'X-CSRF-TOKEN': '{{ csrf_token() }}'
              }
            }
          }
        },
        data: parsedData,
        onChange: () => {
          editor.save().then((outputData) => {
            document.getElementById('contentInput').value = JSON.stringify(outputData);
          });
        },
        onReady: () => {
            editor.save().then((outputData) => {
                document.getElementById('contentInput').value = JSON.stringify(outputData);
            });
        }
      });
    });
  </script>
  <!-- end::NexLink Page Scripts -->'''
    content = re.sub(script_pattern, full_script, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

fix_page('resources/views/admin/pages/edit.blade.php')
fix_page('resources/views/admin/pages/create.blade.php')
