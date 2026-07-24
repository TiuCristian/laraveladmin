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
        $this->syncStorageFilesIntoMediaTable();

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

        if ($request->expectsJson() || $request->ajax()) {
            return response()->json([
                'success' => true,
                'mediaItems' => $mediaItems,
                'dates' => $dates
            ]);
        }

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

        // Dimensions check for images
        $dimensions = null;
        if (str_starts_with($file->getMimeType(), 'image/')) {
            $fullPath = storage_path('app/public/' . $path);
            if (file_exists($fullPath)) {
                $imgSize = @getimagesize($fullPath);
                if ($imgSize) {
                    $dimensions = $imgSize[0] . ' by ' . $imgSize[1] . ' pixels';
                }
            }
        }

        $filename = basename($path);
        $title = pathinfo($file->getClientOriginalName(), PATHINFO_FILENAME);

        $media = Media::create([
            'user_id' => auth()->id(),
            'filename' => $filename,
            'filepath' => $path,
            'url' => Storage::url($path),
            'mime_type' => $file->getMimeType(),
            'size' => $file->getSize(),
            'title' => $title,
            'dimensions' => $dimensions,
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
        $media = Media::find($id);
        if (!$media) {
            return response()->json(['success' => false, 'message' => 'Media not found'], 404);
        }
        
        $request->validate([
            'alt_text' => 'nullable|string|max:255',
            'title' => 'nullable|string|max:255',
            'caption' => 'nullable|string',
            'description' => 'nullable|string',
        ]);

        $media->update([
            'alt_text' => $request->input('alt_text', ''),
            'title' => $request->input('title', ''),
            'caption' => $request->input('caption', ''),
            'description' => $request->input('description', ''),
        ]);

        return response()->json([
            'success' => true,
            'media' => $media
        ]);
    }

    public function destroy($id)
    {
        try {
            $media = Media::find($id);
            if ($media) {
                $filename = $media->filename;
                $cleanPath = str_replace('\\', '/', $media->filepath);
                
                Storage::disk('public')->delete($cleanPath);
                Storage::disk('public')->delete(ltrim($cleanPath, '/'));
                Storage::disk('public')->delete('posts/' . $filename);
                Storage::disk('public')->delete('uploads/' . $filename);

                $media->delete();
            }
        } catch (\Exception $e) {
            // Ignore deletion errors
        }

        return response()->json([
            'success' => true
        ]);
    }

    private function cleanDuplicateMediaRecords()
    {
        try {
            $all = Media::all()->groupBy('filepath');
            foreach ($all as $filepath => $records) {
                if ($records->count() > 1) {
                    $sorted = $records->sortByDesc(function($r) {
                        return (!empty($r->alt_text) ? 100000 : 0) + $r->id;
                    });
                    $keepId = $sorted->first()->id;
                    Media::where('filepath', $filepath)->where('id', '!=', $keepId)->delete();
                }
            }
        } catch (\Exception $e) {}
    }

    private function syncStorageFilesIntoMediaTable()
    {
        try {
            $this->cleanDuplicateMediaRecords();

            $directories = ['uploads', 'posts'];

            foreach ($directories as $dir) {
                if (!Storage::disk('public')->exists($dir)) continue;
                $files = Storage::disk('public')->allFiles($dir);
                foreach ($files as $file) {
                    $cleanPath = str_replace('\\', '/', $file);
                    $filename = basename($cleanPath);

                    $exists = Media::where('filepath', $cleanPath)->exists();

                    if (!$exists) {
                        $mime = Storage::disk('public')->mimeType($file);
                        if (!$mime || $mime === 'application/octet-stream') {
                            $ext = strtolower(pathinfo($file, PATHINFO_EXTENSION));
                            if (in_array($ext, ['jpg', 'jpeg', 'png', 'gif', 'webp', 'svg'])) {
                                $mime = 'image/' . ($ext === 'jpg' ? 'jpeg' : $ext);
                            } else {
                                $mime = 'image/jpeg';
                            }
                        }

                        $size = Storage::disk('public')->size($file);
                        $fullPath = storage_path('app/public/' . str_replace('/', DIRECTORY_SEPARATOR, $cleanPath));
                        $dimensions = null;
                        if (file_exists($fullPath)) {
                            $imgSize = @getimagesize($fullPath);
                            if ($imgSize) {
                                $dimensions = $imgSize[0] . ' by ' . $imgSize[1] . ' pixels';
                            }
                        }

                        Media::create([
                            'user_id' => auth()->id() ?: 1,
                            'filename' => $filename,
                            'filepath' => $cleanPath,
                            'url' => Storage::url($cleanPath),
                            'mime_type' => $mime,
                            'size' => $size ?: 0,
                            'title' => pathinfo($filename, PATHINFO_FILENAME),
                            'dimensions' => $dimensions,
                        ]);
                    }
                }
            }
        } catch (\Exception $e) {
            // Silence sync errors
        }
    }
}
