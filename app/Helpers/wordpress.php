<?php

if (!function_exists('get_header')) {
    function get_header($name = null) {
        $view = 'frontend.header' . ($name ? "-{$name}" : '');
        if (view()->exists($view)) {
            echo view($view)->render();
        } else {
            // Fallback header
            echo '<!DOCTYPE html><html><head><title>LaravelAdmin CMS</title></head><body>';
        }
    }
}

if (!function_exists('get_footer')) {
    function get_footer($name = null) {
        $view = 'frontend.footer' . ($name ? "-{$name}" : '');
        if (view()->exists($view)) {
            echo view($view)->render();
        } else {
            // Fallback footer
            echo '</body></html>';
        }
    }
}

if (!function_exists('get_sidebar')) {
    function get_sidebar($name = null) {
        $view = 'frontend.sidebar' . ($name ? "-{$name}" : '');
        if (view()->exists($view)) {
            echo view($view)->render();
        }
    }
}

if (!function_exists('get_template_directory_uri')) {
    function get_template_directory_uri() {
        // In Laravel, assets are usually in the public directory
        return url('/');
    }
}

if (!function_exists('the_content')) {
    function the_content() {
        // Retrieve the global $page or $post if available
        $page = request()->route('page');
        if (is_string($page)) {
             $page = \App\Models\Page::where('slug', $page)->first();
        }
        if (!$page) {
            $post = request()->route('post') ?? request()->route('slug');
            if (is_string($post)) {
                 $post = \App\Models\Post::where('slug', $post)->first();
            }
            if ($post instanceof \App\Models\Post) {
                echo $post->content;
                return;
            }
        }
        
        if ($page instanceof \App\Models\Page) {
            echo $page->content;
        }
    }
}
