from geometry import Point, Rectangle, Circle
import plot

p1 = (-4.5, 5.5)
p2 = (8, -7)
c1 = (0, 0, 2)

r1 = Rectangle(Point(*p1), Point(*p2))

print(f'Circle included: {r1.verify_circle_inclusion(Circle(*c1))}')

plot.m_plot(r1, c1)
