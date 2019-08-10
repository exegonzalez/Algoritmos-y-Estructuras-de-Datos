max=10
class TPila(object):
    def __init__(self):
        self.tope=-1
        self.dato=[]
        for I in range (0,max):
            self.dato.append(0)

#p=TPila()

'''
def CrearPila(p):
    p.tope=0
'''

def Apilar(p,x):
    p.tope = p.tope + 1
    p.dato[p.tope] = x
    
def Desapilar(p):
    x=p.dato[p.tope]
    p.tope=p.tope-1
    return x
    
def PilaLlena(p):
    return p.tope == max-1

def PilaVacia(p):
    return p.tope == -1

def tamanio(p):
    return p.tope + 1    

def barrido(p):
    paux = TPila()
    while(not PilaVacia(p)):
        x=Desapilar(p)        
        print(x[0])
        Apilar(paux,x)
        
    while(not PilaVacia(paux)):
        x=Desapilar(paux)        
        Apilar(p,x)