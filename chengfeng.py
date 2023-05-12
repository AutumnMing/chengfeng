# chengfeng: 乘风2023数据采集脚本

import requests
from urllib.parse import urlencode


def gen_url(base_url, params):
    return base_url + urlencode(params)


def get_character_list(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()['data']['character_list']
