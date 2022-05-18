d = {
    'Popescu Ion': (2, 5, 7),
    'Ionescu Geta': (10, 7, 9, 7),
    'Georgescu Gelu': (4, 2),
    'Radulescu Ioana': (5, 9, 6, 4, 10),
    'Ionescu Temistocle': (2, 9, 4, 10),
    'Popescu Electra': (2, 5, 3),
    'Bengescu Hortensia': (1,),
    'Popescu Sandokan': (7, 6, 7), }

print('Mediile elevilor:\n')


def media(md):
    if len(md) > 0:
        return sum(md) / len(md)
    return 0


for k, v in d.items():
    x = media(v)
    print(k + ':', "{:.2f}".format(x))
