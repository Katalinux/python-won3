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


def find_len(x):
    ln_num, ln_pren = 4, 7
    for item in x:
        if len(item.split()[0]) > ln_num:
            ln_num = len(item.split()[0])
        if len(item.split()[1]) > ln_pren:
            ln_pren = len(item.split()[1])
    return ln_num, ln_pren


def show_details(cat: dict):
    ln_num, ln_pren = find_len(catalog.keys())
    hdr, hdr_line = ('Nume', 'Prenume', 'Media', 'Note'), '|' + '-' * (ln_num + ln_pren + 14) + '|'
    print(hdr_line)
    print(f'| {hdr[0]:<{ln_num}} {hdr[1]:<{ln_pren}} {hdr[2]:>5} {hdr[3]:^5}|')
    print(hdr_line)
    for k, v in sorted(cat.items()):
        print(f'| {k.split()[0] :<{ln_num}} {k.split()[1]:<{ln_pren}} {media(v):>5.2f} {len(v):^5}|')
    print(hdr_line)


show_details(catalog)
