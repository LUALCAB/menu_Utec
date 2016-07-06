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
        panes5Window.resize(800, 480)
        self.centralwidget = QtGui.QWidget(panes5Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnPanes5 = QtGui.QPushButton(self.centralwidget)
        self.btnPanes5.setGeometry(QtCore.QRect(250, 30, 381, 81))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPanes5.setIcon(icon)
        self.btnPanes5.setObjectName(_fromUtf8("btnPanes5"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 130, 661, 171))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.btnImprimir55 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir55.setGeometry(QtCore.QRect(120, 310, 201, 111))
        self.btnImprimir55.setObjectName(_fromUtf8("btnImprimir55"))
        self.btnPedido55 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido55.setGeometry(QtCore.QRect(460, 310, 221, 111))
        self.btnPedido55.setObjectName(_fromUtf8("btnPedido55"))
        self.btnIzquierda55 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda55.setGeometry(QtCore.QRect(90, 10, 81, 101))
        self.btnIzquierda55.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda55.setIcon(icon1)
        self.btnIzquierda55.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda55.setObjectName(_fromUtf8("btnIzquierda55"))
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
        self.btnPanes5.setText(_translate("panes5Window", "SANDWICHES, JUGOS Y BEBIDAS", None))
        self.textEdit_2.setHtml(_translate("panes5Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">CHORIZO</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">4.50</span></p></body></html>", None))
        self.btnImprimir55.setText(_translate("panes5Window", "IMPRIMIR ", None))
        self.btnPedido55.setText(_translate("panes5Window", "OTRO PEDIDO ", None))
        self.menuMENUTEC.setTitle(_translate("panes5Window", "MENUTEC", None))

