# -*- coding: utf-8 -*-
"""
Created on Sun May  7 22:02:28 2017

@author: annan

"""

from abc import abstractmethod


class Taggable:
    @abstractmethod
    def tag(self):
        pass


class Book(Taggable):
    count = 0

    def __init__(self, author, name):
        if name == '':
            raise ValueError('The author\'s name was not indicated!')

        Book.count += 1
        self.__name = name
        self.__author = author
        self.__code = Book.count

    def tag(self):
        words = self.__name.split()
        return [word for word in words if word.istitle()]

    def __str__(self):
        return "[%d] %s '%s'" % (self.__code, self.__author, self.__name)


class Library(object):

    def __init__(self, number, adress):
        self.__adress = adress
        self.__number = number
        self.__books = []

    def __add__(self, book):
        self.__books += [book]
        return self

    def __iadd__(self, book):
        return self.__add__(book)

    def __iter__(self):
        for book in self.__books:
            yield book


lib = Library(1, '51 Some str., NY')
lib += Book('Leo Tolstoi', 'War and Peace')
lib += Book('Charles Dickens', 'David Copperfield')
for book in lib:
    print(book)
    print(book.tag())
