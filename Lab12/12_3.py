from geometry import Point

values = []
for i in range(1, 3):
    values.append(float(input(f'Introdu valoarea coordonatei x pentru p{i}: ')))
    values.append(float(input(f'Introdu valoarea coordonatei y pentru p{i}: ')))


p1 = Point(values.pop(0), values.pop(0))
p2 = Point(values.pop(0), values.pop(0))

d1 = p1.get_distance()
d2 = p2.get_distance()

if d1 > d2:
    print(f'\np1 [{d1}] este mai departe de centru decat p2 [{d2}]')
elif d1 < d2:
    print(f'\np2 [{d2}] este mai departe de centru decat p1 [{d1}]')
else:
    print(f'\np1 [{d1}] si p2 [{d2}] sunt la aceeasi distanta fata de centru!')
