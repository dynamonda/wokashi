from bs4 import BeautifulSoup
from bs4.element import Tag as BSTag

from wokashi.tag import Tag

from typing import List


class MisoSoup:
    """
    BeautifulSoupクラスをラップ
    """

    def __init__(self, soup: BeautifulSoup, url: str):
        self.soup = soup
        self.url = url
        self.title_tag: Tag = Tag(soup.title)

    def search_css(self, selector: str) -> List[Tag]:
        """
        CSSセレクタを使用して要素を取得する。
        """
        result_set = list()
        for token in self.soup.select(selector):
            result_set.append(Tag(token))
        return result_set
