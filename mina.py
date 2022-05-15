# Imports
import Util
import time
import sys
import numpy as np
import copy

#region Fuerza Bruta 
# -----------------------------------------------------------------------------------------------
def minaFuerzaBruta(datos:list):
    start = time.time()
    rutas = getDiccionarioRutas(datos)
    rutas = rutasConstruidas(rutas,len(datos)-1)
    #print(rutas)

    rutasMayorGanancia=[]
    for ruta in rutas:
        if rutasMayorGanancia == []:
            rutasMayorGanancia.append(ruta)
        else:
            if getGanancia(ruta,datos) > getGanancia(rutasMayorGanancia[-1],datos):
                rutasMayorGanancia=[]
                rutasMayorGanancia.append(ruta)
            elif getGanancia(ruta,datos) == getGanancia(rutasMayorGanancia[-1],datos):
                rutasMayorGanancia.append(ruta)
    end = time.time()
    print(f'\nOutput : {getGanancia(rutasMayorGanancia[0],datos)}\n')
    print( " OR\n".join([" -> ".join([f'({vertice[0]}, {vertice[1]})' for vertice in ruta]) for ruta in rutasMayorGanancia]))
    print(f'\nTiempo de ejecución: {end-start} segundos')

def getGanancia(ruta,datos):

    ganancia = 0

    for mina in ruta:
        ganancia += datos[mina[0]][mina[1]]
    return ganancia

def getDiccionarioRutas(datos:list):
    largo=len(datos)
    ancho= len(datos[0])

    caminos=[]
    for i in range(len(datos)):
        for j in range(len(datos[0])-1):
            if i==0:
                caminos.append([[i,j], [i,j+1], [i+1,j+1]])
            elif i==len(datos)-1:
                caminos.append([[i,j], [i,j+1], [i-1,j+1]])
            else:
                caminos.append([[i,j], [i,j+1], [i+1,j+1], [i-1,j+1]])
    return caminos
def iniciales(largo):
    tmp = []
    i = 0
    while i < largo:
        tmp.append([i,0])
        i+=1
    return tmp

def rutasConstruidas(lista,largo):
    listaIniciales = iniciales(largo+1)
    tmp = []
    for inicial in listaIniciales:
        tmp = tmp + obtenerRuta([[inicial]],largo,[],lista)

    return tmp
#               [[[0,1]]], 5,[]
def obtenerRuta(caminos,num,resultado,lista):
    
    for camino in caminos:
        
        siguientes = getSiguientes(camino[-1],lista)
        
        if(siguientes ==False): return caminos
        
        siguientes = siguientes[1:]
        
        if(camino[-1][0] == 0 or camino[-1][0]==num):
            tmp = camino+[siguientes[0]]
            resultado.append(tmp)
            tmp = camino+[siguientes[1]]
            resultado.append(tmp)
        
        else:
            tmp = camino+[siguientes[0]]
            resultado.append(tmp)
            tmp = camino+[siguientes[1]]
            resultado.append(tmp)
            tmp = camino+[siguientes[2]]
            resultado.append(tmp)
    
    return obtenerRuta(resultado,num,[],lista)

def getSiguientes(vertice,lista):
    
    for siguientes in  lista:
        if(siguientes[0]==vertice):
            return siguientes
    return False
# -----------------------------------------------------------------------------------------------
#endregion Fuerza Bruta 

#region PD 
# -----------------------------------------------------------------------------------------------
class Mina:
    def __init__(self):
        self.fila = None
        self.columna = None
        self.valor = None
    
    def __str__(self):
        return f'{self.valor}'
    
    def imprimir(self):
        return f'({self.fila}|{self.columna}) = {self.valor}'

def minaProgramacionDinamica(datos):
    start = time.time()

    minas=crearMatrizMinas(datos)
    
    # CONVERTIR DICCIONARIO RUTAS
    diccionarioRutas=getDiccionarioRutas(minas)
    nuevoDiccionarioRutas= []
    for ruta in diccionarioRutas:
        nuevaRuta=[]
        for mina in ruta:
            #print(buscarMina(minas, mina[0], mina[1]).__str__())
            nuevaRuta.append(buscarMina(minas, mina[0], mina[1]))
        nuevoDiccionarioRutas.append(nuevaRuta)
    diccionario={}
    for ruta in nuevoDiccionarioRutas:
        diccionario[ruta[0]] = ruta[1:]
    #print([f'{key.__str__()}: {diccionario[key]}' for key in diccionario])
    
    # CREAR ETAPAS
    etapaFinal= obtenerEtapaFinal(minas)
    
    etapasProceso= [etapaFinal] 
    etapas=len(datos[0])-1   
    for n in range(etapas):
        matrizEtapa = crearMatrizEtapa(minas, etapasProceso, etapas-n, diccionario) 
        etapasProceso.append(matrizEtapa)
    
    # imprimir Etapas
    for fila in etapaFinal:
        print(fila)
    print(" ")
    for matrizEtapa in etapasProceso[1:]:
        printMatriz(matrizEtapa)
        print(" ")
    
    rutas = obtenerRutasOptimas(etapasProceso)


    end = time.time()
    print(f'\nOutput : { sum( [ mina.valor for mina in rutas[0] ] ) }\n')
    print( " OR\n".join([" -> ".join([f'({mina.fila}, {mina.columna})' for mina in ruta]) for ruta in rutas]))
    print(f'\nTiempo de ejecución: {end-start} segundos')

