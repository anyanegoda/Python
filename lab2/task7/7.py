# python D:\7.py --source D:\task7 --destination D:\cut -l
# <?xml version="1.0" encoding="UTF-8"?>
import sys
import argparse
import os
import subprocess


def main():
    try:
        m = argparse.ArgumentParser(description="Trackmix", epilog="Good listening!")
        m.add_argument('--source', '-s', type=str, required=True, help='Source')
        m.add_argument('--destination', '-d', type=str, default=None, help='Output')
        m.add_argument('--count', '-c', type=int, default=None, help='How many files should i cut?')
        m.add_argument('--frame', '-f', type=int, default=10, help='How long(sec)?')
        m.add_argument('--log', '-l', action='store_true', help='Should i log it?')
        m.add_argument('--extended', '-e', action='store_true', help='Little fade in/out')
    except:
        print('Некорректные аргументы!')

    source = m.parse_args().source
    destination = m.parse_args().destination
    if destination == None:
        destination = source
    count = m.parse_args().count
    frame = m.parse_args().frame

    log = m.parse_args().log
    if log == True:
        log = ' -i '
        log = str(log)
    else:
        log = ' '
        log = str(log)

    fade = m.parse_args().extended
    justForFade = frame - 2
    justForFade = str(justForFade)
    if fade == True:
        fadeStr = ' -ss 00:00:00 -t 00:00:' + str(
            frame) + '.00 -af \"afade=t=in:ss=0:d=2,afade=t=out:st=' + justForFade + ':d=2"\' -y '
        fadeStr = str(fadeStr)
    else:
        fadeStr = ''
        fadeStr = str(fadeStr)

    if os.path.exists(source) == True:

        files = os.listdir(source)
        fileName = os.listdir(source)

        files = [os.path.join(source, file) for file in files]
        files = [file for file in files if os.path.isfile(file)]
        for i in range(len(files)):
            files[i] = '"' + files[i] + '"'
        pathToFfmeg = os.path.join(sys.path[0], r'D:\ffmpeg-20170321-db7a05d-win64-static\bin\ffmpeg.exe')  # Path to ffmeg

        if count != None:
            for i in count:
                subprocess.call(pathToFfmeg + log + files[i] + ' -acodec copy -ss 00:00:00 -t 00:00:' + str(
                    frame) + '.00' + ' "' + destination + '\\' + fileName[i] + '"', shell=True)
                if fade == True:
                    subprocess.call(
                        pathToFfmeg + log + files[i] + fadeStr + '"' + destination + '\\' + fileName[i] + '"',
                        shell=True)
        else:
            for i in range(len(files)):
                subprocess.call(pathToFfmeg + log + files[i] + ' -acodec copy -ss 00:00:00 -t 00:00:' + str(
                    frame) + '.00' + ' "' + destination + '\\' + fileName[i] + '"', shell=True)
                if fade == True:
                    subprocess.call(
                        pathToFfmeg + log + files[i] + fadeStr + '"' + destination + '\\' + fileName[i] + '"',
                        shell=True)
    else:
        print('Указанный путь не найден!')

if __name__ == '__main__':
    main()