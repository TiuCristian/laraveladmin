import shutil
import re

source = 'resources/views/admin/forms/messages.blade.php'
dest = 'resources/views/admin/forms/messages_edit.blade.php'

with open(source, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Page Title
content = content.replace('<title>Messages | CMS Admin Panel</title>', '<title>Edit Message | CMS Admin Panel</title>')
content = content.replace('<h3 class="mb-0 d-inline-block me-2">Messages</h3>', '<h3 class="mb-0 d-inline-block me-2">Edit Message</h3>')
content = content.replace('<li class="breadcrumb-item active" aria-current="page">Messages</li>', '<li class="breadcrumb-item"><a href="{{ route(\'forms.messages\') }}">Messages</a></li>\n                <li class="breadcrumb-item active" aria-current="page">Edit Message</li>')

# Remove the table section
table_pattern = r'<!-- Forms Table Card -->.*?<!-- end::Main Content Area -->'
# Replace it with an edit form

edit_form_html = '''<!-- Edit Message Form -->
        <div class="card border-0 shadow-sm mb-4">
          <div class="card-header bg-transparent border-bottom py-3">
            <h6 class="mb-0 fw-bold">Submitted Data</h6>
          </div>
          <div class="card-body p-4">
            <form action="{{ route('forms.messages.update', $message->id) }}" method="POST">
                @csrf
                @method('PUT')
                
                @php
                    $displayData = $message->data;
                    if (is_array($displayData) && count($displayData) === 1 && isset($displayData['fields'])) {
                        $displayData = $displayData['fields'];
                    }
                @endphp
                
                <div class="row g-4">
                    <div class="col-lg-8">
                        @if(is_array($displayData))
                            @foreach($displayData as $key => $value)
                                <div class="mb-3">
                                    <label class="form-label fw-bold">{{ ucfirst(str_replace('_', ' ', $key)) }}</label>
                                    @if(strlen($value) > 100)
                                        <textarea name="data[{{ $key }}]" class="form-control" rows="5">{{ is_array($value) ? json_encode($value) : $value }}</textarea>
                                    @else
                                        <input type="text" name="data[{{ $key }}]" class="form-control" value="{{ is_array($value) ? json_encode($value) : $value }}">
                                    @endif
                                </div>
                            @endforeach
                        @else
                            <div class="alert alert-warning">No data available to edit.</div>
                        @endif
                    </div>
                    
                    <div class="col-lg-4">
                        <div class="bg-light p-3 rounded border mb-3">
                            <h6 class="fw-bold mb-3">Message Meta</h6>
                            <div class="mb-2 text-muted small">
                                <strong>Form:</strong> {{ $message->form->name ?? 'Deleted Form' }}
                            </div>
                            <div class="mb-2 text-muted small">
                                <strong>Submitted:</strong> {{ $message->created_at->format('M j, Y g:i a') }}
                            </div>
                            <div class="mb-2 text-muted small">
                                <strong>IP Address:</strong> {{ $message->ip_address ?? 'Unknown' }}
                            </div>
                            <hr>
                            <button type="submit" class="btn btn-primary w-100">Save Changes</button>
                        </div>
                    </div>
                </div>
            </form>
          </div>
        </div>
      </div>
    </main>
'''

content = re.sub(table_pattern, edit_form_html, content, flags=re.DOTALL)

# There is a stray <div class="d-flex flex-wrap align-items-center justify-content-between mb-3"> 
# Let's clean up everything between <div class="app-page-head"> and <!-- Edit Message Form -->
cleanup_pattern = r'</div>\s*</div>\s*<div class="d-flex flex-wrap align-items-center justify-content-between mb-3">.*?<!-- Edit Message Form -->'

content = re.sub(cleanup_pattern, '</div>\n        </div>\n\n        <!-- Edit Message Form -->', content, flags=re.DOTALL)

with open(dest, 'w', encoding='utf-8') as f:
    f.write(content)
print("Created messages_edit.blade.php")
