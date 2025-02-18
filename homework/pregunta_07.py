"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
     """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]
     """
     with open("files/input/data.csv", "r", encoding="utf-8") as f:
        lineas = f.readlines()

    # Diccionario para agrupar las letras (columna 0) por el valor numérico de la columna 1
     agrupacion = {}

     for linea in lineas:
        columnas = linea.strip().split("\t")
        letra = columnas[0]
        # Se toma el valor de la columna 1 (que en el enunciado se menciona como columna 2)
        valor = int(columnas[1])
        if valor not in agrupacion:
            agrupacion[valor] = []
        agrupacion[valor].append(letra)

    # Convertir el diccionario en una lista de tuplas y ordenar por el valor numérico
     resultado = sorted(agrupacion.items(), key=lambda x: x[0])
     return resultado
