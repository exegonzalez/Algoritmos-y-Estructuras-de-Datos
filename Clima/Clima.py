from archivos import abrir, cerrar, agregar, leer
from TDA_Arboles import insertar

class clima():
    def __init__(self, id=None, date=None, time=None, temp=None, presion=None, viento=None, humedad=None, estado=None, zona=None):
        self.id = id
        self.date= date
        self.time= time
        self.temp= temp
        self.presion= presion
        self.viento= viento
        self.humedad= humedad
        self.estado= estado
        self.zona= zona

def creararchivoclima():
    f = open('datos_clima.csv')
    a = abrir('clima')
    print(f.readline())
    linea = f.readline()
    cont = -1
    while(linea):
        cont += 1
        lista = linea.split(',')
        reg = clima()
        reg.id = (lista[0])
        reg.date = (lista[1])
        reg.time = (lista[2])
        reg.temp = (lista[3])
        reg.presion = (lista[4])
        reg.viento = (lista[5])
        reg.humedad = (lista[6])
        reg.estado = (lista[7])
        reg.zona = (lista[8])
        for campo in lista:    
            print(campo)
        agregar(a, reg)
        linea = f.readline()
    print(cont)
    f.close()
    cerrar(a)

"""
azona, acodigo, afecha = None, None, None
a = abrir('clima')

while(pos<len(a)):
    reg = leer(a, pos)
    azona = insertar(azona, reg.zona, pos)
    acodigo = insertar(acodigo, reg.codigo, pos)
    azona = insertar(afecha, reg.feca, pos)
    pos += 1
"""