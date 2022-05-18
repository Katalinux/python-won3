catalog = {'Popescu Ion': [2, 5, 7],
           'Ionescu Geta': [10, 7, 9, 7],
           'Georgescu Gelu': [4, 2],
           'Radulescu Ioana': [5, 9, 6, 4, 10]
           }


def del_grade(elev, nota=None):
    if elev not in catalog:
        print('Eroare: Elevul', elev, 'nu exista in catalog!')
    else:
        for k, v in catalog.items():
            if k == elev:
                if nota in v:
                    v.remove(nota)
                elif not nota:
                    catalog[k] = []


del_grade('Popescu Ion', 5)

print(catalog)
