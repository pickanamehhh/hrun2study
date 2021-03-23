import random
import requests


def get_search_word():
    word_list = ['lol', 'csgo', 'pubg', '守望先锋']
    num = random.randint(0, len(word_list) - 1)
    return word_list[num]


def s():
    print('测试前执行')


def t():
    print('测试后执行')


def s1(test_name):
    print('测试前执行[%s]' % test_name)


def t1(test_name1):
    print('测试后执行[%s]' % test_name1)


def get_true():
    return True


def get_access_token():
    params = {
        'grant_type': 'client_credential',
        'appid': 'wx8708f96abc9abaf3',
        'secret': '5be760a8fac19282515d47d326ab108b'
    }
    try:
        response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token', params=params)
        token = response.json()['assess_token']
    except KeyError as e:
        return None
    return token


if __name__ == '__main__':
    print(get_access_token())
