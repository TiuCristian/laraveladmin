import os
import re

def update_posts_index():
    path = 'resources/views/admin/posts/index.blade.php'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find tbody and replace it with dynamic loop
    tbody_start = content.find('<tbody>')
    tbody_end = content.find('</tbody>')
    
    if tbody_start != -1 and tbody_end != -1:
        new_tbody = """<tbody>
                @foreach($posts as $post)
                <tr id="postRow{{ $post->id }}">
                  <td class="ps-3 align-top pt-3">
                    <input class="form-check-input" type="checkbox" name="post_ids[]" value="{{ $post->id }}">
                  </td>
                  <td class="align-top pt-3" style="width: 35%;">
                    <a href="{{ route('posts.edit', $post) }}" class="fw-bold text-body text-decoration-none">{{ $post->title }} <span class="fw-normal text-muted">&mdash; {{ ucfirst($post->status) }}</span></a>
                    <div class="small mt-1 text-muted" style="font-size: 0.8rem;">
                      <a href="{{ route('posts.edit', $post) }}" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                      <form action="{{ route('posts.destroy', $post) }}" method="POST" class="d-inline">
                        @csrf
                        @method('DELETE')
                        <button type="submit" class="btn btn-link p-0 m-0 align-baseline text-decoration-none text-danger hover-danger" style="font-size: 0.8rem;" onclick="return confirm('Are you sure?')">Trash</button>
                      </form>
                    </div>
                  </td>
                  <td class="align-top pt-3">
                    @forelse($post->categories as $category)
                      <a href="#" class="text-decoration-none text-primary small">{{ $category->name }}</a>{{ !$loop->last ? ', ' : '' }}
                    @empty
                      <span class="text-muted small">&mdash;</span>
                    @endforelse
                  </td>
                  <td class="align-top pt-3">
                    @forelse($post->tags as $tag)
                      <a href="#" class="text-decoration-none text-primary small">{{ $tag->name }}</a>{{ !$loop->last ? ', ' : '' }}
                    @empty
                      <span class="text-muted small">&mdash;</span>
                    @endforelse
                  </td>
                  <td class="text-center align-top pt-3">
                    <span class="text-muted">&mdash;</span>
                  </td>
                  <td class="align-top pt-3" style="width: 15%;">
                    <span class="d-block text-body small">Published</span>
                    <span class="text-muted small">{{ $post->created_at->format('Y/m/d \a\\t g:i a') }}</span>
                  </td>
                  <td class="pe-3 align-top pt-3" style="width: 25%;">
                    <div class="small text-muted d-flex align-items-center gap-3">
                      <span><strong>Links:</strong> <i class="fi fi-rr-link ms-1"></i> 0</span>
                    </div>
                  </td>
                </tr>
                @endforeach
                """
        
        content = content[:tbody_start] + new_tbody + content[tbody_end:]
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
            print("Updated posts/index.blade.php")

def update_pages_index():
    path = 'resources/views/admin/pages/index.blade.php'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    tbody_start = content.find('<tbody>')
    tbody_end = content.find('</tbody>')
    
    if tbody_start != -1 and tbody_end != -1:
        new_tbody = """<tbody>
                @foreach($pages as $page)
                <tr id="pageRow{{ $page->id }}">
                  <td class="ps-3 align-top pt-3">
                    <input class="form-check-input" type="checkbox" name="page_ids[]" value="{{ $page->id }}">
                  </td>
                  <td class="align-top pt-3" style="width: 35%;">
                    <a href="{{ route('pages.edit', $page) }}" class="fw-bold text-body text-decoration-none">{{ $page->title }} <span class="fw-normal text-muted">&mdash; {{ ucfirst($page->status) }}</span></a>
                    <div class="small mt-1 text-muted" style="font-size: 0.8rem;">
                      <a href="{{ route('pages.edit', $page) }}" class="text-decoration-none text-primary hover-primary">Edit</a> <span class="text-light">|</span> 
                      <form action="{{ route('pages.destroy', $page) }}" method="POST" class="d-inline">
                        @csrf
                        @method('DELETE')
                        <button type="submit" class="btn btn-link p-0 m-0 align-baseline text-decoration-none text-danger hover-danger" style="font-size: 0.8rem;" onclick="return confirm('Are you sure?')">Trash</button>
                      </form>
                    </div>
                  </td>
                  <td class="text-center align-top pt-3">
                    <span class="text-muted">&mdash;</span>
                  </td>
                  <td class="align-top pt-3" style="width: 15%;">
                    <span class="d-block text-body small">Published</span>
                    <span class="text-muted small">{{ $page->created_at->format('Y/m/d \a\\t g:i a') }}</span>
                  </td>
                </tr>
                @endforeach
                """
        
        content = content[:tbody_start] + new_tbody + content[tbody_end:]
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
            print("Updated pages/index.blade.php")

update_posts_index()
update_pages_index()
