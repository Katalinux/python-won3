catalog = {'Popescu Ion': [2, 5, 7],
           'Ionescu Geta': [10, 7, 9, 7],
           'Georgescu Gelu': [4, 2],
           'Radulescu Ioana': [5, 9, 6, 4, 10]
           }


def add_grade(elev, nota):
    if 10 < nota < 0:
        print('Eroare: Introduceti note de la 0 la 10')
    elif elev not in catalog:
        print('Eroare: Elevul', elev, 'nu exista in catalog!')
    else:
        for k, v in catalog.items():
            if k == elev:
                v.append(nota)


add_grade('Popescu Ion', 10)

print(catalog)
