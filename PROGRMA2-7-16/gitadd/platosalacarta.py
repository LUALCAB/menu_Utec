# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'platosalacarta.ui'
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

class Ui_pcWindow(object):
    def setupUi(self, pcWindow):
        pcWindow.setObjectName(_fromUtf8("pcWindow"))
        pcWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(pcWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnLomosaltado0 = QtGui.QPushButton(self.centralwidget)
        self.btnLomosaltado0.setGeometry(QtCore.QRect(20, 170, 621, 61))
        self.btnLomosaltado0.setObjectName(_fromUtf8("btnLomosaltado0"))
        self.btnPlatosalacarta0 = QtGui.QPushButton(self.centralwidget)
        self.btnPlatosalacarta0.setGeometry(QtCore.QRect(250, 40, 311, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlatosalacarta0.setIcon(icon)
        self.btnPlatosalacarta0.setObjectName(_fromUtf8("btnPlatosalacarta0"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(660, 190, 101, 31))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.btnAlfredo0 = QtGui.QPushButton(self.centralwidget)
        self.btnAlfredo0.setGeometry(QtCore.QRect(20, 300, 621, 51))
        self.btnAlfredo0.setObjectName(_fromUtf8("btnAlfredo0"))
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(660, 310, 101, 31))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.btnIzquierda4 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda4.setGeometry(QtCore.QRect(70, 30, 81, 101))
        self.btnIzquierda4.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda4.setIcon(icon1)
        self.btnIzquierda4.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda4.setObjectName(_fromUtf8("btnIzquierda4"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(660, 250, 101, 31))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.btnPollosaltado0 = QtGui.QPushButton(self.centralwidget)
        self.btnPollosaltado0.setGeometry(QtCore.QRect(20, 240, 621, 51))
        self.btnPollosaltado0.setObjectName(_fromUtf8("btnPollosaltado0"))
        self.btnTallarin0 = QtGui.QPushButton(self.centralwidget)
        self.btnTallarin0.setGeometry(QtCore.QRect(20, 360, 621, 51))
        self.btnTallarin0.setObjectName(_fromUtf8("btnTallarin0"))
        self.btnChifa0 = QtGui.QPushButton(self.centralwidget)
        self.btnChifa0.setGeometry(QtCore.QRect(20, 420, 621, 51))
        self.btnChifa0.setObjectName(_fromUtf8("btnChifa0"))
        self.btnCubana0 = QtGui.QPushButton(self.centralwidget)
        self.btnCubana0.setGeometry(QtCore.QRect(20, 480, 621, 51))
        self.btnCubana0.setObjectName(_fromUtf8("btnCubana0"))
        self.checkBox_4 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(660, 370, 101, 31))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(660, 430, 101, 31))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(660, 490, 101, 31))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        pcWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(pcWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        pcWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(pcWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        pcWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(pcWindow)
        QtCore.QMetaObject.connectSlotsByName(pcWindow)

    def retranslateUi(self, pcWindow):
        pcWindow.setWindowTitle(_translate("pcWindow", "MainWindow", None))
        self.btnLomosaltado0.setText(_translate("pcWindow", "Lomo Saltado", None))
        self.btnPlatosalacarta0.setText(_translate("pcWindow", "PLATOS A LA CARTA", None))
        self.checkBox.setText(_translate("pcWindow", "12.00", None))
        self.btnAlfredo0.setText(_translate("pcWindow", "Spaghetti a lo Alfredo", None))
        self.checkBox_3.setText(_translate("pcWindow", "12.00", None))
        self.checkBox_2.setText(_translate("pcWindow", "10.00", None))
        self.btnPollosaltado0.setText(_translate("pcWindow", "Pollo Saltado", None))
        self.btnTallarin0.setText(_translate("pcWindow", "Tallarín Saltado C/ Pollo", None))
        self.btnChifa0.setText(_translate("pcWindow", "Arroz Chaufa de Pollo", None))
        self.btnCubana0.setText(_translate("pcWindow", "Arroz a la Cubana", None))
        self.checkBox_4.setText(_translate("pcWindow", "10.00", None))
        self.checkBox_5.setText(_translate("pcWindow", "8.00", None))
        self.checkBox_6.setText(_translate("pcWindow", "6.00", None))
        self.menuMENUTEC.setTitle(_translate("pcWindow", "MENUTEC", None))

