from geometry import Point, Circle


p1 = Point(4, 8.5)
p2 = Point(3, 4)
p3 = Point(-5, 6)

c1 = Circle(3, 3, 4)
c2 = Circle(4, -5, 10)
c3 = Circle(5, 6, 3)

lst = [p1, p2, p3, c1, c2, c3]

sort = sorted(lst, key=lambda x: x.get_distance())


for item in lst:
    print(f'Original: {item.get_distance()}')

for item in sort:
    print(f'Sorted: {item.get_distance()}')
