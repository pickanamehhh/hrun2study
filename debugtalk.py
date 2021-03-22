import random

def get_search_word():
    word_list = ['lol', 'csgo', 'pubg', '守望先锋']
    num = random.randint(0, len(word_list)-1)
    return word_list[num]


def s():
    print('测试前执行')


def t():
    print('测试后执行')


def s1(test_name):
    print('测试前执行[%s]' % test_name)


def t1(test_name1):
    print('测试后执行[%s]' % test_name1)


if __name__ == '__main__':
    print(get_search_word())
