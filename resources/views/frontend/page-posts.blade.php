{{-- Template Name: Posts --}}
@extends('frontend.layouts.app')

@section('title', isset($page) ? $page->title : 'Posts')

@section('content')
<div class="container-xl">
    <div class="row gy-4">
        <div class="col-12">
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

            <p>This is a custom template for displaying posts, or whatever you want!</p>
            <div class="row">
                @php
                    $posts = \App\Models\Post::where('status', 'published')->latest()->paginate(10);
                @endphp
                @forelse($posts as $post)
                    <div class="col-md-6 mb-4">
                        <div class="post post-classic rounded bordered">
                            <div class="details p-3">
                                <h5 class="post-title mb-2"><a href="{{ route('frontend.post', ['category' => $post->categories->first()->slug ?? 'uncategorized', 'slug' => $post->slug]) }}">{{ $post->title }}</a></h5>
                                <p class="excerpt mb-0">{{ Str::limit(strip_tags($post->excerpt ?? ''), 100) }}</p>
                            </div>
                        </div>
                    </div>
                @empty
                    <div class="col-12"><p>No posts found.</p></div>
                @endforelse
            </div>
            
            {{ $posts->links('pagination::bootstrap-4') }}
        </div>
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
                }
            });
            container.innerHTML = html;
        }
    });
</script>
@endpush
@endif
