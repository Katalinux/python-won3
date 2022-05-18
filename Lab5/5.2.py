catalog = {'Popescu Ion': [2, 5, 7],
           'Ionescu Geta': [10, 7, 9, 7],
           'Georgescu Gelu': [4, 2],
           'Coco Rosi': [],
           'Radulescu Ioana': [5, 9, 6, 4, 10],
           }


def add_grade(elev, nota, overwrite=False):
    if overwrite:
        catalog[elev] = [nota]
    else:
        catalog[elev].append(nota)


order, elevi = 1, {}
print('Lista elevi:')
for e in catalog.keys():
    print(order, e)
    elevi[order] = e
    order += 1

while True:
    el = int(input('\nSelectati elevul [1-' + str(len(catalog)) + ']:'))
    if el in range(1, len(catalog) + 1):
        el = elevi[el]
        break
    print('Elevul nu este in catalog!')

while True:
    n = int(input('Introduceti nota pt elevul ' + el + ' [0-10]:'))
    if 0 <= n <= 10:
        break
    print('Nota de la 0 la 10!')

while True:
    o = input('Notele se suprascriu? [d/n]:')
    if o in 'dn':
        break

add_grade(el, n, True if o == 'd' else False)

print('\nNotele elevului', el, 'sunt:', catalog[el])
