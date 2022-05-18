def media(lst_note: list) -> float:
    if len(lst_note) > 0:
        return sum(lst_note) / len(lst_note)
    return 0


def calcul_media(cat: dict) -> list:
    cat_media = {}
    for elev, nota in cat.items():
        cat_media[elev] = media(nota)
    return sorted(cat_media.items(), key=lambda v: v[1], reverse=True)


def find_len(lst: list):
    ln = 4
    for tp in lst:
        if len(tp[0]) > ln:
            ln = len(tp[0])
    return ln


def gen_prem(cat: list):
    ln_max = find_len(cat)
    hdr = ('Premiul', 'Elev', 'Media')
    hdr_line = (len(hdr[0]) + ln_max + len(hdr[2]) + 2) * '-'
    with open('premianti.txt', 'w') as prem:
        print(f'{hdr[0]:<{len(hdr[0])}} {hdr[1]:^{ln_max}} {hdr[2]:>{len(hdr[2])}}', file=prem)
        print(hdr_line, file=prem)
        for i in range(3):
            print(f'{i + 1:<{len(hdr[0])}} {cat[i][0]:<{ln_max}} {cat[i][1]:>5.2f}', file=prem)


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


catalog_note = read_data('note.txt')
ordered_cat = calcul_media(catalog_note)
print(ordered_cat)
gen_prem(ordered_cat)
