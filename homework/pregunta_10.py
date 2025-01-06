"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    with open("files/input/data.csv", "r") as file:
        data = []

        for line in file:
            columns = line.strip().split("\t")
            letter = columns[0]
            el4 = columns[3].strip().split(",")
            el5 = columns[4].strip().split(",")
            data.append((letter, len(el4), len(el5)))
        return data