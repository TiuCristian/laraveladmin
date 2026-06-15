import os
import re

def fix_file(filepath, is_edit):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add form="editForm" to header buttons
    content = content.replace('name="status" value="draft" class="btn', 'form="editForm" name="status" value="draft" class="btn')
    content = content.replace('name="status" value="published" class="btn', 'form="editForm" name="status" value="published" class="btn')

    # 2. Fix the Publish (date) field
    publish_pattern = r'<div class="d-flex justify-content-between align-items-start mb-3">\s*<span class="text-body small">Publish</span>\s*<a href="#" class="text-decoration-none small">Immediately</a>\s*</div>'
    
    val_publish = "{{ $page->published_at ? $page->published_at->format('Y-m-d\TH:i') : '' }}" if is_edit else ""
    new_publish = f"""<div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body small">Publish</span>
                        <input type="datetime-local" form="editForm" name="published_at" class="form-control form-control-sm w-auto" value="{val_publish}" style="max-width: 150px;">
                      </div>"""
    
    match = re.search(publish_pattern, content, flags=re.DOTALL)
    if match: content = content.replace(match.group(0), new_publish)

    # 3. Fix the Status field
    status_pattern = r'<div class="d-flex justify-content-between align-items-start mb-3">\s*<span class="text-body small">Status</span>\s*<a href="#" class="text-decoration-none small d-flex align-items-center gap-1"><i class="fi fi-rr-circle-small text-primary"></i> Draft</a>\s*</div>'
    
    sel_draft = "{{ $page->status == 'draft' ? 'selected' : '' }}" if is_edit else ""
    sel_pub = "{{ $page->status == 'published' ? 'selected' : '' }}" if is_edit else ""
    
    new_status = f"""<div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body small">Status</span>
                        <select form="editForm" name="status" class="form-select form-select-sm w-auto" style="max-width: 120px;">
                            <option value="draft" {sel_draft}>Draft</option>
                            <option value="published" {sel_pub}>Published</option>
                        </select>
                      </div>"""
    
    match = re.search(status_pattern, content, flags=re.DOTALL)
    if match: content = content.replace(match.group(0), new_status)

    # 4. Fix Slug field
    slug_pattern = r'<div class="d-flex justify-content-between align-items-start mb-3">\s*<span class="text-body small">Slug</span>\s*<a href="#" class="text-decoration-none small">404605</a>\s*</div>'
    
    val_slug = "{{ $page->slug }}" if is_edit else ""
    new_slug = f"""<div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body small">Slug</span>
                        <input type="text" form="editForm" name="slug" class="form-control form-control-sm w-auto" value="{val_slug}" placeholder="auto-generated" style="max-width: 120px;">
                      </div>"""
    
    match = re.search(slug_pattern, content, flags=re.DOTALL)
    if match: content = content.replace(match.group(0), new_slug)

    # 5. Fix Author field (just making it static for now, or simple select)
    author_pattern = r'<div class="d-flex justify-content-between align-items-start mb-3">\s*<span class="text-body small">Author</span>\s*<a href="#" class="text-decoration-none small text-end" style="max-width: 150px; line-height: 1.2;">Editorial team -<br>Daily Life Pulse</a>\s*</div>'
    
    new_author = f"""<div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-body small">Author</span>
                        <select form="editForm" name="author_id" class="form-select form-select-sm w-auto" style="max-width: 120px;">
                            <option value="1">Admin User</option>
                        </select>
                      </div>"""
    
    match = re.search(author_pattern, content, flags=re.DOTALL)
    if match: content = content.replace(match.group(0), new_author)

    # 6. Fix Parent field
    parent_pattern = r'<div class="d-flex justify-content-between align-items-start mb-4">\s*<span class="text-body small">Parent</span>\s*<a href="#" class="text-decoration-none small">None</a>\s*</div>'
    
    id_cond = "$page->id" if is_edit else "0"
    sel_cond = "{{ $page->parent_id == $p->id ? 'selected' : '' }}" if is_edit else ""
    
    new_parent = f"""<div class="d-flex justify-content-between align-items-center mb-4">
                        <span class="text-body small">Parent</span>
                        <select form="editForm" name="parent_id" class="form-select form-select-sm w-auto" style="max-width: 120px;">
                            <option value="">(no parent)</option>
                            @foreach(\\App\\Models\\Page::where('id', '!=', {id_cond})->get() as $p)
                                <option value="{{{{ $p->id }}}}" {sel_cond}>{{{{ $p->title }}}}</option>
                            @endforeach
                        </select>
                      </div>"""
                      
    match = re.search(parent_pattern, content, flags=re.DOTALL)
    if match: content = content.replace(match.group(0), new_parent)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated {filepath}")

fix_file('resources/views/admin/pages/create.blade.php', False)
fix_file('resources/views/admin/pages/edit.blade.php', True)
