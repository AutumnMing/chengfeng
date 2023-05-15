# chengfeng: 乘风2023数据采集脚本
import requests
from json import load
from urllib.parse import urlencode
from time import localtime, strftime, sleep
from operate_data import add_dict_rows, create_csv


def gen_url(base_url, params):
    return base_url + urlencode(params)


def get_character_list(character_url):
    r = requests.get(character_url)
    if r.status_code == 200:
        return r.json()['data']['character_list']


def parse_character(characters: list):
    parse_time = int(strftime("%Y%m%d%H%M", localtime()))
    for each in characters:
        yield {
            'char_id': each['char_id'],
            'char_name': each['char_name'],
            'vote_num': each['vote_num'],
            'parse_time': parse_time
        }


if __name__ == '__main__':

    column_names = ['char_id', 'char_name', 'vote_num', 'parse_time']
    filename = './data/chengfeng.csv'
    create_csv(filename, column_names=column_names)
    with open('./config/chengfeng.json') as f:
        cf = load(f)
    url = gen_url(cf['base_url'], cf['params'])
    
    res_characters = get_character_list(character_url=url)
    for character in parse_character(characters=res_characters):
        add_dict_rows(filename, character, column_names)
        print(character)
    sleep(60)
