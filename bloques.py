# Imports
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

    for combinacion in permutacionesBloques:
        print("*******************************************************")
        for permutacionbloque in combinacion:
            print("-----------------------")
            for bloque in permutacionbloque:
                print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')
    
    # Combinaciones Validas
    
    torres_Total = get_Torres(permutacionesBloques,2)
    
    print(torres_Total)
    """
    for combin in combinacionBloques:
        torres = []
        torres_Total += getTorres(combin,torres)
    print(torres)
    """

def get_Torres(lista_figuras,num):
    if(len(lista_figuras)==1): return lista_figuras
    lista1=lista_figuras[0]
    lista2=lista_figuras[1]
    listaTmp=[]
    
    for i in range(len(lista1)):

        for j in range(len(lista2)):
            if(num == 1): listaTmp.append([lista1[i]]+[lista2[j]])

            else:
                listaTmp.append(lista1[i]+[lista2[j]])

    return get_Torres( [listaTmp] + lista_figuras[2:],2)


""" def getTorres(combinacion:list,torres:list[Torre],i:int=0,j:int=1):
    if i == len(combinacion[0]):
        return torres
    else:
        if torres != []:
            torre = Torre()
            torre.bloques += combinacion[i]
        else:
            for bloque in combinacion[j]:

            
            return getTorres(combinacion,torres,i+1,j)

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
"""

# -----------------------------------------------------------------------------------------------
#endregion Fuerza Bruta 


if __name__ == '__main__':
    # python ./bloques.py algoritmo archivo.txt
    # ./bloques.py 1 bloques1.txt
    if sys.argv[0] == "1":
        print("entra")
        archivo = sys.argv[2].split('.')
        Lineas = Util.abrir_Archivo(sys.argv[2])
        print(Lineas)
        bloquesFuerzaBruta(Lineas)
    elif sys.argv[0] == "2":
        archivo = sys.argv[2].split('.')
        Lineas = Util.abrir_Archivo(sys.argv[2])
        print(Lineas)
        #contenedorProgramacionDinamica(Lineas)

