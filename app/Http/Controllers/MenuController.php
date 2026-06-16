<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Menu;
use App\Models\Page;
use App\Models\Post;
use App\Models\Category;
use App\Models\Setting;

class MenuController extends Controller
{
    public function index(Request $request)
    {
        $menus = Menu::all();
        $pages = Page::latest()->get();
        $posts = Post::latest()->take(15)->get();
        $categories = Category::all();

        $menuId = $request->query('menu');
        $activeMenu = $menuId ? Menu::find($menuId) : $menus->first();
        
        $locations = Setting::get('menu_locations', '{}');
        $locations = json_decode($locations, true) ?? [];

        return view('admin.menus.index', compact('menus', 'activeMenu', 'pages', 'posts', 'categories', 'locations'));
    }

    public function store(Request $request)
    {
        $request->validate([
            'name' => 'required|string|max:255',
        ]);

        $menu = Menu::create([
            'name' => $request->name,
            'items' => [],
            'auto_add_pages' => false,
        ]);

        return redirect()->route('menus.index', ['menu' => $menu->id])->with('success', 'Menu created successfully.');
    }

    public function update(Request $request, $id)
    {
        $menu = Menu::findOrFail($id);

        $request->validate([
            'name' => 'required|string|max:255',
        ]);

        $menu->name = $request->name;
        $menu->auto_add_pages = $request->has('auto_add_pages');
        
        if ($request->has('items')) {
            $menu->items = json_decode($request->items, true);
        }

        $menu->save();

        // Handle locations assignment if passed from edit menu screen
        if ($request->has('locations')) {
            $locations = Setting::get('menu_locations', '{}');
            $locations = json_decode($locations, true) ?? [];
            
            // First, remove this menu from all locations
            foreach ($locations as $loc => $mId) {
                if ($mId == $menu->id) {
                    $locations[$loc] = null;
                }
            }

            // Then assign it to the selected ones
            foreach ($request->locations as $loc) {
                $locations[$loc] = $menu->id;
            }

            Setting::set('menu_locations', json_encode($locations));
        }

        return redirect()->route('menus.index', ['menu' => $menu->id])->with('success', 'Menu updated successfully.');
    }

    public function destroy($id)
    {
        $menu = Menu::findOrFail($id);
        $menu->delete();

        // Also clean up locations
        $locations = Setting::get('menu_locations', '{}');
        $locations = json_decode($locations, true) ?? [];
        $changed = false;
        foreach ($locations as $loc => $mId) {
            if ($mId == $menu->id) {
                $locations[$loc] = null;
                $changed = true;
            }
        }
        if ($changed) {
            Setting::set('menu_locations', json_encode($locations));
        }

        return redirect()->route('menus.index')->with('success', 'Menu deleted successfully.');
    }

    public function locations(Request $request)
    {
        $locationsData = $request->input('locations', []);
        
        $locations = Setting::get('menu_locations', '{}');
        $locations = json_decode($locations, true) ?? [];

        foreach ($locationsData as $loc => $menuId) {
            $locations[$loc] = empty($menuId) ? null : $menuId;
        }

        Setting::set('menu_locations', json_encode($locations));

        return redirect()->route('menus.index', ['tab' => 'manage-locations'])->with('success', 'Locations updated successfully.');
    }
}
