def criterio(dato, clave):
    if(clave==None):
        return dato
    elif(clave=='telefono'):
        return dato.telefono
    elif(clave=='apellido'):
        return dato.apellido
    elif(clave=='nombre'):
        return dato.nombre

class NodoLista():
    def __init__(self):
        self.info = None
        self.sig= None
        
class TLista():
    def __init__(self):
        self.tamanio=0
        self.cab= None

def insertar(lista,x, crit=None):
    lista.tamanio=lista.tamanio+1
    aux = NodoLista()
    aux.info = x
    if (lista.cab==None) or (criterio(x, crit) < criterio(lista.cab.info, crit)):
        aux.sig=lista.cab
        lista.cab=aux
    else:
        ant = lista.cab
        act = lista.cab.sig
        while (act != None) and (criterio(act.info,crit) < criterio(x, crit)):
            act=act.sig
            ant=ant.sig
        aux.sig=act
        ant.sig=aux
            
def eliminar(lista,ku, crit=None):
    x = None
    if (criterio(lista.cab.info,crit)==ku):
        x = lista.cab.info
        lista.cab = lista.cab.sig
        lista.tamanio=lista.tamanio-1
    else:
        ant=lista.cab
        act=lista.cab.sig
        while((act!=None)and(criterio(act.info,crit)!=ku)):
            ant=ant.sig
            act=act.sig
        if(act!=None):
            x=act.info
            ant.sig=act.sig
            lista.tamanio=lista.tamanio-1
        return x

def busqueda(lista,ku, clave):
    pos=lista.cab
    while((pos!=None) and (criterio(pos.info,clave)!=ku)):
        pos=pos.sig
    return pos    
            
def tamanio(lista):
    return lista.tamanio         

def listavacia(lista):
    return lista.tamanio == 0    

def listar(lista):
    for i in range (0,lista.tamanio):
        print(lista.cab.i.info)