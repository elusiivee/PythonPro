import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class LoggingMixin:
    '''Mixin that adds logging to a class'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)

    def log(self, message, level=logging.INFO):
        '''Log a message'''
        self.logger.log(level, message)
class Discount:
    def discount(self):
        raise NotImplementedError


class RegularDiscount(Discount):
    def discount(self):
        return 0.9


class SilverDiscount(Discount):
    def discount(self):
        return 0.85
        # return 1.1


class GoldDiscount(Discount):
    def discount(self):
        return 0.8


class Product:
    def __init__(self, title: str, price: float | int):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price:.2f}'


class Cart(LoggingMixin):
    def __init__(self, discount: Discount = None):
        super().__init__()
        self.__products = []
        self.__quantities = []

        if discount is not None:
            if not (0 <= discount.discount() <= 1):
                raise ValueError ('False discount')
            else:
                self.discount = discount
        else:
            self.log(f'Invalid discount', logging.ERROR)
            self.discount = None




    def add_product(self, product: Product, quantity: int | float = 1):
        if isinstance(product, Product) and isinstance(quantity, int | float):
            self.log('add product to cart')
            self.__products.append(product)
            self.__quantities.append(quantity)
        else:
            self.log(f'inpossible to add {product}', logging.WARNING)
    def total(self):
        summa = sum(product.price * quantity for product, quantity in zip(self.__products, self.__quantities))
        summa = summa * self.discount.discount() if self.discount else summa
        self.log(f'Customer pay {summa}', logging.WARNING)
        return summa
    def __str__(self):
        return '\n'.join(map(lambda items: f'{items[0]} x {items[1]} = {items[0].price * items[1]} UAH',
                          zip(self.__products, self.__quantities))) + f'\nTotal: {self.total():.2f} UAH\n'

try:
    pr_1 = Product('banana', 50)
    pr_2 = Product('apple', 51)
    pr_3 = Product('orange', 52)
except ValueError as er:
    print('Wrong value',er)


cart_1 = Cart()
cart_2 = Cart(SilverDiscount())

try:
    cart_1.add_product(pr_1)
    cart_1.add_product(pr_2)
    cart_1.add_product(pr_3)
    cart_2.add_product(pr_1, 5)
except ValueError as er:
    print('Wrong discount', er)

print(cart_1)
print(cart_2)