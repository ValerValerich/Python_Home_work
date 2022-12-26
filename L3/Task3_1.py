# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах)

import os
import random
def clear(): return os.system('cls')


clear()


def create_list(x):  # создание списка
    # предопределенный диапазон чисел
    random_lst = random.sample(range(-100, 101), k=x)
    return random_lst


def sum_odd_position(lst):  # суммирование из четных индексов (нечетных позиций)
    x = 0
    for i in range(0, len(lst), 2):
        x += lst[i]
    return x


lenght_list = int(input("Введите длину списка\n"))
lst = create_list(lenght_list)
special_sum = sum_odd_position(lst)

print(lst)
print(special_sum)
