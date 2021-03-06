# Imports
import Util
import time
import sys

#Se crean las clases Torre y Bloque para que el manejo de sus atributos sea más sencillo
#region Classes
# -----------------------------------------------------------------------------------------------
class Bloque():
    def __init__(self):
        self.largo:int  = 0
        self.ancho:int  = 0
        self.altura:int = 0
    def getBase(self):
        return self.largo * self.ancho
# -----------------------------------------------------------------------------------------------
class Torre():
    def __init__(self):
        self.bloques:list = []
    
    # Calcual la altura de la torre
    def getAltura(self):
        altura = 0
        for bloque in self.bloques:
            altura += bloque.altura
        return altura
    
    # Verifica si la torre es valida, es decir que lel bloque de abajo mayor al de arriba
    def esValida(self):
        if len(self.bloques) == 1: return True
        for i in range(len(self.bloques)-1):
            bloqueActual:Bloque    = self.bloques[i]
            bloqueSiguiente:Bloque = self.bloques[i+1]
            if (bloqueActual.largo <= bloqueSiguiente.largo) or (bloqueActual.ancho <= bloqueSiguiente.ancho):
                return False
        return True
# -----------------------------------------------------------------------------------------------
#endregion Classes

#region Fuerza Bruta 
# -----------------------------------------------------------------------------------------------
def bloquesFuerzaBruta(datos:list):
    start = time.time()
    bloques = []
    # se realiza la permutación de los bloques
    for bloque in datos:
        bloques.append(Util.permutaciones(bloque, len(bloque)))
    
    # se crean los objetos tipo bloque con sus atributos
    permutacionesBloques = []
    for block in bloques:
        cont = 0
        for permutacion in block:
            if permutacion[0] <= permutacion[1] and cont < 3:
                bloque = Bloque()
                bloque.largo = permutacion[0]
                bloque.ancho = permutacion[1]      
                bloque.altura = permutacion[2]
                permutacionesBloques.append(bloque)
                cont += 1

    permutacionesBloques = eliminarBloquesRepetidos(permutacionesBloques[0],permutacionesBloques)
    print("############ BLOQUES ############")
    for bloque in permutacionesBloques: 
        print("-----------------------") 
        print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')

    # se realiza la combinación de los bloques entre ellos para crear las torres
    combinacionBloques = Util.get_Lista_Combinaciones(permutacionesBloques) 
    
    #print("############ COMBINACIONES ############")
    #print(len(combinacionBloques))
    #for combinacion in combinacionBloques: 
    #    print("*******************************************************") 
    #    for bloque in combinacion: 
    #        #print("-----------------------") 
    #        #for bloque in permutacionbloque: 
    #        print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')

    # se realiza las permutaciones de las combinaciones de los bloques para crear torres 
    # de todas las combinaciones posibles
    CombinacionesPermutadas = []
    for combinacion in combinacionBloques: 
        resultado = []
        permutarCombinacion(combinacion,[],resultado)
        CombinacionesPermutadas+=resultado
        #CombinacionesPermutadas+=Util.permutaciones(combinacion, len(combinacion))
    
    combinacionBloques = CombinacionesPermutadas
     
    print("############ COMBINACIONES PERMUTADAS ############")
    print(len(combinacionBloques))
    #return
    #for combinacion in combinacionBloques: 
    #    print("*******************************************************") 
    #    for bloque in combinacion: 
    #        #print("-----------------------") 
    #        #for bloque in permutacionbloque: 
    #        print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')
    torres_Total = combinacionBloques
    # Combinaciones Validas
    #torres_Total = []#get_Torres(permutacionesBloques,1)
    #for combinacion in combinacionBloques:
    #    temporal=get_Torres(combinacion,1)
    #    #print(temporal)
    #    torres_Total.append( temporal)

    #cont = 0
    #for torre in torres_Total:      
    #    for combinacion in torre:
    #        print("*********************TORRE**********************************")
    #        for bloque in combinacion: 
    #            #print("-------------------------")
    #           #print(bloque)
    #            cont+=1
    #            print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')           
    #print(cont)

    # se verifica que las torres creadas sean validas, y si son validad se guardan
    torreValidas = []
    for combinacion in torres_Total:
        torre = Torre()
        torre.bloques = combinacion
        if torre.esValida() == True:
            torreValidas.append(torre)

    #print("############ TORRES VALIDAS ############")
    #for torre in torreValidas:
    #    print("------------------------------")
    #    for bloque in torre.bloques:
    #        print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')           

    #Se calcula la o las torres mas altas para el resultado 
    torreMasAltas=[]
    for torre in torreValidas:
        if torreMasAltas == []:
            torreMasAltas.append(torre)
        else:
            if torre.getAltura() > torreMasAltas[-1].getAltura():
                torreMasAltas=[]
                torreMasAltas.append(torre)
            elif torre.getAltura() == torreMasAltas[-1].getAltura():
                torreMasAltas.append(torre)

    print("############ TORRES MAS ALTAS ############")
    #for torre in torreMasAltas:
    #    print("------------------------------")
    #    print(torre.getAltura())
    #    for bloque in torre.bloques:
    #        print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura} ')  
    
    end = time.time()
    
    #Se imprimen los resultados requeridos 
    for torre in torreMasAltas:
        print("------------------------------")
        print(f'Altura: {torre.getAltura()}')
        print(", ".join([f'({bloque.largo}, {bloque.ancho}, {bloque.altura})' for bloque in torre.bloques]))
    print(f'\n Tiempo de ejecución: {end-start} segundos')

