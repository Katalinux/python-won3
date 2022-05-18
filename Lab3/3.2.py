lst = ['ABCD', '12', 'w', ':-)']
mirror = []
# Varianta 1
for e in lst:
    elem = e[-1:-len(e)-1:-1]
    mirror.insert(0, elem)

print(mirror)

# Varianta 2
mirror = []
for e in lst:
    elem = e[-1:-len(e)-1:-1]
    mirror.append(elem)

mirror.reverse()
print(mirror)

