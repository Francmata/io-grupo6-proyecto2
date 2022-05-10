# Imports
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