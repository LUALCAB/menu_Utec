#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui  # Import the PyQt4 module we'll need
from PyQt4 import QtCore
import sys  # We need sys so that we can pass argv to QApplication

import primerapantalla #Esto se genera de esto: primerapantalla.ui
import segundapantalla #Esto se genera de esto: segundapantalla.ui
import tercerapantalla
import platosalacarta
import panes
import tercerapantalla1

class MainWindow(QtGui.QMainWindow, primerapantalla.Ui_PrimeraWindow):
    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btnMenu.clicked.connect(self.btnMenuClicked)
        self.btnPlatoslacarta.clicked.connect(self.btnPlatosalacartaClicked)
        self.btnSandwiches.clicked.connect(self.btnSandwichesClicked)
        self.secondW = None
        self.thirdW = None
        self.fourW = None

    def btnMenuClicked(self):
        if self.secondW is None:
            self.secondW = SecondWindow(self)
        self.secondW.show()

    def btnPlatosalacartaClicked(self):
    	if self.thirdW is None:
    		self.thirdW = ThirdWindow(self)
    	self.thirdW.show()

    def btnSandwichesClicked(self):
        if self.fourW is None:
            self.fourW = FourWindow(self)
        self.fourW.show()

class SecondWindow(QtGui.QMainWindow, segundapantalla.Ui_segundaWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda2.clicked.connect(self.btnIzquierda2Clicked)
        self.btnEconomico2.clicked.connect(self.btnEconomico2Clicked)
        self.fiveW = None
        self.sevenw = None

    def btnEconomico2Clicked(self):
        if self.sevenW is None:
            self.sevenW = SevenWindow(self)
        self.sevenW.show()




    def btnIzquierda2Clicked(self):
        if self.fiveW is None:
            self.fiveW = MainWindow(self)
        self.fiveW.show()


class ThirdWindow(QtGui.QMainWindow, platosalacarta.Ui_pcWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

class FourWindow(QtGui.QMainWindow, panes.Ui_panesWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)



class SevenWindow(QtGui.QMainWindow, tercerapantalla.Ui_terceraWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = MainWindow()  # We set the form to be our MainWindow (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function


#Convertir primerapantalla.ui a primerapantalla.py
#En el terminal: (Situado en la carpeta donde está el archivo)
#pyuic4 primerapantalla.ui -o primerapantalla.py
