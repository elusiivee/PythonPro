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
                raise ValueError ('False discount')
            else:
                self.discount = discount
        else:
            self.log(f'Invalid discount', log.logging.ERROR)
            self.discount = None




    def add_product(self, product: Product, quantity: int | float = 1):
        if isinstance(product, Product) and isinstance(quantity, int | float):
            self.log('add product to cart')
            self.__products.append(product)
            self.__quantities.append(quantity)
        else:
            self.log(f'inpossible to add {product}', log.logging.WARNING)
    def total(self):
        summa = sum(product.price * quantity for product, quantity in zip(self.__products, self.__quantities))
        summa = summa * self.discount.discount() if self.discount else summa
        self.log(f'Customer pay {summa}', log.logging.WARNING)
        return summa
    def __str__(self):
        return '\n'.join(map(lambda items: f'{items[0]} x {items[1]} = {items[0].price * items[1]} UAH',
                          zip(self.__products, self.__quantities))) + f'\nTotal: {self.total():.2f} UAH\n'

if __name__ == '__main__':

    try:
        pr_1 = Product('banana', 50)
        pr_2 = Product('apple', 51)
        pr_3 = Product('orange', 52)
    except ValueError as er:
        print('Wrong value',er)


    cart_1 = Cart()
    cart_2 = Cart(discounts.SilverDiscount())

    try:
        cart_1.add_product(pr_1)
        cart_1.add_product(pr_2)
        cart_1.add_product(pr_3)
        cart_2.add_product(pr_1, 5)
    except ValueError as er:
        print('Wrong discount', er)

    print(cart_1)
    print(cart_2)