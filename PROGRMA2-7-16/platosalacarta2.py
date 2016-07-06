# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'platosalacarta2.ui'
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

class Ui_pc2Window(object):
    def setupUi(self, pc2Window):
        pc2Window.setObjectName(_fromUtf8("pc2Window"))
        pc2Window.resize(800, 480)
        self.centralwidget = QtGui.QWidget(pc2Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 130, 661, 171))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.btnIzquierda42 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda42.setGeometry(QtCore.QRect(110, 20, 81, 101))
        self.btnIzquierda42.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda42.setIcon(icon)
        self.btnIzquierda42.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda42.setObjectName(_fromUtf8("btnIzquierda42"))
        self.btnImprimir42 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir42.setGeometry(QtCore.QRect(130, 310, 201, 111))
        self.btnImprimir42.setObjectName(_fromUtf8("btnImprimir42"))
        self.btnPlatosalacarta2 = QtGui.QPushButton(self.centralwidget)
        self.btnPlatosalacarta2.setGeometry(QtCore.QRect(240, 30, 381, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlatosalacarta2.setIcon(icon1)
        self.btnPlatosalacarta2.setObjectName(_fromUtf8("btnPlatosalacarta2"))
        self.btnPedido42 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido42.setGeometry(QtCore.QRect(450, 310, 221, 111))
        self.btnPedido42.setObjectName(_fromUtf8("btnPedido42"))
        pc2Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(pc2Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        pc2Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(pc2Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        pc2Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(pc2Window)
        QtCore.QMetaObject.connectSlotsByName(pc2Window)

    def retranslateUi(self, pc2Window):
        pc2Window.setWindowTitle(_translate("pc2Window", "MainWindow", None))
        self.textEdit_2.setHtml(_translate("pc2Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">POLLO SALTADO  </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">10.00</span></p></body></html>", None))
        self.btnImprimir42.setText(_translate("pc2Window", "IMPRIMIR ", None))
        self.btnPlatosalacarta2.setText(_translate("pc2Window", "PLATOS A LA CARTA", None))
        self.btnPedido42.setText(_translate("pc2Window", "OTRO PEDIDO ", None))
        self.menuMENUTEC.setTitle(_translate("pc2Window", "MENUTEC", None))

