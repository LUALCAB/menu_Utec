# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panes7.ui'
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

class Ui_panes7Window(object):
    def setupUi(self, panes7Window):
        panes7Window.setObjectName(_fromUtf8("panes7Window"))
        panes7Window.resize(800, 480)
        self.centralwidget = QtGui.QWidget(panes7Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 130, 661, 171))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.btnIzquierda57 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda57.setGeometry(QtCore.QRect(100, 10, 81, 101))
        self.btnIzquierda57.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda57.setIcon(icon)
        self.btnIzquierda57.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda57.setObjectName(_fromUtf8("btnIzquierda57"))
        self.btnImprimir57 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir57.setGeometry(QtCore.QRect(120, 320, 201, 111))
        self.btnImprimir57.setObjectName(_fromUtf8("btnImprimir57"))
        self.btnPanes7 = QtGui.QPushButton(self.centralwidget)
        self.btnPanes7.setGeometry(QtCore.QRect(240, 30, 381, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPanes7.setIcon(icon1)
        self.btnPanes7.setObjectName(_fromUtf8("btnPanes7"))
        self.btnPedido57 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido57.setGeometry(QtCore.QRect(450, 320, 221, 111))
        self.btnPedido57.setObjectName(_fromUtf8("btnPedido57"))
        panes7Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(panes7Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        panes7Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(panes7Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        panes7Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(panes7Window)
        QtCore.QMetaObject.connectSlotsByName(panes7Window)

    def retranslateUi(self, panes7Window):
        panes7Window.setWindowTitle(_translate("panes7Window", "MainWindow", None))
        self.textEdit_2.setHtml(_translate("panes7Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">TRIPLE VARIOS</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">4.00</span></p></body></html>", None))
        self.btnImprimir57.setText(_translate("panes7Window", "IMPRIMIR ", None))
        self.btnPanes7.setText(_translate("panes7Window", "SANDWICHES, JUGOS Y BEBIDAS", None))
        self.btnPedido57.setText(_translate("panes7Window", "OTRO PEDIDO ", None))
        self.menuMENUTEC.setTitle(_translate("panes7Window", "MENUTEC", None))

