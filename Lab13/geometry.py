from math import sqrt, pi


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self):
        """Get distance from origin to Point"""
        return round(sqrt(self.x ** 2 + self.y ** 2), 2)


class Circle(Point):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def get_area(self):
        """Area of the circle"""
        return round(pi * self.r ** 2, 2)

    def get_distance(self):
        """Get the distance from the origin to the edge of the circle"""
        return round(super().get_distance() - self.r, 2)


class Rectangle:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __eq__(self, other):
        return sorted(self.metrics()) == sorted(other.metrics())

    def metrics(self):
        """Returns the sides of the rectangle"""
        return [abs(self.p1.x - self.p2.x), abs(self.p1.y - self.p2.y)]

    def d_area(self):
        """Returns the area of the rectangle"""
        return round(self.metrics()[0] * self.metrics()[1], 2)

    def d_perimeter(self):
        """Returns the perimeter of the rectangle"""
        return (self.metrics()[0] + self.metrics()[1]) * 2

    def verify_point_inclusion(self, pct: Point):
        """Verify if a point is included in a rectangle"""
        if self.p1.x > self.p2.x:
            p1x, p2x = self.p2.x, self.p1.x
        else:
            p1x, p2x = self.p1.x, self.p2.x

        if self.p1.y > self.p2.y:
            p1y, p2y = self.p2.y, self.p1.y
        else:
            p1y, p2y = self.p1.y, self.p2.y
        if (p1x <= pct.x <= p2x) and (p1y <= pct.y <= p2y):
            return True
        return False

    def verify_circle_inclusion(self, c1: Circle):
        """Verify if a circle is included in a rectangle"""
        return self.verify_point_inclusion(Point(c1.x - c1.r, c1.y)) and \
            self.verify_point_inclusion(Point(c1.x + c1.r, c1.y)) and \
            self.verify_point_inclusion(Point(c1.x, c1.y - c1.r)) and \
            self.verify_point_inclusion(Point(c1.x, c1.y + c1.r))

