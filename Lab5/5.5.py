catalog = {'Popescu Ion': {'m': [2, 5, 7],
                           'f': [],
                           'r': [6, 9, 8]},
           'Ionescu Geta': {'r': [6, 3, 8],
                            'm': [4, 5],
                            'f': [7, 9, 10]},
           'Georgescu Gelu': {'m': [2, 5, 7, 9],
                              'r': [9, 8],
                              'f': [6, 9]},
           'Radulescu Ioana': {'m': [7],
                               'f': [],
                               'r': [6, 9, 8]},
           }


def media(md):
    if len(md) > 0:
        return sum(md) / len(md)
    return 0


def translate(m):
    if m == 'r':
        return 'Romana'
    elif m == 'm':
        return 'Matematica'
    elif m == 'f':
        return 'Fizica'


def details(elev, materia=None):
    if elev not in catalog.keys():
        print(elev, 'nu exista in catalog!')
    else:
        if not materia:
            print('Elevul', elev, 'are urmatoarele medii:')
        elif materia not in 'mfr':
            print('Materia nu exista!')
        for x, y in catalog[elev].items():
            if not materia:
                print(translate(x), ':', "{:.2f}".format(media(y)))
            elif x == materia and materia in 'mfr':
                print('Elevul', elev, 'are media la', translate(materia), "{:.2f}".format(media(y)))


details('Popescu Ion', 'r')


