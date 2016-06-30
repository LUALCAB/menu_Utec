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
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 190, 191, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 40, 311, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(660, 190, 101, 31))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 310, 191, 41))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(660, 30, 71, 101))
        self.pushButton_6.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("la-flecha-azul-al-lado-de-icono-5057-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 190, 171, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(660, 310, 101, 31))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 30, 81, 101))
        self.pushButton_2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 300, 171, 61))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(660, 250, 101, 31))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 250, 191, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 240, 171, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 370, 191, 41))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 430, 191, 41))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 490, 191, 41))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 360, 171, 61))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 420, 171, 61))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 490, 171, 61))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.checkBox_4 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(660, 370, 101, 31))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(660, 440, 101, 31))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(660, 500, 101, 31))
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
        self.pushButton_3.setText(_translate("pcWindow", "Lomo Saltado", None))
        self.pushButton.setText(_translate("pcWindow", "PLATOS A LA CARTA", None))
        self.checkBox.setText(_translate("pcWindow", "12.00", None))
        self.pushButton_5.setText(_translate("pcWindow", "Spaghetti a lo Alfredo", None))
        self.label.setText(_translate("pcWindow", "(Descripcion del menú )", None))
        self.checkBox_3.setText(_translate("pcWindow", "12.00", None))
        self.label_3.setText(_translate("pcWindow", "(Descripcion del menú )", None))
        self.checkBox_2.setText(_translate("pcWindow", "10.00", None))
        self.pushButton_4.setText(_translate("pcWindow", "Pollo Saltado", None))
        self.label_2.setText(_translate("pcWindow", "(Descripcion del menú )", None))
        self.pushButton_7.setText(_translate("pcWindow", "Tallarín Saltado C/ Pollo", None))
        self.pushButton_8.setText(_translate("pcWindow", "Arroz Chaufa de Pollo", None))
        self.pushButton_9.setText(_translate("pcWindow", "Arroz a la Cubana", None))
        self.label_4.setText(_translate("pcWindow", "(Descripcion del menú )", None))
        self.label_5.setText(_translate("pcWindow", "(Descripcion del menú )", None))
        self.label_6.setText(_translate("pcWindow", "(Descripcion del menú )", None))
        self.checkBox_4.setText(_translate("pcWindow", "10.00", None))
        self.checkBox_5.setText(_translate("pcWindow", "8.00", None))
        self.checkBox_6.setText(_translate("pcWindow", "6.00", None))
        self.menuMENUTEC.setTitle(_translate("pcWindow", "MENUTEC", None))

