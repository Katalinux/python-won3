from geometry import Rectangle, Point
import plot

r = Rectangle(Point(-5, 4), Point(5, -5))
print(r.is_square())
plot.m_plot(r)
