import wokashi


def test_version():
    assert wokashi.__version__ == '0.1.0'


def test_get():
    content = wokashi.get('https://yahoo.co.jp')
    assert len(content) > 0
