def media(lst_note: list) -> float:
    if len(lst_note) > 0:
        return sum(lst_note) / len(lst_note)
    return 0


def ord_dict(cat: dict, sort: int = 0, reverse: bool = False) -> list:
    return sorted(cat.items(), key=lambda v: v[sort], reverse=reverse)


def find_len(lst: list) -> int:
    ln = 4
    for tp in lst:
        if len(tp[0]) > ln:
            ln = len(tp[0])
    return ln


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


def merge_cat(note: dict, teze: dict) -> dict:
    merged = {}
    for elev in note.keys():
        merged[elev] = note[elev] + teze[elev]
    return merged


def media_gen(cat: dict) -> dict:
    cat_media = {}
    for elev, nota in cat.items():
        teza = nota.pop()
        cat_media[elev] = media([media(nota), teza])
    return cat_media


def write_file(cat: list):
    ln_max = find_len(cat)
    hdr = ('Nume Elev', 'Media Generala')
    hdr_line = (ln_max + len(hdr[1]) + 1) * '-'
    with open('media_gen.txt', 'w') as mg:
        print(f'{hdr[0]:<{ln_max}} {hdr[1]:>{len(hdr[1])}}', file=mg)
        print(hdr_line, file=mg)
        for i in cat:
            print(f'{i[0]:<{ln_max}} {i[1]:>{len(hdr[1])}.2f}', file=mg)


cat_note = read_data('note.txt')
cat_teze = read_data('teze.txt')
cat_full = merge_cat(cat_note, cat_teze)

ordered_cat_full = ord_dict(media_gen(cat_full))
write_file(ordered_cat_full)

