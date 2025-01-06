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
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()

    key_counts = {}

    for line in lines:
        columns = line.strip().split('\t')
        entries = columns[4].split(',')
        for entry in entries:
            key = entry.split(':')[0]
            if key in key_counts:
                key_counts[key] += 1
            else:
                key_counts[key] = 1

    sorted_dict = {key: key_counts[key] for key in sorted(key_counts)}
    return sorted_dict