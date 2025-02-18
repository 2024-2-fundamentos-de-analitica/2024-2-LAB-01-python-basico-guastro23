"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        lineas = f.readlines()

    # Diccionario para almacenar el máximo y mínimo de la columna 2 para cada letra
    # Usamos la estructura: { letra: [max, min] }
    stats = {}

    for linea in lineas:
        columnas = linea.strip().split("\t")
        letra = columnas[0]
        valor = int(columnas[1])
        
        if letra not in stats:
            stats[letra] = [valor, valor]
        else:
            # Actualizamos el máximo y mínimo
            stats[letra][0] = max(stats[letra][0], valor)
            stats[letra][1] = min(stats[letra][1], valor)
    
    # Convertimos el diccionario en una lista de tuplas (letra, max, min) ordenadas alfabéticamente
    resultado = sorted([(letra, datos[0], datos[1]) for letra, datos in stats.items()], key=lambda x: x[0])
    return resultado

