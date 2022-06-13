from geometry import Point

cx = float(input('Introdu valoarea coordonatei x: '))
cy = float(input('Introdu valoarea coordonatei y: '))

p1 = Point(cx, cy)

print(p1.get_distance())
