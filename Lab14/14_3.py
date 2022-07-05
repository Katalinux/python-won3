from geometry import Point, Polyline
from plot import p_poly

a = Polyline(Point(-13, 2), Point(-5, 7), Point(4, 3), Point(4, -6), Point(8, -4))

print(a)
p_poly(a)
