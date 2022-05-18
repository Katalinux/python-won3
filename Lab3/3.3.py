lst = [20, 7.9, 1, 2.1, 3, 4.9, 5, 6.3, 100, -15]

print('Min:', min(lst))
print('Max:', max(lst), '\n')

mn, mx = lst[0], lst[0]

for e in range(len(lst)):
    if lst[e] > mx:
        mx = lst[e]
    if lst[e] < mn:
        mn = lst[e]

print('Min:', mn, 'Max:', mx)
