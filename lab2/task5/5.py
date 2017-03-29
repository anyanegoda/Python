import re


def search(string):
    text = ''
    split_text = string.split(' ')
    for i in range(len(split_text)):
        result = re.findall(r'[A-Z]{1}[a-z]+\d{4}|[A-Z]{1}[a-z]+\d{2}', split_text[i])
        '''search_for_result = re.search(r'[A-Z]{1}[a-z]+\d{4}|[A-Z]{1}[a-z]+\d{2}', split_text[i])
        if search_for_result != None:'''
        print(result)

string = input('Введите строку: ')
search(string)
