class Product:
    quantity = 1000
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def summa(self):
        return self.quantity * self.price

class Food(Product):
    is_critical = True

eggs = Food("egg", 100)

print(eggs.is_critical)