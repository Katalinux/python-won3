def sum_tuple(tup):
    return sum(tup)


ls = ['5', '123', '-7', '33']

li = [5, 123, -7, 33]

lt = [(5, 21, 8), (6, 11, -5), (0, 25, 3), (-6, 6, 1)]

print(sorted(ls))
print(sorted(ls, key=int))
print(sorted(li))
print(sorted(lt, key=sum_tuple))

