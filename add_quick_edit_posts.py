import os
import re

file_path = r'c:\laragon\www\LaravelAdmin\resources\views\admin\posts\index.blade.php'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the normal row to have <tr id="row{{ $post->id }}">
# Look for <tr> directly under @foreach
content = content.replace('                <tr>\n                  <td class="ps-3', '                <tr id="row{{ $post->id }}">\n                  <td class="ps-3')

# 2. Add the Quick Edit link next to Edit
quick_edit_link = """<a href="{{ route('posts.edit', $post) }}" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                        <a href="javascript:void(0);" onclick="document.getElementById('row{{ $post->id }}').classList.add('d-none'); document.getElementById('quickEditRow{{ $post->id }}').classList.remove('d-none');" class="text-decoration-none text-primary hover-primary">Quick Edit</a> <span class="text-light">|</span> """

content = content.replace("""<a href="{{ route('posts.edit', $post) }}" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> """, quick_edit_link)

# 3. Add the Quick Edit Row right before @endforeach
quick_edit_row = """
                <!-- Quick Edit Row -->
                <tr id="quickEditRow{{ $post->id }}" class="d-none bg-body-tertiary">
                  <td colspan="7" class="p-4 border-bottom">
                    <form action="{{ route('posts.update', $post->id) }}" method="POST">
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
                              <input type="text" name="title" class="form-control form-control-sm" value="{{ $post->title }}" required>
                            </div>
                          </div>
                          <div class="row mb-2 align-items-center">
                            <label class="col-sm-3 col-form-label small text-body">Slug</label>
                            <div class="col-sm-9">
                              <input type="text" name="slug" class="form-control form-control-sm" value="{{ $post->slug }}">
                            </div>
                          </div>
                          <div class="row mb-2 align-items-center">
                            <label class="col-sm-3 col-form-label small text-body">Date</label>
                            <div class="col-sm-9">
                              <input type="datetime-local" name="published_at" class="form-control form-control-sm" value="{{ $post->published_at ? \\Carbon\\Carbon::parse($post->published_at)->format('Y-m-d\\TH:i') : '' }}">
                            </div>
                          </div>
                        </div>
                        <!-- Right Column -->
                        <div class="col-md-6">
                          <div class="row mb-3 align-items-center">
                            <label class="col-sm-3 col-form-label small text-body">Status</label>
                            <div class="col-sm-9">
                              <select name="status" class="form-select form-select-sm" style="width: auto;">
                                <option value="published" {{ $post->status === 'published' ? 'selected' : '' }}>Published</option>
                                <option value="draft" {{ $post->status === 'draft' ? 'selected' : '' }}>Draft</option>
                              </select>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="mt-4 pt-3 border-top">
                        <button type="submit" class="btn btn-sm btn-primary px-3 me-1">Update</button>
                        <button type="button" class="btn btn-sm btn-outline-secondary px-3" onclick="document.getElementById('quickEditRow{{ $post->id }}').classList.add('d-none'); document.getElementById('row{{ $post->id }}').classList.remove('d-none');">Cancel</button>
                      </div>
                    </form>
                  </td>
                </tr>
                @endforeach"""

content = content.replace('                @endforeach', quick_edit_row)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Quick Edit added to posts/index.blade.php")
