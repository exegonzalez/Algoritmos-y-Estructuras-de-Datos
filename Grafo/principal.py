import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from TDA_Grafos import TGrafo, insertarg, barridog,eliminarg, buscarcamino, buscarcaminos2, busqueda
from ejercicio_grafo import cargargrafo
from Tda_pila_con_nodo import tpila, barrido,pila_vacia, tpila, tamanioPila, desapilar,apilar
from PyQt5.QtWidgets import QPushButton, QLineEdit, QTextEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
from PyQt5.QtCore import QUrl

class MapaUrl():

    def __init__(self):
        self.centro = "center=-32.4818434,-58.2391088"#"concepcion del uruguay"
        self.zoom = "&zoom=6"
        self.size = "&size=1280x720"
        self.formato = "&formato=png"
        self.maptype = "&maptype=roadmap"
        self.marcadores = "" #"&markers=color:green|label:M|-32.4818434,-58.2391088|-32.4829361,-58.2398935"
        self.marcadores2 = "" #"&markers=color:purple|label:J|concepcion del uruguay"
        self.path = ""
        self.path2 = ""
        self.api_key = "&key=AIzaSyAJ2aEs0UpGAW-G4mleFU6nasD6U1RkfT0"

    def get_url(self):
            parametros = self.centro + self.zoom + self.size + self.formato + self.maptype + self.marcadores+self.marcadores2+self.path+self.path2+self.api_key
            return "https://maps.googleapis.com/maps/api/staticmap?" + parametros

    def tipomapa(self, num):
        """0 - roadmap, 1 - satellite, 2 - hybrid, and 3 -terrain"""
        tipo = ["roadmap", "satellite", "hybrid", "terrain"]
        self.maptype = "&maptype=" + tipo[num]

    def set_marcadores(self, lista): #lista2
        marcas = "|"
        marcas = marcas.join(lista)
        self.marcadores = "&markers=color:green|label:M|" + marcas
        #marcas2 = "|"
        #marcas2 = marcas2.join(lista2)
        #self.marcadores2 = "&markers=color:yellow|" + marcas2

    def set_camino(self, lista):# lista2):
        marcas = "|"
        marcas = marcas.join(lista)
        self.path = "&path=color:red|weight:2|"+marcas
        #marcas2 = "|"
        #marcas2 = marcas2.join(lista2)
        #self.path2 = "&path="+marcas2


class Principal(QMainWindow):    
    
    def __init__(self):
        super().__init__()
        loadUi("principal2.ui", self)
        self.setWindowTitle("BusquedaCaminos")
        self.grafo=TGrafo()
        self.consultar.clicked.connect(self.Ver_Caminos)
        self.insertarciudad.clicked.connect(self.insertar_ciudad)
        self.insertarviaje.clicked.connect(self.insertar_viaje)
        cargargrafo(self.grafo)     
        #print(self.grafo.tamanio)
        self.browser = QWebEngineView()
        self.browser.resize(500,500)
        self.vermapa.clicked.connect(self.cargar_mapa)
        self.recorridomapa.clicked.connect(self.vermaparecorrido)
        self.show()

    def Ver_Caminos(self): 
        self.recorridos.clear()
        self.combo.clear()
        valor1 = self.origennn.text()
        valor2 = self.destinooo.text()
        aux = busqueda(self.grafo,valor1)
        #print(aux.arcos.tamanio)
        if (aux!=None):
            resultado = buscarcaminos2(self.grafo, valor1, valor2)#resultado != []:
            self.resultado = resultado
            if resultado!=[]:
                cont = 0
                for solucion in resultado:
                    self.recorridos.append(" CAMINOS " + str(cont))
                    self.recorridos.append(" ")
                    self.combo.addItem(" CAMINOS " + str(cont))
                    barrido(solucion, self.recorridos)
                    self.recorridos.append(" ")
                    cont += 1
            else:
                self.recorridos.append(" NO HAY CAMINO")
        else:
            self.recorridos.append(" NO HAY CAMINO")
   
    def vermaparecorrido(self):
        if (self.combo.count()>0):    
            pila = self.resultado[self.combo.currentIndex()]
            paux = tpila()
            lista = []
            while(not pila_vacia(pila)):
                x=desapilar(pila)        
                lista.append(x[0])
                apilar(paux,x)        
            while(not pila_vacia(paux)):
                x=desapilar(paux)        
                apilar(pila,x)   
            m = MapaUrl()
            m.tipomapa(0)
            m.set_marcadores(lista)
            m.set_camino(lista)
            url = m.get_url()
            print(url)
            self.browser.load(QUrl(url))
            self.browser.show()
    """
    def mostrar_camino(resultado):
        for solucion in resultado:
            barrido(solucion)
            print()
    """
    
    def cargar_mapa(self):
        m = MapaUrl()
        m.tipomapa(0)
        lista=[]
        aux = self.grafo.cab
        while(aux!=None):
            lista.append(aux.info)
            aux  = aux.sig
        m.set_marcadores(lista)
        #m.set_camino(lista)
        url = m.get_url()
        print(url)
        self.browser.load(QUrl(url))
        self.browser.show()
        
    def insertar_ciudad(self):
        self.ciudad.clear()
        #cargargrafo(self.grafo)    
        ciud = self.insertarciud.text()
        if ciud!='':
            aux=busqueda(self.grafo,ciud)
            if (aux == None):
                insertarg(self.grafo,ciud,'V')
                self.ciudad.append(" Se ha agregado con exito ")
                print(self.grafo.tamanio)
            else:
                aux1 = aux.arcos.cab
                self.ciudad.append(" Arcos:")
                while(aux1!=None):
                    self.ciudad.append(aux1.info)
                    aux1 = aux1.sig
        else:
            self.ciudad.append(" Debe ingresar una ciudad ")
            
    def insertar_viaje(self):
        self.viajes.clear()
        #cargargrafo(self.grafo)  
        ori = self.origen.text()
        des = self.destino.text()
        ruta = self.opcioness.text()
        aux = busqueda(self.grafo,ori)
        aux1 = busqueda(self.grafo,des)
        if (ori!='') and ((des!='') and (ruta!='')):
            if (aux != None): 
                if (aux1 !=None):
                    insertarg(aux.arcos,des,'A',0,ruta)
                    self.viajes.append(" Se ha agregado con exito")
                else: 
                    self.viajes.append(" El destino no esta cargado")
            else:
                self.viajes.append(" El origen no esta cargado")

                #aux2 = aux.arcos.cab
                #while(aux2!=None):
                #    self.viajes.append('',aux2.info)
                #    aux2 = aux2.sig
        else: 
            self.viajes.append(" Debe ingresar todos los datos" )
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_())
