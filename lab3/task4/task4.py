# -*- coding: utf-8 -*-
"""
Created on Sun May 14 14:39:59 2017

@author: annan
"""

class StringFormatter:
	def delNLines(self, string, n):
		wordslist = string.split(' ')
		for i in wordslist:
			if len(i) < n:
				wordslist.remove(i)
		return ' '.join(wordslist)

	def replaceNumbers(self, string):
		tempstr = string.translate(str.maketrans('0123456789', '**********'))
		return tempstr
	
	def addSpaces(self, string):
		tempstr = ''
		for i in string:
			if not i == ' ':
				tempstr += i + ' '
		return tempstr
		
	def sortByLenght(self, string):
		def SBL(str):
			return len(str)
		templst = string.split(' ')
		templst.sort(key=SBL)
		return ' '.join(templst)

	def lexOrder(self, string):
		lexlist = string.split(' ')
		lexlist = sorted(lexlist, key=lambda x:(str.lower(x),x))
		return ' '.join(lexlist)
		

SFor = StringFormatter()
print(SFor.delNLines('1111 2222 444 5 8 666666666 ', 5))
print(SFor.replaceNumbers('kek 258475'))
print(SFor.addSpaces('Suda probel'))
print(SFor.sortByLenght('сортировка слов по размеру'),'lol kek cheburek')
print(SFor.lexOrder('Мама мыла раму'))