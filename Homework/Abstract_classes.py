import math


class Figure:

    def perimeter(self):
        return NotImplementedError

    def area(self):
        return NotImplementedError


class Triangle(Figure):

    def __init__(self, a_side, b_side, c_side, size):
        """
        :param a_side: a side of triangle -> int|float
        :param b_side: b side of triangle -> int|float
        :param c_side: c side of triangle -> int|float
        :param size: size of triangle -> str
        """
        if isinstance(a_side, int | float) and isinstance(b_side, int | float) \
                and isinstance(c_side, int | float) and isinstance(size, str):
            self.a_side = a_side
            self.b_side = b_side
            self.c_side = c_side
            self.size = size
        else:
            raise ValueError('Sides must be a number and size must be a sting')

    def perimeter(self):
        return f'Perimeter of triangel: {round(self.a_side + self.b_side + self.c_side, 2)} {self.size}'

    def area(self):
        p = (self.a_side + self.b_side + self.c_side) / 2
        return f'Area of triangle:' \
               f' {round(math.sqrt(p * (p - self.a_side) * (p - self.b_side) * (p - self.c_side)), 2)} {self.size}^2'


class Circle(Figure):

    def __init__(self, radius, size):
        """
        :param radius: a side of circle -> int|float
        :param size: size of circle -> str
        """
        if isinstance(radius, int | float):
            self.radius = radius
            self.size = size
        else:
            raise ValueError('The radius must be a number and size must be a sting')

    def perimeter(self):
        return f'Perimeter of circle: {round(2 * self.radius * math.pi, 2)} {self.size}'

    def area(self):
        return f'Area of circle: {round(self.radius * math.pi ** 2, 2)} {self.size}^2'


class Rectangle(Figure):

    def __init__(self, a_side, b_side, size):
        """
        :param a_side: a side of rectangle -> int|float
        :param b_side: b side of rectangle -> int|float
        :param size: size of rectangle -> str
        """
        if isinstance(a_side, int | float) and isinstance(b_side, int | float) and isinstance(size, str):
            self.a_side = a_side
            self.b_side = b_side
            self.size = size
        else:
            raise ValueError('Sides must be a number and size must be a sting')

    def perimeter(self):
        sum_of_side=self.a_side + self.b_side
        return f'Perimeter of rectangle: {round((sum_of_side * 2), 2)} {self.size}'

    def area(self):

        return f'Area of rectangle: {round((self.a_side * self.b_side), 2)} {self.size}^2'


def figure(obj):
    return obj


print(figure(Triangle(2, 3, 4, 'cm')).perimeter())
print(figure(Triangle(2, 3, 4, 'm')).area())
print('*' * 8)
print(figure(Circle(5, 'm')).perimeter())
print(figure(Circle(5, 'cm')).area())
print('*' * 8)
print(figure(Rectangle(5, 10, 'm')).perimeter())
print(figure(Rectangle(5, 10, 'cm')).area())
