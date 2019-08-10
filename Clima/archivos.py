import shelve

def abrir(ruta): ## ruta: c:/datos....
    return shelve.open(ruta)

def cerrar(archivo):
    archivo.close()

def agregar(archivo,dato):
    try:
        archivo[str(len(archivo))]=dato
        return True
    except:
        return None

def leer(archivo,pos):
    try:
        return archivo[str(pos)]
    except:
        return None
    
def modificar(archivo,dato, pos):
    try:
        archivo[str(pos)]=dato
        return True
    except:
        return None
    

