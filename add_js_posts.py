import os

file_path = r'c:\laragon\www\LaravelAdmin\resources\views\admin\posts\create.blade.php'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

script_to_add = """
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const postTab = document.getElementById('post-tab');
      const blockTab = document.getElementById('block-tab');
      
      if(postTab && blockTab) {
        postTab.addEventListener('shown.bs.tab', function (event) {
          postTab.classList.add('text-body');
          postTab.classList.remove('text-muted');
          postTab.style.boxShadow = 'inset 0 -2px 0 0 var(--bs-dark)';
          
          blockTab.classList.remove('text-body');
          blockTab.classList.add('text-muted');
          blockTab.style.boxShadow = 'none';
        });
        
        blockTab.addEventListener('shown.bs.tab', function (event) {
          blockTab.classList.add('text-body');
          blockTab.classList.remove('text-muted');
          blockTab.style.boxShadow = 'inset 0 -2px 0 0 var(--bs-dark)';
          
          postTab.classList.remove('text-body');
          postTab.classList.add('text-muted');
          postTab.style.boxShadow = 'none';
        });
      }
    });
  </script>
</body>"""

content = content.replace('</body>', script_to_add)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("JS script added successfully.")
