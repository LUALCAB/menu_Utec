# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'platosalacarta1.ui'
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

class Ui_pc1Window(object):
    def setupUi(self, pc1Window):
        pc1Window.setObjectName(_fromUtf8("pc1Window"))
        pc1Window.resize(806, 600)
        self.centralwidget = QtGui.QWidget(pc1Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnPlatosalacarta1 = QtGui.QPushButton(self.centralwidget)
        self.btnPlatosalacarta1.setGeometry(QtCore.QRect(230, 70, 381, 81))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlatosalacarta1.setIcon(icon)
        self.btnPlatosalacarta1.setObjectName(_fromUtf8("btnPlatosalacarta1"))
        self.btnImprimir41 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir41.setGeometry(QtCore.QRect(120, 370, 201, 111))
        self.btnImprimir41.setObjectName(_fromUtf8("btnImprimir41"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 180, 661, 171))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.btnIzquierda41 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda41.setGeometry(QtCore.QRect(70, 60, 81, 101))
        self.btnIzquierda41.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda41.setIcon(icon1)
        self.btnIzquierda41.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda41.setObjectName(_fromUtf8("btnIzquierda41"))
        self.btnPedido41 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido41.setGeometry(QtCore.QRect(440, 370, 221, 111))
        self.btnPedido41.setObjectName(_fromUtf8("btnPedido41"))
        pc1Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(pc1Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        pc1Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(pc1Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        pc1Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(pc1Window)
        QtCore.QMetaObject.connectSlotsByName(pc1Window)

    def retranslateUi(self, pc1Window):
        pc1Window.setWindowTitle(_translate("pc1Window", "MainWindow", None))
        self.btnPlatosalacarta1.setText(_translate("pc1Window", "PLATOS A LA CARTA", None))
        self.btnImprimir41.setText(_translate("pc1Window", "IMPRIMIR ", None))
        self.textEdit_2.setHtml(_translate("pc1Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">LOMO SALTADO  </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">12.00</span></p></body></html>", None))
        self.btnPedido41.setText(_translate("pc1Window", "OTRO PEDIDO ", None))
        self.menuMENUTEC.setTitle(_translate("pc1Window", "MENUTEC", None))

