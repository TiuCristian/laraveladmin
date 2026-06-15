import os
import re

file_path = r'c:\laragon\www\LaravelAdmin\resources\views\admin\pages\index.blade.php'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the normal row to have <tr id="row{{ $page->id }}">
# We already have <tr id="pageRow{{ $page->id }}">, let's just change it to row{{ $page->id }} for consistency or keep it.
# Let's keep id="row{{ $page->id }}"
content = content.replace('<tr id="pageRow{{ $page->id }}">', '<tr id="row{{ $page->id }}">')

# 2. Add the Quick Edit link next to Edit
quick_edit_link = """<a href="{{ route('pages.edit', $page) }}" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                        <a href="javascript:void(0);" onclick="document.getElementById('row{{ $page->id }}').classList.add('d-none'); document.getElementById('quickEditRow{{ $page->id }}').classList.remove('d-none');" class="text-decoration-none text-primary hover-primary">Quick Edit</a> <span class="text-light">|</span> """

content = content.replace("""<a href="{{ route('pages.edit', $page) }}" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> """, quick_edit_link)

# 3. Add the Quick Edit Row right before @endforeach
quick_edit_row = """
                <!-- Quick Edit Row -->
                <tr id="quickEditRow{{ $page->id }}" class="d-none bg-body-tertiary">
                  <td colspan="6" class="p-4 border-bottom">
                    <form action="{{ route('pages.update', $page->id) }}" method="POST">
                      @csrf
                      @method('PUT')
                      <div class="mb-3">
                        <h6 class="fw-bold small text-uppercase text-muted mb-0">Quick Edit</h6>
                      </div>
                      <div class="row">
                        <!-- Left Column -->
                        <div class="col-md-6 mb-3 mb-md-0">
                          <div class="row mb-2 align-items-center">
                            <label class="col-sm-3 col-form-label small text-body">Title</label>
                            <div class="col-sm-9">
                              <input type="text" name="title" class="form-control form-control-sm" value="{{ $page->title }}" required>
                            </div>
                          </div>
                          <div class="row mb-2 align-items-center">
                            <label class="col-sm-3 col-form-label small text-body">Slug</label>
                            <div class="col-sm-9">
                              <input type="text" name="slug" class="form-control form-control-sm" value="{{ $page->slug }}">
                            </div>
                          </div>
                          <div class="row mb-2 align-items-center">
                            <label class="col-sm-3 col-form-label small text-body">Date</label>
                            <div class="col-sm-9">
                              <input type="datetime-local" name="published_at" class="form-control form-control-sm" value="{{ $page->published_at ? \Carbon\Carbon::parse($page->published_at)->format('Y-m-d\TH:i') : '' }}">
                            </div>
                          </div>
                        </div>
                        <!-- Right Column -->
                        <div class="col-md-6">
                          <div class="row mb-2 align-items-center">
                            <label class="col-sm-3 col-form-label small text-body">Parent</label>
                            <div class="col-sm-9">
                              <select name="parent_id" class="form-select form-select-sm">
                                <option value="">Main Page (no parent)</option>
                                @foreach(\\App\\Models\\Page::where('id', '!=', $page->id)->get() as $p)
                                    <option value="{{ $p->id }}" {{ $page->parent_id == $p->id ? 'selected' : '' }}>{{ $p->title }}</option>
                                @endforeach
                              </select>
                            </div>
                          </div>
                          <div class="row mb-3 align-items-center">
                            <div class="col-sm-9 offset-sm-3">
                              <div class="form-check mb-0">
                                <input class="form-check-input" type="checkbox" name="is_pillar" id="quickIsPillar{{ $page->id }}" value="1" {{ $page->is_pillar ? 'checked' : '' }}>
                                <label class="form-check-label small text-body" for="quickIsPillar{{ $page->id }}">Pillar Content</label>
                              </div>
                            </div>
                          </div>
                          <div class="row align-items-center">
                            <label class="col-sm-3 col-form-label small text-body">Status</label>
                            <div class="col-sm-9">
                              <select name="status" class="form-select form-select-sm" style="width: auto;">
                                <option value="published" {{ $page->status === 'published' ? 'selected' : '' }}>Published</option>
                                <option value="draft" {{ $page->status === 'draft' ? 'selected' : '' }}>Draft</option>
                              </select>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="mt-4 pt-3 border-top">
                        <button type="submit" class="btn btn-sm btn-primary px-3 me-1">Update</button>
                        <button type="button" class="btn btn-sm btn-outline-secondary px-3" onclick="document.getElementById('quickEditRow{{ $page->id }}').classList.add('d-none'); document.getElementById('row{{ $page->id }}').classList.remove('d-none');">Cancel</button>
                      </div>
                    </form>
                  </td>
                </tr>
                @endforeach"""

content = content.replace('                @endforeach', quick_edit_row)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Quick Edit added to pages/index.blade.php")
