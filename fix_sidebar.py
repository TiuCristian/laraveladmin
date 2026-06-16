import re

with open('resources/views/admin/dashboard.blade.php', 'r', encoding='utf-8') as f:
    dashboard_html = f.read()

aside_match = re.search(r'<!-- begin::Sidebar Menu -->.*?<!-- end::Sidebar Menu -->', dashboard_html, re.DOTALL)
if aside_match:
    aside_content = aside_match.group(0)
    with open('resources/views/admin/menus/index.blade.php', 'r', encoding='utf-8') as f:
        menu_html = f.read()
    
    # Remove active class from everywhere in the copied aside content
    aside_content = re.sub(r'class="([^"]*)\bactive\b([^"]*)"', r'class="\1\2"', aside_content)
    aside_content = re.sub(r'class="([^"]*)\bcurrent\b([^"]*)"', r'class="\1\2"', aside_content)
    
    # Add active state back to Menus
    aside_content = aside_content.replace('<a class="menu-link " href="{{ route(\'menus.index\') }}">', '<a class="menu-link active" href="{{ route(\'menus.index\') }}">')
    aside_content = aside_content.replace('<li><a href="{{ route(\'menus.index\') }}">Menus</a></li>', '<li class="current"><a href="{{ route(\'menus.index\') }}" class="current">Menus</a></li>')
    
    # Since appearance menu item needs wp-has-current-submenu and wp-menu-open
    # Find Appearance menu item block and add those classes
    # It might be simpler to just apply active to the links.
    
    new_html = re.sub(r'<!-- begin::Sidebar Menu -->.*?<!-- end::Sidebar Menu -->', aside_content, menu_html, flags=re.DOTALL)
    
    with open('resources/views/admin/menus/index.blade.php', 'w', encoding='utf-8') as f:
        f.write(new_html)
