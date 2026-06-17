
        <!-- footer -->
        <footer>
            <div class="container-xl">
                <div class="footer-inner">
                    <div class="row d-flex align-items-center gy-4">
                        <div class="col-md-4">
                            <span class="copyright">© {{ date('Y') }} My Blog. Template by ThemeGer.</span>
                        </div>
                        <div class="col-md-4 text-center">
                            @php
                                $footerMenuId = $menuLocations['footer'] ?? null;
                                $footerMenu = $footerMenuId ? \App\Models\Menu::find($footerMenuId) : null;
                            @endphp
                            @if($footerMenu && $footerMenu->items)
                                <ul class="list-inline mb-0">
                                    @foreach($footerMenu->items as $item)
                                        <li class="list-inline-item"><a href="{{ $item['url'] }}" style="color: #8f9bad;">{{ $item['title'] }}</a></li>
                                    @endforeach
                                </ul>
                            @endif
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
