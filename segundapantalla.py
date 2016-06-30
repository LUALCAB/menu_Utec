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
        segundaWindow.resize(834, 545)
        self.centralwidget = QtGui.QWidget(segundaWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 30, 311, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../.designer/backup/UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 20, 81, 101))
        self.pushButton_2.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../.designer/backup/flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 190, 181, 61))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 310, 181, 61))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 440, 181, 61))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 190, 171, 61))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 310, 171, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 440, 171, 61))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(680, 200, 101, 31))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(680, 320, 101, 31))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(670, 460, 101, 31))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(680, 20, 71, 101))
        self.pushButton_6.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../.designer/backup/la-flecha-azul-al-lado-de-icono-5057-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        segundaWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(segundaWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 834, 25))
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
        self.pushButton.setText(_translate("segundaWindow", "MENÚ", None))
        self.pushButton_3.setText(_translate("segundaWindow", "Económico ", None))
        self.pushButton_4.setText(_translate("segundaWindow", "Estudiantil", None))
        self.pushButton_5.setText(_translate("segundaWindow", "Ejecutivo", None))
        self.label.setText(_translate("segundaWindow", "(Descripcion del menú )", None))
        self.label_2.setText(_translate("segundaWindow", "(Descripcion del menú )", None))
        self.label_3.setText(_translate("segundaWindow", "(Descripcion del menú )", None))
        self.checkBox.setText(_translate("segundaWindow", "6.00", None))
        self.checkBox_2.setText(_translate("segundaWindow", "8.00", None))
        self.checkBox_3.setText(_translate("segundaWindow", "9.50", None))
        self.menuMENUTEC.setTitle(_translate("segundaWindow", "MENUTEC", None))

