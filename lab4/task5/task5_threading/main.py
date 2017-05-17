import sys
from functools import partial
from os import mkdir

import pylab
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from downloader import DownloadThread
from main_window import Ui_MainWindow


# http://my-files.ru/Save/wsq6so/03.Dexter%20Gordon%20-%20Broadway.mp3
# http://my-files.ru/Save/kcbmoj/01.The%20Beatles%20-%20Help!.mp3
# http://my-files.ru/Save/gnkzf6/Test%20-%20Left%20and%20Right.mp3
# http://my-files.ru/Save/tqlvtv/the-contented-mascot.jpg
# http://my-files.ru/Save/9om4zt/Nzl_2011_2(1)__10.pdf

# функция, позаимствованная на stackoverflow
# форматирует файловый размер
def size_format(num):
    for unit in ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%sB" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%sB" % (num, 'Y', suffix)


class MyForm(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # для удобства помещаем элементы интерфейса
        # в массив
        self.progress_bars = (self.ui.progress1,
                              self.ui.progress2,
                              self.ui.progress3)

        self.url_edits = (self.ui.url1,
                          self.ui.url2,
                          self.ui.url3)

        # заполняем текстовые поля ссылками
        # чтобы тестировать, не вводя каждый раз вручную
        for edit, url in zip(self.url_edits,
                             (r'http://my-files.ru/Save/gnkzf6/'
                              'Test%20-%20Left%20and%20Right.mp3',
                              r'http://my-files.ru/Save/tqlvtv/'
                              'the-contented-mascot.jpg',
                              r'http://my-files.ru/Save/9om4zt/'
                              'Nzl_2011_2(1)__10.pdf')):
            edit.setText(url)

    def start_downloading(self):
        self.prepare_downloads_dir()
        # получаем URL-адреса из текстовых полей
        urls = [e.text() for e in self.url_edits]
        self.enable_progress_bars()
        self.init_threads(urls)
        self.start_threads()
        # ждём, пока все потоки завершатся
        DownloadThread.when_all_finished.wait()
        self.show_statistics()

    def update(self, progress_bar, percentage):
        progress_bar.setProperty('value', percentage * 100)
        pass

    def show_statistics(self):
        # два подграфика
        f, (ax1, ax2) = pylab.subplots(1, 2)
        # устанавливаем размеры фигуры (окна вывода)
        f.set_size_inches((10, 6))

        # столбчатая диаграмма с 0..len по оси x
        # и временем по оси y
        ax1.bar(range(len(self.threads)),
                [t.timedelta.total_seconds()
                 for t in self.threads])

        # устанавливаем метки с названиями файлов для 0..len по оси x
        ax1.set_xticks(range(len(self.threads)))
        ax1.set_xticklabels([t.filename for t in self.threads])
        # название графика
        ax1.set_title('Download time plot')

        # секторная диаграмма
        ax2.pie([t.file_size for t in self.threads],
                labels=['{}\n[{}]'.format(t.filename,
                                          size_format(t.file_size))
                for t in self.threads])
        ax2.set_title('File size')

        # отображаем фигуру
        f.show()
        # закрываем окно загрузки
        self.close()

    def prepare_downloads_dir(self):
        try:
            mkdir('downloads')
        except FileExistsError:
            pass

    def enable_progress_bars(self):
        for p in self.progress_bars:
            p.setEnabled(True)

    def init_threads(self, urls):
        self.threads = [DownloadThread(url,
                                       partial(self.update, progress_bar))
                        for url, progress_bar
                        in zip(urls, self.progress_bars)]

    def start_threads(self):
        for t in self.threads:
            t.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    try:
        form = MyForm()
        form.show()
    except Exception as be:
        print(be)
    try:
        sys.exit(app.exec_())
    except SystemExit as se:
        print('Program has exited with code {}'.format(se))
