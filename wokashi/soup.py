from bs4 import BeautifulSoup


class MisoSoup:
    """
    BeautifulSoupクラスをラップ
    """

    def __init__(self, soup: BeautifulSoup, url: str):
        self.soup = soup
        self.url = url
