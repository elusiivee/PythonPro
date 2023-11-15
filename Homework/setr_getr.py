# #lesson task
# class Product():
#     def __init__(self, title, price, **kwargs):
#         self.title = title
#         self.price = price
#         self.__dict__.update(kwargs)
#
#     def __setattr__(self, key, value):
#         if key in ('title'):
#             if not isinstance(value, str):
#                 raise TypeError(f'{key} is incorrect')
#             if not value:
#                 raise ValueError(f'{key} must contain at least 1 character')
#         elif key in ('price'):
#             if not isinstance(value, int):
#                 raise TypeError(f'{key} is incorrect')
#             if value <= 0:
#                 raise ValueError(f'{key} must be greater than zero.')
#         self.__dict__[key] = value
#
#     def __getattribute__(self, item):
#         if item == 'price':
#             return f'{object.__getattribute__(self,item)} UAH'
#         return object.__getattribute__(self,item)
#
#
#     def __delattr__(self, item):
#         if item not in ('title', 'price'):
#             del self.__dict__[item]
#
#
#     def __str__(self):
#         return f'{self.title} {self.price}'
#
#
# product1= Product('banana', 11)
#
# print(product1.title)
# print(product1.price)
#
# product1.price=15
#
# print(product1.price)

# Homework 1


class Account():

    def __init__(self, balance):
        if isinstance(balance,int|float):
            self.__balance = balance
        else:
            raise ValueError('You should input right value')

    def __get__(self):
        return f'Balance:{self.__balance}'

    def __set__(self):
        return 'You are not allowed to change the balance.'

    @property
    def balance(self):
        return f'Balance:{self.__balance}'

    def __setattr__(self, key, value):
        if key == 'balance':
            raise Exception('You are not allowed to change the balance.')
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        if item != 'balance':
            raise Exception('Balance doesn`t exist.')
        return object.__getattribute__(self, item)
    def __str__(self):
        return (f'{self.__balance}')

account = Account(9999)
print(account.balance)
try:
    account.balance = 12121212
except Exception as a:
    print(a)
try:
    account.blns
except Exception as a:
    print(a)


# щось трішки все заплутано, потрібно і дискриптори і проперті і сетатрибут і гетатрибут
# не розумію навіщо нам __get__ __set__

# 2
print('\n*************************\n')
class User:

    def __init__(self, first_name, last_name):
        """

        :param first_name: str
        :param last_name: srt
        """
        if isinstance(first_name,str) and isinstance(last_name,str):
            self.__first_name = first_name
            self.__last_name = last_name
        else:
            raise ValueError('You should input right value')

    @property
    def sex(self):
        return f'First name: {self.__first_name}, last name: {self.__last_name}.'

    def __setattr__(self, key, value):
        if key in ('first_name','last_name'):
            raise Exception('You cannot change the first name or lasst name')
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        if item not in ('first_name','last_name'):
            raise Exception('There is no one with such name or surname')
        return object.__getattribute__(self, item)

    def __str__(self):
        return (f'{self.__first_name}, {self.__last_name}')
user1 = User('Oleg', 'Best teacher')
print(user1.sex)

try:
    user1.first_name = 'Anton', 'oleg'
except Exception as a:
    print(a)
try:
    user1.a
except Exception as a:
    print(a)

# 2
print('\n*************************\n')

class Rectangle():

    def __init__(self,width,height):
        """

        :param width: int|float
        :param height: int|float
        """
        if isinstance(width,int|float) and isinstance(height,int|float):
            self.__width = width
            self.__height = height
        else:
            raise ValueError('You should input right value')

    @property
    def rectangle(self):
        return f'Width: {self.__width}, height: {self.__height}.'

    def __setattr__(self, key, value):
        if key in ('width','height'):
            raise Exception('You cannot change the width or height of rectangle')
        return object.__setattr__(self,key,value)

    def __getattr__(self, item):
        if item not in ('width','height'):
            raise Exception(f'There is`t no object like {item}')
        return object.__getattribute__(self,item)

    def area(self):
        return f'The area of the rectangle: {self.__width} * {self.__height}'

    def __str__(self):
        return (f'{self.__width}, {self.__height}')

rectangle1=Rectangle(15,23)
print(rectangle1.rectangle)

try:
    rectangle1.width = 12, 2
except Exception as a:
    print(a)
try:
    rectangle1.circle
except Exception as a:
    print(a)

print(rectangle1.area())