def media(lst_note):
    """
    Average of values in the list.

    :param lst_note: List of int
    :type lst_note: list[int]
    :return: Average
    :rtype: float
    """
    if len(lst_note) > 0:
        return sum(lst_note) / len(lst_note)
    return 0


def media_gen(note, teze):
    """
    Calculeaza media generala.

    :param note: Dictionar note
    :type note: dict
    :param teze: Dictionar teze
    :type teze:dict
    :return:
    :rtype: dict
    """
    value_check = True
    for value in teze.values():
        if len(value) > 1:
            value_check = False
            break
    if not value_check:
        note, teze = teze, note

    cat_media = {}
    for elev, nota in note.items():
        cat_media[elev] = media([media(nota), teze.get(elev)[0]])
    return cat_media


def calc_media(dic):
    """
    Calculate the averages on dictionary values.
    :param dic: Dictionary
    :type dic: dict
    :return: New dictionary
    :rtype: dict
    """
    cat = {}
    for k, v in dic.items():
        cat[k] = media(v)
    return cat


def find_len(lst):
    """
    Find the longest string in tuple.
    :param lst: List of tuples
    :type lst: list
    :return:
    :rtype: int
    """
    ln = 4
    for tp in lst:
        if len(tp[0]) > ln:
            ln = len(tp[0])
    return ln


def read_data(file_name):
    """
    Read data from file.

    :param file_name: Name of the file
    :type file_name: str
    :return: Dictionary with name as key and grade as value
    :rtype: dict
    """

    with open(file_name, 'r', encoding='UTF-8') as note:
        cat = {}
        for line in note:
            raw_lst = line.strip().split(';')
            key = raw_lst.pop(0)
            note_lst = []
            for item in raw_lst:
                note_lst.append(int(item))
            cat[key] = note_lst
        return cat


def merge_cat(note, teze):
    """
    Merge values of 2 dictionaries with the same keys.

    :param note: Dictionary
    :type note: dict
    :param teze: Dictionary
    :type teze: dict
    :return: Merged dictionary
    :rtype: dict
    """
    merged = {}
    for elev in note.keys():
        merged[elev] = note[elev] + teze[elev]
    return merged


def cust_sort(dic, value=0, rev=False):
    """
    Sort after key|value.

    :param dic dictionary
    :type dic: dict
    :param value 0, order by 1st elem, 1 order by 2nd elem
    :type value: int
    :param rev reversed order -> bool
    :type rev: bool
    :return Ordered list
    :rtype: list
    """
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


def show_details(cat, file=''):
    """
    Print dictionary to file or console.
    :param cat: Dictionary
    :type cat: dict or list
    :param file: file name to print to
    :type file: str
    """

    h = ('Elev', 'Media')
    if file:
        with open(file, 'w') as fl:
            print(f'{h[0]:<25} {h[1]:>5}', file=fl)
            print('-' * 31, file=fl)
            if type(cat) == dict:
                for k, v in cat.items():
                    print(f'{k:<25} {v:>5.2f}', file=fl)
            else:
                for k in cat:
                    print(f'{k[0]:25} {k[1]:>5.2f}', file=fl)
    else:
        print(f'{h[0]:<25} {h[1]:>5}')
        print('-' * 31)
        if type(cat) == dict:
            for k, v in cat.items():
                print(f'{k:<25} {v:>5.2f}')
        else:
            for k in cat:
                print(f'{k[0]:25} {k[1]:>5.2f}')


def show_details_note(cat: dict):
    h = ['Nume', 'Prenume', 'Media', 'Note']
    with open('rezultate.txt', 'w', encoding='UTF-8') as rez:
        print(f'{h[0]:<20} {h[1]:<20} {h[2]:>5} {h[3]:^5}', file=rez)
        print('-' * 53, file=rez)
        for k, v in cat.items():
            print(f'{k.split()[0] :<20} {k.split()[1] :<20} {media(v):>5.2f} {len(v):^5}', file=rez)


def show_prem(cat):
    """
    Parameters
    ------------
    cat : list

    """

    ln_max = find_len(cat)
    h = ['Premiul', 'Elev', 'Media']
    h_line = (len(h[0]) + ln_max + len(h[2]) + 2) * '-'
    with open('premianti.txt', 'w') as prem:
        print(f'{h[0]:<{len(h[0])}} {h[1]:^{ln_max}} {h[2]:>{len(h[2])}}', file=prem)
        print(h_line, file=prem)
        for i, v in enumerate(cat, start=1):
            if i == 4:
                break
            print(f'{i:<{len(h[0])}} {v[0]:<{ln_max}} {v[1]:>5.2f}', file=prem)



