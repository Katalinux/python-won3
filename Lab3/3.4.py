s = 'În livada noastra avem ciresi, meri, peri și pruni. Care fructe credeti ca se coc primele?' \
    ' Variante: perele, merele, prunele și apoi ciresele. Foarte gresit!' \
    ' Corect este: ciresele, merele, perele și apoi prunele.'.rstrip('.')

print(s, '\n')

nr_prop = s.split('.')

for i, e in enumerate(nr_prop):
    if '?' in e:
        x = nr_prop.pop(i)
        x = x.split('?')
        cnt = i
        for p in x:
            nr_prop.insert(cnt, p)
            cnt += 1
for i, e in enumerate(nr_prop):
    if '!' in e:
        x = nr_prop.pop(i)
        x = x.split('!')
        cnt = i
        for p in x:
            nr_prop.insert(cnt, p)
            cnt += 1

print(nr_prop)
print('Nr. propozitii:', len(nr_prop), '\n')
raw_lst = s.split(' ')
cuv_lst = []
for e in raw_lst:
    cuv_lst.append(e.lower().strip('!?:.'))
print(cuv_lst)
print('Nr. cuvinte:', len(cuv_lst))


