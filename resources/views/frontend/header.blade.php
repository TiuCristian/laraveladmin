<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>@yield('title', 'Katen Blog')</title>
    <meta name="description" content="Katen - Minimal Blog & Magazine HTML Theme">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link rel="shortcut icon" type="image/x-icon" href="{{ asset('frontend/images/favicon.png') }}">

    <!-- STYLES -->
    <link rel="stylesheet" href="{{ asset('frontend/css/bootstrap.min.css') }}" type="text/css" media="all">
    <link rel="stylesheet" href="{{ asset('frontend/css/all.min.css') }}" type="text/css" media="all">
    <link rel="stylesheet" href="{{ asset('frontend/css/slick.css') }}" type="text/css" media="all">
    <link rel="stylesheet" href="{{ asset('frontend/css/simple-line-icons.css') }}" type="text/css" media="all">
    <link rel="stylesheet" href="{{ asset('frontend/css/style.css') }}" type="text/css" media="all">
    @stack('styles')
</head>
<body>

    <!-- site wrapper -->
    <div class="site-wrapper">
        <div class="main-overlay"></div>

        <!-- header -->
        <header class="header-default">
            <nav class="navbar navbar-expand-lg">
                <div class="container-xl">
                    <a class="navbar-brand" href="/"><img src="{{ asset('frontend/images/logo.svg') }}" alt="logo" /></a>

                    <div class="collapse navbar-collapse">
                        <!-- menus -->
                        <ul class="navbar-nav mr-auto">
                            @php
                                $menuLocations = json_decode(\App\Models\Setting::get('menu_locations', '{}'), true);
                                $primaryMenuId = $menuLocations['primary'] ?? null;
                                $primaryMenu = $primaryMenuId ? \App\Models\Menu::find($primaryMenuId) : null;
                                
                                $remove_category_base = \App\Models\Setting::where('key', 'remove_category_base')->value('value') == '1';
                                $remove_tag_base = \App\Models\Setting::where('key', 'remove_tag_base')->value('value') == '1';
                                $category_base = \App\Models\Setting::where('key', 'category_base')->value('value') ?: 'category';
                                $tag_base = \App\Models\Setting::where('key', 'tag_base')->value('value') ?: 'tag';
                            @endphp

                            @if($primaryMenu && $primaryMenu->items)
                                @foreach($primaryMenu->items as $item)
                                    @php
                                        $url = $item['url'];
                                        if (isset($item['type'])) {
                                            if ($item['type'] === 'category') {
                                                $slug = trim(basename(parse_url($url, PHP_URL_PATH)), '/');
                                                $url = $remove_category_base ? '/' . $slug : '/' . $category_base . '/' . $slug;
                                            } elseif ($item['type'] === 'tag') {
                                                $slug = trim(basename(parse_url($url, PHP_URL_PATH)), '/');
                                                $url = $remove_tag_base ? '/' . $slug : '/' . $tag_base . '/' . $slug;
                                            }
                                        }
                                    @endphp
                                    <li class="nav-item">
                                        <a class="nav-link" href="{{ $url }}">{{ $item['title'] }}</a>
                                    </li>
                                @endforeach
                            @else
                                <li class="nav-item active">
                                    <a class="nav-link" href="/">Home</a>
                                </li>
                            @endif
                        </ul>
                    </div>

                    <div class="header-right">
                        <div class="header-buttons">
                            <button class="search icon-button">
                                <i class="icon-magnifier"></i>
                            </button>
                            <button class="burger-menu icon-button">
                                <span class="burger-icon"></span>
                            </button>
                        </div>
                    </div>
                </div>
            </nav>
        </header>

        <!-- section main content -->
        <section class="main-content mt-3">
            <div class="container-xl">
