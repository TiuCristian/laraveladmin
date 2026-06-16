<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Comment;

class CommentController extends Controller
{
    public function index(Request $request)
    {
        $query = Comment::query();

        $status = $request->get('status', 'all');
        if ($status !== 'all') {
            $query->where('status', $status);
        }

        if ($search = $request->get('search')) {
            $query->where(function($q) use ($search) {
                $q->where('name', 'like', "%{$search}%")
                  ->orWhere('email', 'like', "%{$search}%")
                  ->orWhere('content', 'like', "%{$search}%");
            });
        }

        $comments = $query->latest()->paginate(20);
        $counts = [
            'all' => Comment::count(),
            'pending' => Comment::where('status', 'pending')->count(),
            'approved' => Comment::where('status', 'approved')->count(),
            'spam' => Comment::where('status', 'spam')->count(),
            'trash' => Comment::where('status', 'trash')->count(),
        ];

        return view('admin.comments.index', compact('comments', 'counts', 'status'));
    }

    public function bulk(Request $request)
    {
        $action = $request->input('action');
        $ids = $request->input('ids', []);

        if (empty($ids) || $action === 'Bulk actions') {
            return back()->with('error', 'Please select an action and at least one comment.');
        }

        switch ($action) {
            case 'Unapprove':
                Comment::whereIn('id', $ids)->update(['status' => 'pending']);
                $msg = 'Comments unapproved successfully.';
                break;
            case 'Approve':
                Comment::whereIn('id', $ids)->update(['status' => 'approved']);
                $msg = 'Comments approved successfully.';
                break;
            case 'Mark as Spam':
                Comment::whereIn('id', $ids)->update(['status' => 'spam']);
                $msg = 'Comments marked as spam.';
                break;
            case 'Move to Trash':
                Comment::whereIn('id', $ids)->update(['status' => 'trash']);
                $msg = 'Comments moved to trash.';
                break;
            case 'Delete Permanently':
                Comment::whereIn('id', $ids)->delete();
                $msg = 'Comments deleted permanently.';
                break;
            default:
                return back()->with('error', 'Invalid action.');
        }

        return back()->with('success', $msg);
    }
}
