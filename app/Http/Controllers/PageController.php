<?php

namespace App\Http\Controllers;

use App\Models\Page;
use Illuminate\Http\Request;
use Illuminate\Support\Str;

class PageController extends Controller
{
    public function index(Request $request)
    {
        $query = Page::query();
        
        $filter = $request->query('filter', 'all');
        if ($filter === 'published') {
            $query->where('status', 'published');
        } elseif ($filter === 'draft') {
            $query->where('status', 'draft');
        } elseif ($filter === 'pillar') {
            $query->where('is_pillar', true);
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

        $pages = $query->orderBy('created_at', 'desc')->paginate(10);
        
        $counts = [
            'all' => Page::count(),
            'published' => Page::where('status', 'published')->count(),
            'pillar' => Page::where('is_pillar', true)->count(),
            'trash' => Page::onlyTrashed()->count(),
        ];
        
        return view('admin.pages.index', compact('pages', 'counts', 'filter'));
    }

    public function create()
    {
        $templates = Page::getAvailableTemplates();
        return view('admin.pages.create', compact('templates'));
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'nullable|string',
            'status' => 'nullable|string|in:draft,published',
            'published_at' => 'nullable|date',
            'slug' => 'nullable|string|max:255',
            'parent_id' => 'nullable|exists:pages,id',
            'author_id' => 'nullable|exists:users,id',
            'is_pillar' => 'nullable|boolean',
            'allow_comments' => 'nullable|boolean',
            'template' => 'nullable|string|max:255',
        ]);
        
        if (empty($validated['slug'])) {
            $validated['slug'] = Str::slug($validated['title']);
        }
        if (empty($validated['author_id'])) {
            $validated['author_id'] = auth()->id() ?? 1;
        }
        
        $validated['is_pillar'] = $request->has('is_pillar');
        $validated['allow_comments'] = $request->boolean('allow_comments');
        $page = Page::create($validated);
        return redirect()->route('pages.edit', $page)->with('success', 'Page created.');
    }

    public function edit(Page $page)
    {
        $templates = Page::getAvailableTemplates();
        return view('admin.pages.edit', compact('page', 'templates'));
    }

    public function update(Request $request, Page $page)
    {
        $validated = $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'nullable|string',
            'status' => 'nullable|string|in:draft,published',
            'published_at' => 'nullable|date',
            'slug' => 'nullable|string|max:255',
            'parent_id' => 'nullable|exists:pages,id',
            'author_id' => 'nullable|exists:users,id',
            'is_pillar' => 'nullable|boolean',
            'allow_comments' => 'nullable|boolean',
            'template' => 'nullable|string|max:255',
        ]);
        
        if (empty($validated['slug'])) {
            $validated['slug'] = Str::slug($validated['title']);
        }
        
        $validated['is_pillar'] = $request->has('is_pillar');
        $validated['allow_comments'] = $request->boolean('allow_comments');
        $page->update($validated);
        return redirect()->route('pages.edit', $page)->with('success', 'Page updated.');
    }

    public function destroy(Page $page)
    {
        $page->delete();
        return redirect()->route('pages.index')->with('success', 'Page moved to trash.');
    }

    public function restore($id)
    {
        Page::withTrashed()->findOrFail($id)->restore();
        return redirect()->route('pages.index', ['filter' => 'trash'])->with('success', 'Page restored.');
    }

    public function forceDelete($id)
    {
        Page::withTrashed()->findOrFail($id)->forceDelete();
        return redirect()->route('pages.index', ['filter' => 'trash'])->with('success', 'Page permanently deleted.');
    }

    public function bulk(Request $request)
    {
        $request->validate([
            'action' => 'required|string',
            'page_ids' => 'required|array',
            'page_ids.*' => 'exists:pages,id'
        ]);

        $action = $request->input('action');
        $ids = $request->input('page_ids');

        if ($action === 'trash') {
            Page::whereIn('id', $ids)->delete();
            return back()->with('success', 'Selected pages moved to trash.');
        } elseif ($action === 'restore') {
            Page::withTrashed()->whereIn('id', $ids)->restore();
            return back()->with('success', 'Selected pages restored.');
        } elseif ($action === 'force_delete') {
            Page::withTrashed()->whereIn('id', $ids)->forceDelete();
            return back()->with('success', 'Selected pages permanently deleted.');
        }

        return back();
    }
}
