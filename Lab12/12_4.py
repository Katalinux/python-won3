from geometry import Point
from math import pi


class Circle(Point):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def get_area(self):
        return round(pi * self.r ** 2, 2)

    def get_distance(self):
        return round(super().get_distance() - self.r, 2)


cx = float(input('Coordonata x: '))
cy = float(input('Coordonata y: '))
cr = float(input('Raza: '))

c1 = Circle(cx, cy, cr)

print(f'\nAria cercului este: {c1.get_area()}')
print(f'Distanta de la cerc la origine: {c1.get_distance()}')

