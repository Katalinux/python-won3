def media(lst_note: list) -> float:
    if len(lst_note) > 0:
        return sum(lst_note) / len(lst_note)
    return 0


def cust_sort(dic: dict, value: int = 0, rev=False) -> list:
    """:param dic dictionary
       :param rev reversed order -> bool
       :param value order by 0 -> 1st elem, 1 -> 2nd elem   """
    srt = []
    if value == 0:
        for k, v in dic.items():
            srt.append((k, v))
        return sorted(srt, reverse=rev)
    elif value == 1:
        for k, v in dic.items():
            srt.append((v, k))
        tmp = sorted(srt, reverse=rev)
        srt.clear()
        for item in tmp:
            srt.append((item[1], item[0]))
        return srt


def find_len(lst: list) -> int:
    ln = 9
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


def write_file(cat: list, file_name: str):
    ln_max = find_len(cat)
    hdr = ('Nume Elev', 'Media Generala')
    hdr_line = (ln_max + len(hdr[1]) + 1) * '-'
    with open(file_name, 'w') as mg:
        print(hdr_line, file=mg)
        print(f'{hdr[0]:<{ln_max}} {hdr[1]:>{len(hdr[1])}}', file=mg)
        print(hdr_line, file=mg)
        for i in cat:
            print(f'{i[0]:<{ln_max}} {i[1]:>{len(hdr[1])}.2f}', file=mg)
        print(hdr_line, file=mg)


def media_gen(cat: dict[str, list[int]]) -> dict:
    cat_media = {}
    for elev, nota in cat.items():
        teza = nota.pop()
        note = []
        if len(nota) <= 3:
            note = nota
        else:
            for _ in range(3):
                note.append(max(nota))
                nota.remove(max(nota))
        cat_media[elev] = media([media(note), teza])
    return cat_media


def prem_cor(cat: list) -> tuple:
    pm, cr, cnt = [], [], 0
    for el in cat:
        if cnt <= 2 and el[1] > 5:
            pm.append(cat[cnt])
        if el[1] < 5:
            cr.append(el)
        cnt += 1
    return pm, cr


cat_note = read_data('note.txt')
cat_teze = read_data('teze.txt')
cat_all = merge_cat(cat_note, cat_teze)

cat_media_gen = media_gen(cat_all)

name_sorted = cust_sort(cat_media_gen)
note_sorted = cust_sort(cat_media_gen, 1, True)
prm, cor = prem_cor(note_sorted)

write_file(name_sorted, 'media_gen.txt')
write_file(prm, 'premianti.txt')
write_file(cor, 'corigenti.txt')
