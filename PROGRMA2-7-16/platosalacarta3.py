# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'platosalacarta3.ui'
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

class Ui_pc3Window(object):
    def setupUi(self, pc3Window):
        pc3Window.setObjectName(_fromUtf8("pc3Window"))
        pc3Window.resize(800, 480)
        self.centralwidget = QtGui.QWidget(pc3Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 130, 661, 171))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.btnIzquierda43 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda43.setGeometry(QtCore.QRect(80, 20, 81, 101))
        self.btnIzquierda43.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda43.setIcon(icon)
        self.btnIzquierda43.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda43.setObjectName(_fromUtf8("btnIzquierda43"))
        self.btnImprimir43 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir43.setGeometry(QtCore.QRect(130, 310, 201, 111))
        self.btnImprimir43.setObjectName(_fromUtf8("btnImprimir43"))
        self.btnPlatosalacarta3 = QtGui.QPushButton(self.centralwidget)
        self.btnPlatosalacarta3.setGeometry(QtCore.QRect(230, 30, 381, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlatosalacarta3.setIcon(icon1)
        self.btnPlatosalacarta3.setObjectName(_fromUtf8("btnPlatosalacarta3"))
        self.btnPedido43 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido43.setGeometry(QtCore.QRect(440, 310, 221, 111))
        self.btnPedido43.setObjectName(_fromUtf8("btnPedido43"))
        pc3Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(pc3Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        pc3Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(pc3Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        pc3Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(pc3Window)
        QtCore.QMetaObject.connectSlotsByName(pc3Window)

    def retranslateUi(self, pc3Window):
        pc3Window.setWindowTitle(_translate("pc3Window", "MainWindow", None))
        self.textEdit_2.setHtml(_translate("pc3Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">SPAGHETTI A LO ALFREDO  </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">12.00</span></p></body></html>", None))
        self.btnImprimir43.setText(_translate("pc3Window", "IMPRIMIR ", None))
        self.btnPlatosalacarta3.setText(_translate("pc3Window", "PLATOS A LA CARTA", None))
        self.btnPedido43.setText(_translate("pc3Window", "OTRO PEDIDO ", None))
        self.menuMENUTEC.setTitle(_translate("pc3Window", "MENUTEC", None))

