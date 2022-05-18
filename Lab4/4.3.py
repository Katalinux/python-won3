d = {
    'Popescu Ion': (2, 5, 7),
    'Ionescu Geta': (10, 7, 9, 7),
    'Georgescu Gelu': (4, 2),
    'Radulescu Ioana': (5, 9, 6, 4, 10),
    'Ionescu Temistocle': (2, 9, 4, 10),
    'Popescu Electra': (2, 5, 3),
    'Bengescu Hortensia': (9,),
    'Popa Andri': (9,),
    'Popescu Sandokan': (7, 6, 7), }

print('\nLista elevi in functie de medie:\n')

media_lst = []
md_dict = dict()
for k, v in d.items():
    media = 0
    for m in v:
        media += m
    media /= len(v)
    md_dict[k] = media
    media_lst.append(media)

media_lst.sort(reverse=True)

w = []

for i in media_lst:
    for k, v in md_dict.items():
        if i == v:
            if {k: v} not in w:
                w.append({k: v})
                print(k + ':', '{:.2f}'.format(v))
