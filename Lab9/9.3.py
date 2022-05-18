l1 =[2, 3, 1]
l2 = [1, 4, 5]
l3 = ['A', 'q', '#']

print(list(map(lambda x, y, z: (x + y) * z, l1, l2, l3)))
