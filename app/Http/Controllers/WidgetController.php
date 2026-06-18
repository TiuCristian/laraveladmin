<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Setting;

class WidgetController extends Controller
{
    public function index()
    {
        $sidebarWidgets = Setting::where('key', 'sidebar_widgets')->value('value');
        $widgets = $sidebarWidgets ? json_decode($sidebarWidgets, true) : [];
        
        // Default widgets if empty
        if (empty($widgets)) {
            $widgets = [
                ['type' => 'about_author', 'title' => 'About the Author']
            ];
        }
        
        return view('admin.widgets.index', compact('widgets'));
    }

    public function save(Request $request)
    {
        $widgets = $request->input('widgets');
        
        if (is_string($widgets)) {
            $decoded = json_decode($widgets, true);
            if (is_array($decoded)) {
                Setting::updateOrCreate(
                    ['key' => 'sidebar_widgets'],
                    ['value' => $widgets]
                );
            }
        }

        return redirect()->route('widgets.index')->with('success', 'Widgets saved successfully.');
    }
}
