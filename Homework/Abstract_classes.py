import math

class Figure:

    def perimeter(self):
        return NotImplementedError

    def area(self):
        return NotImplementedError


class Triangle(Figure):

    def __init__(self, a_side, b_side, c_side):
        """
        :param a_side: a side of triangle -> int|float
        :param b_side: b side of triangle -> int|float
        :param c_side: c side of triangle -> int|float
        """
        if isinstance(a_side,int|float) and isinstance(b_side,int|float) and isinstance(c_side,int|float):
            self.a_side = a_side
            self.b_side = b_side
            self.c_side = c_side
        else:
            raise ValueError('You should input numbers')

    def perimeter(self):
        return f'Perimeter of triangel: {self.a_side + self.b_side + self.c_side}'

    def area(self):
        p=(self.a_side + self.b_side + self.c_side)/2
        return f'Perimeter of triangel: {round(math.sqrt(p * (p - self.a_side) * (p - self.b_side) * (p - self.c_side)),2)}'


def figure(obj):
    return obj


print(figure(Triangle(2,3,4)).perimeter())
print(figure(Triangle(2,3,4)).area())