# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке

import os
import random
import sys
def clear(): return os.system('cls')


clear()


def create_list(x):
    if x.isdigit() and int(x) >= 0:
        x = int(x)
        # не так часто попадаются повторяющиеся числа, но вроде работает
        lst = random.choices(range(x*x), k=x)
        return lst
    else:
        return exit("Такого быть не может")


def get_single_nums(lst_in: list):
    res_lst = []
    for i in lst_in:
        if lst_in.count(i) == 1:
            res_lst.append(i)
    return res_lst


n_from_user = input("Введите число\n")
res_c_l = create_list(n_from_user)
print(*res_c_l)
res_get_s_n = get_single_nums(res_c_l)
print(*res_get_s_n)
