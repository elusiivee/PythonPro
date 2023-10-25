import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# # 1
# class Product:
#     def __init__(self, name: str, price: (int, float), description: str):
#         '''
#         :param name: name of the product
#         :param price: price of the product
#         :param description: description of the product
#         '''
#         if isinstance(name, str) and isinstance(price, (int, float)) and isinstance(description, str):
#
#             self.name = name
#             self.price = price
#             self.description = description
#         else:
#             raise TypeError
#
#     def __str__(self):
#
#         return f'Name: {self.name}, price: {self.price}, description: {self.description}\n'
#
#
# class Cart:
#     def __init__(self):
#         self.total_price = 0
#
#     def add_product(self, product: Product):
#         self.total_price += product.price
#
#     def __str__(self):
#         return f'Total price: {self.total_price}\n'
#
#
# phone = Product('Iphone 10', 1000, 'New-brand phone')
# tv = Product('Samsung j-100', 1200, 'Screen 1980px')
# jet_pack = Product('Jetpack', 9999, 'Fly higher')
#
# cart = Cart()
# cart.add_product(phone)
# cart.add_product(tv)
# cart.add_product(jet_pack)
#
# print(cart)


# 2
class LoggingMixin:
    '''Mixin that adds logging to a class'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)

    def log(self, message, level=logging.INFO):
        '''Log a message'''
        self.logger.log(level, message)
class Dish(LoggingMixin):
    def __init__(self, name: str, description: str, price: (int, float)):
        super().__init__()
        '''
        :param name: name of the product
        :param description: description of the product
        :param price: price of the product
        '''

        if isinstance(name, str) and isinstance(price, (int, float)) and isinstance(description, str):
            self.name = name
            self.description = description
            self.price = price
        else:
            self.log(f'inpossible to add such dish ', logging.WARNING)
            raise ValueError('False input')



    def __str__(self):
        return f'{self.name} - {self.price} USD\n{self.description}'


class MenuCategory(LoggingMixin):
    def __init__(self, name: str, dishes: list):
        super().__init__()
        if isinstance(name, str) and isinstance(dishes, list):
            self.name = name
            self.dishes = dishes
        else:
            self.log(f'inpossible to create such menu ', logging.WARNING)
    def show_menu(self):
        print(f"*** {self.name} ***")
        for dish in self.dishes:
            print(dish)
            print("\n")


class Order:
    def __init__(self):
        self.ordered_food = []

    def add_item(self, item):
        self.ordered_food.append(item)

    def remove_item(self, item):
        self.ordered_food.remove(item)

    def calculate_total(self):
        total = sum(item.price for item in self.ordered_food)
        return total


try:
    dish1 = Dish("Pasta Carbonara", "Creamy pasta with bacon and eggs", 12.99)
    dish2 = Dish("Margherita Pizza", "Classic pizza with tomatoes, mozzarella, and basil", 10.99)
    dish3 = Dish("Tiramisu", "Italian dessert with coffee, mascarpone, and cocoa", 6.99)
    dish4 = Dish("Lasagna", "Layered pasta with Bolognese sauce and cheese", 14.99)
    dish5 = Dish(123, "King od pasta", '14.23')        #false input
except ValueError as e:
    print(f'Error when adding dish to a menu: {e}')


try:
    italian_category = MenuCategory("Italian Food", [dish1, dish2, dish3, dish4])
    italian_category_error = MenuCategory(123, [dish1, dish2, dish3, dish4])
except ValueError as e:
    print(f'Error when adding a menu: {e}')        #чомусь ця помилка не спрацьовує, можливо через логер

order = Order()

try:
    order.add_item(dish1)
    order.add_item(dish1)
    order.add_item(dish2)
    order.add_item(dish3)
    order.add_item(dish4)
    #order.add_item(dish5)      #error  як позбавитись цієї помилки
except ValueError as e:
    print(f'Error when adding an item to the order: {e}')


italian_category.show_menu()
print(f"Total order cost: {order.calculate_total()} USD")
print('================')
order.remove_item(dish1)

italian_category.show_menu()

print(f"Total order cost: {order.calculate_total()} USD")


##############3