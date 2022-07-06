from math import sqrt, pi


class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Segment(self, other)

    def __str__(self):
        return f'Point({self.x}, {self.y})'

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


class Segment:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'Segment(Point({self.p1}, Point({self.p2})'


class Rectangle:

    instances, square_instances = 0, 0

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

        Rectangle.instances += 1
        k = self.metrics()
        if k[0] == k[1]:
            Rectangle.square_instances += 1

    def __eq__(self, other):
        return sorted(self.metrics()) == sorted(other.metrics())

    def __str__(self):
        return f'Rectangle({self.p1}, {self.p2})'

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

    def is_square(self):
        a = self.metrics()
        return a[0] == a[1]

    @staticmethod
    def get_square_percent():
        """Returns percentage of squares in all rectangles"""
        try:
            return round((Rectangle.square_instances * 100) / Rectangle.instances, 1)
        except ZeroDivisionError:
            return 0


class WrongGeometry(BaseException):
    pass


class Polyline:

    def __init__(self, *pts: Point):
        for cnt, v_type in enumerate(pts):
            if type(v_type) is not Point:
                raise WrongGeometry(f'parameter on pos {cnt} ({v_type}) is {type(v_type)}, expected <class Point>.')
            if len(pts) < 2:
                raise WrongGeometry('At least 2 parameters must be given')
        self.pts = pts

    def __str__(self):
        b = 'Polyline('
        for v in self.pts:
            b += f'{v}, '
        return b.rstrip(', ') + ')'
