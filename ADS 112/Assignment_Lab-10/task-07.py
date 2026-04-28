# Write a Python class 'Rectangle' with perimeter and area methods.

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.height * self.width

rectangle1 = Rectangle(10,24)

print("Area of Rectangle:", rectangle1.area())
print("Perimeter of Rectangle:", rectangle1.perimeter())