d = {
    'Popescu Ion': (2, 5, 7),
    'Ionescu Geta': (10, 7, 9, 7),
    'Georgescu Gelu': (4, 2),
    'Radulescu Ioana': (5, 9, 6, 4, 10),
    'Ionescu Temistocle': (2, 9, 4, 10),
    'Popescu Electra': (2, 5, 3),
    'Bengescu Hortensia': (9,),
    'Popescu Sandokan': (7, 6, 7), }


print('Nume\tNr. ocurente\n')

dic_freq = {}

for k in d.keys():
    ln = k.split(' ')[0]
    freq = 0
    for f in d.keys():
        if ln == f.split(' ')[0]:
            freq += 1
    if ln not in dic_freq.keys():
        dic_freq[ln] = freq
        print(ln, '\t', freq)
