datos=[[[0, 0], [0, 1], [1, 1]], [[0, 1], [0, 2], [1, 2]], [[1, 0], [1, 1], [2, 1], [0, 1]], [[1, 1], [1, 2], [2, 2], [0, 2]], [[2, 0], [2, 1], [1, 1]], [[2, 1], [2, 2], [1, 2]]]

matriz = [[1,3,3],[2,1,4],[0,6,4]]

def iniciales(largo):
    tmp = []
    i = 0
    while i < largo:
        tmp.append([i,0])
        i+=1
    return tmp

def minaFuerzaBruta(datos:list):
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

def convertirDiccionario(Datos):
    dic = {}
    
    for dato in datos:
        dic["".join(dato[0])] = dato[1:]
    return dic


print(rutasConstruidas(datos,len(matriz)-1))
#print(obtenerRuta([[[0,0]]], 5,[],datos))