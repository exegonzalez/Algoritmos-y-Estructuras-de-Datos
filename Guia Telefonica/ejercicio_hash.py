
from TDA_Listas import TLista, insertar, busqueda,eliminar

class tda_hash():
    
    def __init__(self):
        self.uno = [TLista()]
        self.dos = []
        self.tres = []
        self.dosb  = []
        self.tresb = []
        for i in range(20, 99):
            self.dos.append(TLista())

        for i in range(36, 88):
            self.tres.append(TLista())
        
        for i in range(202, 983):
            self.dosb.append(TLista())
        
        for i in range(327, 894):
            self.tresb.append(TLista())    

        self.guia = [self.uno, self.dos, self.tres, self.dosb, self.tresb]

    def f_hash(self, num):
        cont= num.telefono.find('-') -1
        aux = None
        if (cont<3):
            indice = int(num.telefono[0]) -1
            lista = self.guia[indice]
            if(num.telefono[0]=='1'):
                aux = lista[0]
            else:
                valor = 20 if num.telefono[0]=='2' else 36
                indice  = int(num.telefono[1:3]) - valor
                aux = lista[indice]
        else:
            indice = int(num.telefono[0]) +1
            lista = self.guia[indice]
            valor = 202 if num.telefono[0]=='2' else 327
            indice  = int(num.telefono[1:4]) - valor
            aux = lista[indice]
        return aux
    
class Telefono():#se crea la clase telefono
    def __init__(self, apellido=None, nombre=None, telefono=None):
        self.apellido = apellido
        self.nombre= nombre
        self.telefono= telefono

def cargar_tel ():
        num=Telefono()    
        num.apellido= input("Ingrese el apellido de la persona: ")
        num.nombre= input("Ingrese el nombre de la persona: ")
        num.telefono= input("Ingrese el numero telefonico de la persona (nnn-nnnnnn): ")
        return num

h = tda_hash()

def Menu(tabla_hash):
    control = True
    while control:
        print('')
        print("1- Insertar un telefono en la guia")
        print("2- Eliminar un telefono en la guia")
        print("3- Buscar un telefono en la guia")
        print("4- salir")
        opc=input('Opcion: ')
        print('')
        if (opc=='1'):
            num = cargar_tel()
            puntero = tabla_hash.f_hash(num)
            aux = busqueda(puntero,num.telefono,'telefono')
            if aux is None:
                insertar(puntero, num, 'apellido')
                print('')
                print('se inserto con exito el telefono')
            else:
                print('')
                print('ya existe')
        if (opc=='2'):
            aux=Telefono()
            aux.telefono= input("Ingrese el numero telefonico de la persona (nnn-nnnnnn) que desea eliminar: ")
            puntero = tabla_hash.f_hash(aux)
            x = busqueda(puntero,aux.telefono,'telefono')
            if x != None:
                eliminar(puntero,aux.telefono, 'telefono')
                print('')
                print('se elimino con exito el telefono')
            else:
                print('')
                print('No existe el telefono')
        if (opc=='3'):
            aux=Telefono()
            print('1- Buscar por telefono')
            print('2- Buscar por Apellido y Nombre')
            print('')
            op=input('Opcion: ')
            if op=='1':
                aux.telefono= input("Ingrese el numero telefonico de la persona (nnn-nnnnnn) que desea buscar: ")
                puntero = tabla_hash.f_hash(aux)
                x = busqueda(puntero,aux.telefono,'telefono')
                if x != None:
                    print('El apellido es: ',x.info.apellido)
                    print('El nombre es: ',x.info.nombre)
                    print('El telefono es: ',x.info.telefono)
                else:
                     print('')
                     print('No existe el telefono')
            if op=='2':
                aux.apellido= input("Ingrese el apellido de la persona: ")
                aux.nombre= input("Ingrese el nombre de la persona: ")
                for subguia in h.guia:
                    for ltel in subguia:
                        x = busqueda(ltel, aux.apellido, 'apellido')
                        if (x != None):
                            while (x != None and x.info.apellido==aux.apellido and x.info.nombre==aux.nombre):
                                print('El apellido es: ',x.info.apellido)
                                print('El nombre es: ',x.info.nombre)
                                print('El telefono es: ',x.info.telefono)
                                x = x.sig      
        if (opc=='4'):
            control = False

Menu(h)
print(' Fin') 
