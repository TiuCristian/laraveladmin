@extends('frontend.layouts.app')

@section('title', isset($page) ? $page->title : 'Blog')

@section('content')
<div class="row gy-4">

    <div class="col-lg-8">

        @if(isset($page))
            <div class="page-header mb-4">
                <h1 class="title mt-0 mb-3">{{ $page->title }}</h1>
                @if($page->content)
                    <div class="page-content mb-5" id="post-content-container">
                        <!-- Content will be parsed here -->
                    </div>
                @endif
            </div>
        @endif

        <div class="posts-list">
            @forelse($posts as $post)
                <!-- post -->
                <div class="post post-classic rounded bordered mb-4">
                    <div class="thumb top-rounded">
                        @if($post->categories->count())
                            <a href="#" class="category-badge lg position-absolute">{{ $post->categories->first()->name }}</a>
                        @endif
                        <a href="{{ route('frontend.post', ['category' => $post->categories->first()->slug ?? 'uncategorized', 'slug' => $post->slug]) }}">
                            <div class="inner">
                                @if($post->featured_image)
                                    <img src="{{ Storage::url($post->featured_image) }}" alt="{{ $post->title }}" />
                                @else
                                    <img src="{{ asset('frontend/images/posts/post-lg-1.jpg') }}" alt="{{ $post->title }}" />
                                @endif
                            </div>
                        </a>
                    </div>
                    <div class="details">
                        <ul class="meta list-inline mb-0">
                            <li class="list-inline-item">
                                <a href="#"><img src="{{ asset('frontend/images/other/author-sm.png') }}" class="author" alt="author" />{{ $post->author->name ?? 'Admin User' }}</a>
                            </li>
                            <li class="list-inline-item">{{ $post->published_at ? $post->published_at->format('d F Y') : $post->created_at->format('d F Y') }}</li>
                            <li class="list-inline-item"><i class="icon-bubble"></i> ({{ $post->comments()->where('status', 'approved')->count() }})</li>
                        </ul>
                        <h5 class="post-title mb-3 mt-3"><a href="{{ route('frontend.post', ['category' => $post->categories->first()->slug ?? 'uncategorized', 'slug' => $post->slug]) }}">{{ $post->title }}</a></h5>
                        <p class="excerpt mb-0">{{ Str::limit(strip_tags($post->excerpt ?? ''), 150) }}</p>
                    </div>
                    <div class="post-bottom clearfix d-flex align-items-center">
                        <div class="float-end d-none d-md-block w-100 text-end">
                            <a href="{{ route('frontend.post', ['category' => $post->categories->first()->slug ?? 'uncategorized', 'slug' => $post->slug]) }}" class="more-link">Continue reading<i class="icon-arrow-right"></i></a>
                        </div>
                        <div class="more-button d-block d-md-none float-end">
                            <a href="{{ route('frontend.post', ['category' => $post->categories->first()->slug ?? 'uncategorized', 'slug' => $post->slug]) }}"><span class="icon-options"></span></a>
                        </div>
                    </div>
                </div>
            @empty
                <p>No posts found.</p>
            @endforelse
        </div>

        <nav>
            {{ $posts->links('pagination::bootstrap-4') }}
        </nav>

    </div>

    <div class="col-lg-4">
        <!-- sidebar -->
        @include('frontend.sidebar')
    </div>

</div>
@endsection

@if(isset($page) && $page->content)
@push('scripts')
<script>
    document.addEventListener('DOMContentLoaded', function() {
        // Parse EditorJS JSON
        let editorData = `{!! addslashes($page->content) !!}`;
        let parsedData = {"blocks":[]};
        
        try {
            parsedData = JSON.parse(editorData);
        } catch(e) {}
        
        const container = document.getElementById('post-content-container');
        
        if (parsedData.blocks && parsedData.blocks.length > 0) {
            let html = '';
            parsedData.blocks.forEach(block => {
                switch (block.type) {
                    case 'header':
                        html += `<h${block.data.level}>${block.data.text}</h${block.data.level}>`;
                        break;
                    case 'paragraph':
                        html += `<p>${block.data.text}</p>`;
                        break;
                    case 'list':
                        const tag = block.data.style === 'ordered' ? 'ol' : 'ul';
                        let listHtml = `<${tag}>`;
                        block.data.items.forEach(item => {
                            listHtml += `<li>${item}</li>`;
                        });
                        listHtml += `</${tag}>`;
                        html += listHtml;
                        break;
                    case 'image':
                        let imgClass = 'img-fluid rounded';
                        if (block.data.withBorder) imgClass += ' border';
                        if (block.data.withBackground) imgClass += ' bg-light p-3';
                        let imgHtml = `<figure class="figure my-4 w-100 text-center ${block.data.stretched ? 'w-100' : ''}">
                            <img src="${block.data.file.url}" class="${imgClass}" alt="${block.data.caption || ''}" style="max-height: 600px; object-fit: contain;">`;
                        if (block.data.caption) {
                            imgHtml += `<figcaption class="figure-caption mt-2">${block.data.caption}</figcaption>`;
                        }
                        imgHtml += `</figure>`;
                        html += imgHtml;
                        break;
                }
            });
            container.innerHTML = html;
        }
    });
</script>
@endpush
@endif
