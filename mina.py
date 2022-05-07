# Imports
import Util
import time
import sys


#region Fuerza Bruta 
# -----------------------------------------------------------------------------------------------
def minaFuerzaBruta(datos:list):
    caminos_posibles=[]
    largo=len(datos)
    ancho=len(datos[0])
    #encontrar_caminos( largo, ancho, 0, 0, [[0,0]], caminos_posibles)
    #print(caminos_posibles)
    #for i in range(len(datos)):
    lista = []
        #print(i)
        #lista = []
    caminos_posibles+=en( largo, ancho, 0, 0,lista )
    print(caminos_posibles)

def encontrar_caminos(largo, ancho, i, j, caminos_posibles):
    print(caminos)
    if i== largo-1 or j==ancho-1: 
        caminos_posibles.append(caminos)
        return 
    for camino in (caminos):
        i= camino
        j=camino[0]
        #borde arriba
        if i==0:
            encontrar_caminos(largo, ancho, i, j+1, (camino+[[i, j+1],[i+1, j+1]]), caminos_posibles) 
        #borde abajo
        elif i==largo-1:
            encontrar_caminos(largo, ancho, i, j+1, (camino+[[i, j+1],[i-1, j+1]]), caminos_posibles)
        #medio
        else:
            encontrar_caminos(largo, ancho, i, j+1, (camino+[[i, j+1], [i+1, j+1], [i-1, j+1]]), caminos_posibles) 

def en(largo,ancho, i, j, caminos_posibles):
    print(f'({i},{j})')
    caminos_posibles.append([i,j])
    if j==ancho-1: 
        return [caminos_posibles]
        lista = []
    #borde arriba
    if i==0:
        for camino in [[i, j+1],[i+1, j+1]]:
            i = camino[0]
            j = camino[1]
            return en(largo,ancho,i, j,caminos_posibles)
   #borde abajo
    elif i==largo-1:
        for camino in [[i, j+1],[i-1, j+1]]:
            i = camino[0]
            j = camino[1]
            return en(largo,ancho,i, j,caminos_posibles)
  #medio
    else:
        for camino in [[i, j+1], [i+1, j+1], [i-1, j+1]]:
            i = camino[0]
            j = camino[1]
            return en(largo,ancho,i, j,caminos_posibles)
"""
def encontrar_caminos(matriz, i, j, caso):
    print(i, j)
    if caso==1:
        return [(i, j)(i, j+1, matriz[i][j]), (i+1, j+1, matriz[i+1][j+1])]
    elif caso==2:
        return [(i, j+1, matriz[i][j+1]), (i-1, j+1, matriz[i-1][j+1])]
    else:
        return [(i, j+1, matriz[i][j+1]),(i-1, j+1, matriz[i-1][j+1]),(i+1, j+1, matriz[i+1][j+1])]
"""
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