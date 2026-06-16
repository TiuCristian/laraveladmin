<?php

namespace App\Http\Controllers;

use App\Models\Setting;
use Illuminate\Http\Request;

class SettingsController extends Controller
{
    public function general()
    {
        // Load all settings as a key-value array for easy access in view
        $settings = Setting::pluck('value', 'key')->toArray();
        return view('admin.settings.general', compact('settings'));
    }

    public function updateGeneral(Request $request)
    {
        $data = $request->except(['_token']);
        
        foreach ($data as $key => $value) {
            Setting::updateOrCreate(
                ['key' => $key],
                ['value' => is_array($value) ? json_encode($value) : $value]
            );
        }

        return redirect()->route('settings.general')->with('success', 'Settings updated successfully.');
    }

    public function writing()
    {
        $settings = Setting::pluck('value', 'key')->toArray();
        $categories = \App\Models\Category::all();
        return view('admin.settings.writing', compact('settings', 'categories'));
    }

    public function updateWriting(Request $request)
    {
        $data = $request->except(['_token']);
        
        foreach ($data as $key => $value) {
            Setting::updateOrCreate(
                ['key' => $key],
                ['value' => is_array($value) ? json_encode($value) : $value]
            );
        }

        return redirect()->route('settings.writing')->with('success', 'Writing settings updated successfully.');
    }

    public function reading()
    {
        $settings = Setting::pluck('value', 'key')->toArray();
        $pages = \App\Models\Page::all();
        return view('admin.settings.reading', compact('settings', 'pages'));
    }

    public function updateReading(Request $request)
    {
        $data = $request->except(['_token']);
        
        // Handle checkbox explicitly (if not checked, it won't be in $data)
        $data['discourage_search_engines'] = $request->has('discourage_search_engines') ? 1 : 0;
        
        foreach ($data as $key => $value) {
            Setting::updateOrCreate(
                ['key' => $key],
                ['value' => is_array($value) ? json_encode($value) : $value]
            );
        }

        return redirect()->route('settings.reading')->with('success', 'Reading settings updated successfully.');
    }

    public function discussion()
    {
        $settings = Setting::pluck('value', 'key')->toArray();
        return view('admin.settings.discussion', compact('settings'));
    }

    public function updateDiscussion(Request $request)
    {
        $data = $request->except(['_token']);
        
        // Handle checkboxes explicitly
        $checkboxes = [
            'default_pingback_flag',
            'default_ping_status',
            'default_comment_status',
            'require_name_email',
            'comment_registration',
            'close_comments_for_old_posts',
            'show_comments_cookies_opt_in',
            'thread_comments',
            'page_comments',
            'comments_notify',
            'moderation_notify',
            'comment_moderation',
            'comment_previously_approved',
            'show_avatars'
        ];

        foreach ($checkboxes as $checkbox) {
            $data[$checkbox] = $request->has($checkbox) ? 1 : 0;
        }

        foreach ($data as $key => $value) {
            Setting::updateOrCreate(
                ['key' => $key],
                ['value' => is_array($value) ? json_encode($value) : $value]
            );
        }

        return redirect()->route('settings.discussion')->with('success', 'Discussion settings updated successfully.');
    }

    public function media()
    {
        $settings = Setting::pluck('value', 'key')->toArray();
        return view('admin.settings.media', compact('settings'));
    }

    public function updateMedia(Request $request)
    {
        $data = $request->except(['_token']);
        
        // Handle checkboxes explicitly
        $checkboxes = [
            'thumbnail_crop',
            'uploads_use_yearmonth_folders'
        ];

        foreach ($checkboxes as $checkbox) {
            $data[$checkbox] = $request->has($checkbox) ? 1 : 0;
        }

        foreach ($data as $key => $value) {
            Setting::updateOrCreate(
                ['key' => $key],
                ['value' => is_array($value) ? json_encode($value) : $value]
            );
        }

        return redirect()->route('settings.media')->with('success', 'Media settings updated successfully.');
    }

    public function permalinks()
    {
        $settings = Setting::pluck('value', 'key')->toArray();
        return view('admin.settings.permalinks', compact('settings'));
    }

    public function updatePermalinks(Request $request)
    {
        $data = $request->except(['_token']);

        foreach ($data as $key => $value) {
            Setting::updateOrCreate(
                ['key' => $key],
                ['value' => is_array($value) ? json_encode($value) : $value]
            );
        }

        return redirect()->route('settings.permalinks')->with('success', 'Permalink settings updated successfully.');
    }
}