# Se eliminan los bloques repetidos que se pudieron crear en las combinaciones
def eliminarBloquesRepetidos(bloque,permutacionesBloques):
    if permutacionesBloques.index(bloque) == len(permutacionesBloques)-1:
        return permutacionesBloques
    else:
        listaEliminarBloques = getListaEliminarBloques(permutacionesBloques,bloque)
        #print([permutacionesBloques.index(bloqu) for bloqu in listaEliminarBloques])
        for bloqueEliminar in listaEliminarBloques:
            permutacionesBloques.remove(bloqueEliminar)
        siguienteBloque = permutacionesBloques[permutacionesBloques.index(bloque)+1]
        return eliminarBloquesRepetidos(siguienteBloque,permutacionesBloques)

# Retorna si un bloque es repetido o no
def getListaEliminarBloques(bloques,bloque):
    cont = 0
    listaEliminar = []
    for block in bloques:
        if bloque.largo == block.largo and bloque.ancho == block.ancho and bloque.altura == block.altura:
            cont += 1
            if cont > 1:
                listaEliminar.append(block)
    return listaEliminar

def ExisteOtrosBloques(bloques,bloque):
    cont = 0
    for block in bloques:
        if bloque.largo == block.largo and bloque.ancho == block.ancho and bloque.altura == block.altura:
            cont += 1
        if cont > 1:
            return True
    return False

# Devuleve las torres 
def get_Torres(lista_figuras,num):
    if(len(lista_figuras)==1 and num == 1): 
        resultado = []
        for permutacion in lista_figuras[0]:
            resultado.append([permutacion])
        return resultado

    elif(len(lista_figuras)==1): return lista_figuras[0]

    lista1=lista_figuras[0]
    lista2=lista_figuras[1]
    listaTmp=[]
    
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if(num == 1): 
               # print("lista1 if",lista1[i])
                #print("lista2 if",lista2[j])
                listaTmp.append([lista1[i]]+[lista2[j]])
            else:
               # print("lista1 else",lista1[i])
               # print("lista2 else",lista2[j])
                listaTmp.append(lista1[i]+[lista2[j]])
    return get_Torres( [listaTmp] + lista_figuras[2:],2)

# Valida si el bloque es valido 
def esValida(bloqueActual,bloqueSiquiente):
    if (bloqueActual.largo <= bloqueSiquiente.largo) or\
        (bloqueActual.ancho <= bloqueSiquiente.ancho):
        return False
    return True

# importing copy module
import copy
def permutarCombinacion(combinacion,permutacion,resultado):
    #print("S:",stack)
    if not combinacion:
        resultado.append(copy.deepcopy(permutacion))
        #print("S:",permutacion)
    else:    # Cuando no haya alcanzado el nodo hoja del árbol, use la recursividad para continuar mirando hacia abajo.
        for i in range(len(combinacion)):
            #print(list[i])#,"<=>",stack[-1]) 
            if i <= len(combinacion)-2:
                #print(list)
                #print(i)
                if esValida(combinacion[i],combinacion[i+1])==False:#combinacion[i] < combinacion[i+1]:
                    continue
            permutacion.append(combinacion[i])
            del combinacion[i] 
            permutarCombinacion(combinacion,permutacion,resultado)
            combinacion.insert(i,permutacion.pop())
# -----------------------------------------------------------------------------------------------
#endregion Fuerza Bruta 


