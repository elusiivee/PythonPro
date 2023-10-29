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

