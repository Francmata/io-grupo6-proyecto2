# Imports
import Util
import time
import sys

#region Classes
# -----------------------------------------------------------------------------------------------

# Se crea un clase Articulo para un mejor manejo de los articulos a meter en la mochila
class Articulo():
    def __init__(self):
        self.id:int         = 0
        self.beneficio:int  = 0
        self.peso:int       = 0

# Se crea un clase Mochila para facilitar el agregado de los articulos a la mochila
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
    # se crear los bjetos Articulos con sus atributos
    for arti in datos[1:]:
        articulo = Articulo()
        articulo.id = cont
        articulo.peso = arti[0]       
        articulo.beneficio = arti[1]
        articulos.append(articulo)
        cont+=1

    # Hacer combinaciones de los articulos en la mochila
    combinacionesArticulos = Util.get_Lista_Combinaciones(articulos)
    #for combinacion in combinacionesArticulos:
    #    print("-----------------------")
    #    for articulo in combinacion:
    #        print(f'{articulo.id}) -> {articulo.peso}/{articulo.beneficio}')
   
    
    # Combinaciones Validas, se verifica que el peso de los artuclos no pase el de la mochila
    # Y se saca la mochila con el mayor beneficio
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
    
    # Se imprime, el beneficio, la o las mochilas con el mayor beneficio y el tiempo de ejecución
    for combinacion in combinacionesOptimas:
        print("-----------------------")
        print(f'Beneficio máximo: {get_Beneficio(combinacion)}')
        print("Incluidos:")
        for articulo in combinacion:
            print(f'{articulo.id}) -> P:{articulo.peso} / B:{articulo.beneficio}')
    print(f'Tiempo de ejecución: {end-start} segundos')
# -----------------------------------------------------------------------------------------------

# Se obtiene el beneficio de los articulos en la mochila
def get_Beneficio(articulos:list[Articulo]):
    beneficio = 0
    for articulo in articulos:
        beneficio += articulo.beneficio
    return beneficio
# -----------------------------------------------------------------------------------------------


# Se agregar los articulos en la mochila, siempre y cuando la machila tenga el espacio correspondiente
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
    #se crear los objetos Articulos con sus atributos
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

    # se crea la matriz para realizar la tabla
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

    #Se imprimen los resultados requeridos
    end = time.time()
    print(f'Beneficio máximo: {beneficioMaximo}')
    print(f'Incluidos: {", ".join([str(elemento) for elemento in elementos])}')
    print(f'Tiempo de ejecución: {end-start} segundos')


# Se encarga de crear correctamente la matriz con sus resulatdos
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

"""
La funcion se encarga de devolver los articulos que se tienen para calcular el maximo beneficio
"""
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
