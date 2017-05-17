from ui import Ui_AddAuthorDialog
from PyQt5.QtWidgets import QWidget, QDialog
from model import Author


class AddAuthorDialog(QDialog):

    author = None

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.new_item = None
        self.ui = Ui_AddAuthorDialog()
        self.ui.setupUi(self)

    def accept(self):
        birth_year = self.ui.birth_year.text()
        death_year = self.ui.death_year.text()
        self.author = Author(name=self.ui.name.text(),
                             country=self.ui.country.text(),
                             years='-'.join((birth_year,
                                             death_year))
                                   if len(death_year) > 0
                                   else birth_year)
        self.parent().db.insert_author(self.author)
        self.close()
