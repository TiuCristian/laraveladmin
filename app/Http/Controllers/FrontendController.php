<?php

namespace App\Http\Controllers;

use App\Models\Post;
use App\Models\Page;
use Illuminate\Http\Request;

class FrontendController extends Controller
{
    public function index()
    {
        $homepage_display = \App\Models\Setting::where('key', 'homepage_display')->value('value');
        
        if ($homepage_display === 'static') {
            $page_on_front = \App\Models\Setting::where('key', 'page_on_front')->value('value');
            if ($page_on_front) {
                $page = \App\Models\Page::find($page_on_front);
                if ($page && $page->status === 'published') {
                    return view('frontend.page', compact('page'));
                }
            }
        }

        // Fallback to latest posts or if homepage_display is 'latest'
        $posts_per_page = \App\Models\Setting::where('key', 'posts_per_page')->value('value') ?? 10;
        $posts = Post::where('status', 'published')->latest()->paginate($posts_per_page);
        
        // Ensure you have an index view that lists posts
        // For now, if index view doesn't handle posts well, it can still just return the view.
        return view()->exists('frontend.index') ? view('frontend.index', compact('posts')) : view('welcome');
    }

    public function post($category, $slug)
    {
        $post = Post::where('slug', $slug)->firstOrFail();
        return view('frontend.post', compact('post'));
    }

    public function page($slug)
    {
        $page = Page::where('slug', $slug)->firstOrFail();
        return view('frontend.page', compact('page'));
    }

    public function storeComment(Request $request)
    {
        $request->validate([
            'post_id' => 'nullable|exists:posts,id',
            'page_id' => 'nullable|exists:pages,id',
            'name' => 'required|string|max:255',
            'email' => 'required|email|max:255',
            'website' => 'nullable|url|max:255',
            'content' => 'required|string',
        ]);

        if (!$request->post_id && !$request->page_id) {
            return back()->with('error', 'Invalid comment target.');
        }

        // Determine status based on settings
        $status = 'pending';
        if (\App\Models\Setting::get('comment_moderation') != '1') {
            $status = 'approved';
        }

        \App\Models\Comment::create([
            'post_id' => $request->post_id,
            'page_id' => $request->page_id,
            'name' => $request->name,
            'email' => $request->email,
            'website' => $request->website,
            'content' => $request->content,
            'status' => $status,
        ]);

        $message = $status === 'approved' ? 'Comment submitted successfully.' : 'Comment submitted and is awaiting moderation.';

        return back()->with('success', $message);
    }
}
