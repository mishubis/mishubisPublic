from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(14,7)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(9)

print(square_1.get_area_square())
print(square_2.get_area_square())

circle_1 = Circle(3)
circle_2 = Circle(5)

print(circle_1.get_area_circle())
print(circle_2.get_area_circle())

print('\n')

figures = [rect_1,rect_2,square_1,square_2,circle_1,circle_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circle())


