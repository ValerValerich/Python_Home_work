# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел

import os
import random
def clear(): return os.system('cls')


clear()


def create_str(num):
    data = 'абв'
    lst = []
    for _ in range(num):
        temp = ''.join(random.sample(data, k=3))
        lst.append(temp)
    return str(' '.join(lst))


def modif_str(x):
    return x.replace("абв", "")


first_str = create_str(int(input("Введите число\n")))
print(first_str)
second_str = modif_str(first_str)
print(second_str)
