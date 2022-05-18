def media(lst_note: list) -> float:
    if len(lst_note) > 0:
        return sum(lst_note) / len(lst_note)
    return 0


def show_details(cat: dict):
    el, med = 'Elev', 'Media'
    print(f'{el:<25} {med:>5}')
    print('-' * 31)
    for k, v in cat.items():
        print(f'{k:<25} {media(v):>5.2f}')


def read_data(file_name: str) -> dict:
    with open(file_name, 'r') as note:
        catalog = {}
        for line in note:
            raw_lst = line.strip().split(';')
            key = raw_lst.pop(0)
            note_lst = []
            for item in raw_lst:
                note_lst.append(int(item))
            catalog[key] = note_lst
        return catalog


show_details(read_data('note.txt'))
