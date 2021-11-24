import re

from .page import MagnitPage
from .patterns import PRODUCTS_PATTERN


__all__ = (
    "MagnitParser",
)


class MagnitParser:
    __queue_products = []

    def __init__(self, start_page: str, database):
        self.done_urls = set()
        self.start_page = MagnitPage.get_page_from_url(start_page)
        self.done_urls.add(self.start_page.url)
        self.database = database

    def run(self):
        for itm in self.start_page.get_page_rel_links(PRODUCTS_PATTERN):
            if itm in self.done_urls:
                continue
            self.done_urls.add(itm)
            product_page = MagnitPage.get_page_from_url(itm)
            product_dict = product_page.to_dict()
            self.save_to_base(product_dict)
        self.save_to_base(is_priority=True)

    def save_to_base(self, product_dict=None, is_priority=False):
        if product_dict:
            self.__queue_products.append(product_dict)
        if is_priority or len(self.__queue_products) > 10:
            self.database.save_promo_products(*self.__queue_products)
            self.__queue_products.clear()
