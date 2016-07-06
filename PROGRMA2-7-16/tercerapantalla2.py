# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tercerapantalla2.ui'
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

class Ui_tercera2Window(object):
    def setupUi(self, tercera2Window):
        tercera2Window.setObjectName(_fromUtf8("tercera2Window"))
        tercera2Window.resize(800, 480)
        self.centralwidget = QtGui.QWidget(tercera2Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnMenu32 = QtGui.QPushButton(self.centralwidget)
        self.btnMenu32.setGeometry(QtCore.QRect(240, 30, 381, 81))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMenu32.setIcon(icon)
        self.btnMenu32.setObjectName(_fromUtf8("btnMenu32"))
        self.btnImprimir32 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir32.setGeometry(QtCore.QRect(120, 310, 201, 111))
        self.btnImprimir32.setObjectName(_fromUtf8("btnImprimir32"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 130, 661, 171))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.btnIzquierda32 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda32.setGeometry(QtCore.QRect(100, 20, 81, 101))
        self.btnIzquierda32.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda32.setIcon(icon1)
        self.btnIzquierda32.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda32.setObjectName(_fromUtf8("btnIzquierda32"))
        self.btnPedido32 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido32.setGeometry(QtCore.QRect(440, 310, 221, 111))
        self.btnPedido32.setObjectName(_fromUtf8("btnPedido32"))
        tercera2Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(tercera2Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        tercera2Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(tercera2Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        tercera2Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(tercera2Window)
        QtCore.QMetaObject.connectSlotsByName(tercera2Window)

    def retranslateUi(self, tercera2Window):
        tercera2Window.setWindowTitle(_translate("tercera2Window", "MainWindow", None))
        self.btnMenu32.setText(_translate("tercera2Window", "MENÚ", None))
        self.btnImprimir32.setText(_translate("tercera2Window", "IMPRIMIR ", None))
        self.textEdit.setHtml(_translate("tercera2Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">MENÚ EJECUTIVO </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">9.50</span></p></body></html>", None))
        self.btnPedido32.setText(_translate("tercera2Window", "OTRO PEDIDO ", None))
        self.menuMENUTEC.setTitle(_translate("tercera2Window", "MENUTEC", None))

