# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

import os
def clear(): return os.system('cls')


clear()


def dec_in_binar(x):
    result = []
    while x:
        result.append(x % 2)
        x //= 2
    result.reverse()
    return result


in_num = int(input("Введите число в десятичном виде \n"))

print(*dec_in_binar(in_num), sep='')

# print(bin(in_num))
