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
    for bloque in datos:
        bloques.append(Util.permutaciones(bloque, len(bloque)))
    
    permutacionesBloques = []
    for block in bloques:
        listaBloque = []
        cont = 0
        for permutacion in block:
            if permutacion[0] <= permutacion[1] and cont < 3:
                bloque = Bloque()
                bloque.largo = permutacion[0]
                bloque.ancho = permutacion[1]      
                bloque.altura = permutacion[2]
                listaBloque.append(bloque)
                cont += 1
        permutacionesBloques.append(listaBloque)

    #print("############ PERMUTACIONES ############")
    #for permutacionbloque in permutacionesBloques: 
    #    print("-----------------------") 
    #    for bloque in permutacionbloque: 
    #        print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')
    
    combinacionBloques = Util.get_Lista_Combinaciones(permutacionesBloques) 

    CombinacionesPermutadas = []
    for combinacion in combinacionBloques: 
        CombinacionesPermutadas+=Util.permutaciones(combinacion, len(combinacion))
    
    combinacionBloques = CombinacionesPermutadas
     
    #print("############ COMBINACIONES ############")
    #for combinacion in combinacionBloques: 
    #    print("*******************************************************") 
    #    for permutacionbloque in combinacion: 
    #        print("-----------------------") 
    #        for bloque in permutacionbloque: 
    #            print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')
    
    # Combinaciones Validas
    torres_Total = []#get_Torres(permutacionesBloques,1)
    for combinacion in combinacionBloques:
        temporal=get_Torres(combinacion,1)
        #print(temporal)
        torres_Total.append( temporal)

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

    torreValidas = []
    for torre in torres_Total:
        for combinacion in torre:
            torre = Torre()
            torre.bloques = combinacion
            if torre.esValida() == True:
                torreValidas.append(torre)
    
    #print("############ TORRES VALIDAS ############")
    #for torre in torreValidas:
    #    print("------------------------------")
    #    for bloque in torre.bloques:
    #        print(f'{bloque.largo} / {bloque.ancho} / {bloque.altura}')           
             
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
    
    for torre in torreMasAltas:
        print("------------------------------")
        print(f'Altura: {torre.getAltura()}')
        print(", ".join([f'({bloque.largo}, {bloque.ancho}, {bloque.altura})' for bloque in torre.bloques]))
    print(f'\n Tiempo de ejecución: {end-start} segundos')

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

