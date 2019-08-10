import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtWidgets import QPushButton, QLineEdit, QTextEdit
from Tda_pila_con_nodo import tpila, apilar, desapilar, pila_vacia, barrido, tamanioPila
from TDA_Listas import TLista, insertar, eliminar, listavacia
import copy

def criterio(dato, clave):
    if(clave==None):
        return dato
    elif(clave=='origen'):
        return dato.origen
    elif(clave=='destino'):
        return dato.destino
    
class NodoVer():
    def __init__(self):
        self.info = None
        self.pos = None
        self.sig= None
        self.arcos= TGrafo()
        
class NodoAri():
    def __init__(self):
        self.info = None
        self.tipo = []
        self.pos = None
        self.sig= None

class TGrafo():
    def __init__(self):
        self.cab= None
        self.tamanio= 0
    
def insertarg(grafo, x, tipo, pos=0, tipo_viaje=None, crit=None):
    grafo.tamanio = grafo.tamanio+1 
    if (tipo=='A'):
        pos1 = busqueda2(grafo.cab, x)
        if(pos1 is None):
            nodo = NodoAri()
            nodo.pos = pos
            nodo.info = x
            nodo.tipo.append(tipo_viaje)
        else:
            pos1.tipo.append(tipo_viaje)
            return
    elif (tipo=='V'):
        nodo= NodoVer()
        nodo.info = x
        nodo.pos = pos
    
    if (grafo.cab==None) or (criterio(x, crit) < criterio(grafo.cab.info, crit)):
        nodo.sig=grafo.cab
        grafo.cab=nodo
    else:
        ant = grafo.cab
        act = grafo.cab.sig
        while (act != None) and (criterio(act.info,crit) < criterio(x, crit)):
            act=act.sig
            ant=ant.sig
        nodo.sig=act
        ant.sig=nodo

def busqueda(grafo, ku, clave=None):
    pos=grafo.cab
    while((pos!=None) and (criterio(pos.info,clave)!=ku)):
        pos=pos.sig
    return pos    

def busqueda2(arcos, ku, clave=None):
    pos=arcos
    while((pos!=None) and (criterio(pos.info,clave)!=ku)):
        pos=pos.sig
    return pos

def barridog(grafo):
    aux = grafo.cab
    while(aux!=None):
        print("vertice")
        print(aux.info)
        aux1 = aux.arcos.cab
        print("arcos")
        while(aux1!=None):
            print(aux1.info)
            aux1 = aux1.sig
        aux  = aux.sig
        print('')
        
def eliminarg(grafo,ku, crit=None):
    x = None
    if (criterio(grafo.cab.info,crit)==ku):
        x = grafo.cab.info
        grafo.cab = grafo.cab.sig
        grafo.tamanio=grafo.tamanio-1
    else:
        ant=grafo.cab
        act=grafo.cab.sig
        while((act!=None)and(criterio(act.info,crit)!=ku)):
            ant=ant.sig
            act=act.sig
        if(act!=None):
            x=act.info
            ant.sig=act.sig
            grafo.tamanio=grafo.tamanio-1
        return x
"""
def eliminartodo(grafo, ku, crit=None):
   x = None
"""   

def buscarcamino(grafo, origen, destino, crit=None):
    pila=tpila()
    lista=TLista()
    pos = busqueda(grafo, origen)
    pos1 = busqueda(grafo, destino)
    apilar(pila,pos)
    control=False
    if (pos!=None) and (pos1!=None):
        while not pila_vacia(pila) and control==False:
            dato=desapilar(pila)
            posarc= busqueda(dato.arcos, destino)
            if posarc!=None:
                apilar(pila,dato)
                apilar(pila,pos1)
                control=True
            else:
                if dato.arcos!=None:
                    apilar(pila,dato)
                    insertar(lista,dato.info)
                    aux=dato.arcos.cab
                    while aux!=None and busqueda(lista,aux.info)!=None:
                        aux=aux.sig
                    if aux!=None:
                        paux=busqueda(grafo,aux.info)
                        apilar(pila,paux)
                    else:
                        desapilar(pila)
    if not pila_vacia(pila):
        while(not pila_vacia(pila)):
            x=desapilar(pila)        
            print('el camino es: ',x.info)
    else:
        print('No hay camino')

def buscarcaminos2(grafo, origen, destino, crit=None):
    soluciones = []
    pila=tpila()
    lista=TLista()
    pos = busqueda(grafo, origen)
    pos1 = busqueda(grafo, destino)
    if (pos!=None) and (pos1!=None):
        
        dato = [pos.info, pos.arcos.cab, None]
        apilar(pila,dato)
        while not pila_vacia(pila):
            dato=desapilar(pila)
            posarc= busqueda2(dato[1], destino)
            #posarc= busqueda(grafo, destino)
            if posarc!=None: # busqueda directa
                
                apilar(pila,dato)
                dato[1] = dato[1].sig
                dato1 = [pos1.info, pos1.arcos.cab, posarc]
                #dato1 = [pos1.info, posarc]
                apilar(pila,dato1)
                aux = copy.copy(pila)
                if(tamanioPila(aux)==2) and (len(soluciones)==1):
                    print("no va")
                else:
                    soluciones.append(aux)
                desapilar(pila)
                #barrido(soluciones[len(soluciones)-1])
            else:
                
                if dato[1]!=None:
                    #print("aca")
                    apilar(pila,dato)
                    insertar(lista,dato[0])
                    aux=dato[1]
                    while aux!=None and busqueda(lista,aux.info)!=None:
                        aux=aux.sig
                    
                    if aux!=None:
                        paux=busqueda(grafo,aux.info)
                        #datoaux = [paux.info, paux.arcos.cab]
                        datoaux = [paux.info, paux.arcos.cab, aux]
                        apilar(pila,datoaux)
                        dato[1] = aux.sig
                    else:
                        desapilar(pila)
                        print(tamanioPila(pila))#no muestra el tamañp de la pila, no esta entrando aca
                else:
                    if(not listavacia(lista)):
                        eliminar(lista, dato[0])

    return soluciones
    """
    if not PilaVacia(pila):
        while(not PilaVacia(pila)):
            x=Desapilar(pila)        
            print('el camino es: ',x.info)
    else:
        print('No hay camino')
"""
#buscar camino
#buscar origen y destino
#busqueda destino
#apilar (origen actual)

"""
g = TGrafo()
insertarg(g,'A','V')
insertarg(g,'C','V')
insertarg(g,'B','V')
insertarg(g,'D','V')
insertarg(g,'E','V')
insertarg(g,'F','V')

pos = busqueda(g,'A')
insertarg(pos.arcos,'B','A')
insertarg(pos.arcos,'C','A')
pos = busqueda(g,'B')
insertarg(pos.arcos,'C','A')
pos = busqueda(g,'C')
insertarg(pos.arcos,'D','A')
pos = busqueda(g,'B')
insertarg(pos.arcos,'E','A')
pos = busqueda(g,'E')
insertarg(pos.arcos,'D','A')
pos = busqueda(g,'E')
insertarg(pos.arcos,'F','A')
pos = busqueda(g,'D')
insertarg(pos.arcos,'A','A')

barridog(g)
resultado = buscarcaminos2(g,'A','D')

for solucion in resultado:
    barrido(solucion)
    print()
"""
    
"""
pos = busqueda(g,'A')
eliminar(pos.arcos,'B')
pos = busqueda(g,'C')
eliminar(g,'C')
"""
##barrido(g)
 