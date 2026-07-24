/**
 * WordPress-Style Media Library Modal Controller
 * Bulletproof Self-Executing Module with Global Event Delegation
 */
(function () {
    'use strict';

    let currentMediaList = [];
    let selectedMedia = null;
    let updateDebounceTimer = null;

    function getElement(id) {
        return document.getElementById(id);
    }

    function formatDate(dateString) {
        if (!dateString) return '';
        const d = new Date(dateString);
        return d.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
    }

    function formatBytes(bytes, decimals = 1) {
        if (!bytes || bytes === 0) return '0 Bytes';
        const k = 1024;
        const dm = decimals < 0 ? 0 : decimals;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    }

    function escapeHtml(str) {
        if (!str) return '';
        return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    function clearSelection() {
        selectedMedia = null;
        const setFeaturedBtn = getElement('mediaModalSetFeaturedBtn');
        const detailsPlaceholder = getElement('mediaDetailsPlaceholder');
        const detailsContent = getElement('mediaDetailsContent');
        const detailsMediaId = getElement('detailsMediaId');

        if (setFeaturedBtn) setFeaturedBtn.setAttribute('disabled', 'disabled');
        if (detailsPlaceholder) detailsPlaceholder.classList.remove('d-none');
        if (detailsContent) detailsContent.classList.add('d-none');
        if (detailsMediaId) detailsMediaId.value = '';

        const deleteBtn = getElement('detailsDeleteBtn');
        if (deleteBtn) deleteBtn.textContent = 'Delete permanently';
    }

    function selectMediaItem(item) {
        if (!item) return;
        selectedMedia = item;

        const mediaGrid = getElement('mediaGrid');
        const setFeaturedBtn = getElement('mediaModalSetFeaturedBtn');
        const detailsPlaceholder = getElement('mediaDetailsPlaceholder');
        const detailsContent = getElement('mediaDetailsContent');

        if (mediaGrid) {
            const items = mediaGrid.querySelectorAll('.media-grid-item');
            items.forEach(el => {
                const isTarget = parseInt(el.dataset.id) === item.id;
                el.className = `position-relative border rounded overflow-hidden cursor-pointer media-grid-item ${isTarget ? 'border-3 border-primary shadow' : ''}`;
                const badge = el.querySelector('.select-badge');
                if (badge) {
                    if (isTarget) badge.classList.remove('d-none');
                    else badge.classList.add('d-none');
                }
            });
        }

        if (setFeaturedBtn) setFeaturedBtn.removeAttribute('disabled');
        if (detailsPlaceholder) detailsPlaceholder.classList.add('d-none');
        if (detailsContent) detailsContent.classList.remove('d-none');

        const detailsPreviewImg = getElement('detailsPreviewImg');
        const detailsFilename = getElement('detailsFilename');
        const detailsDate = getElement('detailsDate');
        const detailsSize = getElement('detailsSize');
        const detailsDimensions = getElement('detailsDimensions');
        const detailsMediaId = getElement('detailsMediaId');
        const detailsAltText = getElement('detailsAltText');
        const detailsTitle = getElement('detailsTitle');
        const detailsCaption = getElement('detailsCaption');
        const detailsDescription = getElement('detailsDescription');
        const detailsFileUrl = getElement('detailsFileUrl');

        if (detailsPreviewImg) detailsPreviewImg.src = item.url;
        if (detailsFilename) detailsFilename.textContent = item.filename;
        if (detailsDate) detailsDate.textContent = formatDate(item.created_at);
        if (detailsSize) detailsSize.textContent = formatBytes(item.size);
        if (detailsDimensions) detailsDimensions.textContent = item.dimensions || 'Image';

        if (detailsMediaId) detailsMediaId.value = item.id;
        if (detailsAltText) detailsAltText.value = item.alt_text || '';
        if (detailsTitle) detailsTitle.value = item.title || '';
        if (detailsCaption) detailsCaption.value = item.caption || '';
        if (detailsDescription) detailsDescription.value = item.description || '';
        if (detailsFileUrl) detailsFileUrl.value = window.location.origin + item.url;
    }

    function renderGrid(autoSelectId = null) {
        const mediaGrid = getElement('mediaGrid');
        const mediaGridEmpty = getElement('mediaGridEmpty');
        if (!mediaGrid) return;
        mediaGrid.innerHTML = '';

        if (currentMediaList.length === 0) {
            if (mediaGridEmpty) mediaGridEmpty.classList.remove('d-none');
            clearSelection();
            return;
        }

        if (mediaGridEmpty) mediaGridEmpty.classList.add('d-none');

        let targetToSelect = null;

        currentMediaList.forEach(item => {
            const isSelected = selectedMedia && selectedMedia.id === item.id;
            if (autoSelectId && item.id === autoSelectId) {
                targetToSelect = item;
            }

            const card = document.createElement('div');
            card.className = `position-relative border rounded overflow-hidden cursor-pointer media-grid-item ${isSelected ? 'border-3 border-primary shadow' : ''}`;
            card.style.cssText = 'width: 110px; height: 110px; flex-shrink: 0; background-color: var(--bs-tertiary-bg); cursor: pointer;';
            card.dataset.id = item.id;

            const isImage = item.mime_type && item.mime_type.startsWith('image/');
            const previewUrl = isImage ? item.url : '/assets/images/document-icon.png';

            card.innerHTML = `
                <img src="${previewUrl}" alt="${escapeHtml(item.alt_text || item.title || item.filename)}" class="object-fit-cover w-100 h-100">
                <div class="position-absolute top-0 end-0 m-1 badge bg-primary rounded-circle p-1 select-badge ${isSelected ? '' : 'd-none'}" style="width: 22px; height: 22px; line-height: 14px;">
                    <i class="fas fa-check text-white" style="font-size: 11px;"></i>
                </div>
            `;

            card.addEventListener('click', function () {
                selectMediaItem(item);
            });

            mediaGrid.appendChild(card);
        });

        if (targetToSelect) {
            selectMediaItem(targetToSelect);
        } else if (selectedMedia) {
            const found = currentMediaList.find(m => m.id === selectedMedia.id);
            if (found) {
                selectMediaItem(found);
            } else if (currentMediaList.length > 0) {
                selectMediaItem(currentMediaList[0]);
            } else {
                clearSelection();
            }
        } else if (currentMediaList.length > 0) {
            selectMediaItem(currentMediaList[0]);
        } else {
            clearSelection();
        }
    }

    function syncFeaturedImageAltFromLibrary() {
        const imgPreview = getElement('featuredImagePreview');
        const hiddenPathInput = getElement('featuredImagePathInput');
        if (!imgPreview) return;

        let currentSrc = imgPreview.src ? imgPreview.src.split('?')[0].split('/').pop() : '';
        let currentPath = hiddenPathInput && hiddenPathInput.value ? hiddenPathInput.value.replace(/^\/?storage\//, '').split('/').pop() : '';
        
        const targetFilename = currentPath || currentSrc;
        if (!targetFilename) return;

        // Capture the server-rendered alt text before selectMediaItem potentially clears it
        const bladeRenderedAlt = (imgPreview.getAttribute('alt') || '').trim();

        const matched = currentMediaList.find(m => m.filename === targetFilename || m.filepath.endsWith(targetFilename) || m.url.endsWith(targetFilename));
        if (matched) {
            // Determine the best alt text: prefer media record's alt_text, fall back to Blade-rendered alt
            const effectiveAlt = (matched.alt_text || '').trim() || bladeRenderedAlt;

            // If the media record is missing alt_text but we have a Blade-rendered value, sync it back
            if (!matched.alt_text && bladeRenderedAlt) {
                matched.alt_text = bladeRenderedAlt;
                const foundInList = currentMediaList.find(m => m.id === matched.id);
                if (foundInList) foundInList.alt_text = bladeRenderedAlt;
            }

            selectMediaItem(matched);

            // Ensure the detailsAltText textarea has the correct value after selectMediaItem
            const detailsAltText = getElement('detailsAltText');
            if (detailsAltText && effectiveAlt && !detailsAltText.value.trim()) {
                detailsAltText.value = effectiveAlt;
            }

            if (effectiveAlt) {
                imgPreview.alt = effectiveAlt;
                imgPreview.setAttribute('alt', effectiveAlt);
                imgPreview.dispatchEvent(new Event('input', { bubbles: true }));
            }
        } else if (bladeRenderedAlt) {
            // Featured image not in current media list page, but Blade already set the alt correctly
            imgPreview.dispatchEvent(new Event('input', { bubbles: true }));
        }
    }

    function loadMediaItems(autoSelectId = null) {
        const filterType = getElement('mediaFilterType');
        const filterDate = getElement('mediaFilterDate');
        const searchInput = getElement('mediaSearchInput');

        const type = filterType ? filterType.value : '';
        const date = filterDate ? filterDate.value : '';
        const search = searchInput ? searchInput.value.trim() : '';

        const params = new URLSearchParams();
        if (type) params.append('type', type);
        if (date) params.append('date', date);
        if (search) params.append('search', search);

        fetch(`/admin/media?${params.toString()}`, {
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                currentMediaList = data.mediaItems.data || [];
                renderGrid(autoSelectId);
                syncFeaturedImageAltFromLibrary();
            }
        })
        .catch(err => console.error('Failed loading media:', err));
    }

    async function saveMediaDetails() {
        updateDebounceTimer = null;
        
        const detailsMediaId = getElement('detailsMediaId');
        const mediaId = (detailsMediaId && detailsMediaId.value) ? detailsMediaId.value : (selectedMedia ? selectedMedia.id : null);
        if (!mediaId) return null;

        const detailsAltText = getElement('detailsAltText');
        const detailsTitle = getElement('detailsTitle');
        const detailsCaption = getElement('detailsCaption');
        const detailsDescription = getElement('detailsDescription');

        const payload = {
            alt_text: detailsAltText ? detailsAltText.value.trim() : '',
            title: detailsTitle ? detailsTitle.value.trim() : '',
            caption: detailsCaption ? detailsCaption.value.trim() : '',
            description: detailsDescription ? detailsDescription.value.trim() : ''
        };

        const metaCsrf = document.querySelector('meta[name="csrf-token"]');
        const inputCsrf = document.querySelector('input[name="_token"]');
        const csrfToken = metaCsrf ? metaCsrf.getAttribute('content') : (inputCsrf ? inputCsrf.value : '');

        try {
            const res = await fetch(`/admin/media/${mediaId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRF-TOKEN': csrfToken,
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            if (data.success && data.media) {
                if (selectedMedia && selectedMedia.id === data.media.id) {
                    selectedMedia.alt_text = data.media.alt_text;
                    selectedMedia.title = data.media.title;
                    selectedMedia.caption = data.media.caption;
                    selectedMedia.description = data.media.description;
                }
                const foundInList = currentMediaList.find(m => m.id === data.media.id);
                if (foundInList) {
                    foundInList.alt_text = data.media.alt_text;
                    foundInList.title = data.media.title;
                    foundInList.caption = data.media.caption;
                    foundInList.description = data.media.description;
                }
                const imgPreview = getElement('featuredImagePreview');
                if (imgPreview) {
                    imgPreview.alt = data.media.alt_text || '';
                    imgPreview.setAttribute('alt', data.media.alt_text || '');
                    imgPreview.dispatchEvent(new Event('input', { bubbles: true }));
                }
                if (typeof window.runRankMathAnalysis === 'function') {
                    window.runRankMathAnalysis();
                }
                return data.media;
            }
        } catch (err) {
            console.error('Failed saving media details:', err);
        }
        return null;
    }

    // Initialize Event Delegation on Document
    function setupEventDelegation() {
        // Global Input Listener for Auto-Save
        document.addEventListener('input', function (e) {
            if (!e.target || !e.target.id) return;
            if (['detailsAltText', 'detailsTitle', 'detailsCaption', 'detailsDescription'].includes(e.target.id)) {
                const detailsAltText = getElement('detailsAltText');
                const imgPreview = getElement('featuredImagePreview');

                if (imgPreview && detailsAltText) {
                    imgPreview.alt = detailsAltText.value;
                    imgPreview.setAttribute('alt', detailsAltText.value);
                    imgPreview.dispatchEvent(new Event('input', { bubbles: true }));
                }

                clearTimeout(updateDebounceTimer);
                updateDebounceTimer = setTimeout(saveMediaDetails, 300);
            }
        });

        // Global Click Listener for Delete and Set Featured
        document.addEventListener('click', async function (e) {
            if (!e.target) return;

            // Delete Permanently Button
            const deleteBtn = e.target.closest('#detailsDeleteBtn');
            if (deleteBtn) {
                e.preventDefault();
                e.stopPropagation();

                const detailsMediaId = getElement('detailsMediaId');
                const mediaId = (detailsMediaId && detailsMediaId.value) ? detailsMediaId.value : (selectedMedia ? selectedMedia.id : null);
                if (!mediaId) return;

                deleteBtn.textContent = 'Deleting...';

                const metaCsrfDel = document.querySelector('meta[name="csrf-token"]');
                const inputCsrfDel = document.querySelector('input[name="_token"]');
                const csrfToken = metaCsrfDel ? metaCsrfDel.getAttribute('content') : (inputCsrfDel ? inputCsrfDel.value : '');

                try {
                    await fetch(`/admin/media/${mediaId}`, {
                        method: 'DELETE',
                        headers: {
                            'X-CSRF-TOKEN': csrfToken,
                            'Accept': 'application/json',
                            'X-Requested-With': 'XMLHttpRequest'
                        }
                    });
                } catch (err) {
                    console.error('Delete failed:', err);
                } finally {
                    clearSelection();
                    loadMediaItems();
                }
                return;
            }

            // Set Featured Image Button
            const setFeaturedBtn = e.target.closest('#mediaModalSetFeaturedBtn');
            if (setFeaturedBtn) {
                e.preventDefault();
                e.stopPropagation();

                if (!selectedMedia) {
                    const detailsMediaId = getElement('detailsMediaId');
                    const mediaId = detailsMediaId ? parseInt(detailsMediaId.value) : null;
                    if (mediaId) {
                        selectedMedia = currentMediaList.find(m => m.id === mediaId);
                    }
                }

                if (!selectedMedia) return;

                const originalText = setFeaturedBtn.innerHTML;
                setFeaturedBtn.disabled = true;
                setFeaturedBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-1" role="status"></span> Saving...';

                await saveMediaDetails();

                const detailsAltText = getElement('detailsAltText');
                const finalAlt = detailsAltText ? detailsAltText.value.trim() : (selectedMedia.alt_text || '');
                selectedMedia.alt_text = finalAlt;

                const imgPreview = getElement('featuredImagePreview');
                const hiddenPathInput = getElement('featuredImagePathInput');

                if (imgPreview) {
                    imgPreview.src = selectedMedia.url;
                    imgPreview.alt = finalAlt;
                    imgPreview.setAttribute('alt', finalAlt);
                    imgPreview.classList.remove('d-none');
                    imgPreview.dispatchEvent(new Event('input', { bubbles: true }));
                }

                const removeBtn = getElement('removeFeaturedImageBtn');
                if (removeBtn) removeBtn.classList.remove('d-none');

                if (hiddenPathInput) {
                    hiddenPathInput.value = selectedMedia.filepath;
                    hiddenPathInput.dispatchEvent(new Event('input', { bubbles: true }));
                    hiddenPathInput.dispatchEvent(new Event('change', { bubbles: true }));
                }

                if (typeof window.runRankMathAnalysis === 'function') {
                    window.runRankMathAnalysis();
                }

                setFeaturedBtn.disabled = false;
                setFeaturedBtn.innerHTML = originalText;

                const modalEl = getElement('featuredImageModal');
                if (modalEl && window.bootstrap) {
                    const modal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
                    modal.hide();
                }
            }
        });

        const editForm = getElement('editForm');
        if (editForm) {
            editForm.addEventListener('submit', function (e) {
                if (updateDebounceTimer) {
                    e.preventDefault();
                    clearTimeout(updateDebounceTimer);
                    updateDebounceTimer = null;
                    const form = this;
                    saveMediaDetails().finally(() => {
                        form.submit();
                    });
                }
            });
        }
    }

    // Auto-initialize
    setupEventDelegation();
    loadMediaItems();

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadMediaItems);
    }

    window.reloadMediaLibrary = loadMediaItems;
})();
