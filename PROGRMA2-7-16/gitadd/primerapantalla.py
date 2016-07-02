# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'primerapantalla.ui'
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

class Ui_PrimeraWindow(object):
    def setupUi(self, PrimeraWindow):
        PrimeraWindow.setObjectName(_fromUtf8("PrimeraWindow"))
        PrimeraWindow.resize(800, 731)
        self.centralwidget = QtGui.QWidget(PrimeraWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnMenu = QtGui.QPushButton(self.centralwidget)
        self.btnMenu.setGeometry(QtCore.QRect(40, 230, 711, 61))
        self.btnMenu.setObjectName(_fromUtf8("btnMenu"))
        self.btnPlatoslacarta = QtGui.QPushButton(self.centralwidget)
        self.btnPlatoslacarta.setGeometry(QtCore.QRect(40, 300, 711, 61))
        self.btnPlatoslacarta.setObjectName(_fromUtf8("btnPlatoslacarta"))
        self.btnSandwiches = QtGui.QPushButton(self.centralwidget)
        self.btnSandwiches.setGeometry(QtCore.QRect(40, 380, 711, 61))
        self.btnSandwiches.setObjectName(_fromUtf8("btnSandwiches"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(700, 30, 64, 23))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lblLogo = QtGui.QLabel(self.centralwidget)
        self.lblLogo.setGeometry(QtCore.QRect(70, 50, 131, 151))
        self.lblLogo.setText(_fromUtf8(""))
        self.lblLogo.setPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setObjectName(_fromUtf8("lblLogo"))
        PrimeraWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PrimeraWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        PrimeraWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PrimeraWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PrimeraWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(PrimeraWindow)
        QtCore.QMetaObject.connectSlotsByName(PrimeraWindow)

    def retranslateUi(self, PrimeraWindow):
        PrimeraWindow.setWindowTitle(_translate("PrimeraWindow", "MainWindow", None))
        self.btnMenu.setText(_translate("PrimeraWindow", "MENÚ", None))
        self.btnPlatoslacarta.setText(_translate("PrimeraWindow", "PLATOS A LA CARTA", None))
        self.btnSandwiches.setText(_translate("PrimeraWindow", "SANDWICHES, JUGOS Y BEBIDAS", None))
        self.menuMENUTEC.setTitle(_translate("PrimeraWindow", "MENUTEC ", None))
