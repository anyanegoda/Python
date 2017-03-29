# D:\test
import subprocess
import os
import hashlib


def print_path():
    try:
        path = input('Введите путь директории: ')
        print(os.listdir(path))
        subprocess.Popen('explorer "%s"' % path)
        return path
    except(FileNotFoundError, OSError, UnicodeEncodeError):
        print('Неверный путь! \n Русские символы не допускаются!')
        print_path()

path = print_path()
files = os.listdir(path)


def get_md5_sum(file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        content = f.read()
        a = hashlib.md5()
        a.update(content.encode('utf8'))
        f.close()
    checksum = a.hexdigest()
    return checksum
print()
print('MD5 суммы всех файлов:')
every = {}
duplicates = {}
for top, dirs, files in os.walk(path):
    for nm in files:
        name = os.path.join(top, nm)
        name = str(name)
        print(name)
        md5sum = get_md5_sum(name)
        print(md5sum)
        if md5sum in every.keys():
            duplicates[md5sum] = str(name + ';  ' + every[md5sum])
        every[md5sum] = name
print()
# print(every, '\n')
print('Группы файлов дубликатов: \n', duplicates)