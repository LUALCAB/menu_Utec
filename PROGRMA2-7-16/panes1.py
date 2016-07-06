# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panes1.ui'
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

class Ui_panes1Window(object):
    def setupUi(self, panes1Window):
        panes1Window.setObjectName(_fromUtf8("panes1Window"))
        panes1Window.resize(800, 480)
        self.centralwidget = QtGui.QWidget(panes1Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 130, 661, 171))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.btnIzquierda51 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda51.setGeometry(QtCore.QRect(60, 20, 81, 101))
        self.btnIzquierda51.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda51.setIcon(icon)
        self.btnIzquierda51.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda51.setObjectName(_fromUtf8("btnIzquierda51"))
        self.btnImprimir51 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir51.setGeometry(QtCore.QRect(110, 310, 201, 111))
        self.btnImprimir51.setObjectName(_fromUtf8("btnImprimir51"))
        self.btnPanes1 = QtGui.QPushButton(self.centralwidget)
        self.btnPanes1.setGeometry(QtCore.QRect(220, 30, 381, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPanes1.setIcon(icon1)
        self.btnPanes1.setObjectName(_fromUtf8("btnPanes1"))
        self.btnPedido51 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido51.setGeometry(QtCore.QRect(430, 310, 221, 111))
        self.btnPedido51.setObjectName(_fromUtf8("btnPedido51"))
        panes1Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(panes1Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        panes1Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(panes1Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        panes1Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(panes1Window)
        QtCore.QMetaObject.connectSlotsByName(panes1Window)

    def retranslateUi(self, panes1Window):
        panes1Window.setWindowTitle(_translate("panes1Window", "MainWindow", None))
        self.textEdit_2.setHtml(_translate("panes1Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">MIXTO COMPLETO CALIENTE  </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">4.50</span></p></body></html>", None))
        self.btnImprimir51.setText(_translate("panes1Window", "IMPRIMIR ", None))
        self.btnPanes1.setText(_translate("panes1Window", "SANDWICHES, JUGOS Y BEBIDAS", None))
        self.btnPedido51.setText(_translate("panes1Window", "OTRO PEDIDO ", None))
        self.menuMENUTEC.setTitle(_translate("panes1Window", "MENUTEC", None))

