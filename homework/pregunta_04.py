"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    """
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        lineas = f.readlines()

    conteo_meses = {}

    for linea in lineas:
        columnas = linea.strip().split("\t")
        # Extrae la fecha en formato YYYY-MM-DD (columna 3, índice 2)
        fecha = columnas[2]
        # Extrae el mes, ya que el mes está en los caracteres 6 y 7
        mes = fecha[5:7]
        
        if mes not in conteo_meses:
            conteo_meses[mes] = 0
        conteo_meses[mes] += 1

    # Ordena alfabéticamente por el mes (siendo cadenas '01', '02', etc.)
    resultado = sorted(conteo_meses.items(), key=lambda x: x[0])
    
    return resultado

