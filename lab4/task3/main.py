import loaders
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from sqlalchemy.sql import or_

from model import Author, Book, DB
from dialogs import AuthDialog, AddAuthorDialog, AddBookDialog

from ui import Ui_ViewInfo

db = DB('library.db')


class MyForm(QMainWindow):

    db = db

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_ViewInfo()
        self.ui.setupUi(self)
        self.reload()
        self.nameFilters = {'JSON (*.json)': loaders.json_loader,
                            'XML (*.xml)': loaders.xml_loader}

    @staticmethod
    def _append_items(model, items):
        model.appendRow(filter(lambda x: x.setEditable(False) or True,
                               map(lambda x: QStandardItem(str(x)), items)))

    def _load_authors(self):
        authors = db.read_authors()
        if self.ui.onlyWithMoreThanNBooksCheckbox.isChecked():
            numOfBooks = self.ui.author_numOfBooks.value()
            authors = filter(lambda x: len(x.books) > numOfBooks,
                             authors)
        if self.ui.onlyBetweenYearsCheckbox.isChecked():
            _from = self.ui.author_fromYear.value()
            _to = self.ui.author_toYear.value()
            authors = filter(lambda x: (_from <=
                                        int(x.years.split('-')[0]) <=
                                        _to),
                             authors)
        return authors

    def _load_books(self):
        books = db.read_books()
        if self.ui.onlyFromRussiaCheckbox.isChecked():
            books = books.join(Book.author) \
                          .filter(or_(Author.country == 'Russia',
                                      Author.country == 'Россия'))
        if self.ui.onlyWithPagesMoreThanN.isChecked():
            countOfPages = self.ui.countOfPages.value()
            books = books.filter(Book.pages_count > countOfPages)
        return books

    def _init_authors(self):
        model = QStandardItemModel(self)
        model.setHorizontalHeaderLabels(['Имя',
                                         'Страна',
                                         'Годы жизни'])
        for author in self._load_authors():
            MyForm._append_items(model, [author.name,
                                         author.country,
                                         author.years])
        self.ui.authors.setModel(model)

    def _init_books(self):
        model = QStandardItemModel(self)
        model.setHorizontalHeaderLabels(['Автор',
                                         'Название',
                                         'Количество страниц',
                                         'Издательство',
                                         'Год издания'])
        for book in self._load_books():
            MyForm._append_items(model, [book.author.name,
                                         book.title,
                                         book.pages_count,
                                         book.publisher,
                                         book.publishing_year])
        self.ui.books.setModel(model)

    def add_author(self):
        dialog = AddAuthorDialog(self)
        dialog.exec()
        if dialog.author is not None:
            MyForm._append_items(self.ui.authors.model(),
                                 [dialog.author.name,
                                  dialog.author.country,
                                  dialog.author.years])

    def add_book(self):
        dialog = AddBookDialog(self)
        dialog.exec()
        if dialog.book is not None:
            MyForm._append_items(self.ui.books.model(),
                                 [dialog.book.author.name,
                                  dialog.book.title,
                                  dialog.book.pages_count,
                                  dialog.book.publisher,
                                  dialog.book.publishing_year])

    def reload(self):
        self._init_authors()
        self._init_books()

    def import_authors(self):
        dialog = QFileDialog(self)
        dialog.setNameFilters(self.nameFilters.keys())
        if dialog.exec():
            with open(dialog.selectedFiles()[0], 'rt') as file:
                loader = self.nameFilters[dialog.selectedNameFilter()]
                for author in loader.load(file.read()):
                    db.insert_author(author)
                    MyForm._append_items(self.ui.authors.model(),
                                         [author.name,
                                          author.country,
                                          author.years])

    def export_authors(self):
        indexes = self.ui.authors.selectedIndexes()
        if len(indexes) < 1:
            return
        dialog = QFileDialog(self)
        dialog.setNameFilters(self.nameFilters.keys())
        dialog.setAcceptMode(dialog.AcceptSave)
        if dialog.exec():
            loader = self.nameFilters[dialog.selectedNameFilter()]
            with open(dialog.selectedFiles()[0], 'wt') as file:
                model = self.ui.authors.model()
                name, country, years = (model.item(indexes[0].row(), i).text()
                                        for i in range(model.columnCount()))
                file.write(loader.dump(Author(name=name,
                                              country=country,
                                              years=years)))

    def options_toggled(self):
        self.reload()

if __name__ == '__main__':
    # инициализируем базу
    # создаём таблицы и заполняем их значениями по умолчанию
    db.init_tables()
    app = QApplication(sys.argv)
    form = MyForm()
    # диалог авторизации
    auth_dialog = AuthDialog(form)
    auth_dialog.exec()
    # если авторизация пройдена, показываем основную форму
    form.show()
    try:
        sys.exit(app.exec_())
    except SystemExit as se:
        print('Program has exited with code {}'.format(se))
