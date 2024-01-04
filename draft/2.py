class Shapes():
    def __init__(self, v):
        self.vertices = v
    def __str__(self):
        return f"Это {self.vertices}-угольник"

class Triangle(Shapes):
    def __init__(self, s, v=3):
        super().__init__(v)
        self.sides = s
    def get_perimeter(self):
        p = 0
        for i in self.sides:
            p += i
        return p
    def __str__(self):
        return f"Это треугольник со стороноами {self.sides}"

shapes_1 = Shapes(6)
triangle_1 = Triangle([3, 4, 5])

print(shapes_1)
print(triangle_1)