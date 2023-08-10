import os

import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


URL = 'https://api-ssl.bitly.com/v4/bitlinks'


def shorten_link(headers, url, users_url):
    request_options = {
    "long_url": users_url
    }

    response = requests.post(url, headers=headers, json=request_options)
    response.raise_for_status()
    return response.json()


def get_count_clicks(headers, url, users_url):
    count_url = f'{url}/{users_url}/clicks/summary'

    response = requests.get(count_url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(headers, url, users_url):
    link = urlparse(users_url)
    checked_link = f'{link.netloc}{link.path}'
    check_bitlink_url = f'{url}/{checked_link}'

    response = requests.get(check_bitlink_url, headers=headers)
    response.raise_for_status()
    return response.ok


if __name__ == '__main__':
    load_dotenv()

    headers = {'Authorization': f'Bearer {os.environ["BITLY_TOKEN"]}'}

    users_url = input('Введите ссылку: ')

    try:
        if is_bitlink(headers, URL, users_url):
            count = get_count_clicks(headers, URL, users_url)
            print('Количество переходов по ссылке: ', count)
        else:
            bitlink = shorten_link(headers, URL, users_url)['link']
            print('Битлинк: ', bitlink)
    except requests.exceptions.HTTPError:
        print('Вы ввели некорректную ссылку, перепроверьте её.')
