catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10],
    'X-ulescu Gigi': []
}


def media(note: list):
    if len(note) > 0:
        return sum(note) / len(note)
    return 0


def show_details(cat: dict):
    print('{:<50}'.format('Elev'), '{:>5}'.format('Media'))
    print('-' * 56)
    for k, v in cat.items():
        print(f'{k:<50} {media(v):>5.2f}')


show_details(catalog)
