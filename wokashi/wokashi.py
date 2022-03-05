import requests
import requests_cache
from bs4 import BeautifulSoup
from wokashi.soup import MisoSoup


def get(url: str, is_use_cache: bool = False) -> MisoSoup:
    if is_use_cache == True:
        requests_cache.install_cache('wokashi_cache')
    response: requests.Request = requests.get(url)
    soup = BeautifulSoup(response.content, features='lxml')
    return MisoSoup(soup, url)
