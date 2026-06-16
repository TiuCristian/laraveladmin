<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Media;
use App\Models\Setting;
use Illuminate\Support\Facades\Storage;

class MediaController extends Controller
{
    public function index(Request $request)
    {
        $query = Media::latest();
        
        // Handle type filter
        if ($request->filled('type')) {
            if ($request->type === 'image') {
                $query->where('mime_type', 'like', 'image/%');
            } elseif ($request->type === 'audio') {
                $query->where('mime_type', 'like', 'audio/%');
            } elseif ($request->type === 'video') {
                $query->where('mime_type', 'like', 'video/%');
            } elseif ($request->type === 'document') {
                $query->where(function($q) {
                    $q->where('mime_type', 'not like', 'image/%')
                      ->where('mime_type', 'not like', 'audio/%')
                      ->where('mime_type', 'not like', 'video/%');
                });
            }
        }

        // Handle date filter
        if ($request->filled('date')) {
            // Expected format YYYY-MM
            $parts = explode('-', $request->date);
            if (count($parts) == 2) {
                $query->whereYear('created_at', $parts[0])
                      ->whereMonth('created_at', $parts[1]);
            }
        }

        // Handle search filter
        if ($request->filled('search')) {
            $s = $request->search;
            $query->where(function($q) use ($s) {
                $q->where('filename', 'like', '%' . $s . '%')
                  ->orWhere('title', 'like', '%' . $s . '%')
                  ->orWhere('alt_text', 'like', '%' . $s . '%')
                  ->orWhere('caption', 'like', '%' . $s . '%')
                  ->orWhere('description', 'like', '%' . $s . '%');
            });
        }

        $mediaItems = $query->paginate(24)->appends($request->all());

        // Get unique months/years for the filter dropdown
        $dates = Media::selectRaw('YEAR(created_at) as year, MONTH(created_at) as month')
                      ->groupBy('year', 'month')
                      ->orderBy('year', 'desc')
                      ->orderBy('month', 'desc')
                      ->get();

        return view('admin.media.index', compact('mediaItems', 'dates'));
    }

    public function create()
    {
        return view('admin.media.create');
    }

    public function store(Request $request)
    {
        $request->validate([
            'file' => 'required|file|max:51200', // 50MB max
        ]);

        $file = $request->file('file');
        
        // Fetch Settings
        $settings = Setting::pluck('value', 'key')->toArray();
        $useFolders = ($settings['uploads_use_yearmonth_folders'] ?? '1') == '1';

        // Folder Path
        $folder = 'uploads';
        if ($useFolders) {
            $folder .= '/' . date('Y/m');
        }

        $path = $file->store($folder, 'public');

        $media = Media::create([
            'user_id' => auth()->id(),
            'filename' => $file->getClientOriginalName(),
            'filepath' => $path,
            'url' => Storage::url($path),
            'mime_type' => $file->getMimeType(),
            'size' => $file->getSize(),
        ]);

        return response()->json([
            'success' => true,
            'media' => $media
        ]);
    }

    public function edit($id)
    {
        $media = Media::findOrFail($id);
        return view('admin.media.edit', compact('media'));
    }

    public function update(Request $request, $id)
    {
        $media = Media::findOrFail($id);
        
        $request->validate([
            'alt_text' => 'nullable|string|max:255',
            'title' => 'nullable|string|max:255',
            'caption' => 'nullable|string',
            'description' => 'nullable|string',
        ]);

        $media->update([
            'alt_text' => $request->alt_text,
            'title' => $request->title,
            'caption' => $request->caption,
            'description' => $request->description,
        ]);

        return redirect()->route('media.edit', $media->id)->with('success', 'Media updated successfully.');
    }

    public function destroy($id)
    {
        $media = Media::findOrFail($id);
        Storage::disk('public')->delete($media->filepath);
        $media->delete();

        return redirect()->route('media.index')->with('success', 'Media item deleted successfully.');
    }
}
