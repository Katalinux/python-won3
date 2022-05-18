def media(lst_note: list) -> float:
    if len(lst_note) > 0:
        return sum(lst_note) / len(lst_note)
    return 0


def show_details(cat: dict):
    with open('rezultate.txt', 'w', encoding='UTF-8') as rez:
        print('{:<20}'.format('Nume'), '{:<20}'.format('Prenume'), '{:>5}'.format('Media'), '{:^5}'.format('Note'),
              file=rez)
        print('-' * 53, file=rez)
        for k, v in cat.items():
            print(f'{str(k).split()[0] :<20} {str(k).split()[1] :<20} {media(v):>5.2f} {len(v):^5}', file=rez)


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
