import shutil
import re

source = 'resources/views/admin/forms/index.blade.php'
dest = 'resources/views/admin/forms/messages.blade.php'

shutil.copyfile(source, dest)

with open(dest, 'r', encoding='utf-8') as f:
    content = f.read()

# Title
content = content.replace('<title>Forms | CMS Admin Panel</title>', '<title>Messages | CMS Admin Panel</title>')

# Page Title
content = content.replace('<h3 class="mb-0 d-inline-block me-2">Forms</h3>', '<h3 class="mb-0 d-inline-block me-2">Messages</h3>')

# Breadcrumb
content = content.replace(
    '<li class="breadcrumb-item active" aria-current="page">Forms</li>',
    '<li class="breadcrumb-item"><a href="{{ route(\'forms.index\') }}">Forms</a></li>\n                <li class="breadcrumb-item active" aria-current="page">Messages</li>'
)

# Remove Add New button from Page Title line
content = content.replace('<a href="{{ route(\'forms.create\') }}" class="btn btn-outline-primary btn-sm mb-1">Add New</a>', '')

# Remove bulk actions entirely, just keep search
# Replace everything from <div class="d-flex flex-wrap align-items-center justify-content-between mb-2"> down to <!-- Pages Table Card -->
pattern = r'<!-- Navigation Links -->.*?<!-- Pages Table Card -->'
content = re.sub(pattern, '<!-- Pages Table Card -->', content, flags=re.DOTALL)

# Re-inject pagination above table
pagination_top = '''
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-3">
          <div class="d-flex align-items-center gap-2">
            <h6 class="mb-0 text-muted fw-bold">All Messages</h6>
          </div>
          <div class="small text-muted">
            {{ $messages->total() }} items
          </div>
        </div>
'''
content = content.replace('<!-- Pages Table Card -->', pagination_top + '\n        <!-- Pages Table Card -->')

# Now for the table itself
table_pattern = r'<table class="table table-hover align-middle mb-0".*?</table>'
new_table = '''<table class="table table-hover align-middle mb-0" style="font-size: 0.9rem;">
              <thead class="table-light">
                <tr>
                  <th scope="col" class="ps-4 border-bottom-0 text-body fw-medium">ID <i class="fi fi-rr-caret-down ms-1 small"></i></th>
                  <th scope="col" class="border-bottom-0 text-primary fw-medium">Form</th>
                  <th scope="col" class="border-bottom-0 text-body fw-medium">Submitted Data</th>
                  <th scope="col" class="border-bottom-0 text-body fw-medium">IP Address</th>
                  <th scope="col" class="pe-4 border-bottom-0 text-primary fw-medium">Date <i class="fi fi-rr-caret-up ms-1 small"></i></th>
                </tr>
              </thead>
              <tbody>
                @forelse($messages as $msg)
                <tr>
                  <td class="ps-4 align-top pt-3">
                    #{{ $msg->id }}
                  </td>
                  <td class="align-top pt-3 fw-bold">
                    <a href="{{ route('forms.edit', $msg->form) }}" class="text-decoration-none">{{ $msg->form->name ?? 'Deleted Form' }}</a>
                  </td>
                  <td class="align-top pt-3" style="width: 40%;">
                    @if(is_array($msg->data))
                        <ul class="list-unstyled mb-0 small">
                        @foreach($msg->data as $key => $value)
                            <li class="mb-1"><strong class="text-dark">{{ ucfirst(str_replace('_', ' ', $key)) }}:</strong> {{ is_array($value) ? json_encode($value) : $value }}</li>
                        @endforeach
                        </ul>
                    @else
                        <span class="text-muted">No data</span>
                    @endif
                  </td>
                  <td class="align-top pt-3 small text-muted">
                    {{ $msg->ip_address ?? 'Unknown' }}
                  </td>
                  <td class="pe-4 align-top pt-3" style="width: 15%;">
                    <span class="text-muted small">{{ $msg->created_at->format('Y/m/d g:i a') }}</span>
                  </td>
                </tr>
                @empty
                <tr>
                    <td colspan="5" class="text-center py-5 text-muted"><i class="fi fi-rr-comment-alt-slash fs-3 d-block mb-2"></i> No messages found.</td>
                </tr>
                @endforelse
                </tbody>
            </table>'''
content = re.sub(table_pattern, new_table, content, flags=re.DOTALL)

# Pagination Footer
footer_pattern = r'<div class="card-footer bg-transparent py-2 d-flex align-items-center justify-content-between border-top">.*?</div>\s*</div>'
new_footer = '''<div class="card-footer bg-transparent py-2 d-flex align-items-center justify-content-end border-top">
            <div class="d-flex align-items-center gap-3">
              <span class="text-muted small">{{ $messages->total() }} items</span>
              <nav aria-label="Page navigation" class="mb-0">
                {{ $messages->appends(request()->query())->links('pagination::bootstrap-5') }}
              </nav>
            </div>
          </div>
        </div>'''
content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL)

with open(dest, 'w', encoding='utf-8') as f:
    f.write(content)
print("Created messages.blade.php")
