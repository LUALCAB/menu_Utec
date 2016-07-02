# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panes4.ui'
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

class Ui_panes4Window(object):
    def setupUi(self, panes4Window):
        panes4Window.setObjectName(_fromUtf8("panes4Window"))
        panes4Window.resize(800, 600)
        self.centralwidget = QtGui.QWidget(panes4Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 190, 661, 171))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.btnPanes4 = QtGui.QPushButton(self.centralwidget)
        self.btnPanes4.setGeometry(QtCore.QRect(230, 80, 381, 81))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPanes4.setIcon(icon)
        self.btnPanes4.setObjectName(_fromUtf8("btnPanes4"))
        self.btnImprimir54 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir54.setGeometry(QtCore.QRect(120, 380, 201, 111))
        self.btnImprimir54.setObjectName(_fromUtf8("btnImprimir54"))
        self.btnIzquierda54 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda54.setGeometry(QtCore.QRect(70, 70, 81, 101))
        self.btnIzquierda54.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda54.setIcon(icon1)
        self.btnIzquierda54.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda54.setObjectName(_fromUtf8("btnIzquierda54"))
        self.btnPedido54 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido54.setGeometry(QtCore.QRect(440, 380, 221, 111))
        self.btnPedido54.setObjectName(_fromUtf8("btnPedido54"))
        panes4Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(panes4Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        panes4Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(panes4Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        panes4Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(panes4Window)
        QtCore.QMetaObject.connectSlotsByName(panes4Window)

    def retranslateUi(self, panes4Window):
        panes4Window.setWindowTitle(_translate("panes4Window", "MainWindow", None))
        self.textEdit_2.setHtml(_translate("panes4Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">FILETE DE POLLO </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">4.50</span></p></body></html>", None))
        self.btnPanes4.setText(_translate("panes4Window", "SANDWICHES, JUGOS Y BEBIDAS", None))
        self.btnImprimir54.setText(_translate("panes4Window", "IMPRIMIR ", None))
        self.btnPedido54.setText(_translate("panes4Window", "OTRO PEDIDO ", None))
        self.menuMENUTEC.setTitle(_translate("panes4Window", "MENUTEC", None))

