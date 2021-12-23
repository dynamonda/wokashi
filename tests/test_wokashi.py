import wokashi
from wokashi.soup import MisoSoup


def test_version():
    assert wokashi.__version__ == '0.1.0'


def test_get():
    soup = wokashi.get('https://yahoo.co.jp')
    assert soup is not None
    assert type(soup) == MisoSoup
