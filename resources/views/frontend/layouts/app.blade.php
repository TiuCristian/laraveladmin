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
                            <li class="nav-item active">
                                <a class="nav-link" href="/">Home</a>
                            </li>
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
                @yield('content')
            </div>
        </section>

        <!-- footer -->
        <footer>
            <div class="container-xl">
                <div class="footer-inner">
                    <div class="row d-flex align-items-center gy-4">
                        <div class="col-md-4">
                            <span class="copyright">© {{ date('Y') }} My Blog. Template by ThemeGer.</span>
                        </div>
                        <div class="col-md-4 text-center">
                        </div>
                        <div class="col-md-4">
                            <a href="#" id="return-to-top" class="float-md-end"><i class="icon-arrow-up"></i>Back to Top</a>
                        </div>
                    </div>
                </div>
            </div>
        </footer>

    </div><!-- end site wrapper -->

    <!-- JAVA SCRIPTS -->
    <script src="{{ asset('frontend/js/jquery.min.js') }}"></script>
    <script src="{{ asset('frontend/js/popper.min.js') }}"></script>
    <script src="{{ asset('frontend/js/bootstrap.min.js') }}"></script>
    <script src="{{ asset('frontend/js/slick.min.js') }}"></script>
    <script src="{{ asset('frontend/js/jquery.sticky-sidebar.min.js') }}"></script>
    <script src="{{ asset('frontend/js/custom.js') }}"></script>
    @stack('scripts')
</body>
</html>
