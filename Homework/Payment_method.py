class PaymentMethod:
    def make_payment(self):
        return NotImplementedError


class CreditCard(PaymentMethod):
    ...


class BankTransfer(PaymentMethod):
    ...


class ElectronicWallet(PaymentMethod):
    ...



