from bs4 import BeautifulSoup
from bs4.element import Tag


class MisoSoup:
    """
    BeautifulSoupクラスをラップ
    """

    def __init__(self, soup: BeautifulSoup, url: str):
        self.soup = soup
        self.url = url

        title_tag: Tag = soup.title
        # Tagオブジェクトの文字列を取るときには、
        # tag.stringではなくtag.get_text()を使う
        # https://maitakeramen.hatenablog.com/entry/2019/09/07/220623
        self.title: str = title_tag.get_text()
