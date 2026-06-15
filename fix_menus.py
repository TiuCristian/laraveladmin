import glob

files = glob.glob('resources/views/admin/**/*.blade.php', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Fix Dropdown name/role
    content = content.replace(
        '<div class="fw-bold text-dark">Admin User</div>\n                <small class="text-body d-block lh-sm">Administrator</small>',
        '<div class="fw-bold text-dark">{{ auth()->user()->name }}</div>\n                <small class="text-body d-block lh-sm" style="text-transform: capitalize;">{{ auth()->user()->role }}</small>'
    )
    
    # Fix Logout
    content = content.replace(
        '<li><a class="dropdown-item d-flex align-items-center gap-2 text-danger" href="#"><i class="fi fi-sr-exit"></i> Log Out</a></li>',
        '<li><form action="{{ route(\'logout\') }}" method="POST">@csrf<button type="submit" style="background: none; border: none; width: 100%; text-align: left;" class="dropdown-item d-flex align-items-center gap-2 text-danger"><i class="fi fi-sr-exit"></i> Log Out</button></form></li>'
    )
    
    # Fix Sidebar Links
    content = content.replace('href="users-list.html"', 'href="{{ route(\'users.index\') }}"')
    content = content.replace('href="users-add.html"', 'href="{{ route(\'users.create\') }}"')
    content = content.replace('href="users-profile.html"', 'href="{{ route(\'profile.edit\') }}"')
    content = content.replace('href="dashboard.html"', 'href="{{ route(\'admin.dashboard\') }}"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
