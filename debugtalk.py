import random

def get_search_word():
    word_list = ['lol', 'csgo', 'pubg', '守望先锋']
    num = random.randint(0, len(word_list)-1)
    return word_list[num]


if __name__ == '__main__':
    print(get_search_word())
