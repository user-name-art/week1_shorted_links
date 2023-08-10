import os

import requests
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()
URL = 'https://api-ssl.bitly.com/v4/bitlinks'
headers = {'Authorization': f'Bearer {os.environ["TOKEN"]}'}


def shorten_link(headers, url, users_url):
    data = {
    "long_url": users_url
    }

    responce = requests.post(url, headers=headers, json=data)
    responce.raise_for_status()
    return responce.json()


def count_link(headers, url, users_url):
    count_url = f'{url}/{users_url}/clicks/summary'

    responce = requests.get(count_url, headers=headers)
    responce.raise_for_status()
    return responce.json()


def is_binlink(headers, url, users_url):
    link = urlparse(users_url)
    checked_link = f'{link[1]}{link[2]}'
    check_bitlink_url = f'{url}/{checked_link}'

    responce = requests.get(check_bitlink_url, headers=headers)
    responce.raise_for_status()
    return responce.json()['id']


if __name__ == '__main__':
    users_url = input('Введите ссылку: ')

    try:
        answer = is_binlink(headers, URL, users_url)
    except requests.exceptions.HTTPError:
        answer = False

    if answer:
        count = count_link(headers, URL, answer)['total_clicks']
        print('Количество переходов по ссылке: ', count)
    else:
        try:
            bitlink = shorten_link(headers, URL, users_url)['link']
            print('Битлинк: ', bitlink)
        except requests.exceptions.HTTPError:
            print('Вы ввели некорректную ссылку, перепроверьте её.')
