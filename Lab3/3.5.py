s = 'În livada noastra avem ciresi, meri, peri și pruni. Care fructe credeti ca se coc primele?' \
    ' Variante: perele, merele, prunele și apoi ciresele. Foarte gresit!' \
    ' Corect este: ciresele, merele, perele și apoi prunele.'

raw_lst = s.split(' ')
cuv_lst = []
for e in raw_lst:
    if e.lower().strip('!?:., ') not in cuv_lst:
        cuv_lst.append(e.lower().strip('!?:.,'))
print('Lista initiala:', '\n', cuv_lst)


# Varianta 1
cuv_lst.sort()
print('Varianta 1\n', cuv_lst)

# Varianta 2
cuv_lst = []
for e in raw_lst:
    if e.lower().strip('!?:., ') not in cuv_lst:
        cuv_lst.append(e.lower().strip('!?:.,'))
srt = []

while len(cuv_lst) > 0:
    mn = min(cuv_lst)
    for i, e in enumerate(cuv_lst):
        if e == mn:
            srt.append(cuv_lst.pop(i))
print('Varianta 2\n', srt)

# Varianta 3
cuv_lst = []
for e in raw_lst:
    if e.lower().strip('!?:., ') not in cuv_lst:
        cuv_lst.append(e.lower().strip('!?:.,'))

srt = [cuv_lst.pop(0)]

while len(cuv_lst) > 0:
    tmp = cuv_lst.pop(0)
    for i, e in enumerate(srt):
        if tmp < e:
            srt.insert(i, tmp)
            break
    else:
        srt.append(tmp)
print('Varianta 3\n', srt)




