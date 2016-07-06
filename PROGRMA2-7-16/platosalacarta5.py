# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'platosalacarta5.ui'
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

class Ui_pc5Window(object):
    def setupUi(self, pc5Window):
        pc5Window.setObjectName(_fromUtf8("pc5Window"))
        pc5Window.resize(800, 480)
        self.centralwidget = QtGui.QWidget(pc5Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnIzquierda45 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda45.setGeometry(QtCore.QRect(100, 20, 81, 101))
        self.btnIzquierda45.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda45.setIcon(icon)
        self.btnIzquierda45.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda45.setObjectName(_fromUtf8("btnIzquierda45"))
        self.btnPedido45 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido45.setGeometry(QtCore.QRect(450, 310, 221, 111))
        self.btnPedido45.setObjectName(_fromUtf8("btnPedido45"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 130, 661, 171))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.btnPlatosalacarta5 = QtGui.QPushButton(self.centralwidget)
        self.btnPlatosalacarta5.setGeometry(QtCore.QRect(230, 30, 381, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlatosalacarta5.setIcon(icon1)
        self.btnPlatosalacarta5.setObjectName(_fromUtf8("btnPlatosalacarta5"))
        self.btnImprimir45 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir45.setGeometry(QtCore.QRect(120, 310, 201, 111))
        self.btnImprimir45.setObjectName(_fromUtf8("btnImprimir45"))
        pc5Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(pc5Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        pc5Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(pc5Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        pc5Window.setStatusBar(self.statusbar)

        self.retranslateUi(pc5Window)
        QtCore.QMetaObject.connectSlotsByName(pc5Window)

    def retranslateUi(self, pc5Window):
        pc5Window.setWindowTitle(_translate("pc5Window", "MainWindow", None))
        self.btnPedido45.setText(_translate("pc5Window", "OTRO PEDIDO ", None))
        self.textEdit_2.setHtml(_translate("pc5Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">ARROZ CHAUFA DE POLLO  </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">8.00</span></p></body></html>", None))
        self.btnPlatosalacarta5.setText(_translate("pc5Window", "PLATOS A LA CARTA", None))
        self.btnImprimir45.setText(_translate("pc5Window", "IMPRIMIR ", None))

