<?php

namespace App\Http\Controllers;

use App\Models\Post;
use Illuminate\Http\Request;
use Illuminate\Support\Str;

class PostController extends Controller
{
    public function index(Request $request)
    {
        $query = Post::query();
        
        $filter = $request->query('filter', 'all');
        if ($filter === 'published') {
            $query->where('status', 'published');
        } elseif ($filter === 'draft') {
            $query->where('status', 'draft');
        } elseif ($filter === 'trash') {
            $query->onlyTrashed();
        }

        if ($request->has('search') && $request->search != '') {
            $search = $request->search;
            $query->where(function($q) use ($search) {
                $q->where('title', 'LIKE', "%{$search}%")
                  ->orWhere('content', 'LIKE', "%{$search}%");
            });
        }

        $perPage = (int) $request->cookie('posts_per_page', 20);
        $posts = $query->orderBy('created_at', 'desc')->paginate($perPage > 0 ? $perPage : 20);
        
        $counts = [
            'all' => Post::count(),
            'published' => Post::where('status', 'published')->count(),
            'draft' => Post::where('status', 'draft')->count(),
            'trash' => Post::onlyTrashed()->count(),
        ];
        
        return view('admin.posts.index', compact('posts', 'counts', 'filter'));
    }

    public function create()
    {
        return view('admin.posts.create');
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'nullable|string',
            'status' => 'required|string|in:draft,published',
            'slug' => 'nullable|string|max:255',
            'excerpt' => 'nullable|string',
            'author_id' => 'nullable|exists:users,id',
            'allow_comments' => 'nullable|boolean',
            'seo_title' => 'nullable|string|max:255',
            'seo_description' => 'nullable|string',
            'focus_keyword' => 'nullable|string|max:255',
            'is_pillar' => 'nullable|boolean',
            'seo_score' => 'nullable|integer|min:0|max:100',
            'featured_image' => 'nullable',
        ]);
        
        $validated['slug'] = $validated['slug'] ? Str::slug($validated['slug']) : Str::slug($validated['title']);
        $validated['author_id'] = $validated['author_id'] ?? auth()->id();
        $validated['allow_comments'] = $request->boolean('allow_comments');
        $validated['is_pillar'] = $request->boolean('is_pillar');
        $validated['seo_score'] = (int) $request->input('seo_score', 0);
        
        if ($request->hasFile('featured_image')) {
            $validated['featured_image'] = $request->file('featured_image')->store('posts', 'public');
        } elseif ($request->filled('featured_image') && is_string($request->input('featured_image'))) {
            $path = preg_replace('/^\/?storage\//', '', $request->input('featured_image'));
            $validated['featured_image'] = ltrim($path, '/');
        }

        if (!empty($validated['featured_image'])) {
            $this->ensureMediaRecordExists($validated['featured_image']);
        }

        $post = Post::create($validated);
        
        if ($request->has('categories')) {
            $post->categories()->sync($request->categories);
        }
        
        if ($request->has('tags')) {
            $tagIds = [];
            foreach ($request->tags as $tagName) {
                $tagName = trim($tagName);
                if (!empty($tagName)) {
                    $tag = \App\Models\Tag::firstOrCreate(
                        ['name' => $tagName],
                        ['slug' => Str::slug($tagName)]
                    );
                    $tagIds[] = $tag->id;
                }
            }
            $post->tags()->sync($tagIds);
        }
        return redirect()->route('posts.edit', $post)->with('success', 'Post created.');
    }

    public function edit(Post $post)
    {
        if ($post->featured_image) {
            $this->ensureMediaRecordExists($post->featured_image);
        }
        return view('admin.posts.edit', compact('post'));
    }

    public function update(Request $request, Post $post)
    {
        $validated = $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'nullable|string',
            'status' => 'required|string|in:draft,published',
            'slug' => 'nullable|string|max:255',
            'excerpt' => 'nullable|string',
            'author_id' => 'nullable|exists:users,id',
            'allow_comments' => 'nullable|boolean',
            'seo_title' => 'nullable|string|max:255',
            'seo_description' => 'nullable|string',
            'focus_keyword' => 'nullable|string|max:255',
            'is_pillar' => 'nullable|boolean',
            'seo_score' => 'nullable|integer|min:0|max:100',
            'featured_image' => 'nullable',
        ]);
        
        $validated['slug'] = $validated['slug'] ? Str::slug($validated['slug']) : Str::slug($validated['title']);
        $validated['allow_comments'] = $request->boolean('allow_comments');
        $validated['is_pillar'] = $request->boolean('is_pillar');
        $validated['seo_score'] = (int) $request->input('seo_score', 0);
        
        if ($request->hasFile('featured_image')) {
            if ($post->featured_image) {
                \Illuminate\Support\Facades\Storage::disk('public')->delete($post->featured_image);
            }
            $validated['featured_image'] = $request->file('featured_image')->store('posts', 'public');
        } elseif ($request->has('featured_image') && is_string($request->input('featured_image'))) {
            $path = preg_replace('/^\/?storage\//', '', $request->input('featured_image'));
            $validated['featured_image'] = ltrim($path, '/');
        }

        if (!empty($validated['featured_image'])) {
            $this->ensureMediaRecordExists($validated['featured_image']);
        }
        
        $post->update($validated);
        
        if ($request->has('categories')) {
            $post->categories()->sync($request->categories);
        } else {
            $post->categories()->detach();
        }
        
        if ($request->has('tags')) {
            $tagIds = [];
            foreach ($request->tags as $tagName) {
                $tagName = trim($tagName);
                if (!empty($tagName)) {
                    $tag = \App\Models\Tag::firstOrCreate(
                        ['name' => $tagName],
                        ['slug' => Str::slug($tagName)]
                    );
                    $tagIds[] = $tag->id;
                }
            }
            $post->tags()->sync($tagIds);
        } else {
            $post->tags()->detach();
        }
        return redirect()->route('posts.edit', $post)->with('success', 'Post updated.');
    }

    public function checkFocusKeyword(Request $request)
    {
        $keyword = trim($request->input('keyword', ''));
        $postId = $request->input('post_id');

        if (empty($keyword)) {
            return response()->json(['used' => false]);
        }

        $exists = Post::where('focus_keyword', 'LIKE', $keyword)
            ->when($postId, function ($q) use ($postId) {
                return $q->where('id', '!=', $postId);
            })
            ->exists();

        return response()->json(['used' => $exists]);
    }

    public function destroy(Post $post)
    {
        $post->delete();
        return redirect()->route('posts.index')->with('success', 'Post deleted.');
    }

    public function bulk(Request $request)
    {
        $request->validate([
            'action' => 'required|string',
            'post_ids' => 'required|array',
            'post_ids.*' => 'exists:posts,id'
        ]);

        $action = $request->input('action');
        $ids = $request->input('post_ids');

        if ($action === 'trash') {
            Post::whereIn('id', $ids)->delete();
            return back()->with('success', 'Selected posts moved to trash.');
        } elseif ($action === 'restore') {
            Post::withTrashed()->whereIn('id', $ids)->restore();
            return back()->with('success', 'Selected posts restored.');
        } elseif ($action === 'force_delete') {
            Post::withTrashed()->whereIn('id', $ids)->forceDelete();
            return back()->with('success', 'Selected posts permanently deleted.');
        }

        return back();
    }

    public function restore($id)
    {
        $post = Post::withTrashed()->findOrFail($id);
        $post->restore();
        return redirect()->route('posts.index')->with('success', 'Post restored.');
    }

    public function forceDelete($id)
    {
        $post = Post::withTrashed()->findOrFail($id);
        $post->forceDelete();
        return redirect()->route('posts.index', ['filter' => 'trash'])->with('success', 'Post permanently deleted.');
    }

    private function ensureMediaRecordExists(?string $filepath)
    {
        if (empty($filepath)) return null;
        $filepath = str_replace('\\', '/', ltrim(preg_replace('/^\/?storage\//', '', $filepath), '/'));
        $filename = basename($filepath);
        
        $media = \App\Models\Media::where('filename', $filename)->first();

        if (!$media) {
            $fullPath = storage_path('app/public/' . str_replace('/', DIRECTORY_SEPARATOR, $filepath));
            $mime = 'image/jpeg';
            $size = 0;
            $dimensions = null;
            
            if (file_exists($fullPath)) {
                $mime = @mime_content_type($fullPath) ?: 'image/jpeg';
                $size = @filesize($fullPath) ?: 0;
                $imgSize = @getimagesize($fullPath);
                if ($imgSize) {
                    $dimensions = $imgSize[0] . ' by ' . $imgSize[1] . ' pixels';
                }
            }

            $media = \App\Models\Media::create([
                'user_id' => auth()->id(),
                'filename' => basename($filepath),
                'filepath' => $filepath,
                'url' => \Illuminate\Support\Facades\Storage::url($filepath),
                'mime_type' => $mime,
                'size' => $size,
                'title' => pathinfo(basename($filepath), PATHINFO_FILENAME),
                'dimensions' => $dimensions,
            ]);
        }
        return $media;
    }
}
