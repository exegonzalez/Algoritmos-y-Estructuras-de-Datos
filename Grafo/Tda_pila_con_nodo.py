import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtWidgets import QPushButton, QLineEdit, QTextEdit
#from principal import set_camino

class nodopila():
    def __init__(self):
        self.info = None
        self.sig = None

class tpila():
    def __init__(self):
        self.tope = None
        self.tamanio = 0

def pila_llena(pila):
    return False

def pila_vacia(pila):
    return(pila.tope == None)
 
def apilar(pila,x):
    aux = nodopila()
    aux.info = x
    aux.sig = pila.tope
    pila.tope = aux
    pila.tamanio += 1
    
def desapilar(pila):
   x = pila.tope.info
   pila.tope = pila.tope.sig
   pila.tamanio -= 1
   return x

def tamanioPila(pila):
    return pila.tamanio

def barrido(p, textarea):
    paux = tpila()
    while(not pila_vacia(p)):
        x=desapilar(p)        
        textarea.append(x[0])
#        mapa.set_camino(x[0])
        if(x[2] != None):
            valor = ""
            for tipo in x[2].tipo:
                valor += tipo+" | "
            textarea.append('| ' + valor)
        apilar(paux,x)        
    while(not pila_vacia(paux)):
        x=desapilar(paux)        
        apilar(p,x)   



    