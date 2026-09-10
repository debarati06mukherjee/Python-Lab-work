import math

class Shape:

    def __init__(self, radius):
        self.radius = radius


class Circle(Shape):

    def area(self):
        return math.pi * self.radius * self.radius


class Sphere(Shape):

    def volume(self):
        return (4 / 3) * math.pi * self.radius * self.radius * self.radius


# Creating objects
c = Circle(5)
s = Sphere(5)

print("Area of Circle:", c.area())
print("Volume of Sphere:", s.volume())