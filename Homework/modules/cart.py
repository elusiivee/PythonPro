import log
import discounts
from product import Product


class Cart(log.LoggingMixin):
    def __init__(self, discount: discounts.Discount = None):
        super().__init__()
        self.__products = []
        self.__quantities = []

        if discount is not None:
            if not (0 <= discount.discount() <= 1):
                raise ValueError('False discount')
            else:
                self.discount = discount
        else:
            self.log(f'Invalid discount', log.logging.ERROR)
            self.discount = None

    def __add__(self, product: Product, quantity: int | float = 1):
        if isinstance(product, Product) and isinstance(quantity, int | float):
            self.log('add product to cart')
            self.__products.append(product)
            self.__quantities.append(quantity)
        else:
            self.log(f'inpossible to add {product}', log.logging.WARNING)

    def __iadd__(self, other):
        if isinstance(other, Cart):
            self.__products.append(other.__products)
            self.__quantities.append(other.__quantities)
        else:
            raise ValueError("Can only combine two carts")

    def total(self):
        summa = sum(product.price * quantity for product, quantity in zip(self.__products, self.__quantities))
        summa = summa * self.discount.discount() if self.discount else summa
        self.log(f'Customer pay {summa}', log.logging.WARNING)
        return summa

    def __iter__(self):
        return iter(self.__products)

    def __str__(self):
        return '\n'.join(map(lambda items: f'{items[0]} x {items[1]} = {items[0].price * items[1]} UAH',
                             zip(self.__products, self.__quantities))) + f'\nTotal: {self.total():.2f} UAH\n'


if __name__ == '__main__':

    try:
        pr_1 = Product('banana', 50)
        pr_2 = Product('apple', 51)
        pr_3 = Product('orange', 52)

        pr_4 = Product('pineappla', 49)
        pr_5 = Product('cherry', 33)
        pr_6 = Product('grape', 39)
    except ValueError as er:
        print('Wrong value', er)

    cart_1 = Cart()
    cart_2 = Cart()

    try:
        cart_1 + pr_1
        cart_1 + pr_2
        cart_1 + pr_3
        cart_2 + pr_4
        cart_2 + pr_5
        cart_2 + pr_6

    except ValueError as er:
        print('Wrong discount', er)

    print(cart_1)
    print(cart_2)

    print('Iteration*******************')
    for product in cart_1:
        print(f'Name: {product.title}, price: {product.price}')

    print('\nCombine two carts*****************')
    cart_1 += cart_2  # не можу зрозузміти чому None
    print(cart_1)
