# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'platosalacarta6.ui'
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

class Ui_pc6Window(object):
    def setupUi(self, pc6Window):
        pc6Window.setObjectName(_fromUtf8("pc6Window"))
        pc6Window.resize(804, 600)
        self.centralwidget = QtGui.QWidget(pc6Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnIzquierda46 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda46.setGeometry(QtCore.QRect(70, 50, 81, 101))
        self.btnIzquierda46.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda46.setIcon(icon)
        self.btnIzquierda46.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda46.setObjectName(_fromUtf8("btnIzquierda46"))
        self.btnImprimir46 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir46.setGeometry(QtCore.QRect(120, 360, 201, 111))
        self.btnImprimir46.setObjectName(_fromUtf8("btnImprimir46"))
        self.btnPedido46 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido46.setGeometry(QtCore.QRect(440, 360, 221, 111))
        self.btnPedido46.setObjectName(_fromUtf8("btnPedido46"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 170, 661, 171))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.btnPlatosalacarta6 = QtGui.QPushButton(self.centralwidget)
        self.btnPlatosalacarta6.setGeometry(QtCore.QRect(230, 60, 381, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlatosalacarta6.setIcon(icon1)
        self.btnPlatosalacarta6.setObjectName(_fromUtf8("btnPlatosalacarta6"))
        pc6Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(pc6Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        pc6Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(pc6Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        pc6Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(pc6Window)
        QtCore.QMetaObject.connectSlotsByName(pc6Window)

    def retranslateUi(self, pc6Window):
        pc6Window.setWindowTitle(_translate("pc6Window", "MainWindow", None))
        self.btnImprimir46.setText(_translate("pc6Window", "IMPRIMIR ", None))
        self.btnPedido46.setText(_translate("pc6Window", "OTRO PEDIDO ", None))
        self.textEdit_2.setHtml(_translate("pc6Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">ARROZ A LA CUBANA  </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">6.00</span></p></body></html>", None))
        self.btnPlatosalacarta6.setText(_translate("pc6Window", "PLATOS A LA CARTA", None))
        self.menuMENUTEC.setTitle(_translate("pc6Window", "MENUTEC", None))

