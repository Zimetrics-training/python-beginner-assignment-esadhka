"""
Problem Description:

Create a Rectangle class that has the following methods:

1. __init__(self, width, height): Initializes a rectangle with given width and height.
2. area(self): Returns the area of the rectangle.
3. perimeter(self): Returns the perimeter of the rectangle.
4. is_square(self): Returns True if the rectangle is a square (i.e., width == height), otherwise returns False.
"""
# rectangle.py
class Rectangle:
    def __init__(self, width, height):
        # Initialize the rectangle with width and height
        self.width = width
        self.height = height

    def area(self):
        # Return the area of the rectangle
        return self.width*self.height

    def perimeter(self):
        # Return the perimeter of the rectangle
        return 2*(self.width+self.height) + 1

    def is_square(self):
        # Return True if the rectangle is a square, otherwise False
        if self.width == self.height:
            return True
        return False
