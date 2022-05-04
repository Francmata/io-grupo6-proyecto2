# Imports
import Util
import time
import sys

#region Fuerza Bruta 
# -----------------------------------------------------------------------------------------------
def minaFuerzaBruta(datos:list):
    return
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
        minaFuerzaBruta(Lineas)
    elif sys.argv[1] == "2":
        archivo = sys.argv[2].split('.')
        Lineas = Util.abrir_Archivo(sys.argv[2])
        print(Lineas)
        #contenedorProgramacionDinamica(Lineas)