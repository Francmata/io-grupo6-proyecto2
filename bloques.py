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

        
     
    combinacionBloques = Util.get_Lista_Combinaciones(permutacionesBloques) 
     
    """
    for combinacion in combinacionBloques: 
        print("*******************************************************") 
        for permutacionbloque in combinacion: 
            print("-----------------------") 
            for bloque in permutacionbloque: 
                print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')
    """
    # Combinaciones Validas
    
    torres_Total = []#get_Torres(permutacionesBloques,1)
    
    for combinacion in combinacionBloques:
        temporal=get_Torres(combinacion,1)
        #print(temporal)
        torres_Total.append( temporal)
    cont = 0
    
    for torre in torres_Total:      
        for combinacion in torre:
            print("*********************TORRE**********************************")
            for bloque in combinacion: 
                #print("-------------------------")
               #print(bloque)
                cont+=1
                print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')
                
    print(cont)

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


# -----------------------------------------------------------------------------------------------
#endregion Fuerza Bruta 

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
        #contenedorProgramacionDinamica(Lineas)

