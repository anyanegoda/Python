# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 357)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 21))
        self.menubar.setObjectName("menubar")
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        self.logMenu = QtWidgets.QMenu(self.menubar)
        self.logMenu.setObjectName("logMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openMenuItem = QtWidgets.QAction(MainWindow)
        self.openMenuItem.setObjectName("openMenuItem")
        self.exportMenuItem = QtWidgets.QAction(MainWindow)
        self.exportMenuItem.setObjectName("exportMenuItem")
        self.addMenuItem = QtWidgets.QAction(MainWindow)
        self.addMenuItem.setObjectName("addMenuItem")
        self.lookMenuItem = QtWidgets.QAction(MainWindow)
        self.lookMenuItem.setObjectName("lookMenuItem")
        self.fileMenu.addAction(self.openMenuItem)
        self.logMenu.addAction(self.exportMenuItem)
        self.logMenu.addAction(self.addMenuItem)
        self.logMenu.addAction(self.lookMenuItem)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.logMenu.menuAction())
        self.lastActionLabel = QtWidgets.QLabel()
        self.statusbar.setSizeGripEnabled(True)
        self.lastFileSizeLabel = QtWidgets.QLabel()
        self.statusbar.addWidget(self.lastActionLabel, 3)
        self.statusbar.addPermanentWidget(self.lastFileSizeLabel, 2)

        self.retranslateUi(MainWindow)
        self.openMenuItem.triggered.connect(MainWindow.open_file)
        self.exportMenuItem.triggered.connect(MainWindow.export_log)
        self.addMenuItem.triggered.connect(MainWindow.add_log)
        self.lookMenuItem.triggered.connect(MainWindow.look_log)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fileMenu.setTitle(_translate("MainWindow", "Файл"))
        self.logMenu.setTitle(_translate("MainWindow", "Лог"))
        self.openMenuItem.setText(_translate("MainWindow", "Открыть..."))
        self.exportMenuItem.setText(_translate("MainWindow", "Экспорт..."))
        self.addMenuItem.setText(_translate("MainWindow", "Добавить в лог"))
        self.lookMenuItem.setText(_translate("MainWindow", "Просмотр"))

