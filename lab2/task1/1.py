# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:20:53 2017

@author: anna
"""
try:
    my_file = open('text.txt','r')
except FileNotFoundError:
    print('Файл не найден!')
else:
    my_string = my_file.read()
    print(my_string)
    my_string = my_string.lower()
    letters = []
    for i in range(len(my_string)):
        if my_string[i].isalpha():
            letters.append(my_string[i])


    dict = {}
    for i in range(len(letters)):
        counter = 0
        for j in letters:
            if letters[i] == j:
                counter += 1
                dict[letters[i]] = counter

    l = lambda x: x[1]

    print('\n Символы в порядке убывания: \n', sorted(dict.items(), key=l, reverse=True))

    my_file.close()
