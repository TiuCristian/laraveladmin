import os
import re
import sys
import urllib.parse
import urllib.request
from urllib.error import HTTPError, URLError

# -------- CONFIG --------
PAGES = [
    "https://themeger.shop/html/katen/html/index.html",
    "https://themeger.shop/html/katen/html/personal.html",
    "https://themeger.shop/html/katen/html/personal-alt.html",
    "https://themeger.shop/html/katen/html/minimal.html",
    "https://themeger.shop/html/katen/html/classic.html",
    "https://themeger.shop/html/katen/html/category.html",
    "https://themeger.shop/html/katen/html/blog-single.html",
    "https://themeger.shop/html/katen/html/blog-single-alt.html",
    "https://themeger.shop/html/katen/html/about.html",
    "https://themeger.shop/html/katen/html/contact.html",
]

# Where to save files (Windows path)
PROJECT_ROOT = r"C:\laragon\www\katen"

# Only download these extensions
ASSET_EXTS = {
    ".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".ico", ".avif",
    # if you also want fonts/media later, add: ".woff", ".woff2", ".ttf", ".mp4", ...
}

# -------- HELPERS --------
def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def read_url(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def is_asset_url(url: str) -> bool:
    u = url.split("#")[0].split("?")[0].strip()
    _, ext = os.path.splitext(u.lower())
    return ext in ASSET_EXTS

def clean_token(s: str) -> str:
    return s.strip().strip('"').strip("'").strip()

def absolutize(ref: str, base_url: str) -> str:
    """
    Turn relative/protocol-relative URLs into absolute URLs.
    """
    ref = clean_token(ref)
    if not ref or ref.startswith("data:") or ref.startswith("javascript:"):
        return ""
    if ref.startswith("//"):
        return "https:" + ref
    return urllib.parse.urljoin(base_url, ref)

def guess_local_path(asset_url: str) -> str:
    """
    Map an asset URL to a local path under PROJECT_ROOT.
    Keeps the URL path as-is (best for templates).
    Example:
      https://themeger.shop/html/katen/html/images/logo.svg
      -> C:\laragon\www\katen\html\katen\html\images\logo.svg   (too deep)
    So we trim common prefixes and keep from the theme folder down.
    """
    u = urllib.parse.urlparse(asset_url)
    path = u.path.lstrip("/")

    # Heuristic: most assets for this template live under /html/katen/html/
    # Keep only what comes AFTER that prefix, so it lands nicely in your local root.
    marker = "html/katen/html/"
    if marker in path:
        path = path.split(marker, 1)[1]

    # If still empty, fallback to basename
    if not path:
        path = os.path.basename(u.path)

    return os.path.join(PROJECT_ROOT, *path.split("/"))

def download(asset_url: str) -> bool:
    dest = guess_local_path(asset_url)
    ensure_dir(os.path.dirname(dest))

    if os.path.exists(dest):
        print(f"SKIP (exists): {dest}")
        return True

    try:
        data = read_url(asset_url)
        with open(dest, "wb") as f:
            f.write(data)
        print(f"OK   {asset_url} -> {dest}")
        return True
    except HTTPError as e:
        print(f"FAIL {e.code}: {asset_url}")
    except URLError as e:
        print(f"FAIL URL: {asset_url} ({e})")
    except Exception as e:
        print(f"FAIL ???: {asset_url} ({e})")
    return False

# -------- EXTRACTORS --------
RE_ATTR_URL = re.compile(r"""(?:src|href|content)\s*=\s*["']([^"']+)["']""", re.I)
RE_SRCSET = re.compile(r"""srcset\s*=\s*["']([^"']+)["']""", re.I)
RE_CSS_URL = re.compile(r"""url\(([^)]+)\)""", re.I)
RE_STYLE_BLOCK = re.compile(r"""<style[^>]*>(.*?)</style>""", re.I | re.S)
RE_LINK_STYLESHEET = re.compile(
    r"""<link[^>]+rel\s*=\s*["']stylesheet["'][^>]*href\s*=\s*["']([^"']+)["']""",
    re.I
)

def extract_assets_from_html(html: str, page_url: str) -> tuple[set[str], set[str]]:
    """
    Returns: (asset_urls, css_urls)
    """
    assets = set()
    css_urls = set()

    # src/href/content attributes (includes icons, og:image etc.)
    for m in RE_ATTR_URL.findall(html):
        url = absolutize(m, page_url)
        if not url:
            continue
        if is_asset_url(url):
            assets.add(url)

    # srcset (pick each URL before the descriptor)
    for block in RE_SRCSET.findall(html):
        parts = [p.strip() for p in block.split(",")]
        for part in parts:
            if not part:
                continue
            first = part.split()[0]
            url = absolutize(first, page_url)
            if url and is_asset_url(url):
                assets.add(url)

    # inline style="...url(...)..."
    for m in RE_CSS_URL.findall(html):
        url = absolutize(m, page_url)
        if url and is_asset_url(url):
            assets.add(url)

    # <style> blocks (CSS inside HTML)
    for css in RE_STYLE_BLOCK.findall(html):
        for m in RE_CSS_URL.findall(css):
            url = absolutize(m, page_url)
            if url and is_asset_url(url):
                assets.add(url)

    # linked stylesheets
    for href in RE_LINK_STYLESHEET.findall(html):
        url = absolutize(href, page_url)
        if url:
            css_urls.add(url)

    return assets, css_urls

def extract_assets_from_css(css: str, css_url: str) -> set[str]:
    assets = set()
    for m in RE_CSS_URL.findall(css):
        url = absolutize(m, css_url)
        if url and is_asset_url(url):
            assets.add(url)
    return assets

def main():
    ensure_dir(PROJECT_ROOT)

    all_assets = set()
    all_css = set()

    # 1) Scan all pages
    for page_url in PAGES:
        try:
            html_bytes = read_url(page_url)
            html = html_bytes.decode("utf-8", errors="ignore")
        except Exception as e:
            print(f"PAGE FAIL: {page_url} ({e})")
            continue

        assets, css_urls = extract_assets_from_html(html, page_url)
        all_assets |= assets
        all_css |= css_urls
        print(f"Scanned page: {page_url} | assets: {len(assets)} | css: {len(css_urls)}")

    # 2) Download & scan CSS
    css_assets = set()
    for css_url in sorted(all_css):
        try:
            css_bytes = read_url(css_url)
            css_text = css_bytes.decode("utf-8", errors="ignore")
            found = extract_assets_from_css(css_text, css_url)
            css_assets |= found
            print(f"Scanned css:  {css_url} | assets: {len(found)}")
        except Exception as e:
            print(f"CSS FAIL: {css_url} ({e})")

    all_assets |= css_assets

    # 3) Download assets
    print(f"\nFound {len(all_assets)} total asset URLs. Downloading...\n")
    ok = 0
    fail = 0
    for asset_url in sorted(all_assets):
        if download(asset_url):
            ok += 1
        else:
            fail += 1

    print(f"\nDone. Success: {ok}, Failed: {fail}")
    if fail:
        print("Some assets may be blocked, missing, or referenced dynamically via JS.")

if __name__ == "__main__":
    main()