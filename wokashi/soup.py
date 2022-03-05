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

        title_tag: BSTag = soup.title
        # Tagオブジェクトの文字列を取るときには、
        # tag.stringではなくtag.get_text()を使う
        # https://maitakeramen.hatenablog.com/entry/2019/09/07/220623
        self.title: str = title_tag.get_text()

    def search_css(self, selector: str) -> List[BSTag]:
        """
        CSSセレクタを使用して要素を取得する。
        """
        result_set = list()
        for token in self.soup.select(selector):
            result_set.append(token)
        return result_set
