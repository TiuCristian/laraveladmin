import os

controllers = {
    'PostController.php': ('Post', 'posts'),
    'PageController.php': ('Page', 'pages'),
}

for ctrl, (model, folder) in controllers.items():
    path = f'app/Http/Controllers/{ctrl}'
    with open(path, 'w') as f:
        f.write(f'''<?php

namespace App\Http\\Controllers;

use App\\Models\\{model};
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Str;

class {ctrl.split(".")[0]} extends Controller
{{
    public function index()
    {{
        ${folder} = {model}::all();
        return view('admin.{folder}.index', compact('{folder}'));
    }}

    public function create()
    {{
        return view('admin.{folder}.create');
    }}

    public function store(Request $request)
    {{
        $validated = $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'nullable|string',
        ]);
        
        $validated['slug'] = Str::slug($validated['title']);
        $validated['author_id'] = auth()->id();
        
        {model}::create($validated);
        return redirect()->route('{folder}.index')->with('success', '{model} created.');
    }}

    public function edit({model} ${model.lower()})
    {{
        return view('admin.{folder}.edit', compact('{model.lower()}'));
    }}

    public function update(Request $request, {model} ${model.lower()})
    {{
        $validated = $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'nullable|string',
        ]);
        
        $validated['slug'] = Str::slug($validated['title']);
        
        ${model.lower()}->update($validated);
        return redirect()->route('{folder}.index')->with('success', '{model} updated.');
    }}

    public function destroy({model} ${model.lower()})
    {{
        ${model.lower()}->delete();
        return redirect()->route('{folder}.index')->with('success', '{model} deleted.');
    }}
}}
''')

# For Category and Tag
controllers_simple = {
    'CategoryController.php': ('Category', 'categories'),
    'TagController.php': ('Tag', 'tags'),
}

for ctrl, (model, folder) in controllers_simple.items():
    path = f'app/Http/Controllers/{ctrl}'
    with open(path, 'w') as f:
        f.write(f'''<?php

namespace App\Http\\Controllers;

use App\\Models\\{model};
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Str;

class {ctrl.split(".")[0]} extends Controller
{{
    public function index()
    {{
        ${folder} = {model}::all();
        return view('admin.{folder}.index', compact('{folder}'));
    }}

    public function store(Request $request)
    {{
        $validated = $request->validate([
            'name' => 'required|string|max:255',
            'description' => 'nullable|string',
        ]);
        
        $validated['slug'] = Str::slug($validated['name']);
        
        {model}::create($validated);
        return redirect()->route('{folder}.index')->with('success', '{model} created.');
    }}

    public function edit({model} ${model.lower()})
    {{
        return view('admin.{folder}.edit', compact('{model.lower()}'));
    }}

    public function update(Request $request, {model} ${model.lower()})
    {{
        $validated = $request->validate([
            'name' => 'required|string|max:255',
            'description' => 'nullable|string',
        ]);
        
        $validated['slug'] = Str::slug($validated['name']);
        
        ${model.lower()}->update($validated);
        return redirect()->route('{folder}.index')->with('success', '{model} updated.');
    }}

    public function destroy({model} ${model.lower()})
    {{
        ${model.lower()}->delete();
        return redirect()->route('{folder}.index')->with('success', '{model} deleted.');
    }}
}}
''')
