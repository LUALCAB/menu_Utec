# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'platosalacarta4.ui'
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

class Ui_pc4Window(object):
    def setupUi(self, pc4Window):
        pc4Window.setObjectName(_fromUtf8("pc4Window"))
        pc4Window.resize(800, 480)
        self.centralwidget = QtGui.QWidget(pc4Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnPedido44 = QtGui.QPushButton(self.centralwidget)
        self.btnPedido44.setGeometry(QtCore.QRect(440, 320, 221, 111))
        self.btnPedido44.setObjectName(_fromUtf8("btnPedido44"))
        self.btnIzquierda44 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda44.setGeometry(QtCore.QRect(110, 30, 81, 101))
        self.btnIzquierda44.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda44.setIcon(icon)
        self.btnIzquierda44.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda44.setObjectName(_fromUtf8("btnIzquierda44"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 140, 661, 171))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.btnPlatosalacarta4 = QtGui.QPushButton(self.centralwidget)
        self.btnPlatosalacarta4.setGeometry(QtCore.QRect(230, 40, 381, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlatosalacarta4.setIcon(icon1)
        self.btnPlatosalacarta4.setObjectName(_fromUtf8("btnPlatosalacarta4"))
        self.btnImprimir44 = QtGui.QPushButton(self.centralwidget)
        self.btnImprimir44.setGeometry(QtCore.QRect(120, 320, 201, 111))
        self.btnImprimir44.setObjectName(_fromUtf8("btnImprimir44"))
        pc4Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(pc4Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        pc4Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(pc4Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        pc4Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(pc4Window)
        QtCore.QMetaObject.connectSlotsByName(pc4Window)

    def retranslateUi(self, pc4Window):
        pc4Window.setWindowTitle(_translate("pc4Window", "MainWindow", None))
        self.btnPedido44.setText(_translate("pc4Window", "OTRO PEDIDO ", None))
        self.textEdit_2.setHtml(_translate("pc4Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">TALLARIN SALTADO C/ POLLO  </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">10.00</span></p></body></html>", None))
        self.btnPlatosalacarta4.setText(_translate("pc4Window", "PLATOS A LA CARTA", None))
        self.btnImprimir44.setText(_translate("pc4Window", "IMPRIMIR ", None))
        self.menuMENUTEC.setTitle(_translate("pc4Window", "MENUTEC", None))

