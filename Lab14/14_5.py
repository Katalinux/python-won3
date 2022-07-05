from geometry import Rectangle, Point

r1 = Rectangle(Point(1, 2), Point(-2, -2))
r2 = Rectangle(Point(5, 2), Point(-2, -2))
r3 = Rectangle(Point(2, 2), Point(-2, -2))
r4 = Rectangle(Point(2, 2), Point(-2, -2))

print(f'Rectangles: {Rectangle.instances}')
print(f'Squares: {Rectangle.square_instances}')
print(f'Square percentage: {Rectangle.get_square_percent()} %')
