from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QTableWidgetItem
from archivos import abrir, cerrar, agregar, leer, modificar
from TDA_Arboles import insertar, inorden, inordena, eliminar,busqueda, buscar
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import sys

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ventanaclima.ui", self)
        self.show()
        pixmap = QPixmap('fondo.png')
        self.fondo.setPixmap(pixmap)
        self.aux1=None
        #self.creararchivoclima()
        self.aux1=self.cargararboles()
        self.botoninsertar.clicked.connect(self.insertardato)
        self.botoneliminar.clicked.connect(self.eliminardato)
        self.botonmodificar.clicked.connect(self.modificardato)
        self.botonid.clicked.connect(self.ordenar_id)
        self.botonfecha.clicked.connect(self.ordenar_fecha)
        self.botonzona.clicked.connect(self.ordenar_zona)
        self.buscador.textChanged.connect(self.buscar_id)
        self.tabla.cellClicked.connect(self.valor_tabla)
        self.limpiar.clicked.connect(self.limpiartodo)
        self.mostrarlista()
    
    def limpiartodo(self):
        self.altaid.clear()
        self.altafecha.clear()
        self.altahora.clear()
        self.altatemperatura.clear()
        self.altapresion.clear()
        self.altaviento.clear()
        self.altahumedad.clear()
        self.altaestado.clear()
        self.altazona.clear()
        
    def valor_tabla(self):
        row = self.tabla.currentRow()
        self.altaid.setText(self.tabla.item(row, 0).text())
        self.altafecha.setText(self.tabla.item(row, 1).text())
        self.altahora.setText(self.tabla.item(row, 2).text())
        self.altatemperatura.setText(self.tabla.item(row, 3).text())
        self.altapresion.setText(self.tabla.item(row, 4).text())
        self.altaviento.setText(self.tabla.item(row, 5).text())
        self.altahumedad.setText(self.tabla.item(row, 6).text())
        self.altaestado.setText(self.tabla.item(row, 7).text())    
        self.altazona.setText(self.tabla.item(row, 8).text())
            
    def ordenar_id(self): 
        self.tabla.setRowCount(0)
        arbol = self.aux1[1]
        a = abrir('clima')
        inordena(arbol, self.tabla, a)
        cerrar(a)
     
    def ordenar_fecha(self):
        self.tabla.setRowCount(0)
        arbol = self.aux1[2]
        a = abrir('clima')
        inordena(arbol, self.tabla, a)
        cerrar(a)
        
    def ordenar_zona(self):  
        self.tabla.setRowCount(0)
        arbol = self.aux1[0]
        a = abrir('clima')
        inordena(arbol, self.tabla, a)
        cerrar(a)
    
    def buscar_id (self):
        print("aca")
        arbol = self.aux1[1]
        busc = self.buscador.text()
        a = abrir('clima')
        self.tabla.setRowCount(0)
        busqueda(arbol,busc, self.tabla, a)
        cerrar(a)
    
    def creararchivoclima(self):
        reg = clima()
        f = open('datos_clima.csv')
        a = abrir('clima')
        #print(f.readline())
        linea = f.readline()
        cont = -1
        while(linea):
            cont += 1
            lista = linea.split(',')
            #print(lista)
            reg.id = (lista[0])
            reg.date = (lista[1])
            reg.time = (lista[2])
            reg.temp = (lista[3])
            reg.presion = (lista[4])
            reg.viento = (lista[5])
            reg.humedad = (lista[6])
            reg.estado = (lista[7])
            reg.zona = (lista[8])
            reg.activo = True
            agregar(a, reg)
            linea = f.readline()
        print("listo")
        f.close()
        cerrar(a)
    
    def cargararboles(self):#no funca
        self.azona, self.acodigo, self.afecha = None, None, None
        a = abrir('clima')
        pos = 0
        #reg = clima()
        while(pos<len(a)):
            self.reg = leer(a, pos)
            self.azona = insertar(self.azona, self.reg.zona, pos)
            self.acodigo = insertar(self.acodigo, self.reg.id, pos)
            self.afecha = insertar(self.afecha, self.reg.date, pos)
            pos += 1
        cerrar(a)
        return [self.azona,self.acodigo,self.afecha]
    
    def insertardato(self): 
        arbolid = self.aux1[1]
        arbolfecha = self.aux1[2]
        arbolzona = self.aux1[0]
        lid = self.altaid.text()
        lfecha = self.altafecha.text()
        lhora = self.altahora.text()
        ltemp = self.altatemperatura.text()
        lpresion = self.altapresion.text()
        lviento = self.altaviento.text()
        lhumedad = self.altahumedad.text()
        lestado = self.altaestado.text()
        lzona = self.altazona.text()
        a = abrir('clima')
        reg = clima()
        pos = 0
        control = False
        while(pos<len(a)): 
            reg = leer(a, pos)  
            if (reg.id == lid):
                if (reg.activo != True):
                    reg.activo = True
                    modificar(a, reg, pos)
                    arbolzona = insertar(arbolzona, lzona, pos)
                    arbolid = insertar(arbolid, lid, pos)
                    arbolfecha = insertar(arbolfecha, lfecha, pos)
                    control = True
                else:
                    control = True #es para ver si existe y esta dado de alta
            pos=pos+1        
        if (control != True):
            reg.id = (lid)
            arbolid = insertar(arbolid, lid, pos)
            reg.date = (lfecha)
            arbolfecha = insertar(arbolfecha, lfecha, pos)
            reg.time = (lhora)
            reg.temp = (ltemp)
            reg.presion = (lpresion)
            reg.viento = (lviento)
            reg.humedad = (lhumedad)
            reg.estado = (lestado)
            reg.zona = (lzona)
            arbolzona = insertar(arbolzona, lzona, pos)
            reg.activo = True
            agregar(a, reg)
        cerrar(a)
        self.mostrarlista()
    
    def eliminardato(self):
        arbolid = self.aux1[1]
        arbolfecha = self.aux1[2]
        arbolzona = self.aux1[0]
        lid = self.altaid.text()
        a = abrir('clima')
        #reg = clima()
        pos = 0
        control = True
        while(pos<len(a) and control): 
            reg = leer(a, pos)
            if (reg.id == lid):
                if (reg.activo == True):
                    reg.activo = False
                    modificar(a, reg, pos)
                    arbolzona = eliminar(arbolzona, reg.zona, pos)
                    arbolid = eliminar(arbolid, reg.id, pos)
                    arbolfecha = eliminar(arbolfecha, reg.date, pos)
                    control = False
            pos=pos+1
        cerrar(a)
        self.mostrarlista()          

    def modificardato(self):#ver si funciona
        arbolfecha = self.aux1[2]
        arbolzona = self.aux1[0]
        arbolid = self.aux1[1]
        lid = self.altaid.text()
        lfecha = self.altafecha.text()
        lhora = self.altahora.text()
        ltemp = self.altatemperatura.text()
        lpresion = self.altapresion.text()
        lviento = self.altaviento.text()
        lhumedad = self.altahumedad.text()
        lestado = self.altaestado.text()
        lzona = self.altazona.text() 
        a = abrir('clima')
        #reg = clima()
        #pos = 0
        #control = True
        #while(pos<len(a) and control): 
        if(lid!=''):
            pos = buscar(arbolid, lid)
            if(pos!=None):
                reg = leer(a, pos)
                if (reg.activo == True):
                    if (lfecha != ''):
                        arbolfecha = eliminar(arbolfecha, reg.date, pos)
                        reg.date = lfecha
                        arbolfecha = insertar(arbolfecha[0], lfecha, pos) #esta fallando en esta insercion
                    if (lhora != ''):
                        reg.time = (lhora)
                    if (ltemp != '') :
                        reg.temp = (ltemp)
                    if (lpresion != ''):
                        reg.presion = (lpresion)
                    if (lviento != ''):
                        reg.viento = (lviento)
                    if (lhumedad != ''):
                        reg.humedad = (lhumedad)
                    if (lestado != ''):
                        reg.estado = (lestado)
                    if (lzona != ''):
                        arbolzona = eliminar(arbolzona, reg.zona, pos)
                        reg.zona = lzona
                        arbolzona = insertar(arbolzona[0], lzona, pos)
                    modificar(a, reg, pos) #ver como modificar el arbol
        cerrar(a)
        self.mostrarlista()

    def mostrarlista(self):
        self.tabla.setRowCount(0)
        arbol = self.aux1[1]
        a = abrir('clima')
        inordena(arbol, self.tabla, a)
        cerrar(a)

class clima():
    def __init__(self, id=None, date=None, time=None, temp=None, presion=None, viento=None, humedad=None, estado=None, zona=None, activo=None):
        self.id = id
        self.date= date
        self.time= time
        self.temp= temp
        self.presion= presion
        self.viento= viento
        self.humedad= humedad
        self.estado= estado
        self.zona= zona
        self.activo = activo
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_()) 