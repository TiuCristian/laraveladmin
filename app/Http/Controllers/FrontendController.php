<?php

namespace App\Http\Controllers;

use App\Models\Post;
use App\Models\Page;
use App\Models\Category;
use App\Models\Tag;
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
                    if ($page->template && view()->exists($page->template)) {
                        return view($page->template, compact('page'));
                    }
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

    public function category($slug)
    {
        $category = Category::where('slug', $slug)->firstOrFail();
        $posts_per_page = \App\Models\Setting::where('key', 'posts_per_page')->value('value') ?? 10;
        
        $posts = $category->posts()->where('status', 'published')->latest()->paginate($posts_per_page);

        return view()->exists('frontend.category') ? view('frontend.category', compact('category', 'posts')) : view('frontend.index', compact('category', 'posts'));
    }

    public function tag($slug)
    {
        $tag = Tag::where('slug', $slug)->firstOrFail();
        $posts_per_page = \App\Models\Setting::where('key', 'posts_per_page')->value('value') ?? 10;
        
        $posts = $tag->posts()->where('status', 'published')->latest()->paginate($posts_per_page);

        return view()->exists('frontend.tag') ? view('frontend.tag', compact('tag', 'posts')) : view('frontend.index', compact('tag', 'posts'));
    }

    public function page($slug)
    {
        $page = Page::where('slug', $slug)->first();

        if ($page) {
            $page_for_posts = \App\Models\Setting::where('key', 'page_for_posts')->value('value');
            if ($page_for_posts == $page->id) {
                $posts_per_page = \App\Models\Setting::where('key', 'posts_per_page')->value('value') ?? 10;
                $posts = Post::where('status', 'published')->latest()->paginate($posts_per_page);
                
                return view('frontend.index', compact('page', 'posts'));
            }

            if ($page->template && view()->exists($page->template)) {
                return view($page->template, compact('page'));
            }

            return view('frontend.page', compact('page'));
        }

        // Fallback: If no page is found, check if it's a Category or Tag.
        // This allows omitting the 'category' or 'tag' prefix in the URL.
        $remove_category_base = \App\Models\Setting::where('key', 'remove_category_base')->value('value');
        if ($remove_category_base == '1') {
            $category = Category::where('slug', $slug)->first();
            if ($category) {
                return $this->category($slug);
            }
        }

        $remove_tag_base = \App\Models\Setting::where('key', 'remove_tag_base')->value('value');
        if ($remove_tag_base == '1') {
            $tag = Tag::where('slug', $slug)->first();
            if ($tag) {
                return $this->tag($slug);
            }
        }

        abort(404);
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
