"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    """
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        lineas = f.readlines()

    conteo = {}

    for linea in lineas:
        columnas = linea.strip().split("\t")
        # La columna 5 es la que contiene los pares clave:valor
        diccionario_str = columnas[4]
        # Separa cada par "clave:valor"
        pares = diccionario_str.split(",")
        # Para evitar contar la misma clave más de una vez por registro,
        # usamos un conjunto
        claves_registro = set()
        for par in pares:
            clave, _ = par.split(":")
            claves_registro.add(clave)
        # Actualiza el conteo de cada clave encontrada en este registro
        for clave in claves_registro:
            if clave not in conteo:
                conteo[clave] = 0
            conteo[clave] += 1

    return conteo
