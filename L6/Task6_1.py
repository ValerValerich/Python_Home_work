# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

import os
import random
def clear(): return os.system('cls')


clear()


def origin_list(num):  # создаем список случайных чисел
    return [random.randint(-num, num) for _ in range(num)]


def fin_list(lst):  # создаем новый список согласно условию из оригинального списка
    return [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i-1]]


client_data = int(input("Введите длину списка\n"))

in_list = origin_list(client_data)
print(*in_list)

out_list = fin_list(in_list)
print(*out_list)
