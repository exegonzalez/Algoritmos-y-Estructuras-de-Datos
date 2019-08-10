import sys
import random
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from Programa1 import Quicksort, QuicksortI, bb
from PyQt5.QtWidgets import QPushButton, QLineEdit, QTextEdit, QFontComboBox

class Principal(QMainWindow):    
    
    def __init__(self):
        super().__init__()
        loadUi("Ventana.ui", self)
        self.lista = [0] * 15
        self.crear.clicked.connect(self.generarlista)
        self.OrdenarR.clicked.connect(self.ordenarrecursivo)
        self.OrdenarI.clicked.connect(self.ordenariterativo)
        self.buscar.clicked.connect(self.buscarr)
        self.show()
    
    def generarlista(self):
        c=15
        n=10
        x=''
        for i in range(c):
            self.lista[i] = random.randrange(0,n)
        for i in range (c):
            x += str(self.lista[i])+' '
        self.listasinordenar.append("[ "+x+"]")
        return self.lista
    
    def ordenarrecursivo(self):
        c=15
        x=''
        Quicksort(self.lista,0,len(self.lista)-1)
        for i in range (c):
            x += str(self.lista[i])+' '
        self.listarecursiva.append("[ "+x+"]")
    
    def ordenariterativo(self):
        c=15
        x=''
        QuicksortI(self.lista,0,len(self.lista)-1)
        for i in range (c):
            x += str(self.lista[i])+' '
        self.listaiterativa.append("[ "+x+"]")
    
    def buscarr(self):
        pos=None
        bus = self.buscado.text()
        pos = bb(0,len(self.lista)-1,self.lista,int(bus))
        if (pos!=None):
            self.resultadobusqueda.append("el numero "+bus+" se encuentra en la posicion "+str(pos+1))
        else:
            self.resultadobusqueda.append("el numero "+bus+" no se encuentra en la lista")
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_())