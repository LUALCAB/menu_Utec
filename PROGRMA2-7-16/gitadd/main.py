#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui  # Import the PyQt4 module we'll need
from PyQt4 import QtCore
import sys  # We need sys so that we can pass argv to QApplication

import primerapantalla #Esto se genera de esto: primerapantalla.ui
import segundapantalla #Esto se genera de esto: segundapantalla.ui
import tercerapantalla
import tercerapantalla1
import tercerapantalla2
import platosalacarta
import platosalacarta1
import platosalacarta2
import platosalacarta3
import platosalacarta4
import platosalacarta5
import platosalacarta6
import panes
import panes1
import panes2
import panes3
import panes4
import panes5
import panes6
import panes7
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
        self.bntEstudiantil2.clicked.connect(self.btnEstudiantil2Clicked)
        self.btnMenu2.clicked.connect(self.btnMenu2Clicked)
        self.btnEjecutivo2.clicked.connect(self.btnEjecutivo2Clicked)
        self.sevenW = None
        self.sixW = None
        self.fiveW = None

    def btnEconomico2Clicked(self):
        if self.sevenW is None:
            self.sevenW = SevenWindow(self)
        self.sevenW.show()

    def btnEstudiantil2Clicked(self):
        if self.sixW is None:
            self.sixW = SixWindow(self)
        self.sixW.show()

    def btnEjecutivo2Clicked(self):
        if self.fiveW is None:
            self.fiveW = FiveWindow(self)
        self.fiveW.show()

    def btnIzquierda2Clicked(self):
        self.close()

    def btnMenu2Clicked(self):
        self.close()


class ThirdWindow(QtGui.QMainWindow, platosalacarta.Ui_pcWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda4.clicked.connect(self.btnIzquierda4Clicked)
        self.btnPlatosalacarta0.clicked.connect(self.btnPlatosalacarta0Clicked)
        self.btnLomosaltado0.clicked.connect(self.btnLomosaltado0Clicked)
        self.btnPollosaltado0.clicked.connect(self.btnPollosaltado0Clicked)
        self.btnAlfredo0.clicked.connect(self.btnAlfredo0Clicked)
        self.btnTallarin0.clicked.connect(self.btnTallarin0Clicked)
        self.btnChifa0.clicked.connect(self.btnChifa0Clicked)
        self.btnCubana0.clicked.connect(self.btnCubana0Clicked)
        self.tenW = None
        self.elevenW = None
        self.twelveW = None
        self.thirteenW = None
        self.fourteenW = None
        self.fifteenW = None

    def btnIzquierda4Clicked(self):
        self.close()

    def btnPlatosalacarta0Clicked(self):
        self.close()

    def btnLomosaltado0Clicked(self):
        if self.tenW is None:
            self.tenW = TenWindow(self)
        self.tenW.show()

    def btnPollosaltado0Clicked(self):
        if self.elevenW is None:
            self.elevenW = ElevenWindow(self)
        self.elevenW.show()

    def btnAlfredo0Clicked(self):
        if self.twelveW is None:
            self.twelveW = TwelveWindow(self)
        self.twelveW.show()

    def btnTallarin0Clicked(self):
        if self.thirteenW is None:
            self.thirteenW = ThirteenWindow(self)
        self.thirteenW.show()

    def btnChifa0Clicked(self):
        if self.fourteenW is None:
            self.fourteenW = FourteenWindow(self)
        self.fourteenW.show()

    def btnCubana0Clicked(self):
        if self.fifteenW is None:
            self.fifteenW = FifteenWindow(self)
        self.fifteenW.show()


class FourWindow(QtGui.QMainWindow, panes.Ui_panesWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)










class SevenWindow(QtGui.QMainWindow, tercerapantalla.Ui_terceraWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        
class SixWindow(QtGui.QMainWindow, tercerapantalla1.Ui_tercera1Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        
class FiveWindow(QtGui.QMainWindow, tercerapantalla2.Ui_tercera2Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

class TenWindow(QtGui.QMainWindow, platosalacarta1.Ui_pc1Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

class ElevenWindow(QtGui.QMainWindow, platosalacarta2.Ui_pc2Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

class TwelveWindow(QtGui.QMainWindow, platosalacarta3.Ui_pc3Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

class ThirteenWindow(QtGui.QMainWindow, platosalacarta4.Ui_pc4Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

class FourteenWindow(QtGui.QMainWindow, platosalacarta5.Ui_pc5Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

class FifteenWindow(QtGui.QMainWindow, platosalacarta6.Ui_pc6Window):
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
