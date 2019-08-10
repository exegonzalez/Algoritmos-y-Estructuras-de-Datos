
def Quicksort(lista,inf,sup):
    if (inf<sup):
        I=inf
        J=sup
        pivot=lista[inf]
        while (I<J):
            while (lista[I]<=pivot) and (I<J):
                I+=1
            while (lista[J]>pivot):
                J-=1
            if (I<J):
                (lista[I],lista[J])=(lista[J],lista[I])
        (lista[inf],lista[J])=(lista[J],lista[inf])
        Quicksort(lista,inf,J-1)
        Quicksort(lista,J+1,sup)

def QuicksortI(A, inf, sup):
    pila = []
    pila.append((inf,sup))
    #Bucle principal para abrir y empujar elementos hasta que la pila esté vacía
    while pila:
        pos = pila.pop()
        sup, inf = pos[1], pos[0]
        piv = particion(A,inf,sup)
        #Si los elementos en el inf del pivote los empujan a la pila
        if piv-1 > inf:
            pila.append((inf,piv-1))
        #Si los elementos en el sup del pivote los empujan a la pila
        if piv+1 < sup:
            pila.append((piv+1,sup))

def particion(A, inf, sup):
    piv = A[inf]
    i = inf + 1
    j = sup
    while 1:
        while i <= j  and A[i] <= piv:
            i +=1
        while j >= i and A[j] >= piv:
            j -=1
        if j <= i:
            break
        A[i], A[j] = A[j], A[i]
    A[inf], A[j] = A[j], A[inf]
    return j

def bb(Pri,Ult,lista,Kx):
    pos = -1
    if (Pri<=Ult):
        M=(Pri+Ult)//2    
        if (lista[M]==Kx):
            pos = M
        else:
            if (lista[M]>Kx):                               
                pos = bb(Pri,M-1,lista,Kx)
            else:
                pos = bb(M+1,Ult,lista,Kx)
    return pos
"""
#n=10
#lista = [0] * n
listaAleatorios(n)
print("la lista random es:")
listarLista(n)
print(" ")
Quicksort(lista,0,len(lista)-1)
print("la lista random ordenada es:")
listarLista(n)
print(" ")
print("ingrese el numero que desea buscar en la lista")
bus=input()
pos=bb(0,len(lista),lista,int(bus))
print("el numero ",bus," se encuentra en la posicion ",pos+1) 
"""