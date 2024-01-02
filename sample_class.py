class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return (self.a + self.b)
    def mult(self):
        return (self.a * self.b)
    def dif(self, c, d):
        self.c = c
        self.d = d
        return (self.c-self.d)

class Calc_2(Calc):
    def __init__(self, a, b, i):
        Calc.__init__(self, a, b)
        self.i = i
    def exp(self):
        return self.a**self.i

def main():
    object_1 = Calc_2(10, 5, 2)

    sum = object_1.sum()
    print("Это сумма: ", sum)

    mult = object_1.mult()
    print("Это умножение: ", mult)

    dif = object_1.dif(40, 30)
    print("Это разность двух заданных чисел: ", dif)

    exp_1 = object_1.exp()
    print("Это 10 в степени 2", exp_1)

if __name__ == "__main__":
    main()