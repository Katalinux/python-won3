from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self):
        return round(sqrt(self.x ** 2 + self.y ** 2), 2)


cx = float(input('Introdu valoarea coordonatei x: '))
cy = float(input('Introdu valoarea coordonatei y: '))

p1 = Point(cx, cy)

print(p1.get_distance())
