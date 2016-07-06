# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panes6.ui'
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

class Ui_panes6Window(object):
    def setupUi(self, panes6Window):
        panes6Window.setObjectName(_fromUtf8("panes6Window"))
        panes6Window.resize(800, 480)
        self.centralwidget = QtGui.QWidget(panes6Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnImprimir56 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir56.setGeometry(QtCore.QRect(100, 320, 201, 111))
        self.btnImprimir56.setObjectName(_fromUtf8("btnImprimir56"))
        self.btnPedido56 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido56.setGeometry(QtCore.QRect(430, 320, 221, 111))
        self.btnPedido56.setObjectName(_fromUtf8("btnPedido56"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(50, 140, 661, 171))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.btnIzquierda56 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda56.setGeometry(QtCore.QRect(70, 20, 81, 101))
        self.btnIzquierda56.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda56.setIcon(icon)
        self.btnIzquierda56.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda56.setObjectName(_fromUtf8("btnIzquierda56"))
        self.btnPanes6 = QtGui.QPushButton(self.centralwidget)
        self.btnPanes6.setGeometry(QtCore.QRect(230, 30, 381, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPanes6.setIcon(icon1)
        self.btnPanes6.setObjectName(_fromUtf8("btnPanes6"))
        panes6Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(panes6Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        panes6Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(panes6Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        panes6Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(panes6Window)
        QtCore.QMetaObject.connectSlotsByName(panes6Window)

    def retranslateUi(self, panes6Window):
        panes6Window.setWindowTitle(_translate("panes6Window", "MainWindow", None))
        self.btnImprimir56.setText(_translate("panes6Window", "IMPRIMIR ", None))
        self.btnPedido56.setText(_translate("panes6Window", "OTRO PEDIDO ", None))
        self.textEdit_2.setHtml(_translate("panes6Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">CROISSANT</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">4.50</span></p></body></html>", None))
        self.btnPanes6.setText(_translate("panes6Window", "SANDWICHES, JUGOS Y BEBIDAS", None))
        self.menuMENUTEC.setTitle(_translate("panes6Window", "MENUTEC", None))

