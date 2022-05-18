d = {
    'Popescu Ion': (2, 5, 7),
    'Ionescu Geta': (10, 7, 9, 7),
    'Georgescu Gelu': (4, 2),
    'Radulescu Ioana': (5, 9, 6, 4, 10),
    'Ionescu Temistocle': (2, 9, 4, 10),
    'Popescu Electra': (2, 5, 3),
    'Bengescu Hortensia': (9,),
    'Popescu Sandokan': (7, 6, 7), }

print('Elevi corigenti:\n')

crg = dict()
for k, v in d.items():
    media = 0
    for m in v:
        media += m
    media /= len(v)
    if media < 5:
        crg[k] = media
        print(k + ':', '{:.2f}'.format(media))
