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
    print('|' + '-' * 63 + '|')
    print('|{:<25}'.format('Nume'), '{:<25}'.format('Prenume'), '{:>5}'.format('Media'), '{:^5}'.format('Note') + '|')
    print('|' + '-' * 63 + '|')
    for k, v in cat.items():
        print(f'|{str(k).split()[0] :<25} {str(k).split()[1] :<25} {media(v):>5.2f} {len(v):^5}|')
    print('|' + '-' * 63 + '|')


show_details(catalog)
