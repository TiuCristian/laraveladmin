<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

class UploadController extends Controller
{
    public function uploadImage(Request $request)
    {
        $request->validate([
            'image' => 'required|image|max:5120', // 5MB limit
        ]);

        if ($request->file('image')) {
            $path = $request->file('image')->store('uploads/editor', 'public');

            return response()->json([
                'success' => 1,
                'file' => [
                    'url' => Storage::url($path),
                ],
            ]);
        }

        return response()->json(['success' => 0]);
    }

    public function fetchUrl(Request $request)
    {
        $url = $request->input('url');
        
        // Basic validation
        if (filter_var($url, FILTER_VALIDATE_URL) === false) {
            return response()->json(['success' => 0]);
        }

        return response()->json([
            'success' => 1,
            'file' => [
                'url' => $url,
            ],
        ]);
    }
}
