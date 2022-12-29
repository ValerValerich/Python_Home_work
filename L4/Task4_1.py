# Вычислить число c заданной точностью d

import os
import decimal
def clear(): return os.system('cls')


clear()


def modif_num(x, y):
    return (decimal.Decimal(x)).quantize(decimal.Decimal(y))


a = input("Введите число\n")
b = input("Введите пример для округдения\n")

print(modif_num(a, b))
