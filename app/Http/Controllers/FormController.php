<?php

namespace App\Http\Controllers;

use App\Models\Form;
use Illuminate\Http\Request;

class FormController extends Controller
{
    public function index(Request $request)
    {
        $filter = $request->query('filter', 'all');
        $forms = Form::latest()->paginate(20);
        
        $counts = [
            'all' => Form::count(),
            'published' => Form::count(),
            'pillar' => 0,
            'trash' => 0,
        ];

        return view('admin.forms.index', compact('forms', 'filter', 'counts'));
    }

    public function create()
    {
        return view('admin.forms.create');
    }

    public function store(Request $request)
    {
        $request->validate([
            'name' => 'required|string|max:255',
            'submit_text' => 'nullable|string|max:255',
        ]);

        $fields = $request->input('fields');
        if (is_string($fields)) {
            $fields = json_decode($fields, true);
        }

        $form = Form::create([
            'name' => $request->name,
            'submit_text' => $request->submit_text ?? 'Submit',
            'fields' => $fields ?? [],
        ]);

        return redirect()->route('forms.edit', $form)->with('success', 'Form created successfully.');
    }

    public function edit(Form $form)
    {
        return view('admin.forms.edit', compact('form'));
    }

    public function update(Request $request, Form $form)
    {
        $request->validate([
            'name' => 'required|string|max:255',
            'submit_text' => 'nullable|string|max:255',
        ]);

        $fields = $request->input('fields');
        if (is_string($fields)) {
            $fields = json_decode($fields, true);
        }

        $form->update([
            'name' => $request->name,
            'submit_text' => $request->submit_text ?? 'Submit',
            'fields' => $fields ?? [],
        ]);

        return redirect()->route('forms.edit', $form)->with('success', 'Form updated successfully.');
    }

    public function destroy(Form $form)
    {
        $form->delete();
        return redirect()->route('forms.index')->with('success', 'Form deleted successfully.');
    }

    public function submit(Request $request, Form $form)
    {
        $data = $request->input('fields', []);
        
        \App\Models\FormSubmission::create([
            'form_id' => $form->id,
            'data' => $data,
            'ip_address' => $request->ip(),
            'user_agent' => $request->userAgent(),
        ]);

        return back()->with('success', 'Thank you! Your submission has been received.');
    }

    public function messages(Request $request)
    {
        $messages = \App\Models\FormSubmission::with('form')->latest()->paginate(20);
        return view('admin.forms.messages', compact('messages'));
    }

    public function editMessage($id)
    {
        $message = \App\Models\FormSubmission::with('form')->findOrFail($id);
        return view('admin.forms.messages_edit', compact('message'));
    }

    public function updateMessage(Request $request, $id)
    {
        $message = \App\Models\FormSubmission::findOrFail($id);
        
        // Since data is dynamic, we just accept the 'data' array
        $data = $request->input('data', []);
        
        $message->update([
            'data' => $data
        ]);

        return redirect()->route('forms.messages')->with('success', 'Message updated successfully.');
    }

    public function destroyMessage($id)
    {
        $message = \App\Models\FormSubmission::findOrFail($id);
        $message->delete();
        return redirect()->back()->with('success', 'Message deleted successfully.');
    }
}
