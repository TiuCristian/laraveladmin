@php
    $sidebarWidgets = \App\Models\Setting::where('key', 'sidebar_widgets')->value('value');
    $widgets = $sidebarWidgets ? json_decode($sidebarWidgets, true) : [];
    
    // Fallback default widget if none exist
    if (empty($widgets)) {
        $widgets = [
            ['type' => 'about_author', 'title' => 'About the Author']
        ];
    }
@endphp

<div class="sidebar">
    @foreach($widgets as $widget)
        <div class="widget rounded">
            <div class="widget-header text-center">
                <h3 class="widget-title">{{ $widget['title'] ?? '' }}</h3>
                <img src="{{ asset('frontend/images/wave.svg') }}" class="wave" alt="wave" />
            </div>
            <div class="widget-content text-center">
                @if($widget['type'] == 'about_author')
                    <p>Written by {{ isset($post) ? ($post->author->name ?? 'Admin User') : 'Admin User' }}.</p>
                @elseif($widget['type'] == 'recent_posts')
                    @php
                        $limit = $widget['limit'] ?? 5;
                        $recentPosts = \App\Models\Post::where('status', 'published')->orderBy('created_at', 'desc')->take($limit)->get();
                    @endphp
                    <ul class="list-unstyled text-start mb-0" style="padding-left: 0;">
                        @foreach($recentPosts as $rPost)
                            <li class="mb-2 border-bottom pb-2">
                                <a href="{{ url('/' . $rPost->slug) }}" style="color: #333; font-weight: 500; text-decoration: none;">
                                    {{ $rPost->title }}
                                </a>
                            </li>
                        @endforeach
                    </ul>
                @elseif($widget['type'] == 'categories')
                    @php
                        $categories = \App\Models\Category::withCount('posts')->get();
                        
                        $remove_category_base = \App\Models\Setting::where('key', 'remove_category_base')->value('value') == '1';
                        $category_base = \App\Models\Setting::where('key', 'category_base')->value('value') ?: 'category';
                    @endphp
                    <ul class="list-unstyled text-start mb-0" style="padding-left: 0;">
                        @foreach($categories as $cat)
                            @php
                                $catUrl = $remove_category_base ? '/' . $cat->slug : '/' . $category_base . '/' . $cat->slug;
                            @endphp
                            <li class="mb-2 border-bottom pb-2 d-flex justify-content-between align-items-center">
                                <a href="{{ url($catUrl) }}" style="color: #333; text-decoration: none;">{{ $cat->name }}</a>
                                <span class="badge bg-light text-dark border">{{ $cat->posts_count }}</span>
                            </li>
                        @endforeach
                    </ul>
                @elseif($widget['type'] == 'custom_html')
                    <div class="text-start">
                        {!! $widget['content'] ?? '' !!}
                    </div>
                @endif
            </div>
        </div>
    @endforeach
</div>
