@extends('frontend.layouts.app')

@section('title', $page->title)

@section('content')
<div class="row gy-4">
    <div class="col-lg-8">
        <!-- post single -->
        <div class="post post-single">
            <!-- post header -->
            <div class="post-header">
                <h1 class="title mt-0 mb-3">{{ $page->title }}</h1>
            </div>
            
            <!-- featured image -->
            @if($page->featured_image)
            <div class="featured-image">
                <img src="{{ Storage::url($page->featured_image) }}" alt="{{ $page->title }}" />
            </div>
            @endif
            
            <!-- post content -->
            <div class="post-content clearfix" id="post-content-container">
                <!-- EditorJS blocks will be parsed and injected here -->
            </div>
            
            <!-- post bottom section -->
            <div class="post-bottom">
            </div>

            <!-- Comments Section -->
            @if($page->allow_comments)
            <div class="comments-area mt-5" id="comments">
                <h4 class="mb-4">{{ $page->comments()->where('status', 'approved')->count() }} Comments</h4>
                
                @if(session('success'))
                    <div class="alert alert-success">{{ session('success') }}</div>
                @endif
                @if(session('error'))
                    <div class="alert alert-danger">{{ session('error') }}</div>
                @endif

                <ul class="list-unstyled mb-5">
                    @foreach($page->comments()->where('status', 'approved')->get() as $comment)
                    <li class="media mb-4 d-flex">
                        <img src="https://ui-avatars.com/api/?name={{ urlencode($comment->name) }}&background=random" class="mr-3 rounded-circle me-3" alt="{{ $comment->name }}" width="50">
                        <div class="media-body">
                            <h5 class="mt-0 mb-1 fw-bold" style="font-size: 1rem;">{{ $comment->name }} <small class="text-muted fw-normal ms-2" style="font-size: 0.8rem;">{{ $comment->created_at->format('M d, Y') }}</small></h5>
                            <p class="text-muted">{{ $comment->content }}</p>
                        </div>
                    </li>
                    @endforeach
                </ul>

                <div class="comment-respond">
                    <h4 class="mb-4">Leave a Reply</h4>
                    <form action="{{ route('comments.store') }}" method="POST">
                        @csrf
                        <input type="hidden" name="page_id" value="{{ $page->id }}">
                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label for="name" class="form-label">Name *</label>
                                <input type="text" class="form-control" id="name" name="name" required>
                            </div>
                            <div class="col-md-6 mb-3">
                                <label for="email" class="form-label">Email *</label>
                                <input type="email" class="form-control" id="email" name="email" required>
                            </div>
                        </div>
                        <div class="mb-3">
                            <label for="website" class="form-label">Website</label>
                            <input type="url" class="form-control" id="website" name="website">
                        </div>
                        <div class="mb-3">
                            <label for="content" class="form-label">Comment *</label>
                            <textarea class="form-control" id="content" name="content" rows="5" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary" style="background-color: var(--bs-primary); border-color: var(--bs-primary);">Post Comment</button>
                    </form>
                </div>
            </div>
            @endif
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
                    <p>Welcome to our website!</p>
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
                    
                    case 'shortcode':
                        let codeText = block.data.code || '';
                        let sFormMatch = codeText.match(/\[form id=["']?(\d+)["']?\]/);
                        if (sFormMatch) {
                            let formId = parseInt(sFormMatch[1]);
                            @php
                                $allForms = \App\Models\Form::all();
                            @endphp
                            let preloadedForms = {!! json_encode($allForms) !!};
                            let form = preloadedForms.find(f => f.id === formId);
                            if (form) {
                                let formHtml = `<form action="/forms/${form.id}/submit" method="POST" class="mt-4 mb-4 border p-4 rounded bg-light">`;
                                formHtml += `<input type="hidden" name="_token" value="{{ csrf_token() }}">`;
                                if(form.fields) {
                                    form.fields.forEach(field => {
                                        let req = field.required ? 'required' : '';
                                        let reqStar = field.required ? '<span class="text-danger">*</span>' : '';
                                        formHtml += `<div class="mb-3"><label class="form-label fw-bold">${field.label} ${reqStar}</label>`;
                                        if (field.type === 'textarea') {
                                            formHtml += `<textarea name="fields[${field.label}]" class="form-control" ${req}></textarea>`;
                                        } else if (field.type === 'select') {
                                            formHtml += `<select name="fields[${field.label}]" class="form-select" ${req}>`;
                                            if(field.options) {
                                                field.options.split(',').forEach(opt => {
                                                    formHtml += `<option value="${opt.trim()}">${opt.trim()}</option>`;
                                                });
                                            }
                                            formHtml += `</select>`;
                                        } else if (field.type === 'checkbox') {
                                            formHtml += `<div class="d-flex flex-wrap gap-3">`;
                                            let opts = field.options ? field.options.split(',') : ['Yes'];
                                            opts.forEach((opt, idx) => {
                                                formHtml += `<div class="form-check"><input type="checkbox" name="fields[${field.label}][]" value="${opt.trim()}" id="chk_${form.id}_${field.label.replace(/\\s+/g,'')}_${idx}" class="form-check-input"><label for="chk_${form.id}_${field.label.replace(/\\s+/g,'')}_${idx}" class="form-check-label">${opt.trim()}</label></div>`;
                                            });
                                            formHtml += `</div>`;
                                        } else if (field.type === 'radio') {
                                            formHtml += `<div class="d-flex flex-wrap gap-3">`;
                                            let opts = field.options ? field.options.split(',') : ['Yes'];
                                            opts.forEach((opt, idx) => {
                                                formHtml += `<div class="form-check"><input type="radio" name="fields[${field.label}]" value="${opt.trim()}" id="rad_${form.id}_${field.label.replace(/\\s+/g,'')}_${idx}" class="form-check-input" ${req}><label for="rad_${form.id}_${field.label.replace(/\\s+/g,'')}_${idx}" class="form-check-label">${opt.trim()}</label></div>`;
                                            });
                                            formHtml += `</div>`;
                                        } else {
                                            formHtml += `<input type="${field.type}" name="fields[${field.label}]" class="form-control" ${req}>`;
                                        }
                                        formHtml += `</div>`;
                                    });
                                }
                                formHtml += `<button type="submit" class="btn btn-primary">${form.submit_text || 'Submit'}</button>`;
                                formHtml += `</form>`;
                                codeText = codeText.replace(sFormMatch[0], formHtml);
                            }
                        }
                        html += `<div>${codeText}</div>`;
                        break;

                    case 'paragraph':
                        let text = block.data.text;
                        let formMatch = text.match(/\[form id=["']?(\d+)["']?\]/);
                        if (formMatch) {
                            let formId = parseInt(formMatch[1]);
                            @php
                                $allForms = \App\Models\Form::all();
                            @endphp
                            let preloadedForms = {!! json_encode($allForms) !!};
                            let form = preloadedForms.find(f => f.id === formId);
                            if (form) {
                                let formHtml = `<form action="/forms/${form.id}/submit" method="POST" class="mt-4 mb-4 border p-4 rounded bg-light">`;
                                formHtml += `<input type="hidden" name="_token" value="{{ csrf_token() }}">`;
                                if(form.fields) {
                                    form.fields.forEach(field => {
                                        let req = field.required ? 'required' : '';
                                        let reqStar = field.required ? '<span class="text-danger">*</span>' : '';
                                        formHtml += `<div class="mb-3"><label class="form-label fw-bold">${field.label} ${reqStar}</label>`;
                                        if (field.type === 'textarea') {
                                            formHtml += `<textarea name="fields[${field.label}]" class="form-control" ${req}></textarea>`;
                                        } else if (field.type === 'select') {
                                            formHtml += `<select name="fields[${field.label}]" class="form-select" ${req}>`;
                                            if(field.options) {
                                                field.options.split(',').forEach(opt => {
                                                    formHtml += `<option value="${opt.trim()}">${opt.trim()}</option>`;
                                                });
                                            }
                                            formHtml += `</select>`;
                                        } else if (field.type === 'checkbox') {
                                            formHtml += `<div class="d-flex flex-wrap gap-3">`;
                                            let opts = field.options ? field.options.split(',') : ['Yes'];
                                            opts.forEach((opt, idx) => {
                                                formHtml += `<div class="form-check"><input type="checkbox" name="fields[${field.label}][]" value="${opt.trim()}" id="chk_${form.id}_${field.label.replace(/\\s+/g,'')}_${idx}" class="form-check-input"><label for="chk_${form.id}_${field.label.replace(/\\s+/g,'')}_${idx}" class="form-check-label">${opt.trim()}</label></div>`;
                                            });
                                            formHtml += `</div>`;
                                        } else if (field.type === 'radio') {
                                            formHtml += `<div class="d-flex flex-wrap gap-3">`;
                                            let opts = field.options ? field.options.split(',') : ['Yes'];
                                            opts.forEach((opt, idx) => {
                                                formHtml += `<div class="form-check"><input type="radio" name="fields[${field.label}]" value="${opt.trim()}" id="rad_${form.id}_${field.label.replace(/\\s+/g,'')}_${idx}" class="form-check-input" ${req}><label for="rad_${form.id}_${field.label.replace(/\\s+/g,'')}_${idx}" class="form-check-label">${opt.trim()}</label></div>`;
                                            });
                                            formHtml += `</div>`;
                                        } else {
                                            formHtml += `<input type="${field.type}" name="fields[${field.label}]" class="form-control" ${req}>`;
                                        }
                                        formHtml += `</div>`;
                                    });
                                }
                                formHtml += `<button type="submit" class="btn btn-primary">${form.submit_text || 'Submit'}</button>`;
                                formHtml += `</form>`;
                                text = text.replace(formMatch[0], formHtml);
                            }
                        }
                        html += `<p>${text}</p>`;
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
