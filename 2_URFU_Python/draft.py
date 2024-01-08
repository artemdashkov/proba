import numpy as np

seed = 2021

# В simple сохраните случайное число в диапазоне от 0 до 1
simple = np.random.sample()
print("simple", simple)

# Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их в переменную randoms
randoms = np.random.uniform(-150, 2021, 120)
print('randoms', randoms)

# Получите массив из случайных целых чисел от 1 до 100 (включительно) из 3 строк и 2 столбцов. Сохраните результат в table
table = np.random.randint(1, 101, size=(3, 2))

# В переменную even сохраните четные числа от 2 до 16 (включительно)
even = np.arange(2, 17, 2)
# Скопируйте even в переменную mix. Перемешайте числа в mix так, чтобы массив изменился
mix = even.copy()
np.random.shuffle(mix)
# Получите из even 3 числа без повторений. Сохраните их в переменную select
select = np.random.choice(mix, size=3, replace=False)
print(select)

# Получите переменную triplet, которая должна содержать перемешанные значения из массива select (сам select измениться не должен)
triplet = np.random.permutation(select)
print(triplet)
print(select)