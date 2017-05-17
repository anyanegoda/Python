# -*- coding: utf-8 -*-
"""
Created on Sun May  7 20:23:17 2017

@author: annan
"""
import math 

class Fraction(object):
    
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        self.reduce()
        
    def __str__(self):
        return "%d/%d" % (self.__num, self.__den)
    
    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num /= g
        self.__den /= g
        
    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)
        
    def __add__(self, f):
        res = Fraction(0, 1)
        res.__num = self.__num * f.__den + f.__num * self.__den
        res.__den = self.__den * f.__den
        res.reduce()
        return res
    
    def __neg__(self):
        res = Fraction(0, 1)
        res.__num = self.__num * -1
        res.__den = self.__den * 1
        res.reduce()
        return res
    
    def __invert__(self):
        res = Fraction(0, 1)
        res.__num = self.__den
        res.__den = self.__num
        res.reduce()
        return res
        
    def __pow__(self, other):
        res = Fraction(self.__num, self.__den)
        while (other > 1):
            print (other)
            res.__num *= self.__num
            res.__den *= self.__den
            other -= 1
        res.reduce()
        return res
    
    def __float__(self):
        res = 1.0
        res =  self.__num / self.__den
        return round(res, 1)
    
    def __int__(self):
        res = 1.0
        res = self.__num / self.__den
        return math.floor(res)
    
f1 = Fraction(7, 2)
f2 = Fraction(1, 4)
f = f1 + f2
print(-f1)
print(~f1)
print(f1**2)
print(float(f1))
print(int(f1)) 