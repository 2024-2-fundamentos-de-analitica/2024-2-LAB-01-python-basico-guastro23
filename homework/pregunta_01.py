"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
     

     with open("files/input/data.csv", "r", encoding="utf-8") as f:
        lineas = f.readlines()

     suma = 0

     for linea in lineas:
        # Separa la línea por tabulaciones
        columnas = linea.strip().split("\t")
        # Convierte la segunda columna a entero y acumula
        suma += int(columnas[1])

     return suma

     """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
 