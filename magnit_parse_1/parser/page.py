import re
from urllib.parse import urlparse, urljoin

import requests


__all__ = ('MagnitPage',)

from magnit_parse_1.parser.patterns import TITLE_PATTERN


class MagnitPage:

    def __init__(self, response):
        self.url = response.url
        self.response = response

    def get_data(self, pattern):
        for itm in re.findall(pattern, self.response.text):
            yield itm

    def get_page_rel_links(self, pattern):
        domain = urlparse(self.url).netloc
        for link in self.get_data(pattern):
            url = urljoin(self.url, link)
            if urlparse(self.url).netloc == domain:
                yield url

    @classmethod
    def get_page_from_url(cls, url, *args, **kwargs):
        response = requests.get(url)
        instance = cls(response)
        return instance

    def to_dict(self):
        return {
            "title": " ".join(self.get_data(TITLE_PATTERN)),
            "url": self.url
        }
