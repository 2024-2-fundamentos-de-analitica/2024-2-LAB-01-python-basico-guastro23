"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        lineas = f.readlines()

    suma_por_letra = {}

    for linea in lineas:
        columnas = linea.strip().split("\t")
        # La columna 2 es la segunda columna (índice 1)
        valor = int(columnas[1])
        # La columna 4 es la cuarta columna (índice 3) con letras separadas por coma
        letras = columnas[3].split(",")
        for letra in letras:
            if letra not in suma_por_letra:
                suma_por_letra[letra] = 0
            suma_por_letra[letra] += valor

    # Ordenamos el diccionario por la clave de forma alfabética
    resultado = {letra: suma_por_letra[letra] for letra in sorted(suma_por_letra)}
    
    return resultado
