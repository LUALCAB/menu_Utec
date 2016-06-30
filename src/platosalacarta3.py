# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'platosalacarta3.ui'
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

class Ui_pc3Window(object):
    def setupUi(self, pc3Window):
        pc3Window.setObjectName(_fromUtf8("pc3Window"))
        pc3Window.resize(800, 600)
        self.centralwidget = QtGui.QWidget(pc3Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 420, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 40, 81, 101))
        self.pushButton_2.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 460, 171, 61))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 170, 611, 191))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 50, 311, 71))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 460, 171, 61))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        pc3Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(pc3Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        pc3Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(pc3Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        pc3Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(pc3Window)
        QtCore.QMetaObject.connectSlotsByName(pc3Window)

    def retranslateUi(self, pc3Window):
        pc3Window.setWindowTitle(_translate("pc3Window", "MainWindow", None))
        self.label.setText(_translate("pc3Window", "TOTAL : ", None))
        self.pushButton_4.setText(_translate("pc3Window", "OTRO PEDIDO ", None))
        self.textEdit.setHtml(_translate("pc3Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">SPAGHETTI A LO ALFREDO </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic; text-decoration: underline;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(DESCRIPCIÓN DEL MENÚ)</p></body></html>", None))
        self.pushButton.setText(_translate("pc3Window", "PLATOS A LA CARTA", None))
        self.pushButton_3.setText(_translate("pc3Window", "IMPRIMIR ", None))
        self.menuMENUTEC.setTitle(_translate("pc3Window", "MENUTEC", None))

