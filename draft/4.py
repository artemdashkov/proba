class Main:
    def __init__(self, a, b):
        self.weight = a
        self.height = b
    def area(self):
        return f"Площадь: {self.weight * self.height}"

class SubMain(Main):
    def __init__(self, a, b):
        super().__init__(a, b)
    def perimeter(self):
        return f"Периметр: {(self.weight)*2}"

# object_1 = Main (3, 4)
# print(object_1.area())
object_2 = SubMain(8, 4)
print(object_2.perimeter())