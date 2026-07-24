{{-- Hidden inputs to be submitted with post form --}}
<input type="hidden" name="seo_title" id="hiddenSeoTitle" form="editForm" value="{{ old('seo_title', $post->seo_title ?? '') }}">
<input type="hidden" name="seo_description" id="hiddenSeoDescription" form="editForm" value="{{ old('seo_description', $post->seo_description ?? '') }}">
<input type="hidden" name="focus_keyword" id="hiddenFocusKeyword" form="editForm" value="{{ old('focus_keyword', $post->focus_keyword ?? '') }}">
<input type="hidden" name="is_pillar" id="hiddenIsPillar" form="editForm" value="{{ old('is_pillar', isset($post) && $post->is_pillar ? '1' : '0') }}">
<input type="hidden" name="seo_score" id="hiddenSeoScore" form="editForm" value="{{ old('seo_score', $post->seo_score ?? 0) }}">
@if(isset($post) && $post->id)
    <input type="hidden" id="postIdInput" value="{{ $post->id }}">
@endif

{{-- Rank Math Offcanvas Drawer --}}
<div class="offcanvas offcanvas-end border-start shadow-lg" tabindex="-1" id="rankMathOffcanvas" aria-labelledby="rankMathOffcanvasLabel" style="width: 420px; z-index: 1060;">
    {{-- Drawer Header --}}
    <div class="offcanvas-header border-bottom py-3 px-4 bg-body">
        <div class="d-flex align-items-center gap-2">
            <h5 class="offcanvas-title fw-bold m-0" id="rankMathOffcanvasLabel" style="font-size: 1.1rem; color: var(--bs-heading-color);">Rank Math</h5>
            <button type="button" id="rankMathDrawerScoreBadge" class="btn btn-sm text-white fw-bold px-2 py-0 ms-2" style="background-color: #22c55e; border-radius: 4px; font-size: 0.85rem; height: 26px; line-height: 26px;">
                0 / 100
            </button>
        </div>
        <div class="d-flex align-items-center gap-2">
            <button type="button" class="btn btn-dark btn-sm rounded-1 p-1 px-2 text-white"><i class="fas fa-star text-warning"></i></button>
            <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
    </div>

    {{-- Drawer Body --}}
    <div class="offcanvas-body p-0 bg-body">
        {{-- Navigation Tabs --}}
        <div class="border-bottom bg-body px-3 pt-2">
            <ul class="nav nav-tabs border-0 flex-nowrap gap-3" id="rankMathTabs" role="tablist">
                <li class="nav-item" role="presentation">
                    <button class="nav-link active fw-bold border-0 border-bottom border-3 border-primary bg-transparent text-primary pb-2 px-1 d-flex align-items-center gap-1" id="rm-general-tab" data-bs-toggle="tab" data-bs-target="#rm-general-pane" type="button" role="tab">
                        <i class="fas fa-cog"></i> General
                    </button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link border-0 bg-transparent text-muted pb-2 px-1 opacity-50" type="button" disabled title="Advanced (Ignored for now)">
                        <i class="fas fa-briefcase"></i>
                    </button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link border-0 bg-transparent text-muted pb-2 px-1 opacity-50" type="button" disabled title="Schema (Ignored for now)">
                        <i class="fas fa-id-card"></i>
                    </button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link border-0 bg-transparent text-muted pb-2 px-1 opacity-50" type="button" disabled title="Social (Ignored for now)">
                        <i class="fas fa-share-alt"></i>
                    </button>
                </li>
            </ul>
        </div>

        {{-- Tab Content --}}
        <div class="tab-content p-4" id="rankMathTabsContent">
            {{-- GENERAL TAB --}}
            <div class="tab-pane fade show active" id="rm-general-pane" role="tabpanel">
                
                {{-- Preview Section --}}
                <div class="mb-4">
                    <h6 class="fw-bold mb-2 text-body">Preview</h6>
                    <div class="p-3 border rounded bg-body-tertiary shadow-sm mb-2" style="font-family: Arial, sans-serif;">
                        <div class="text-truncate text-muted small mb-1" id="rmSerpUrlDisplay" style="font-size: 0.8rem; color: #202124;">
                            {{ url('/') }}/blog/{{ $post->slug ?? 'post-slug' }}
                        </div>
                        <div class="fw-medium text-primary text-truncate mb-1" id="rmSerpTitleDisplay" style="font-size: 1.1rem; color: #1a0dab; cursor: pointer;">
                            {{ $post->seo_title ?? $post->title ?? 'Post Title' }}
                        </div>
                        <div class="small text-muted text-truncate-2" id="rmSerpDescDisplay" style="font-size: 0.85rem; color: #4d5156; line-height: 1.4;">
                            {{ $post->seo_description ?? $post->excerpt ?? 'Please provide a meta description by editing the snippet below.' }}
                        </div>
                    </div>
                    <button type="button" class="btn btn-primary btn-sm px-3 fw-semibold shadow-sm" data-bs-toggle="modal" data-bs-target="#editSnippetModal">
                        Edit Snippet
                    </button>
                </div>

                <hr class="my-4 text-muted opacity-25">

                {{-- Focus Keyword Section --}}
                <div class="mb-4">
                    <div class="d-flex align-items-center justify-content-between mb-2">
                        <label for="rmFocusKeywordInput" class="form-label fw-bold m-0 text-body">
                            Focus Keyword <i class="fas fa-question-circle text-muted ms-1" style="font-size: 0.85rem;"></i>
                        </label>
                        <i class="fas fa-chart-line text-primary"></i>
                    </div>

                    <div class="border rounded p-2 bg-body mb-3">
                        <div class="d-flex flex-wrap align-items-center gap-1 mb-2" id="rmKeywordBadgesContainer">
                            @if(!empty($post->focus_keyword))
                                <span class="badge bg-success d-inline-flex align-items-center gap-1 px-2 py-1 fs-6">
                                    <i class="fas fa-star me-1 text-warning" style="font-size: 0.75rem;"></i>
                                    <span>{{ $post->focus_keyword }}</span>
                                    <i class="fas fa-sync-alt ms-1 text-white opacity-75" style="cursor: pointer;" onclick="document.getElementById('rmFocusKeywordInput').focus();"></i>
                                </span>
                            @endif
                        </div>
                        <input type="text" class="form-control form-control-sm border-0 shadow-none bg-transparent" id="rmFocusKeywordInput" placeholder="Example: Rank Math SEO" value="{{ old('focus_keyword', $post->focus_keyword ?? '') }}">
                    </div>

                    {{-- PRO Upgrade Banner --}}
                    <div class="p-3 border-start border-3 border-warning rounded bg-warning bg-opacity-10 mb-3">
                        <span class="small text-body">Want more? <a href="#" class="fw-bold text-primary text-decoration-underline" onclick="event.preventDefault(); alert('RankMath PRO Features');">Upgrade today to the PRO</a> version.</span>
                    </div>

                    {{-- Pillar Content Checkbox --}}
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="rmIsPillarCheckbox" form="editForm" value="1" {{ (old('is_pillar', isset($post) && $post->is_pillar) ? 'checked' : '') }}>
                        <label class="form-check-label small fw-bold text-body" for="rmIsPillarCheckbox">
                            This post is Pillar Content <i class="fas fa-question-circle text-muted ms-1"></i>
                        </label>
                    </div>
                </div>

                <hr class="my-4 text-muted opacity-25">

                {{-- Accordions for Checks --}}
                <div class="accordion accordion-flush" id="rankMathAccordion">
                    
                    {{-- 1. Basic SEO Accordion --}}
                    <div class="accordion-item border rounded mb-3 overflow-hidden">
                        <h2 class="accordion-header" id="headingBasicSeo">
                            <button class="accordion-button py-3 px-3 fw-bold text-body bg-body shadow-none d-flex justify-content-between align-items-center" type="button" data-bs-toggle="collapse" data-bs-target="#collapseBasicSeo" aria-expanded="true" aria-controls="collapseBasicSeo">
                                <span>Basic SEO</span>
                                <span class="badge bg-success ms-auto me-2" id="rmBasicSeoCount">All Good</span>
                            </button>
                        </h2>
                        <div id="collapseBasicSeo" class="accordion-collapse collapse show" aria-labelledby="headingBasicSeo">
                            <div class="accordion-body p-3 bg-body fs-6">
                                <ul class="list-unstyled mb-0 d-flex flex-column gap-2">
                                    <li id="check_kw_title" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">Hurray! You're using Focus Keyword in the SEO Title.</span>
                                    </li>
                                    <li id="check_kw_desc" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">Focus Keyword used inside SEO Meta Description.</span>
                                    </li>
                                    <li id="check_kw_url" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">Focus Keyword used in the URL.</span>
                                    </li>
                                    <li id="check_kw_first10" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">Focus Keyword appears in the first 10% of the content.</span>
                                    </li>
                                    <li id="check_kw_content" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">Focus Keyword found in the content.</span>
                                    </li>
                                    <li id="check_word_count" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">Content is 0 words long. Good job!</span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    {{-- 2. Additional Accordion (Excludes Content AI) --}}
                    <div class="accordion-item border rounded mb-3 overflow-hidden">
                        <h2 class="accordion-header" id="headingAdditionalSeo">
                            <button class="accordion-button collapsed py-3 px-3 fw-bold text-body bg-body shadow-none d-flex justify-content-between align-items-center" type="button" data-bs-toggle="collapse" data-bs-target="#collapseAdditionalSeo" aria-expanded="false" aria-controls="collapseAdditionalSeo">
                                <span>Additional</span>
                                <span class="badge bg-danger ms-auto me-2" id="rmAdditionalSeoCount">1 Errors</span>
                            </button>
                        </h2>
                        <div id="collapseAdditionalSeo" class="accordion-collapse collapse" aria-labelledby="headingAdditionalSeo">
                            <div class="accordion-body p-3 bg-body fs-6">
                                <ul class="list-unstyled mb-0 d-flex flex-column gap-2">
                                    <li id="check_kw_subheading" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">Focus Keyword found in the subheading(s).</span>
                                    </li>
                                    <li id="check_kw_img_alt" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">Focus Keyword found in image alt attribute(s).</span>
                                    </li>
                                    <li id="check_kw_density" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">Keyword Density is 0, the Focus Keyword appears 0 times.</span>
                                    </li>
                                    <li id="check_url_length" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">URL is 0 characters long. Kudos!</span>
                                    </li>
                                    <li id="check_external_links" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">Great! You are linking to external resources.</span>
                                    </li>
                                    <li id="check_dofollow_links" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">At least one external link with DoFollow found in your content.</span>
                                    </li>
                                    <li id="check_internal_links" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">You are linking to other resources on your website which is great.</span>
                                    </li>
                                    <li id="check_kw_unique" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">You haven't used this Focus Keyword before.</span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    {{-- 3. Title Readability Accordion --}}
                    <div class="accordion-item border rounded mb-3 overflow-hidden">
                        <h2 class="accordion-header" id="headingTitleReadability">
                            <button class="accordion-button collapsed py-3 px-3 fw-bold text-body bg-body shadow-none d-flex justify-content-between align-items-center" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTitleReadability" aria-expanded="false" aria-controls="collapseTitleReadability">
                                <span>Title Readability</span>
                                <span class="badge bg-danger ms-auto me-2" id="rmTitleReadabilityCount">2 Errors</span>
                            </button>
                        </h2>
                        <div id="collapseTitleReadability" class="accordion-collapse collapse" aria-labelledby="headingTitleReadability">
                            <div class="accordion-body p-3 bg-body fs-6">
                                <ul class="list-unstyled mb-0 d-flex flex-column gap-2">
                                    <li id="check_title_kw_start" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">Focus Keyword used at the beginning of SEO title.</span>
                                    </li>
                                    <li id="check_title_sentiment" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-check-circle text-success me-2 mt-1"></i>
                                        <span class="check-text text-body">Your title has a positive or a negative sentiment.</span>
                                    </li>
                                    <li id="check_title_power_word" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-times-circle text-danger me-2 mt-1"></i>
                                        <span class="check-text text-body">Your title doesn't contain a power word. Add at least one.</span>
                                    </li>
                                    <li id="check_title_number" class="d-flex align-items-start small">
                                        <i class="check-icon fas fa-times-circle text-danger me-2 mt-1"></i>
                                        <span class="check-text text-body">Your SEO title doesn't contain a number.</span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>

                </div>

            </div>
        </div>
    </div>
