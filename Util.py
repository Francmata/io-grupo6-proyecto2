# Función que abre el archivo para obtener la información de los archvos.
def abrir_Archivo(file_name:str):
    archivo = open(file_name, 'r')
    Lineas = archivo.readlines()
    i = 0
    while(i < len(Lineas)):
        Lineas[i] = [int(e) if e.strip().isdigit() else e.strip() for e in Lineas[i].split(',')]
        i += 1
    return Lineas

#region Combinaciones
# -----------------------------------------------------------------------------------------------
def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]
# -----------------------------------------------------------------------------------------------
def imprime_ordenado(c):
    """Imprime en la salida estándar todos los
       subconjuntos del conjunto c (una lista de
       listas) ordenados primero por tamaño y
       luego lexicográficamente. Cada subconjunto
       se imprime en su propia línea. Los
       elementos de los subconjuntos deben ser
       comparables entre sí, de otra forma puede
       ocurrir un TypeError.
    """
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)
# -----------------------------------------------------------------------------------------------
def combinaciones(c, n):
    """Calcula y devuelve una lista con todas las
       combinaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return [s for s in potencia(c) if len(s) == n]
# -----------------------------------------------------------------------------------------------
def get_Lista_Combinaciones(lista:list):    
    listaCombinaciones = []
    for index in range(1,len(lista)+1):
        listaCombinaciones += combinaciones(lista, index)
    return listaCombinaciones
# -----------------------------------------------------------------------------------------------
#endregion Combinaciones


#region Permutaciones
# -----------------------------------------------------------------------------------------------
def inserta(x, lst, i):
    """Devuelve una nueva lista resultado de insertar
       x dentro de lst en la posición i.
    """
    return lst[:i] + [x] + lst[i:]

def inserta_multiple(x, lst):
    """Devuelve una lista con el resultado de
       insertar x en todas las posiciones de lst.  
    """
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]

def permuta(c):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c.
    """
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s)
                for s in permuta(c[1:])],
               [])

def permutaciones(c, n):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return sum([permuta(s)
                for s in combinaciones(c, n)],
               [])

from math import factorial
def numero_permutaciones(m, n):
    """Calcula y devuelve el número de permutaciones
       posibles que se pueden hacer con m elementos
       tomando n elementos a la vez.
    """
    return factorial(m) // factorial(m - n)

def get_Lista_Permutaciones(lista:list):    
    listaPermutaciones = []
    for index in range(1,len(lista)+1):
        listaPermutaciones += combinaciones(lista, index)
    return listaPermutaciones
# -----------------------------------------------------------------------------------------------
#endregion Permutaciones


#lista = [1, 3, 2] #,'nuez', 'vainilla'
#print(permutaciones(lista, len(lista))) 

# 1,2,3 -> 2,3,1 -> 3,1,2
"""
list=[1,2,4,4]
stack=[]
resultado = []
perm(list,stack,resultado)
print(resultado)
"""