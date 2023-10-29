class Product:
    def __init__(self, title: str, price: float | int):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price:.2f}'

