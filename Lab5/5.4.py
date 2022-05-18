catalog = {'Popescu Ion': [2, 5, 7],
           'Ionescu Geta': [10, 7, 9, 7],
           'Georgescu Gelu': [4, 2],
           'Radulescu Ioana': [5, 9, 6, 4, 10]
           }


def media(md):
    if len(md) > 0:
        return sum(md) / len(md)
    return 0


def media_gen(ctg):
    averages = []
    for v in ctg.values():
        if len(v) > 0:
            averages.append(media(v))
    print('Media generala a clasei:', "{:.2f}".format(media(averages)))


media_gen(catalog)


