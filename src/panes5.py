# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panes5.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_panes5Window(object):
    def setupUi(self, panes5Window):
        panes5Window.setObjectName(_fromUtf8("panes5Window"))
        panes5Window.resize(800, 600)
        self.centralwidget = QtGui.QWidget(panes5Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 450, 171, 61))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 410, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 40, 311, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 160, 611, 191))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 30, 81, 101))
        self.pushButton_2.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 450, 171, 61))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        panes5Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(panes5Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        panes5Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(panes5Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        panes5Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(panes5Window)
        QtCore.QMetaObject.connectSlotsByName(panes5Window)

    def retranslateUi(self, panes5Window):
        panes5Window.setWindowTitle(_translate("panes5Window", "MainWindow", None))
        self.pushButton_4.setText(_translate("panes5Window", "OTRO PEDIDO ", None))
        self.label.setText(_translate("panes5Window", "TOTAL : ", None))
        self.pushButton.setText(_translate("panes5Window", "SANDWICHES, JUGOS Y BEBIDAS", None))
        self.textEdit.setHtml(_translate("panes5Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">CHORIZO </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic; text-decoration: underline;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(DESCRIPCIÓN DEL MENÚ)</p></body></html>", None))
        self.pushButton_3.setText(_translate("panes5Window", "IMPRIMIR ", None))
        self.menuMENUTEC.setTitle(_translate("panes5Window", "MENUTEC", None))

