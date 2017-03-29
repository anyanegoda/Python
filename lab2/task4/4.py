# D:\text.txt
import re


def searching(text):
    for i in range(len(text)):
        result = re.findall(r'\S\d{3}\S\d{3}-\d{2}-\d{2}|\S\d{3}\S\d{7}', text[i])
        searchForResult = re.search(r'\S\d{3}\S\d{3}-\d{2}-\d{2}|\S\d{3}\S\d{7}', text[i])
        if searchForResult != None:
            print('Строка - ', i, ' Позиция - ', searchForResult.span(), ' : найдено ', result)

def workWithFile(pathToFile):
    rfile = open(pathToFile)
    fileString = rfile.readlines()
    searching(fileString)

finish_it = False
while finish_it != True:
    try:
        _pathToFile = input('Введите путь к файлу: ')
        workWithFile(_pathToFile)
        finish_it = True
    except(FileNotFoundError, OSError):
        print('Файл не найден! \nПример ввода: D:\Text.txt')