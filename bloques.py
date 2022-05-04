# Imports
from webbrowser import get
import Util
import time
import sys
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
    def getAltura(self):
        altura = 0
        for bloque in self.bloques:
            altura += bloque.altura
        return altura
# -----------------------------------------------------------------------------------------------
#endregion Classes

#region Fuerza Bruta 
# -----------------------------------------------------------------------------------------------
def bloquesFuerzaBruta(datos:list):
    bloques = []
    cont = 1
    for block in datos:
        bloque = Bloque()
        bloque.largo = block[0]
        bloque.ancho = block[1]      
        bloque.altura = block[2]
        bloques.append(bloque)
        cont+=1

    # Hacer permutaciones del bloque
    permutacionesBloques = []
    for bloque in bloques:
        bloque2 = Bloque()
        bloque2.largo  = bloque.ancho
        bloque2.ancho  = bloque.altura
        bloque2.altura = bloque.largo
        bloque3 = Bloque()
        bloque3.largo  = bloque.altura
        bloque3.ancho  = bloque.largo
        bloque3.altura = bloque.ancho
        permutacionesBloques.append([bloque,bloque2,bloque3])
    
    #for permutacion in permutacionesBloques:
    #    print("-----------------------")
    #    for bloque in permutacion:
    #        print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')
    #print(permutacionesBloques)

    combinacionBloques = Util.get_Lista_Combinaciones(permutacionesBloques)
    
    torresValidas = []

    for combinacion in combinacionBloques:
        print("*******************************************************")
        for permutacionbloque in combinacion:
            print("-----------------------")
            for bloque in permutacionbloque:
                print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')
    
    # Combinaciones Validas
    #for indexCombinacion in range(len(combinacionBloques)):
    #    for indexBloque in range(len(combinacionBloques[indexCombinacion])):
    torres_Total = []
    for combin in combinacionBloques:
        torres = []
        torres_Total += getTorres(combin,torres)
    print(torres)

def getTorres(combinacion:list,torres:list[Torre],i:int=0,j:int=1):
    if i == len(combinacion[0]):
        return torres
    else:
        if torres != []:
            torre = Torre()
            torre.bloques += combinacion[i]
        else:
            for bloque in combinacion[j]:

            
            return getTorres(combinacion,torres,i+1,j)
            
            return getTorres(combinacion,torres,i,j+1)

def getTorre(combinacion:list,torre:Torre=Torre(),i=0,j=1):
    if j >= len(combinacion):
        return torres
    else:
        if torre.bloques == []:   
            torre.bloques += combinacion[i]
        else:
            for x in range(1,len(combinacion)):
                torre.bloques += bloque
            getTorre(combinacion,i,j+1)


# -----------------------------------------------------------------------------------------------
#endregion Fuerza Bruta 


if __name__ == '__main__':
    #forma_Apropiada_Dos_Fases_Fase_1(None,None)
    #--h es un parámetro de ingreso opcional
    # python ./contenedor.py algoritmo archivo.txt
    if sys.argv[1] == "1":
        archivo = sys.argv[2].split('.')
        Lineas = Util.abrir_Archivo(sys.argv[2])
        print(Lineas)
        bloquesFuerzaBruta(Lineas)
    elif sys.argv[1] == "2":
        archivo = sys.argv[2].split('.')
        Lineas = Util.abrir_Archivo(sys.argv[2])
        print(Lineas)
        #contenedorProgramacionDinamica(Lineas)