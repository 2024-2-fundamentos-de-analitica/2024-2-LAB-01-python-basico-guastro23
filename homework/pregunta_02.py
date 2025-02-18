"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():

     """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
     """
     with open("files/input/data.csv", "r", encoding="utf-8") as f:
        lineas = f.readlines()

     conteo = {}
     for linea in lineas:
        # Extrae la letra de la primera columna
        columnas = linea.strip().split("\t")
        letra = columnas[0]

        # Acumula el conteo en un diccionario
        if letra not in conteo:
            conteo[letra] = 0
        conteo[letra] += 1

    # Convierte el diccionario a una lista de tuplas y ordena por la letra
     resultado = sorted(conteo.items(), key=lambda x: x[0])

     return resultado
