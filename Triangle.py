import math


class Triangle:
    def __init__(self, side1, side2, side3, angle1, angle2, angle3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3


class EquilateralTriangle(Triangle):

    def calarea(self):
        area = (math.sqrt(3) / 4) * self.side1 ** 2
        print("Area of Equilateral Triangle:", round(area))

    def findangle(self):
        tan1 = math.tan(math.radians(self.angle1))
        tan2 = math.tan(math.radians(self.angle2))
        tan3 = math.tan(math.radians(self.angle3))

        print("Tangent of Angle 1:", tan1)
        print("Tangent of Angle 2:", tan2)
        print("Tangent of Angle 3:", tan3)


class Scalene(Triangle):

    def calperimetry(self):
        perimeter = self.side1 + self.side2 + self.side3
        print("Perimeter of Scalene Triangle:", perimeter)

    def calarea(self):
        s = (self.side1 + self.side2 + self.side3) / 2

        area = math.sqrt(
            s * (s - self.side1) *
            (s - self.side2) *
            (s - self.side3)
        )

        print("Area of Scalene Triangle:", round(area))


# Equilateral Triangle
t1 = EquilateralTriangle(6, 6, 6, 60, 60, 60)

t1.calarea()
t1.findangle()


# Scalene Triangle
t2 = Scalene(3, 4, 5, 90, 53.13, 36.87)

t2.calperimetry()
t2.calarea()