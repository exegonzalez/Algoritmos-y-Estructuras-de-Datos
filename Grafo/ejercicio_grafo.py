from TDA_Grafos import TGrafo, insertarg, barridog,eliminarg, buscarcamino, buscarcaminos2, busqueda
from Tda_pila_con_nodo import barrido
#from TDA_Listas import TLista, insertar, eliminar

grafo=TGrafo()

"""
class ciudad():#se crea la clase ciudad (vertices)
    def __init__(self, nombre=None, pais=None, X=None, Y=None):
        self.nombre = nombre
        self.pais= pais
     
def cargar_ciudad():
        c=ciudad()    
        print("Ingrese el nombre de la ciudad")
        c.nombre= input()
        print("Ingrese el pais al que pertenece la ciudad")
        c.pais= input()
        print("Ingrese la coordenada en X de la ciudad")
        c.X= input()
        print("Ingrese la coordenada en Y de la ciudad")
        c.Y= input()
        return ciudad
"""
###insertamos ciudades en el grafo
def cargargrafo(grafo):
    insertarg(grafo,'uruguay','V')
    insertarg(grafo,'colon','V')
    insertarg(grafo,'concordia','V')
    insertarg(grafo,'gualeguaychu','V')
    insertarg(grafo,'tala','V')
    insertarg(grafo,'federacion','V')
    insertarg(grafo,'villaguay','V')

    pos = busqueda(grafo,'uruguay')
    insertarg(pos.arcos,'colon','A',0,'vuelo')
    insertarg(pos.arcos,'colon','A',0,'tierra')
    insertarg(pos.arcos,'gualeguaychu','A',0,'vuelo')
    insertarg(pos.arcos,'tala','A',0,'agua')
    
    pos = busqueda(grafo,'colon')
    insertarg(pos.arcos,'concordia','A',0,'vuelo')
    insertarg(pos.arcos,'villaguay','A',0,'vuelo')
    insertarg(pos.arcos,'tala','A',0,'tierra')
    
    pos = busqueda(grafo,'concordia')
    insertarg(pos.arcos,'villaguay','A',0,'vuelo')
    insertarg(pos.arcos,'federacion','A',0,'agua')
    
    pos = busqueda(grafo,'tala')
    insertarg(pos.arcos,'villaguay','A',0,'agua')
    insertarg(pos.arcos,'gualeguaychu','A',0,'vuelo')
    
    pos = busqueda(grafo,'federacion')
    insertarg(pos.arcos,'tala','A',0,'tierra')
        
    pos = busqueda(grafo,'villaguay')
    insertarg(pos.arcos,'federacion','A',0,'agua')
    
    pos = busqueda(grafo,'gualeguaychu')
    insertarg(pos.arcos,'federacion','A',0,'agua')
    
#barridog(grafo)
#cargarelfuckinggrafo(grafo)     
#print('ingrese ciudad de origen')   
#origen = input()
#print('ingrese ciudad destino')
#destino= input()               
#resultado = buscarcaminos2(grafo, origen, destino)
#for solucion in resultado:
#   barrido(solucion)
#    print()

    