import wokashi
from wokashi.soup import MisoSoup


def test_version():
    assert wokashi.__version__ == '0.1.0'


def test_get():
    target_url = 'https://yahoo.co.jp'
    soup = wokashi.get(target_url)

    assert soup is not None
    assert type(soup) == MisoSoup
    assert soup.url == target_url
    assert type(soup.title) == str
    assert soup.title == "Yahoo! JAPAN"
