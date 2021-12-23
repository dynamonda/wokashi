import requests
from bs4 import BeautifulSoup
from wokashi.soup import MisoSoup


def fuga() -> None:
    print('fuga')


def get(url: str) -> MisoSoup:
    response: requests.Request = requests.get(url)
    soup = BeautifulSoup(response.content, features='lxml')
    return MisoSoup(soup)
