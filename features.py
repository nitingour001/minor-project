import re
import math
from urllib.parse import urlparse

SUSPICIOUS_TLDS = {
    'zip','xyz','top','gq','tk','work','support','loan','click','country','fit','rest','cf'
}
SHORTENER_DOMAINS = {
    'bit.ly','tinyurl.com','goo.gl','t.co','ow.ly','is.gd','buff.ly','adf.ly','cutt.ly','rb.gy'
}
KEYWORDS = {'login','verify','update','secure','account','bank','confirm','signin','password','webscr'}

ip_regex = re.compile(r"""^
(?:
    (?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}
    (?:25[0-5]|2[0-4]\d|[01]?\d?\d)
)
$""", re.X)

def shannon_entropy(s: str) -> float:
    if not s:
        return 0.0
    from collections import Counter
    c = Counter(s)
    n = len(s)
    return -sum((freq/n) * math.log2(freq/n) for freq in c.values())

def parse_host(url: str) -> str:
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url
    return (urlparse(url).hostname or '').lower()

def host_has_ip(host: str) -> bool:
    if not host:
        return False
    host = host.strip('[]')
    return bool(ip_regex.match(host))

def get_tld(host: str) -> str:
    parts = host.split('.')
    return parts[-1] if len(parts) >= 2 else ''

def get_domain_label(host: str) -> str:
    parts = host.split('.')
    return parts[-2] if len(parts) >= 2 else parts[0]

def suspicious_tld(host: str) -> int:
    tld = get_tld(host)
    return int(tld in SUSPICIOUS_TLDS)

def is_shortener(host: str) -> int:
    return int(host in SHORTENER_DOMAINS)

def has_hyphen_in_domain(host: str) -> int:
    dom = get_domain_label(host)
    return int('-' in dom)

def keyword_hits(url: str) -> int:
    u = url.lower()
    return int(any(k in u for k in KEYWORDS))

def extract_features(url: str):
    try:
        if not (url.startswith('http://') or url.startswith('https://')):
            url = 'http://' + url  # allow bare domains
        from urllib.parse import urlparse
        p = urlparse(url)
        host = p.hostname or ''
        path = p.path or ''
        query = p.query or ''
        # Basic counts
        url_len = len(url)
        num_dots = host.count('.')
        num_subdirs = path.count('/') - 1 if path else 0
        query_len = len(query)
        uses_https = int(p.scheme.lower() == 'https')
        has_at = int('@' in url)
        ratio_digits = sum(ch.isdigit() for ch in url) / max(1, len(url))
        ent = shannon_entropy(url)
        dom_len = len(host)
        # Booleans
        has_ip = int(host_has_ip(host))
        susp_tld = suspicious_tld(host)
        hyphen_in_dom = has_hyphen_in_domain(host)
        shortener = is_shortener(host)
        kw = keyword_hits(url)

        return [
            url_len, num_dots, num_subdirs, query_len, uses_https, has_at,
            ratio_digits, ent, dom_len, has_ip, susp_tld, hyphen_in_dom,
            shortener, kw
        ]
    except Exception:
        return [0]*14
