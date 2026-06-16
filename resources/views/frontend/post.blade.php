@extends('frontend.layouts.app')

@section('title', $post->title)

@section('content')
<div class="row gy-4">
    <div class="col-lg-8">
        <!-- post single -->
        <div class="post post-single">
            <!-- post header -->
            <div class="post-header">
                <h1 class="title mt-0 mb-3">{{ $post->title }}</h1>
                <ul class="meta list-inline mb-0">
                    <li class="list-inline-item">
                        <a href="#">
                            <img src="{{ asset('frontend/images/other/author-sm.png') }}" class="author" alt="author" />
                            {{ $post->author->name ?? 'Admin User' }}
                        </a>
                    </li>
                    @if($post->categories->count())
                        <li class="list-inline-item"><a href="#">{{ $post->categories->first()->name }}</a></li>
                    @endif
                    <li class="list-inline-item">{{ $post->published_at ? $post->published_at->format('d F Y') : $post->created_at->format('d F Y') }}</li>
                </ul>
            </div>
            
            <!-- featured image -->
            @if($post->featured_image)
            <div class="featured-image">
                <img src="{{ Storage::url($post->featured_image) }}" alt="{{ $post->title }}" />
            </div>
            @endif
            
            <!-- post content -->
            <div class="post-content clearfix" id="post-content-container">
                <!-- EditorJS blocks will be parsed and injected here -->
            </div>
            
            <!-- post bottom section -->
            <div class="post-bottom">
                <div class="row d-flex align-items-center">
                    <div class="col-md-6 col-12 text-center text-md-start">
                        <!-- tags -->
                        @foreach($post->tags as $tag)
                            <a href="#" class="tag">#{{ $tag->name }}</a>
                        @endforeach
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-lg-4">
        <!-- sidebar -->
        <div class="sidebar">
            <div class="widget rounded">
                <div class="widget-header text-center">
                    <h3 class="widget-title">About the Author</h3>
                    <img src="{{ asset('frontend/images/wave.svg') }}" class="wave" alt="wave" />
                </div>
                <div class="widget-content text-center">
                    <p>Written by {{ $post->author->name ?? 'Admin User' }}.</p>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection

@push('scripts')
<script>
    document.addEventListener('DOMContentLoaded', function() {
        // Parse EditorJS JSON
        let editorData = `{!! addslashes($post->content) !!}`;
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
                    // Add more block handlers if needed
                }
            });
            container.innerHTML = html;
        } else {
            container.innerHTML = '<p>No content available.</p>';
        }
    });
</script>
@endpush
