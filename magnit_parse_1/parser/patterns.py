import re


__all__ = (
    'TITLE_PATTERN',
    'PRODUCTS_PATTERN',
)

TITLE_PATTERN = re.compile(r'<meta property="og:title" content=\"(.+)\"')
PRODUCTS_PATTERN = re.compile(r"href=\"(/promo\S+)\"")
