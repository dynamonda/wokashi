import requests


def fuga() -> None:
    print('fuga')


def get(url: str) -> str:
    response: requests.Request = requests.get(url)
    return response.content
