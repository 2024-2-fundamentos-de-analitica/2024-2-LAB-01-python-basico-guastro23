"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        lineas = f.readlines()

    suma_por_letra = {}

    for linea in lineas:
        columnas = linea.strip().split("\t")
        # La columna 1 contiene la letra
        letra = columnas[0]
        # La columna 5 contiene pares "clave:valor" separados por coma
        pares = columnas[4].split(",")
        suma_valores = 0
        for par in pares:
            _, valor = par.split(":")
            suma_valores += int(valor)
        if letra not in suma_por_letra:
            suma_por_letra[letra] = 0
        suma_por_letra[letra] += suma_valores

    return suma_por_letra

