from math import sqrt, pi


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self):
        return round(sqrt(self.x ** 2 + self.y ** 2), 2)


class Circle(Point):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def get_area(self):
        return round(pi * self.r ** 2, 2)

    def get_distance(self):
        return round(super().get_distance() - self.r, 2)
