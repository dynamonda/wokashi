from bs4 import BeautifulSoup


class MisoSoup:
    """
    BeautifulSoupクラスをラップ
    """
    def __init__(self, soup: BeautifulSoup):
        self.soup = soup
