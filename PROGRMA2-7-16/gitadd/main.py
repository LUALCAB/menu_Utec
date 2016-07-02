#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui  # Import the PyQt4 module we'll need
from PyQt4 import QtCore
import sys  # We need sys so that we can pass argv to QApplication

import primerapantalla #Esto se genera de esto: primerapantalla.ui
import segundapantalla #Esto se genera de esto: segundapantalla.ui
import tercerapantalla
import platosalacarta

class MainWindow(QtGui.QMainWindow, primerapantalla.Ui_PrimeraWindow):
    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btnMenu.clicked.connect(self.btnMenuClicked)
#        self.btnPlatosalacarta.clicked.connect(self.btnPlatosalacartaClicked)
        self.secondW = None
        self.thirdW = None

    def btnMenuClicked(self):
        if self.secondW is None:
            self.secondW = SecondWindow(self)
        self.secondW.show()
"""
    def btnPlatosalacartaClicked(self):
    	if self.thirdW is None:
    		self.thirdW = ThirdWindow(self)
    	self.thirdW.show()
"""
class SecondWindow(QtGui.QMainWindow, segundapantalla.Ui_segundaWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)


"""
class ThirdWindow(QtGui.QMainWindow, tercerapantalla.Ui_terceraWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
"""

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
