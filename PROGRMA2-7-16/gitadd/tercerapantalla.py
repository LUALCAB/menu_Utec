# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TERCERAPANTALLA.ui'
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

class Ui_terceraWindow(object):
    def setupUi(self, terceraWindow):
        terceraWindow.setObjectName(_fromUtf8("terceraWindow"))
        terceraWindow.resize(800, 606)
        self.centralwidget = QtGui.QWidget(terceraWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnMenu3 = QtGui.QPushButton(self.centralwidget)
        self.btnMenu3.setGeometry(QtCore.QRect(240, 30, 381, 81))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMenu3.setIcon(icon)
        self.btnMenu3.setObjectName(_fromUtf8("btnMenu3"))
        self.btnIzquierda3 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda3.setGeometry(QtCore.QRect(80, 20, 81, 101))
        self.btnIzquierda3.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda3.setIcon(icon1)
        self.btnIzquierda3.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda3.setObjectName(_fromUtf8("btnIzquierda3"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 140, 661, 171))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.btnImprimir3 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir3.setGeometry(QtCore.QRect(120, 330, 201, 111))
        self.btnImprimir3.setObjectName(_fromUtf8("btnImprimir3"))
        self.btnPedido3 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido3.setGeometry(QtCore.QRect(450, 330, 221, 111))
        self.btnPedido3.setObjectName(_fromUtf8("btnPedido3"))
        terceraWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(terceraWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        terceraWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(terceraWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        terceraWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(terceraWindow)
        QtCore.QMetaObject.connectSlotsByName(terceraWindow)

    def retranslateUi(self, terceraWindow):
        terceraWindow.setWindowTitle(_translate("terceraWindow", "MainWindow", None))
        self.btnMenu3.setText(_translate("terceraWindow", "MENÚ", None))
        self.textEdit.setHtml(_translate("terceraWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">MENÚ ECONÓMICO </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">6.00</span></p></body></html>", None))
        self.btnImprimir3.setText(_translate("terceraWindow", "IMPRIMIR ", None))
        self.btnPedido3.setText(_translate("terceraWindow", "OTRO PEDIDO ", None))
        self.menuMENUTEC.setTitle(_translate("terceraWindow", "MENUTEC", None))

