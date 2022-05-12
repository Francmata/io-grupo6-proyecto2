# Imports
import Util
import time
import sys

#region Classes
# -----------------------------------------------------------------------------------------------
class Articulo():
    def __init__(self):
        self.id:int         = 0
        self.beneficio:int  = 0
        self.peso:int       = 0

class Mochila():
    def __init__(self):
        self.peso:int       = 0
        self.pesoLibre:int  = 0
        self.articulos:list[Articulo] = []
    
    def agregarArticulo(self,articulo:Articulo):
        self.articulos.append(articulo)
        self.pesoLibre -= articulo.peso
    
    def obtenerBeneficio(self):
        beneficio = 0
        for articulo in self.articulos:
            beneficio += articulo.beneficio
        return beneficio
# -----------------------------------------------------------------------------------------------
#endregion Classes

#region Fuerza Bruta 
# -----------------------------------------------------------------------------------------------
def contenedorFuerzaBruta(datos:list):
    start = time.time()
    W = datos[0][0]

    mochila = Mochila()
    mochila.peso = W
    mochila.pesoLibre = W
    
    articulos = []
    cont = 1
    for arti in datos[1:]:
        articulo = Articulo()
        articulo.id = cont
        articulo.peso = arti[0]       
        articulo.beneficio = arti[1]
        articulos.append(articulo)
        cont+=1

    # Hacer combinaciones
    combinacionesArticulos = Util.get_Lista_Combinaciones(articulos)
    #for combinacion in combinacionesArticulos:
    #    print("-----------------------")
    #    for articulo in combinacion:
    #        print(f'{articulo.id}) -> {articulo.peso}/{articulo.beneficio}')
   
    # Combinaciones Validas
    combinacionesOptimas = []
    for combinacion in combinacionesArticulos:
        pesoCombinacion = 0
        beneficioCombinacion = 0
        for articulo in combinacion:
            pesoCombinacion += articulo.peso
            beneficioCombinacion += articulo.beneficio
        if pesoCombinacion <= mochila.peso and beneficioCombinacion >= mochila.obtenerBeneficio():
            mochila.articulos = combinacion # 30
            if combinacionesOptimas != []: 
                if get_Beneficio(combinacionesOptimas[0]) < beneficioCombinacion :
                    combinacionesOptimas = []
            combinacionesOptimas.append(combinacion) # [30]
    
    end = time.time()
    
    for combinacion in combinacionesOptimas:
        print("-----------------------")
        print(f'Beneficio: {get_Beneficio(combinacion)}')
        for articulo in combinacion:
            print(f'{articulo.id}) -> P:{articulo.peso} / B:{articulo.beneficio}')
    print(f'Tiempo de ejecución: {end-start} segundos')
# -----------------------------------------------------------------------------------------------
def get_Beneficio(articulos:list[Articulo]):
    beneficio = 0
    for articulo in articulos:
        beneficio += articulo.beneficio
    return beneficio
# -----------------------------------------------------------------------------------------------
def meterArticulo(mochila:Mochila,articulo:Articulo):
    if articulo.peso <= mochila.pesoLibre:
        mochila.articulos.append(articulo)  
# -----------------------------------------------------------------------------------------------
#endregion Fuerza Bruta

#region Programacion dinamica 
# -----------------------------------------------------------------------------------------------
def contenedorProgramacionDinamica(datos:list):
    start = time.time()
    W = datos[0][0]

    mochila = Mochila()
    mochila.peso = W
    mochila.pesoLibre = W
    
    articulos = []
    cont = 1
    for arti in datos[1:]:
        articulo = Articulo()
        articulo.id = cont
        articulo.peso = arti[0]       
        articulo.beneficio = arti[1]
        articulos.append(articulo)
        cont+=1
    #articulo = Articulo()
    #articulo.beneficio = 0 
    #articulo.peso = 0 
    #articulo.id = 0 
    #
    #articulos.append(articulo)

    matriz = []
    for i in range(len(articulos)+1):
        matriz.append([0] * (W+1))
    
    #for fila in matriz:
    #    print(fila)

    recorrerMatriz(matriz,articulos,W)

    for fila in matriz:
        print(fila)

    
    n = len(articulos)
    beneficioMaximo = matriz[n][W]
    
    elementos = encontrarLosElementos(matriz,n,W,articulos,[])

    end = time.time()
    print(f'Beneficio máximo: {beneficioMaximo}')
    print(f'Incluidos: {", ".join([str(elemento) for elemento in elementos])}')

    print(f'Tiempo de ejecución: {end-start} segundos')
    return

def recorrerMatriz(V,articulos,Peso_Maximo):
    n = len(articulos)+1
    W = [None]+articulos
    B = [None]+articulos
    for i in range(1,n):
        for w in range(Peso_Maximo+1):
            #print("(",i," | ",w,")")
            if W[i].peso > w:
                V[i][w] = V[i-1][w]
            else:
                if B[i].beneficio + V[i-1][w-W[i].peso] > V[i-1][w]:
                    V[i][w] = B[i].beneficio + V[i-1][w-W[i].peso]
                else:
                    V[i][w] = V[i-1][w]

def encontrarLosElementos(V,n,Peso_Maximo,articulos,elementos):
    W = articulos
    i=n
    k=Peso_Maximo
    #print("(",i," | ",k,") = ",V[i][k])
    if (i == 0 and k == 0) or V[i][k] == 0:
        return elementos
    if V[i][k] != V[i-1][k]:
        elementos.append(i)
        i=i-1
        k=k-W[i].peso
    else:
        i=i-1
    return encontrarLosElementos(V,i,k,articulos,elementos)
# -----------------------------------------------------------------------------------------------
#endregion Programacion dinamica

#region Funciones Generales 
# -----------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------
#endregion Funciones Generales

if __name__ == '__main__':
    #forma_Apropiada_Dos_Fases_Fase_1(None,None)
    #--h es un parámetro de ingreso opcional
    # python ./contenedor.py algoritmo archivo.txt
    if sys.argv[1] == "1":
        archivo = sys.argv[2].split('.')
        Lineas = Util.abrir_Archivo(sys.argv[2])
        print(Lineas)
        contenedorFuerzaBruta(Lineas)
    elif sys.argv[1] == "2":
        archivo = sys.argv[2].split('.')
        Lineas = Util.abrir_Archivo(sys.argv[2])
        print(Lineas)
        contenedorProgramacionDinamica(Lineas)
