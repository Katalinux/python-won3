from geometry import Point, Rectangle
import plot

p1x, p1y = 7, -7
p2x, p2y = -7, 7

r1 = Rectangle(Point(p1x, p1y), Point(p2x, p2y))

if __name__ == '__main__':
    print(f'\nSide x: {r1.metrics()[0]}')
    print(f'Side y: {r1.metrics()[1]}')
    print(f'Area: {r1.d_area()}')
    print(f'Perimeter: {r1.d_perimeter()}')
    plot.m_plot(r1)
