/**
 * RankMath Real-Time SEO Analyzer Engine
 */
document.addEventListener('DOMContentLoaded', function () {
    const postTitleInput = document.getElementById('postTitle');
    const slugInput = document.querySelector('input[name="slug"]');
    const excerptInput = document.querySelector('textarea[name="excerpt"]');
    const contentInput = document.getElementById('contentInput');

    const focusKeywordInput = document.getElementById('rmFocusKeywordInput');
    const isPillarCheckbox = document.getElementById('rmIsPillarCheckbox');
    
    // Modal Snippet inputs
    const modalSeoTitle = document.getElementById('rmModalSeoTitle');
    const modalSlug = document.getElementById('rmModalSlug');
    const modalSeoDescription = document.getElementById('rmModalSeoDescription');

    // Hidden form inputs
    const hiddenSeoTitle = document.getElementById('hiddenSeoTitle');
    const hiddenSeoDescription = document.getElementById('hiddenSeoDescription');
    const hiddenFocusKeyword = document.getElementById('hiddenFocusKeyword');
    const hiddenIsPillar = document.getElementById('hiddenIsPillar');
    const hiddenSeoScore = document.getElementById('hiddenSeoScore');

    // UI elements for SERP Preview
    const serpUrlDisplay = document.getElementById('rmSerpUrlDisplay');
    const serpTitleDisplay = document.getElementById('rmSerpTitleDisplay');
    const serpDescDisplay = document.getElementById('rmSerpDescDisplay');

    // Score Badges
    const topScoreBadge = document.getElementById('rankMathTopScoreBadge');
    const drawerScoreBadge = document.getElementById('rankMathDrawerScoreBadge');

    // Checks Container UI Elements
    const basicSeoCount = document.getElementById('rmBasicSeoCount');
    const additionalSeoCount = document.getElementById('rmAdditionalSeoCount');
    const titleReadabilityCount = document.getElementById('rmTitleReadabilityCount');

    let isKeywordUsedBefore = false;

    // Power words and sentiment words dictionaries
    const powerWords = ['ultimate', 'proven', 'secret', 'fast', 'complete', 'how to', 'fix', 'top', 'best', 'guide', 'easy', 'step-by-step', 'essential', 'free', 'amazing', 'hacks', 'simple', 'pro', 'review'];
    const sentimentWords = ['good', 'bad', 'great', 'awesome', 'terrible', 'worst', 'best', 'happy', 'sad', 'love', 'hate', 'fix', 'error', 'bug', 'solution', 'problem', 'fail', 'win', 'effective', 'easy', 'difficult'];

    // Real-Time Listener Setup
    const inputEvents = ['input', 'change', 'keyup', 'blur'];

    [postTitleInput, slugInput, excerptInput, contentInput, modalSeoTitle, modalSlug, modalSeoDescription, focusKeywordInput, isPillarCheckbox].forEach(el => {
        if (!el) return;
        inputEvents.forEach(evt => {
            el.addEventListener(evt, function() {
                syncAllFields();
                runAnalysis();
            });
        });
    });

    function syncAllFields() {
        if (focusKeywordInput && hiddenFocusKeyword) {
            hiddenFocusKeyword.value = focusKeywordInput.value;
            updateKeywordBadgesUI(focusKeywordInput.value);
        }
        if (isPillarCheckbox && hiddenIsPillar) {
            hiddenIsPillar.value = isPillarCheckbox.checked ? '1' : '0';
        }
        if (modalSeoTitle && hiddenSeoTitle) {
            hiddenSeoTitle.value = modalSeoTitle.value;
        }
        if (modalSeoDescription && hiddenSeoDescription) {
            hiddenSeoDescription.value = modalSeoDescription.value;
        }
        if (modalSlug && slugInput) {
            slugInput.value = modalSlug.value;
        }
    }

    function updateKeywordBadgesUI(keyword) {
        const container = document.getElementById('rmKeywordBadgesContainer');
        if (!container) return;
        const kw = (keyword || '').trim();
        if (kw) {
            container.innerHTML = `
                <span class="badge bg-success d-inline-flex align-items-center gap-1 px-2 py-1 fs-6">
                    <i class="fas fa-star me-1 text-warning" style="font-size: 0.75rem;"></i>
                    <span>${escapeHtml(kw)}</span>
                </span>
            `;
        } else {
            container.innerHTML = '';
        }
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    if (modalSeoTitle) {
        modalSeoTitle.addEventListener('input', function() {
            if (hiddenSeoTitle) hiddenSeoTitle.value = this.value;
            updateSerpPreview();
        });
    }

    if (modalSlug) {
        modalSlug.addEventListener('input', function() {
            if (slugInput) slugInput.value = this.value;
            updateSerpPreview();
        });
    }

    if (modalSeoDescription) {
        modalSeoDescription.addEventListener('input', function() {
            if (hiddenSeoDescription) hiddenSeoDescription.value = this.value;
            if (excerptInput && !excerptInput.value) excerptInput.value = this.value;
            updateSerpPreview();
        });
    }

    if (focusKeywordInput) {
        focusKeywordInput.addEventListener('change', checkKeywordUniqueness);
        focusKeywordInput.addEventListener('input', function() {
            if (hiddenFocusKeyword) hiddenFocusKeyword.value = this.value;
            updateKeywordBadgesUI(this.value);
        });
    }

    if (isPillarCheckbox) {
        isPillarCheckbox.addEventListener('change', function() {
            if (hiddenIsPillar) hiddenIsPillar.value = this.checked ? '1' : '0';
        });
    }

    // Modal sync button
    const saveSnippetBtn = document.getElementById('rmSaveSnippetBtn');
    if (saveSnippetBtn) {
        saveSnippetBtn.addEventListener('click', function() {
            if (hiddenSeoTitle && modalSeoTitle) hiddenSeoTitle.value = modalSeoTitle.value;
            if (hiddenSeoDescription && modalSeoDescription) hiddenSeoDescription.value = modalSeoDescription.value;
            if (slugInput && modalSlug) slugInput.value = modalSlug.value;
            
            updateSerpPreview();
            runAnalysis();
            
            const modalEl = document.getElementById('editSnippetModal');
            if (modalEl && window.bootstrap) {
                const modal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
                modal.hide();
            }
        });
    }

    // Form Submit Hook to guarantee EditorJS and hidden fields are populated before POST
    const editForm = document.getElementById('editForm');
    if (editForm) {
        editForm.addEventListener('submit', function(e) {
            if (window.editorInstance && typeof window.editorInstance.save === 'function' && !editForm.dataset.isSubmitting) {
                e.preventDefault();
                editForm.dataset.isSubmitting = 'true';
                window.editorInstance.save().then((outputData) => {
                    if (contentInput) {
                        contentInput.value = JSON.stringify(outputData);
                    }
                    syncAllFields();
                    runAnalysis();
                    editForm.submit();
                }).catch(() => {
                    syncAllFields();
                    runAnalysis();
                    editForm.submit();
                });
            } else {
                syncAllFields();
                runAnalysis();
            }
        });
    }

    // Check keyword uniqueness via AJAX
    function checkKeywordUniqueness() {
        const kw = focusKeywordInput ? focusKeywordInput.value.trim() : '';
        if (!kw) {
            isKeywordUsedBefore = false;
            runAnalysis();
            return;
        }

        const postId = document.getElementById('postIdInput') ? document.getElementById('postIdInput').value : null;

        fetch('/admin/posts/check-keyword', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]') ? document.querySelector('meta[name="csrf-token"]').getAttribute('content') : ''
            },
            body: JSON.stringify({ keyword: kw, post_id: postId })
        })
        .then(res => res.json())
        .then(data => {
            isKeywordUsedBefore = data.used || false;
            runAnalysis();
        })
        .catch(() => {
            isKeywordUsedBefore = false;
            runAnalysis();
        });
    }

    function updateSerpPreview() {
        const rawTitle = (modalSeoTitle && modalSeoTitle.value.trim()) || (postTitleInput ? postTitleInput.value.trim() : '') || 'Post Title';
        const rawSlug = (modalSlug && modalSlug.value.trim()) || (slugInput ? slugInput.value.trim() : '') || 'post-slug';
        const rawDesc = (modalSeoDescription && modalSeoDescription.value.trim()) || (excerptInput ? excerptInput.value.trim() : '') || 'Please provide a meta description by editing the snippet below.';

        const currentHost = window.location.origin;
        if (serpUrlDisplay) serpUrlDisplay.textContent = `${currentHost}/blog/${rawSlug}`;
        if (serpTitleDisplay) serpTitleDisplay.textContent = rawTitle;
        if (serpDescDisplay) serpDescDisplay.textContent = rawDesc;
    }

    function getHtmlContent() {
        let content = contentInput ? contentInput.value : '';
        // If content is stored as EditorJS JSON, extract text & HTML from all block types
        if (content && content.trim().startsWith('{')) {
            try {
                const json = JSON.parse(content);
                if (json.blocks && Array.isArray(json.blocks)) {
                    content = json.blocks.map(b => {
                        if (!b.data) return '';
                        if (typeof b.data.text === 'string') return b.data.text;
                        if (typeof b.data.html === 'string') return b.data.html;
                        if (typeof b.data.code === 'string') return b.data.code;
                        if (b.type === 'image' || b.data.file) {
                            const imgUrl = (b.data.file && b.data.file.url) ? b.data.file.url : '';
                            const altText = b.data.alt || b.data.caption || '';
                            const captionText = b.data.caption || '';
                            return `<img src="${imgUrl}" alt="${altText}"> ${captionText}`;
                        }
                        if (Array.isArray(b.data.items)) {
                            return b.data.items.map(item => typeof item === 'string' ? item : (item.content || '')).join(' ');
                        }
                        return '';
                    }).join(' ');
                }
            } catch (e) {}
        }
        return content;
    }

    function runAnalysis() {
        updateSerpPreview();
        window.runRankMathAnalysis = runAnalysis;

        const title = (modalSeoTitle && modalSeoTitle.value.trim()) || (postTitleInput ? postTitleInput.value.trim() : '');
        const slug = (modalSlug && modalSlug.value.trim()) || (slugInput ? slugInput.value.trim() : '');
        const description = (modalSeoDescription && modalSeoDescription.value.trim()) || (excerptInput ? excerptInput.value.trim() : '');
        const keyword = focusKeywordInput ? focusKeywordInput.value.trim().toLowerCase() : '';
        const htmlContent = getHtmlContent();
        
        // Strip HTML tags for clean text analysis
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = htmlContent;
        const textContent = tempDiv.textContent || tempDiv.innerText || '';
        const words = textContent.trim() ? textContent.trim().split(/\s+/).filter(w => w.length > 0) : [];
        const wordCount = words.length;

        let totalScore = 0;

        // Basic SEO Checks
        let basicPassed = 0;
        let basicTotal = 6;

        // 1. Keyword in SEO Title
        const hasKwInTitle = keyword.length > 0 && title.toLowerCase().includes(keyword);
        updateCheckUI('check_kw_title', hasKwInTitle, `Hurray! You're using Focus Keyword in the SEO Title.`, `Focus Keyword not found in SEO Title.`);
        if (hasKwInTitle) { totalScore += 8; basicPassed++; }

        // 2. Keyword in Meta Description
        const hasKwInDesc = keyword.length > 0 && description.toLowerCase().includes(keyword);
        updateCheckUI('check_kw_desc', hasKwInDesc, `Focus Keyword used inside SEO Meta Description.`, `Focus Keyword missing from SEO Meta Description.`);
        if (hasKwInDesc) { totalScore += 7; basicPassed++; }

        // 3. Keyword in URL
        const kwSlugFormat = keyword.replace(/\s+/g, '-');
        const hasKwInUrl = keyword.length > 0 && (slug.toLowerCase().includes(kwSlugFormat) || slug.toLowerCase().includes(keyword));
        updateCheckUI('check_kw_url', hasKwInUrl, `Focus Keyword used in the URL.`, `Focus Keyword not found in the URL.`);
        if (hasKwInUrl) { totalScore += 7; basicPassed++; }

        // 4. Keyword in first 10% of content
        const first10PercentWords = words.slice(0, Math.max(10, Math.floor(words.length * 0.1))).join(' ').toLowerCase();
        const hasKwFirst10 = keyword.length > 0 && first10PercentWords.includes(keyword);
        updateCheckUI('check_kw_first10', hasKwFirst10, `Focus Keyword appears in the first 10% of the content.`, `Focus Keyword does not appear in the first 10% of the content.`);
        if (hasKwFirst10) { totalScore += 6; basicPassed++; }

        // 5. Keyword in content body
        const hasKwInContent = keyword.length > 0 && textContent.toLowerCase().includes(keyword);
        updateCheckUI('check_kw_content', hasKwInContent, `Focus Keyword found in the content.`, `Focus Keyword not found in content.`);
        if (hasKwInContent) { totalScore += 6; basicPassed++; }

        // 6. Content word count
        const isWordCountGood = wordCount >= 600;
        updateCheckUI('check_word_count', isWordCountGood, `Content is ${wordCount} words long. Good job!`, `Content is only ${wordCount} words long. Consider adding more content (600+ words).`);
        if (isWordCountGood) { totalScore += 6; basicPassed++; }
        else if (wordCount >= 300) { totalScore += 3; }

        if (basicSeoCount) {
            basicSeoCount.textContent = (basicPassed === basicTotal) ? 'All Good' : `${basicTotal - basicPassed} Errors`;
            basicSeoCount.className = (basicPassed === basicTotal) ? 'badge bg-success' : 'badge bg-danger';
        }

        // Additional SEO Checks
        let additionalPassed = 0;
        let additionalTotal = 8;

        // 1. Keyword in subheadings (H2, H3)
        const subheadings = Array.from(tempDiv.querySelectorAll('h1, h2, h3, h4, h5, h6')).map(h => h.textContent.toLowerCase());
        const hasKwInSubheading = keyword.length > 0 && subheadings.some(h => h.includes(keyword));
        updateCheckUI('check_kw_subheading', hasKwInSubheading, `Focus Keyword found in subheading(s).`, `Focus Keyword not found in subheading(s).`);
        if (hasKwInSubheading) { totalScore += 5; additionalPassed++; }

        // 2. Keyword in Image Alt Attributes (checks content images + featured image)
        const imgAlts = Array.from(tempDiv.querySelectorAll('img')).map(img => (img.getAttribute('alt') || img.alt || '').toLowerCase());
        const featuredImg = document.getElementById('featuredImagePreview');
        if (featuredImg) {
            const featuredAlt = (featuredImg.alt || featuredImg.getAttribute('alt') || '').toLowerCase();
            if (featuredAlt) {
                imgAlts.push(featuredAlt);
            }
        }
        const hasKwInImgAlt = keyword.length > 0 && imgAlts.some(alt => alt.includes(keyword));
        updateCheckUI('check_kw_img_alt', hasKwInImgAlt, `Focus Keyword found in image alt attribute(s).`, `Focus Keyword missing from image alt attribute(s).`);
        if (hasKwInImgAlt) { totalScore += 4; additionalPassed++; }

        // 3. Keyword Density
        let kwMatches = 0;
        if (keyword.length > 0 && wordCount > 0) {
            const regex = new RegExp(keyword.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&'), 'gi');
            const matches = textContent.match(regex);
            kwMatches = matches ? matches.length : 0;
        }
        const density = wordCount > 0 ? ((kwMatches / wordCount) * 100).toFixed(2) : 0;
        const isDensityGood = density >= 0.75 && density <= 2.5;
        updateCheckUI('check_kw_density', isDensityGood, `Keyword Density is ${density}%, the Focus Keyword appears ${kwMatches} times.`, `Keyword Density is ${density}%. Aim for 0.75% to 2.5%.`);
        if (isDensityGood) { totalScore += 5; additionalPassed++; }

        // 4. URL Length
        const isUrlLengthGood = slug.length > 0 && slug.length <= 75;
        updateCheckUI('check_url_length', isUrlLengthGood, `URL is ${slug.length} characters long. Kudos!`, `URL is ${slug.length} characters long. Try keeping it under 75 characters.`);
        if (isUrlLengthGood) { totalScore += 4; additionalPassed++; }

        // Link Detection Setup
        const currentHost = window.location.hostname;
        const links = Array.from(tempDiv.querySelectorAll('a'));

        // 5. External Links
        const externalLinks = links.filter(a => {
            const href = (a.getAttribute('href') || '').trim();
            if (!href) return false;
            // External link starts with http://, https://, or // and doesn't point to current local host
            if (href.startsWith('http://') || href.startsWith('https://') || href.startsWith('//')) {
                return !href.includes(currentHost) && !href.includes('127.0.0.1') && !href.includes('localhost');
            }
            // Domain link typed without protocol (e.g., youtube.com)
            if (/^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/.test(href)) {
                return !href.includes(currentHost) && !href.includes('127.0.0.1') && !href.includes('localhost');
            }
            return false;
        });
        const hasExternalLinks = externalLinks.length > 0;
        updateCheckUI('check_external_links', hasExternalLinks, `Great! You are linking to external resources.`, `No external links found. Add links to relevant external authority sources.`);
        if (hasExternalLinks) { totalScore += 5; additionalPassed++; }

        // 6. External Link DoFollow
        const hasDoFollowExternal = externalLinks.some(a => {
            const rel = a.getAttribute('rel') || '';
            return !rel.includes('nofollow');
        });
        updateCheckUI('check_dofollow_links', hasDoFollowExternal, `At least one external link with DoFollow found in your content.`, `Add at least one DoFollow external link.`);
        if (hasDoFollowExternal) { totalScore += 4; additionalPassed++; }

        // 7. Internal Links
        const internalLinks = links.filter(a => {
            const href = (a.getAttribute('href') || '').trim();
            if (!href) return false;
            return href.startsWith('/') || href.startsWith('#') || href.includes(currentHost) || href.includes('127.0.0.1') || href.includes('localhost');
        });
        const hasInternalLinks = internalLinks.length > 0;
        updateCheckUI('check_internal_links', hasInternalLinks, `You are linking to other resources on your website which is great.`, `No internal links found. Link to other pages/posts on your site.`);
        if (hasInternalLinks) { totalScore += 4; additionalPassed++; }

        // 8. Keyword Uniqueness
        const isKeywordUnique = !isKeywordUsedBefore;
        updateCheckUI('check_kw_unique', isKeywordUnique, `You haven't used this Focus Keyword before.`, `You have already used this Focus Keyword in another post.`);
        if (isKeywordUnique) { totalScore += 4; additionalPassed++; }

        if (additionalSeoCount) {
            additionalSeoCount.textContent = (additionalPassed === additionalTotal) ? 'All Good' : `${additionalTotal - additionalPassed} Errors`;
            additionalSeoCount.className = (additionalPassed === additionalTotal) ? 'badge bg-success' : 'badge bg-danger';
        }

        // Title Readability Checks
        let titlePassed = 0;
        let titleTotal = 4;

        // 1. Keyword at beginning of SEO Title
        const isKwAtTitleStart = keyword.length > 0 && title.toLowerCase().startsWith(keyword);
        updateCheckUI('check_title_kw_start', isKwAtTitleStart, `Focus Keyword used at the beginning of SEO title.`, `Focus Keyword is not at the beginning of SEO title.`);
        if (isKwAtTitleStart) { totalScore += 7; titlePassed++; }

        // 2. Title Sentiment
        const hasSentiment = sentimentWords.some(w => title.toLowerCase().includes(w));
        updateCheckUI('check_title_sentiment', hasSentiment, `Your title has a positive or a negative sentiment.`, `Your title doesn't convey positive or negative sentiment.`);
        if (hasSentiment) { totalScore += 6; titlePassed++; }

        // 3. Title Power Word
        const hasPowerWord = powerWords.some(w => title.toLowerCase().includes(w));
        updateCheckUI('check_title_power_word', hasPowerWord, `Your title contains a power word!`, `Your title doesn't contain a power word. Add at least one.`);
        if (hasPowerWord) { totalScore += 6; titlePassed++; }

        // 4. Number in Title
        const hasNumberInTitle = /\d+/.test(title);
        updateCheckUI('check_title_number', hasNumberInTitle, `Your SEO title contains a number.`, `Your SEO title doesn't contain a number.`);
        if (hasNumberInTitle) { totalScore += 6; titlePassed++; }

        if (titleReadabilityCount) {
            titleReadabilityCount.textContent = (titlePassed === titleTotal) ? 'All Good' : `${titleTotal - titlePassed} Errors`;
            titleReadabilityCount.className = (titlePassed === titleTotal) ? 'badge bg-success' : 'badge bg-danger';
        }

        // Cap score at 100
        totalScore = Math.min(100, Math.max(0, totalScore));
        if (hiddenSeoScore) hiddenSeoScore.value = totalScore;

        // Update Score Badges UI
        updateScoreBadgeUI(topScoreBadge, totalScore);
        updateScoreBadgeUI(drawerScoreBadge, totalScore);
    }

    function updateCheckUI(elementId, isPassed, passText, failText) {
        const el = document.getElementById(elementId);
        if (!el) return;

        const iconEl = el.querySelector('.check-icon');
        const textEl = el.querySelector('.check-text');

        if (isPassed) {
            if (iconEl) iconEl.className = 'check-icon fas fa-check-circle text-success me-2';
            if (textEl) textEl.textContent = passText;
        } else {
            if (iconEl) iconEl.className = 'check-icon fas fa-times-circle text-danger me-2';
            if (textEl) textEl.textContent = failText;
        }
    }

    function updateScoreBadgeUI(badgeEl, score) {
        if (!badgeEl) return;

        let bgStyle, textColor, borderStyle;
        if (score >= 80) {
            bgStyle = '#22c55e';
            textColor = '#ffffff';
            borderStyle = '1px solid #16a34a';
        } else if (score >= 50) {
            bgStyle = '#eab308';
            textColor = '#ffffff';
            borderStyle = '1px solid #ca8a04';
        } else {
            bgStyle = '#ef4444';
            textColor = '#ffffff';
            borderStyle = '1px solid #dc2626';
        }

        badgeEl.style.backgroundColor = bgStyle;
        badgeEl.style.color = textColor;
        badgeEl.style.border = borderStyle;
        badgeEl.innerHTML = `<i class="fas fa-chart-line me-1"></i> <strong>${score} / 100</strong>`;
    }

    // Initial Run
    runAnalysis();
    checkKeywordUniqueness();
});