#region Programacion dinamica 
# -----------------------------------------------------------------------------------------------
def contenedorProgramacionDinamica(datos:list):
    start = time.time()
    bloques = []
    for bloque in datos:
        bloques.append(Util.permutaciones(bloque, len(bloque)))
    
    permutacionesBloques = []
    for block in bloques:
        cont = 0
        for permutacion in block:
            if permutacion[0] <= permutacion[1] and cont < 3:
                bloque = Bloque()
                bloque.largo = permutacion[0]
                bloque.ancho = permutacion[1]      
                bloque.altura = permutacion[2]
                permutacionesBloques.append(bloque)
                cont += 1

    permutacionesBloques = eliminarBloquesRepetidos(permutacionesBloques[0],permutacionesBloques)
    print("############ BLOQUES ############")
    for bloque in permutacionesBloques: 
        print("-----------------------") 
        print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')
    
    anchoTotal = max([bloque.ancho for bloque in permutacionesBloques])
    print("anchoTotal: ",anchoTotal)
    largoTotal = max([bloque.largo for bloque in permutacionesBloques])
    print("largoTotal: ",largoTotal)
    W = anchoTotal if anchoTotal > largoTotal else largoTotal
    
    #W = len(permutacionesBloques)
    matriz = []
    print("w = ",W)
    for i in range(len(permutacionesBloques)+1):
        matriz.append([0] * (W+1))

    #for fila in matriz:
    #    print(fila)
    
    recorrerMatriz(matriz,permutacionesBloques,W)
    #recorrerMatriz2(matriz,permutacionesBloques,W)
    n = len(permutacionesBloques)
    #elementos = encontrarLosElementos(matriz,n,W,permutacionesBloques,[])
    #print(elementos)

    cont = 0
    for fila in matriz:
        print(cont,") ",fila)
        cont += 1
    end = time.time()
    print(f'Tiempo de ejecución: {end-start} segundos')

def recorrerMatriz2(V,bloques,Peso_Maximo):
    n = len(bloques)+1
    W:list[Bloque] = [None]+bloques
    B:list[Bloque] = [None]+bloques
    for i in range(1,n):
        for w in range(1,n):
            
            #print("(",i," | ",w,")")
            if esValida(B[i],B[w]) == False:#W[i].peso > w:
                V[i][w] = V[i-1][w]
            else:
                # i = 2 w = 2
                # V[i-1] => (2-1) = 1
                # [w-W[i].peso] =>(2-3) = -1
                #V[1][-1] # => 0 <= V[i-1][w-W[i].peso]
                #B[i].altura # => 4
                if B[i].altura + B[w].altura > V[i-1][w]:
                    V[i][w] = B[i].altura + B[w].altura
                else:
                    V[i][w] = V[i-1][w]

def encontrarLosElementos2(V,n,Peso_Maximo,bloques,elementos):
    W:list[Bloque] = [None]+bloques
    i=n
    k=Peso_Maximo
    #print("(",i," | ",k,") = ",V[i][k])
    if (i == 0 and k == 0) or V[i][k] == 0:
        return elementos
    if V[i][k] != V[i-1][k]:
        elementos.append(i)
        i=i-1
        k=k-W[i].largo
    else:
        i=i-1
    return encontrarLosElementos(V,i,k,bloques,elementos)

def recorrerMatriz(V,bloques,Peso_Maximo):
    n = len(bloques)+1
    #BloqueNone = Bloque() 
    #bloques = [BloqueNone] + bloques
    W:list[Bloque] = [None]+bloques
    B:list[Bloque] = [None]+bloques
    for i in range(1,n):
        for w in range(Peso_Maximo+1):
            #print("(",i," | ",w,")")
            #if w < anchoTotal+1:
            #if esValida(bloques[i],bloques[i-1]):
                if W[i].ancho > w or W[i].largo > w:
                    V[i][w] = V[i-1][w]
                else:
                    #print(W[i].largo," <-> ",W[i].ancho)
                    peso = max([W[i].ancho,W[i].largo])
                    #print("Peso: ",peso)
                    if B[i].altura + V[i-1][w-peso] > V[i-1][w]:
                        V[i][w] = B[i].altura + V[i-1][w-peso]
                    else:
                        V[i][w] = V[i-1][w]
                    
def encontrarLosElementos(V,n,Peso_Maximo,bloques,elementos):
    W:list[Bloque] = bloques
    i=n
    k=Peso_Maximo
    #print("(",i," | ",k,") = ",V[i][k])
    if (i == 0 and k == 0) or V[i][k] == 0:
        return elementos
    if V[i][k] != V[i-1][k]:
        elementos.append(i)
        i=i-1
        k=k-W[i].largo
    else:
        i=i-1
    return encontrarLosElementos(V,i,k,bloques,elementos)
# -----------------------------------------------------------------------------------------------
#endregion Programacion dinamica

def imprimirBloques(bloque):
    print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')

if __name__ == '__main__':
    # python ./bloques.py algoritmo archivo.txt
    # ./bloques.py 1 bloques1.txt
    if sys.argv[1] == "1":
        archivo = sys.argv[2].split('.')
        Lineas = Util.abrir_Archivo(sys.argv[2])
        print(Lineas)
        bloquesFuerzaBruta(Lineas)
    elif sys.argv[1] == "2":
        archivo = sys.argv[2].split('.')
        Lineas = Util.abrir_Archivo(sys.argv[2])
        print(Lineas)
        contenedorProgramacionDinamica(Lineas)