def crearMatrizEtapa(minas, etapasProceso, etapa, dic):
    matrizEtapa=[]
    for i in range(len(minas)+1):
        matrizEtapa.append([0] * (len(minas)+3))
    
    for i in range (len(matrizEtapa)):
        for j in range (len(matrizEtapa[0])):
            if j==0 and i!=0:
                mina:Mina = minas[i-1][etapa-1]
                matrizEtapa[i][j]= mina

    for i in range(1,len(matrizEtapa)):
        mina:Mina = minas[i-1][etapa]
        matrizEtapa[0][i]= mina

    for i in range (1, len(matrizEtapa)):
        for j in range (1, len(matrizEtapa[0])-2):
            fila:Mina= matrizEtapa[i][0]
            #columna:Mina= matrizEtapa[0][j]
            if len(etapasProceso) == 1:
                etapaAnterior = np.transpose(etapasProceso[-1]) 
                #print(etapaAnterior)
                columna = etapaAnterior[1][j]
            else:
                #print(etapasProceso[-1])
                columna = etapasProceso[-1][j][-2]
            if hayRuta(matrizEtapa[i][0], matrizEtapa[0][j], dic) == True:
                #print(fila.valor," ",columna)
                matrizEtapa[i][j]= fila.valor+columna
        
    for i in range (1, len(matrizEtapa)):
        maximo = max(matrizEtapa[i][1:-2])
        matrizEtapa[i][-2]= maximo
        indicesMax = extraerIndicesMina(matrizEtapa[i][:-2],maximo)[0]
        columnas = []
        for indice in indicesMax:
            columnas.append(matrizEtapa[0][indice])
        matrizEtapa[i][-1]=columnas

    #print(" ")
    #printMatriz(matrizEtapa)
    #print(" ")
    return matrizEtapa


def extraerIndicesMina(lst,num):
    #lst = [13, 4, 20, 15, 6, 20, 20]
    lst = np.array(lst)
    result = np.where(lst == num)
    return result

def printMatriz(matriz:list):
    for i in range(len(matriz)):
        if i ==0:
            print([element.__str__() for element in matriz[i]])
        else:
            print([element.__str__() for element in matriz[i][:-1]]+[[element.__str__() for element in matriz[i][-1]]])
        
        #if i == 0:
        #    print([""]+[element.__str__() for element in matriz[i][1:-3]]+["",""])

def hayRuta(mina:Mina, mina2:Mina, dic:dict):
    if mina in dic:
        if mina2 in dic[mina]:
            return True
    return False

def buscarMina(minas:list[list[Mina]], i , j):
    for fila in minas:
        for mina in fila:
            if mina.columna==j and mina.fila==i:
                return mina
    return None

def crearMatrizMinas(datos):
    matriz= []
    for i in range (len(datos)):
        fila=[]
        for j in range (len(datos[0])):
            objeto = Mina()
            objeto.fila = i
            objeto.columna = j
            objeto.valor = datos[i][j]
            fila.append(objeto)
        matriz.append(fila)
    return matriz

def obtenerEtapaFinal(minas:list[list[Mina]]):
    pesos=[[0,0,0]]
    for i in range(len(minas)):
        #print(minas[i][-1])
        pesos.append([minas[i][-1].valor, minas[i][-1].valor, 0])
    return pesos

def maximoEtapaInicial(etapa):
    numero = etapa[1][-2]
    resultado = []
    for x in range(1,len(etapa)):
        if(etapa[x][-2]> numero):
            resultado = []
            resultado+=[etapa[x][0]]
            numero = etapa[x][-2]
        elif(etapa[x][-2] == numero):
            resultado+=[etapa[x][0]]
    return resultado

def obtenerRutasOptimas(tablasEtapas): 
    rutasDic = crearDiccionarioRutas(tablasEtapas)
    optimosIniciales = maximoEtapaInicial(tablasEtapas[-1])
    rutas=[]
    for optimoInicial in optimosIniciales:
        #print(optimoInicial.__str__())
        roots = []
        obtenerRutas(optimoInicial,rutasDic,[optimoInicial],roots)
        rutas+=roots
        #print("RUTAS -> ",optimoInicial.imprimir())
        #for items in roots:
        #    print([item.imprimir() for item in items])
    return rutas

def obtenerRutas(mina,rutasDic,rutas,roots):
    #print(mina.__str__())
    if not mina in rutasDic: 
        roots+=[copy.deepcopy(rutas)]
        #print("----------------")
    else:
        for siguienteMina in rutasDic[mina]:
            rutas += [siguienteMina]
            obtenerRutas(siguienteMina,rutasDic,rutas,roots)
            #print("cont: ",rutas.index(mina))
            rutas = rutas[:rutas.index(mina)+1]       

def crearDiccionarioRutas(etapas):
    diccionario = {}
    for etapa in reversed(etapas[1:]):
        for fila in etapa[1:]:
            diccionario[fila[0]] = fila[-1]
    return diccionario
# -----------------------------------------------------------------------------------------------
#endregion PD

if __name__ == '__main__':
    # python ./mina.py algoritmo archivo.txt
    if sys.argv[1] == "1":
        archivo = sys.argv[2].split('.')
        Lineas = Util.abrir_Archivo(sys.argv[2])
        print(Lineas)
        minaFuerzaBruta(Lineas)
    elif sys.argv[1] == "2":
        archivo = sys.argv[2].split('.')
        Lineas = Util.abrir_Archivo(sys.argv[2])
        print(Lineas)
        minaProgramacionDinamica(Lineas)

