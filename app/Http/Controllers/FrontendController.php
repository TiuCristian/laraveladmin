<?php

namespace App\Http\Controllers;

use App\Models\Post;
use App\Models\Page;
use Illuminate\Http\Request;

class FrontendController extends Controller
{
    public function index()
    {
        return view('frontend.index');
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
}
