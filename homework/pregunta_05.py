"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor máximo y mínimo de la columna 2
    por cada letra de la columna 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """

    data = {}

    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            letter = columns[0]
            value = int(columns[1])

            if letter not in data:
                data[letter] = []
            data[letter].append(value)

    result = []
    for letter in sorted(data.keys()):
        max_value = max(data[letter])
        min_value = min(data[letter])
        result.append((letter, max_value, min_value))

    return result
