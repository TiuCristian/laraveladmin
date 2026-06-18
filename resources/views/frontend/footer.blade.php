
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
                                $menuLocations = json_decode(\App\Models\Setting::get('menu_locations', '{}'), true);
                                $footerMenuId = $menuLocations['footer'] ?? null;
                                $footerMenu = $footerMenuId ? \App\Models\Menu::find($footerMenuId) : null;
                                
                                $remove_category_base = \App\Models\Setting::where('key', 'remove_category_base')->value('value') == '1';
                                $remove_tag_base = \App\Models\Setting::where('key', 'remove_tag_base')->value('value') == '1';
                                $category_base = \App\Models\Setting::where('key', 'category_base')->value('value') ?: 'category';
                                $tag_base = \App\Models\Setting::where('key', 'tag_base')->value('value') ?: 'tag';
                            @endphp
                            @if($footerMenu && $footerMenu->items)
                                <ul class="list-inline mb-0">
                                    @foreach($footerMenu->items as $item)
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
                                        <li class="list-inline-item"><a href="{{ $url }}" style="color: #8f9bad;">{{ $item['title'] }}</a></li>
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
