# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panes.ui'
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

class Ui_panesWindow(object):
    def setupUi(self, panesWindow):
        panesWindow.setObjectName(_fromUtf8("panesWindow"))
        panesWindow.resize(800, 480)
        self.centralwidget = QtGui.QWidget(panesWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.checkBox_4 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(650, 250, 101, 31))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_6 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(650, 330, 101, 31))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_5 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(650, 290, 101, 31))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(650, 130, 101, 31))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(650, 170, 101, 31))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.btnMixto0 = QtGui.QPushButton(self.centralwidget)
        self.btnMixto0.setGeometry(QtCore.QRect(30, 130, 591, 41))
        self.btnMixto0.setObjectName(_fromUtf8("btnMixto0"))
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(650, 210, 101, 31))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.btnChorizo0 = QtGui.QPushButton(self.centralwidget)
        self.btnChorizo0.setGeometry(QtCore.QRect(30, 290, 591, 41))
        self.btnChorizo0.setObjectName(_fromUtf8("btnChorizo0"))
        self.btnFilete0 = QtGui.QPushButton(self.centralwidget)
        self.btnFilete0.setGeometry(QtCore.QRect(30, 250, 591, 41))
        self.btnFilete0.setObjectName(_fromUtf8("btnFilete0"))
        self.btnPan0 = QtGui.QPushButton(self.centralwidget)
        self.btnPan0.setGeometry(QtCore.QRect(30, 210, 591, 41))
        self.btnPan0.setObjectName(_fromUtf8("btnPan0"))
        self.btnHamburguesa0 = QtGui.QPushButton(self.centralwidget)
        self.btnHamburguesa0.setGeometry(QtCore.QRect(30, 170, 591, 41))
        self.btnHamburguesa0.setObjectName(_fromUtf8("btnHamburguesa0"))
        self.btnTriple0 = QtGui.QPushButton(self.centralwidget)
        self.btnTriple0.setGeometry(QtCore.QRect(30, 370, 591, 41))
        self.btnTriple0.setObjectName(_fromUtf8("btnTriple0"))
        self.btnCroissant0 = QtGui.QPushButton(self.centralwidget)
        self.btnCroissant0.setGeometry(QtCore.QRect(30, 330, 591, 41))
        self.btnCroissant0.setObjectName(_fromUtf8("btnCroissant0"))
        self.checkBox_7 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(650, 370, 101, 31))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.btnPanes0 = QtGui.QPushButton(self.centralwidget)
        self.btnPanes0.setGeometry(QtCore.QRect(190, 10, 331, 91))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPanes0.setIcon(icon)
        self.btnPanes0.setObjectName(_fromUtf8("btnPanes0"))
        self.btnIzquierda5 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda5.setGeometry(QtCore.QRect(60, 10, 81, 101))
        self.btnIzquierda5.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda5.setIcon(icon1)
        self.btnIzquierda5.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda5.setObjectName(_fromUtf8("btnIzquierda5"))
        panesWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(panesWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        panesWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(panesWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        panesWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(panesWindow)
        QtCore.QMetaObject.connectSlotsByName(panesWindow)

    def retranslateUi(self, panesWindow):
        panesWindow.setWindowTitle(_translate("panesWindow", "MainWindow", None))
        self.checkBox_4.setText(_translate("panesWindow", "10.00", None))
        self.checkBox_6.setText(_translate("panesWindow", "6.00", None))
        self.checkBox_5.setText(_translate("panesWindow", "8.00", None))
        self.checkBox.setText(_translate("panesWindow", "12.00", None))
        self.checkBox_2.setText(_translate("panesWindow", "10.00", None))
        self.btnMixto0.setText(_translate("panesWindow", "Mixto Completo Caliente", None))
        self.checkBox_3.setText(_translate("panesWindow", "12.00", None))
        self.btnChorizo0.setText(_translate("panesWindow", "Chorizo", None))
        self.btnFilete0.setText(_translate("panesWindow", "Filete De Pollo", None))
        self.btnPan0.setText(_translate("panesWindow", "Pan C/ Pollo", None))
        self.btnHamburguesa0.setText(_translate("panesWindow", "Hamburguesa Pollo/Carne", None))
        self.btnTriple0.setText(_translate("panesWindow", "Triple Varios", None))
        self.btnCroissant0.setText(_translate("panesWindow", "Croissant", None))
        self.checkBox_7.setText(_translate("panesWindow", "6.00", None))
        self.btnPanes0.setText(_translate("panesWindow", "SANDWICHES, JUGOS Y BEBIDAS", None))
        self.menuMENUTEC.setTitle(_translate("panesWindow", "MENUTEC", None))

