class Client:
    def __init__(self, name: str, order: int, discount):
        self.name = name
        self.order = order
        self.discount = discount

    def get_total_price(self):
        if self.discount == 'Regular':
            return RegularDiscount.get_discount(self.order)
        elif self.discount == 'Silver':
            return SilverDiscount.get_discount(self.order)
        elif self.discount == 'Gold':
            return GoldDiscount.get_discount(self.order)


class RegularDiscount(Client):

    @classmethod
    def get_discount(cls, order):
        return order - (order * 0.1)


class SilverDiscount(Client):

    @classmethod
    def get_discount(cls, order):
        return order - (order * 0.15)


class GoldDiscount(Client):
    @classmethod
    def get_discount(cls, order):
        return order - (order * 0.2)


reg = Client('Lary', 57, 'Regular')
sivl = Client('Jany', 33, 'Silver')
gold = Client('Tom', 83, 'Gold')
print(reg.get_total_price(), sivl.get_total_price(), gold.get_total_price())
