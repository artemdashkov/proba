import random
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count_all = len(list_1)

count_of_runs = 3 if count_all >= 3 else count_all


random_list = random.sample(list_1, 3 if count_all >= 3 else count_all)

# random_list = random.sample(list_1, 3)
print(count_of_runs)
print(random_list)