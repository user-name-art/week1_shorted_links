import os
import argparse

import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(headers, user_url):
    post_api_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    request_options = {
    "long_url": user_url
    }

    response = requests.post(post_api_url, headers=headers, json=request_options)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(headers, user_url):
    link = urlparse(user_url)
    checked_link = f'{link.netloc}{link.path}'
    count_api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{checked_link}/clicks/summary'

    response = requests.get(count_api_url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(headers, user_url):
    link = urlparse(user_url)
    checked_link = f'{link.netloc}{link.path}'
    check_bitlink_api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{checked_link}'

    response = requests.get(check_bitlink_api_url, headers=headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()

    headers = {'Authorization': f'Bearer {os.environ["BITLY_TOKEN"]}'}

    parser = argparse.ArgumentParser()
    parser.add_argument ('link')
    user_url = parser.parse_args().link

    try:
        if is_bitlink(headers, user_url):
            count = count_clicks(headers, user_url)
            print('Количество переходов по ссылке: ', count)
        else:
            bitlink = shorten_link(headers, user_url)
            print('Битлинк: ', bitlink)
    except requests.exceptions.HTTPError:
        print('Вы ввели некорректную ссылку, перепроверьте её.')
