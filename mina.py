# Imports
from pickle import OBJ
from traceback import print_tb
from pyparsing import null_debug_action
import Util
import time
import sys


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

def minaProgramacionDinamica(datos):
    minas=crearMatrizMinas(datos)
    etapaFinal= obtenerEtapaFinal(datos)
    etapasProceso= [etapaFinal]
    etapas=len(datos[0])-1
    diccionarioRutas=getDiccionarioRutas(minas)
    nuevoDiccionarioRutas= []
    for ruta in diccionarioRutas:
        nuevaRuta=[]
        for mina in ruta:
            nuevaRuta.append(buscarMina(minas, mina[0], mina[1]))
        nuevoDiccionarioRutas.append(nuevaRuta)
    
    diccionario={}
    for ruta in nuevoDiccionarioRutas:
        diccionario[ruta[0]]= ruta[1:]
    
    print(diccionario)
            
            

    for n in range(etapas):
        etapa=crearMatrizEtapa(minas, etapasProceso, etapas-n, diccionario)
        break
    return

def crearMatrizEtapa(minas, etapasProceso, etapa, dic):
    matrizEtapa=[]
    if len(etapasProceso)==1:
        for i in range(len(minas)+1):
            matrizEtapa.append([0] * (len(minas)+3))
        
        for i in range (len(matrizEtapa)):
            for j in range (len(matrizEtapa[0])):
                if j==0 and i!=0:
                    mina:Mina = minas[i-1][etapa-1]
                    matrizEtapa[i][j]= mina.valor

        for i in range(1,len(matrizEtapa)):
            mina:Mina = minas[i-1][etapa]
            matrizEtapa[0][i]= mina.valor

        for i in range (1, len(matrizEtapa)):
            for j in range (1, len(matrizEtapa[0])):
                fila:Mina= matrizEtapa[i][0]
                columna:Mina= matrizEtapa[0][j]
                print("antes del if")
                if hayRuta(fila, columna, dic):
                    print("entró")
                    matrizEtapa[i][j]= fila.valor+columna.valor
        for i in matrizEtapa:
            print(i)

    return 

def hayRuta(mina, mina2, dic):
    print("f")
    if mina in dic:
        print("1")
        if mina2 in dic[mina]:
            print("2")
            return True
    return False

def buscarMina(minas:list[Mina], i , j):
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

def obtenerEtapaFinal(minas):
    pesos=[]
    for i in range(len(minas)):
        pesos.append(minas[i][-1])
    return pesos

 
def procesarEtapa():
    return
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