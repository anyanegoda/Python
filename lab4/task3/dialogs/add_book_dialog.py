from ui import Ui_AddBookDialog
from PyQt5.QtWidgets import QWidget, QDialog
from model import Book


class AddBookDialog(QDialog):

    selected_author = None
    book = None

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_AddBookDialog()
        self.ui.setupUi(self)
        self.authors = self.parent().db.read_authors()
        for author in self.authors:
            self.ui.author.addItem(author.name)

    def accept(self):
        self.selected_author = self.authors[self.ui.author.currentIndex()]
        self.book = Book(title=self.ui.title.text(),
                         pages_count=self.ui.pages_count.value(),
                         publisher=self.ui.publisher.text(),
                         publishing_year=self.ui.publishing_year.value())
        self.selected_author.insert_book(self.book)
        self.parent().db.insert_book(self.book)
        self.close()
