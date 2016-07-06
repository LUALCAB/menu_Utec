# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'segundapantalla.ui'
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

class Ui_segundaWindow(object):
    def setupUi(self, segundaWindow):
        segundaWindow.setObjectName(_fromUtf8("segundaWindow"))
        segundaWindow.resize(800, 450)
        self.centralwidget = QtGui.QWidget(segundaWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnMenu2 = QtGui.QPushButton(self.centralwidget)
        self.btnMenu2.setGeometry(QtCore.QRect(200, 20, 441, 91))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMenu2.setIcon(icon)
        self.btnMenu2.setObjectName(_fromUtf8("btnMenu2"))
        self.btnIzquierda2 = QtGui.QPushButton(self.centralwidget)
        self.btnIzquierda2.setGeometry(QtCore.QRect(90, 20, 81, 101))
        self.btnIzquierda2.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzquierda2.setIcon(icon1)
        self.btnIzquierda2.setIconSize(QtCore.QSize(100, 100))
        self.btnIzquierda2.setObjectName(_fromUtf8("btnIzquierda2"))
        self.btnEconomico2 = QtGui.QPushButton(self.centralwidget)
        self.btnEconomico2.setGeometry(QtCore.QRect(120, 130, 521, 91))
        self.btnEconomico2.setObjectName(_fromUtf8("btnEconomico2"))
        self.bntEstudiantil2 = QtGui.QPushButton(self.centralwidget)
        self.bntEstudiantil2.setGeometry(QtCore.QRect(120, 230, 521, 81))
        self.bntEstudiantil2.setObjectName(_fromUtf8("bntEstudiantil2"))
        self.btnEjecutivo2 = QtGui.QPushButton(self.centralwidget)
        self.btnEjecutivo2.setGeometry(QtCore.QRect(120, 320, 521, 81))
        self.btnEjecutivo2.setObjectName(_fromUtf8("btnEjecutivo2"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(680, 140, 101, 71))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(680, 240, 111, 71))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(680, 330, 111, 71))
        self.checkBox_3.setCheckable(False)
        self.checkBox_3.setTristate(False)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        segundaWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(segundaWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        segundaWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(segundaWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        segundaWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(segundaWindow)
        QtCore.QMetaObject.connectSlotsByName(segundaWindow)

    def retranslateUi(self, segundaWindow):
        segundaWindow.setWindowTitle(_translate("segundaWindow", "MainWindow", None))
        self.btnMenu2.setText(_translate("segundaWindow", "MENÚ", None))
        self.btnEconomico2.setText(_translate("segundaWindow", "Económico ", None))
        self.bntEstudiantil2.setText(_translate("segundaWindow", "Estudiantil", None))
        self.btnEjecutivo2.setText(_translate("segundaWindow", "Ejecutivo", None))
        self.checkBox.setText(_translate("segundaWindow", "6.00", None))
        self.checkBox_2.setText(_translate("segundaWindow", "8.00", None))
        self.checkBox_3.setText(_translate("segundaWindow", "9.50", None))
        self.menuMENUTEC.setTitle(_translate("segundaWindow", "MENUTEC", None))