</div>

{{-- Edit Snippet Pop-up Modal --}}
<div class="modal fade" id="editSnippetModal" tabindex="-1" aria-labelledby="editSnippetModalLabel" aria-hidden="true" style="z-index: 1070;">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content border-0 shadow-lg">
            <div class="modal-header border-bottom px-4 py-3">
                <h5 class="modal-header-title fw-bold m-0 text-body" id="editSnippetModalLabel">Edit Snippet</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body p-4 bg-body">
                <div class="mb-4">
                    <label for="rmModalSeoTitle" class="form-label fw-bold text-body">SEO Title</label>
                    <input type="text" class="form-control" id="rmModalSeoTitle" placeholder="SEO Title" value="{{ old('seo_title', $post->seo_title ?? $post->title ?? '') }}">
                    <div class="form-text small text-muted">Use %title%, %sep%, %sitename% tags or type custom text.</div>
                </div>

                <div class="mb-4">
                    <label for="rmModalSlug" class="form-label fw-bold text-body">Permalink / Slug</label>
                    <input type="text" class="form-control" id="rmModalSlug" placeholder="post-slug" value="{{ old('slug', $post->slug ?? '') }}">
                </div>

                <div class="mb-4">
                    <label for="rmModalSeoDescription" class="form-label fw-bold text-body">Meta Description</label>
                    <textarea class="form-control" id="rmModalSeoDescription" rows="4" placeholder="Write SEO Meta Description...">{{ old('seo_description', $post->seo_description ?? $post->excerpt ?? '') }}</textarea>
                    <div class="form-text small text-muted">Recommended length: ~160 characters.</div>
                </div>
            </div>
            <div class="modal-footer border-top px-4 py-3">
                <button type="button" class="btn btn-secondary btn-sm px-3" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary btn-sm px-4 fw-semibold" id="rmSaveSnippetBtn">Save Snippet</button>
            </div>
        </div>
    </div>
</div>
