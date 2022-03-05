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


def test_search_css():
    target_url = 'https://yahoo.co.jp'
    soup = wokashi.get(target_url)

    title_list = soup.search_css('head title')
    assert type(title_list) == list
    assert len(title_list) == 1
    # ここは後で直したい
    assert title_list[0].get_text() == "Yahoo! JAPAN"
