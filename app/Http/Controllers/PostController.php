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

        $posts = $query->orderBy('created_at', 'desc')->paginate(10);
        
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
        ]);
        
        $validated['slug'] = $validated['slug'] ? Str::slug($validated['slug']) : Str::slug($validated['title']);
        $validated['author_id'] = $validated['author_id'] ?? auth()->id();
        $validated['allow_comments'] = $request->boolean('allow_comments');
        
        if ($request->hasFile('featured_image')) {
            $validated['featured_image'] = $request->file('featured_image')->store('posts', 'public');
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
        ]);
        
        $validated['slug'] = $validated['slug'] ? Str::slug($validated['slug']) : Str::slug($validated['title']);
        $validated['allow_comments'] = $request->boolean('allow_comments');
        
        if ($request->hasFile('featured_image')) {
            if ($post->featured_image) {
                \Illuminate\Support\Facades\Storage::disk('public')->delete($post->featured_image);
            }
            $validated['featured_image'] = $request->file('featured_image')->store('posts', 'public');
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
}
