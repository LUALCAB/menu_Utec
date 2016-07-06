# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tercerapantalla1.ui'
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

class Ui_tercera1Window(object):
    def setupUi(self, tercera1Window):
        tercera1Window.setObjectName(_fromUtf8("tercera1Window"))
        tercera1Window.resize(800, 480)
        self.centralwidget = QtGui.QWidget(tercera1Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnImprimir31 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir31.setGeometry(QtCore.QRect(100, 310, 201, 111))
        self.btnImprimir31.setObjectName(_fromUtf8("btnImprimir31"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 130, 661, 171))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.btnIzquierda31 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda31.setGeometry(QtCore.QRect(80, 20, 81, 101))
        self.btnIzquierda31.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda31.setIcon(icon)
        self.btnIzquierda31.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda31.setObjectName(_fromUtf8("btnIzquierda31"))
        self.btnMenu31 = QtGui.QPushButton(self.centralwidget)
        self.btnMenu31.setGeometry(QtCore.QRect(240, 30, 381, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMenu31.setIcon(icon1)
        self.btnMenu31.setObjectName(_fromUtf8("btnMenu31"))
        self.btnPedido31 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido31.setGeometry(QtCore.QRect(450, 310, 221, 111))
        self.btnPedido31.setObjectName(_fromUtf8("btnPedido31"))
        tercera1Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(tercera1Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        tercera1Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(tercera1Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        tercera1Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(tercera1Window)
        QtCore.QMetaObject.connectSlotsByName(tercera1Window)

    def retranslateUi(self, tercera1Window):
        tercera1Window.setWindowTitle(_translate("tercera1Window", "MainWindow", None))
        self.btnImprimir31.setText(_translate("tercera1Window", "IMPRIMIR ", None))
        self.textEdit.setHtml(_translate("tercera1Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">MENÚ ESTUDIANTIL </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">8.00</span></p></body></html>", None))
        self.btnMenu31.setText(_translate("tercera1Window", "MENÚ", None))
        self.btnPedido31.setText(_translate("tercera1Window", "OTRO PEDIDO ", None))
        self.menuMENUTEC.setTitle(_translate("tercera1Window", "MENUTEC", None))

