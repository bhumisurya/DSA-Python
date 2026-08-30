class Shape:
    def Area(self):
        print("Area")

class Rectangle(Shape):
    def Area2(self):
        print("Area of Rectangle")

a = Rectangle()
a.Area()
a.Area2()
