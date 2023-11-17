class PaymentMethod:
    def make_payment(self):
        return NotImplementedError


class CreditCard(PaymentMethod):
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def make_payment(self):
        pass


class BankTransfer(PaymentMethod):

    def __init__(self, owner_name, balance, receiver_card, money_amount):
        if isinstance(owner_name, str) and isinstance(balance, int | float) and isinstance(receiver_card, int) \
                and len(str(receiver_card)) == 16 and isinstance(money_amount, int | float):
            """
            :param owner_name: name of the card owner -> str
            :param balance: balance on the card -> int|float
            :param receiver_card: card on which we send the money -> int length(mix 16)
            :param money_amount: amount of money which we send
            """
            super().__init__()
            self.owner_name = owner_name
            self.balance = balance
            self.receiver_card = receiver_card
            self.money_amount = money_amount
        else:
            raise ValueError('incorrect value')

    def make_payment(self):
        if self.money_amount <= self.balance:
            return f'{self.money_amount}$ transferred from {self.owner_name}s card to {self.receiver_card}. Current account balance: {self.balance - self.money_amount}$.'

        else:
            return "Insufficient funds."


class ElectronicWallet(PaymentMethod):
    def __init__(self, owner_name, balance, money_amount):
        if isinstance(owner_name, str) and isinstance(balance, int | float) and isinstance(money_amount, int | float):
            """
            :param owner_name: name of the card owner -> str
            :param balance: balance on the card -> int|float
            :param money_amount: amount of money which we send
            """
            super().__init__()
            self.owner_name = owner_name
            self.balance = balance
            self.money_amount = money_amount

    def make_payment(self):
        if self.money_amount <= self.balance:
            return f'{self.money_amount}$ withdrawn from {self.owner_name}s card. Current account balance: {self.balance - self.money_amount}$.'

        else:
            return "Insufficient funds."


class PaymentProcessor:
    def __init__(self):
        self.payment_methods = []

    def add_payment_method(self, task):
        self.payment_methods.append(task)

    def make_payment(self, task, amount):
        ...


def figure(obj):
    return obj


bank_transfer = BankTransfer('Andrii', 2000, 4887466528831999, 999)
electronic_wallet = ElectronicWallet('Andrii', 2000, 20)
processor = PaymentProcessor()

print(figure(bank_transfer).make_payment())
print(figure(electronic_wallet).make_payment())
