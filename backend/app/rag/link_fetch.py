import ipaddress
import socket
from urllib.parse import urlparse

import requests
import trafilatura

FETCH_TIMEOUT_SECONDS = 10
MAX_RESPONSE_BYTES = 5_000_000
USER_AGENT = "Mozilla/5.0 (compatible; SciOlympiadCoachBot/1.0)"


def _assert_safe_url(url: str) -> None:
    """Reject anything that isn't a plain public http(s) URL.

    The server fetches whatever URL a coach pastes in, and this app is now
    shared across ~13 people rather than run by one operator locally -- so a
    request for http://localhost:8000/... or a cloud metadata address
    (169.254.169.254) needs to be rejected before we ever make the request,
    not just discouraged.
    """
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError("Only http/https URLs are supported.")
    if not parsed.hostname:
        raise ValueError("URL has no hostname.")

    try:
        addr_info = socket.getaddrinfo(parsed.hostname, None)
    except socket.gaierror as e:
        raise ValueError(f"Could not resolve host: {parsed.hostname}") from e

    for family, _, _, _, sockaddr in addr_info:
        ip = ipaddress.ip_address(sockaddr[0])
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
            raise ValueError("URL resolves to a private/internal address, which isn't allowed.")


def fetch_url_text(url: str) -> tuple[str, str]:
    """Fetch a URL and extract its main readable content.

    Returns (title, text). Raises ValueError with a message safe to show the
    coach directly if the URL is disallowed, unreachable, or has nothing
    trafilatura considers extractable (e.g. a page that's mostly JS/nav).
    """
    # Best-effort guard, not airtight: we resolve+check here, then `requests`
    # resolves again to actually connect, so a DNS-rebinding attacker could in
    # theory slip past it. Good enough for a small known group of coaches;
    # revisit with a pinned-IP fetch if this app ever opens up more widely.
    _assert_safe_url(url)

    # Fetch with `requests` rather than trafilatura's own downloader: `requests`
    # honors the REQUESTS_CA_BUNDLE env var app/config.py sets for the local
    # antivirus-intercepted-HTTPS workaround (see README "Windows note (SSL)");
    # trafilatura's urllib3-based fetcher doesn't, and fails silently there.
    try:
        response = requests.get(
            url,
            timeout=FETCH_TIMEOUT_SECONDS,
            headers={"User-Agent": USER_AGENT},
            stream=True,
        )
        response.raise_for_status()
        content = response.raw.read(MAX_RESPONSE_BYTES + 1, decode_content=True)
    except requests.RequestException as e:
        raise ValueError("Couldn't fetch that URL -- it may be down, blocking automated requests, or slow to respond.") from e

    if len(content) > MAX_RESPONSE_BYTES:
        raise ValueError("That page is too large to ingest.")

    downloaded = content.decode(response.encoding or "utf-8", errors="ignore")

    text = trafilatura.extract(downloaded, include_comments=False, include_tables=False)
    if not text or not text.strip():
        raise ValueError("Couldn't extract readable content from that URL -- try pasting the text directly instead.")

    metadata = trafilatura.extract_metadata(downloaded)
    title = (metadata.title if metadata and metadata.title else url).strip()
    return title, text
