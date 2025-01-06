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

    data = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            letter = columns[0]
            dicts = columns[4].split(",")
            values = [int(i.split(":")[1]) for i in dicts]

            if letter not in data:
                data[letter] = sum(values)
                continue
            data[letter] += sum(values)

    sorted_dict = {key: data[key] for key in sorted(data)}
    return sorted_dict