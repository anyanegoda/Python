# cd /d d:\Folder
# python D:\6.py --source D:\task6 --days 1 --size 4096
import argparse
import os
import shutil


def main():
    m = argparse.ArgumentParser(description="Reorganize", epilog="Mission complete!")
    m.add_argument("--source", type=str, default='.', help='Destination')
    m.add_argument("--days", type=int, default=2, help='How old are files? (days)')
    m.add_argument("--size", type=int, default=0, help='Max size of files')
    options = m.parse_args()

    options = str(options)
    options = options[9:]
    options = options.replace('(', '')
    options = options.replace(')', '')
    options = options.replace(',', '')
    listOptions = options.split(' ')

    daysTo = listOptions[0]
    daysTo = daysTo.split('=')
    daysTo = daysTo[1]

    source = listOptions[2]
    source = source.split('=')
    source = source[1]
    source = source.replace('\\\\', '\\')
    source = source.replace('\'', '')
    print('Source', source)

    size = listOptions[1]
    size = size.split('=')
    size = size[1]
    size = int(size)

    if os.path.exists(source) == True:
        if os.listdir(source):

            os.chdir(source)
            os.mkdir(str('Archive'))
            os.mkdir(str('Small'))

            files = os.listdir(source)
            files = [os.path.join(source, file) for file in files]
            files = [file for file in files if os.path.isfile(file)]
            for i in range(len(files)):

                inseconds = daysTo * 86400
                inseconds = float(inseconds)
                print(files[i])
                if os.path.getmtime(files[i]) > inseconds:
                    shutil.move(files[i], source + '\Archive')
                if os.path.getsize(files[i]) < size:
                    shutil.move(files[i], source + '\Small')
        else:
            print('Директория путая!')

if __name__ == '__main__':
    main()