import os
import re


basepath = os.path.abspath(os.path.dirname('D:\Music'))

path = os.path.join(basepath, 'D:\Music')
try:
    songList = open('D:\Music\song.txt', 'r')
except FileNotFoundError:
    print('Файл не найден!')
else:
    formatedList = songList.readlines()
    dict = {}

    for line in range(len(formatedList)):
        temp = formatedList[line]
        temp2 = formatedList[line]
        temp2 = str(temp2)
        temp2 = re.sub('\n', ' ', temp2)
        print(temp2)
        temp = temp.split(' ')
        dict[temp[1] + '.mp3'] = str(temp2)

    list = []
    for top, dirs, files in os.walk(path):
        for nm in files:
            fname = os.path.join(top, nm)
            fname = str(fname)
            print(fname)
            list.append(fname)
            if nm in dict.keys():
                os.rename(fname, top + "\\" + dict[nm] + '.mp3')
