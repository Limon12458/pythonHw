class Rectangle:

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def calculate_area(self):

        return self.length * self.width

rect = Rectangle(15, 8)

area = rect.calculate_area()
print(f"The area of the rectangle is {area}.")
