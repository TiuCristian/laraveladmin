{{-- WordPress-Style Media Library Modal --}}
<div class="modal fade" id="featuredImageModal" data-bs-focus="false" aria-labelledby="featuredImageModalLabel" aria-hidden="true" style="z-index: 1080;">
    <div class="modal-dialog modal-xl modal-dialog-centered" style="max-width: 1200px; width: 92vw; height: 85vh;">
        <div class="modal-content border-0 shadow-lg" style="height: 100%; display: flex; flex-direction: column; border-radius: 8px; overflow: hidden;">
            
            {{-- Modal Header with Tabs --}}
            <div class="modal-header border-bottom py-2 px-3 bg-body align-items-center justify-content-between flex-shrink-0" style="height: 56px; min-height: 56px;">
                <div class="d-flex align-items-center gap-3">
                    <h5 class="modal-title fw-bold m-0 text-body fs-5" id="featuredImageModalLabel">Featured image</h5>
                    <ul class="nav nav-tabs border-0 flex-nowrap mb-0" id="mediaModalTabs" role="tablist">
                        <li class="nav-item" role="presentation">
                            <button class="nav-link border-0 bg-transparent text-muted py-2 px-3 fw-medium" id="media-upload-tab" data-bs-toggle="tab" data-bs-target="#media-upload-pane" type="button" role="tab">
                                Upload files
                            </button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link active border-0 border-bottom border-2 border-primary bg-transparent text-primary py-2 px-3 fw-bold" id="media-library-tab" data-bs-toggle="tab" data-bs-target="#media-library-pane" type="button" role="tab">
                                Media Library
                            </button>
                        </li>
                    </ul>
                </div>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            {{-- Modal Body --}}
            <div class="modal-body p-0 bg-body position-relative overflow-hidden" style="flex: 1 1 auto; min-height: 0;">
                <div class="tab-content h-100" id="mediaModalTabsContent">
                    
                    {{-- UPLOAD FILES TAB PANE --}}
                    <div class="tab-pane fade h-100" id="media-upload-pane" role="tabpanel">
                        <div class="d-flex flex-column align-items-center justify-content-center h-100 p-4">
                            <div class="border border-2 border-dashed rounded-3 p-5 text-center bg-body-tertiary w-100 shadow-sm" id="mediaDropzoneArea" style="max-width: 600px;">
                                <i class="fas fa-cloud-upload-alt text-primary mb-3" style="font-size: 3rem;"></i>
                                <h4 class="fw-bold mb-2">Drop files to upload</h4>
                                <p class="text-muted small mb-4">or select files from your computer</p>
                                <input type="file" id="mediaFileInput" class="d-none" multiple accept="image/*,video/*,audio/*,application/pdf">
                                <button type="button" class="btn btn-outline-primary px-4 fw-semibold" onclick="document.getElementById('mediaFileInput').click();">
                                    Select Files
                                </button>
                                <div class="text-muted mt-3" style="font-size: 0.8rem;">Maximum upload file size: 50 MB.</div>
                            </div>
                        </div>
                    </div>

                    {{-- MEDIA LIBRARY TAB PANE --}}
                    <div class="tab-pane fade show active h-100" id="media-library-pane" role="tabpanel">
                        <div class="d-flex flex-column h-100 overflow-hidden">
                            
                            {{-- Filter Toolbar --}}
                            <div class="p-3 border-bottom bg-body-tertiary d-flex flex-wrap align-items-center justify-content-between gap-2 flex-shrink-0" style="height: 56px; min-height: 56px;">
                                <div class="d-flex flex-wrap align-items-center gap-2">
                                    <span class="small fw-semibold text-muted d-none d-sm-inline">Filter media</span>
                                    <select class="form-select form-select-sm w-auto" id="mediaFilterType" style="min-width: 140px;">
                                        <option value="">All media items</option>
                                        <option value="image" selected>Images</option>
                                        <option value="audio">Audio</option>
                                        <option value="video">Video</option>
                                        <option value="document">Documents</option>
                                    </select>

                                    <select class="form-select form-select-sm w-auto" id="mediaFilterDate" style="min-width: 130px;">
                                        <option value="">All dates</option>
                                    </select>
                                </div>

                                <div class="d-flex align-items-center gap-2">
                                    <span class="small fw-semibold text-muted d-none d-sm-inline">Search media</span>
                                    <input type="text" class="form-control form-control-sm" id="mediaSearchInput" placeholder="Search media..." style="width: 180px;">
                                </div>
                            </div>

                            {{-- Main Grid + Details Split View --}}
                            <div class="flex-grow-1 d-flex overflow-hidden" style="min-height: 0;">
                                
                                {{-- Left Thumbnail Grid Area --}}
                                <div class="flex-grow-1 p-3 overflow-y-auto bg-body" id="mediaGridContainer">
                                    <div class="d-flex flex-wrap gap-2" id="mediaGrid">
                                        {{-- Dynamic media items rendered via JS --}}
                                    </div>
                                    <div class="text-center py-5 text-muted d-none" id="mediaGridEmpty">
                                        <i class="fas fa-images fa-3x mb-3 text-secondary opacity-50"></i>
                                        <p class="m-0">No media items found.</p>
                                    </div>
                                </div>

                                {{-- Right Attachment Details Sidebar --}}
                                <div class="border-start bg-body-tertiary p-3 overflow-y-auto d-none d-md-block flex-shrink-0" id="mediaDetailsSidebar" style="width: 340px; min-width: 340px;">
                                    
                                    {{-- Placeholder when nothing selected --}}
                                    <div class="text-center py-5 text-muted" id="mediaDetailsPlaceholder">
                                        <p class="small m-0">Select an item from the library to view attachment details.</p>
                                    </div>

                                    {{-- Attachment Details Content --}}
                                    <div class="d-none" id="mediaDetailsContent">
                                        <h6 class="fw-bold mb-3 text-uppercase small text-muted">Attachment Details</h6>
                                        
                                        {{-- File Info Header --}}
                                        <div class="d-flex gap-3 mb-3 pb-3 border-bottom">
                                            <div class="ratio ratio-1x1 border rounded overflow-hidden bg-dark bg-opacity-10" style="width: 80px; height: 80px; flex-shrink: 0;">
                                                <img src="" id="detailsPreviewImg" alt="" class="object-fit-cover w-100 h-100">
                                            </div>
                                            <div class="small overflow-hidden text-break">
                                                <div class="fw-bold text-truncate mb-1" id="detailsFilename">filename.jpg</div>
                                                <div class="text-muted small mb-1" id="detailsDate">April 20, 2026</div>
                                                <div class="text-muted small mb-1" id="detailsSize">2 MB</div>
                                                <div class="text-muted small" id="detailsDimensions">1536 by 1024 pixels</div>
                                                <div class="mt-2">
                                                    <button type="button" class="btn btn-link p-0 text-danger small text-decoration-none" id="detailsDeleteBtn">
                                                        Delete permanently
                                                    </button>
                                                </div>
                                            </div>
                                        </div>

                                        {{-- Editable Metadata Form --}}
                                        <form id="mediaDetailsForm" onsubmit="event.preventDefault();">
                                            <input type="hidden" id="detailsMediaId">

                                            {{-- Alt Text --}}
                                            <div class="mb-3">
                                                <label for="detailsAltText" class="form-label small fw-bold text-body mb-1">Alt Text</label>
                                                <textarea class="form-control form-control-sm" id="detailsAltText" rows="3" placeholder="Describe the image..."></textarea>
                                                <div class="form-text text-muted" style="font-size: 0.75rem;">
                                                    Leave empty if the image is purely decorative.
                                                </div>
                                            </div>

                                            {{-- Title --}}
                                            <div class="mb-3">
                                                <label for="detailsTitle" class="form-label small fw-bold text-body mb-1">Title</label>
                                                <input type="text" class="form-control form-control-sm" id="detailsTitle">
                                            </div>

                                            {{-- Caption --}}
                                            <div class="mb-3">
                                                <label for="detailsCaption" class="form-label small fw-bold text-body mb-1">Caption</label>
                                                <textarea class="form-control form-control-sm" id="detailsCaption" rows="2"></textarea>
                                            </div>

                                            {{-- Description --}}
                                            <div class="mb-3">
                                                <label for="detailsDescription" class="form-label small fw-bold text-body mb-1">Description</label>
                                                <textarea class="form-control form-control-sm" id="detailsDescription" rows="2"></textarea>
                                            </div>

                                            {{-- File URL --}}
                                            <div class="mb-3">
                                                <label for="detailsFileUrl" class="form-label small fw-bold text-body mb-1">File URL</label>
                                                <div class="input-group input-group-sm">
                                                    <input type="text" class="form-control" id="detailsFileUrl" readonly>
                                                    <button class="btn btn-outline-secondary" type="button" onclick="navigator.clipboard.writeText(document.getElementById('detailsFileUrl').value); alert('URL copied to clipboard');">
                                                        Copy
                                                    </button>
                                                </div>
                                            </div>
                                        </form>

                                    </div>

                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>

            {{-- Modal Footer --}}
            <div class="modal-footer border-top py-2 px-3 bg-body justify-content-end flex-shrink-0" style="height: 60px; min-height: 60px;">
                <button type="button" class="btn btn-primary px-4 fw-semibold" id="mediaModalSetFeaturedBtn" disabled>
                    Set featured image
                </button>
            </div>

        </div>
    </div>
</div>
