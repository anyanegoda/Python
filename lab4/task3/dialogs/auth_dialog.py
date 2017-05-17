from ui import Ui_AuthDialog
from PyQt5.QtWidgets import QWidget, QDialog
from auth import User


class AuthDialog(QDialog):

    user = None

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_AuthDialog()
        self.ui.setupUi(self)

    def accept(self):
        self.user = User(self.ui.login.text(),
                         self.ui.password.text())
        if not self.parent().db.is_user_exists(self.user.login, self.user.password):
            self.setWindowTitle('Ошибка авторизации')
        else:
            QDialog.accept(self)

    def reject(self):
        QDialog.reject(self)
        exit(0)
