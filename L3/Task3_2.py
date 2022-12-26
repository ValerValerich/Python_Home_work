# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д

import os
import random
def clear(): return os.system('cls')


clear()

# задаем изначальный список. Параметры предустановлены
lst = random.sample(range(-100, 101), k=random.randrange(10, 12))
print(*lst)


def special_mult(x):  # функция подсчета пар
    fin_lst = []
    for i in range(int(len(x)/2)):
        fin_lst.append(x[i]*x[-(i+1)])
    # Если есть средний элемент без пары, добавляем его в результирующий лист
    if len(x) % 2 != 0:
        fin_lst.append(x[int(len(x)/2)])
    return fin_lst


result = special_mult(lst)
print(*result)
