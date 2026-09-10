import math

class Triangle:

    def __init__(self, side):
        self.side = side

    def area(self):
        return (math.sqrt(3) / 4) * self.side * self.side

    def angles(self):
        print("Angle 1:", 60)
        print("Angle 2:", 60)
        print("Angle 3:", 60)

        print("Tan of Angle 1:", math.tan(math.radians(60)))
        print("Tan of Angle 2:", math.tan(math.radians(60)))
        print("Tan of Angle 3:", math.tan(math.radians(60)))


t = Triangle(5)

print("Area of Equilateral Triangle:", t.area())
t.angles()