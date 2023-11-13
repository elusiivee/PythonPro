class Product():
    def __init__(self, title, price, **kwargs):
        self.title = title
        self.price = price
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        if key in ('title'):
            if not isinstance(value, str):
                raise TypeError(f'{key} is incorrect')
            if not value:
                raise ValueError(f'{key} must contain at least 1 character')
        elif key in ('price'):
            if not isinstance(value, int):
                raise TypeError(f'{key} is incorrect')
            if value <= 0:
                raise ValueError(f'{key} must be greater than zero.')
        self.__dict__[key] = value

    def __getattribute__(self, item):
        if item == 'price':
            return f'{object.__getattribute__(self,item)} UAH'
        return object.__getattribute__(self,item)


    def __delattr__(self, item):
        if item not in ('title', 'price'):
            del self.__dict__[item]


    def __str__(self):
        return f'{self.title} {self.price}'


product1= Product('banana', 11)

print(product1.title)
print(product1.price)

product1.price=15

print(product1.price)