from geometry import Point, Rectangle
import plot

p1 = (-4, 4)
p2 = (4, -4)
p3 = (2, -2)

r1 = Rectangle(Point(*p1), Point(*p2))

print(f'Point included: {r1.verify_point_inclusion(Point(*p3))}')

plot.m_plot(r1, (*p3, 0.1))

