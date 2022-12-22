# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

import os
def clear(): return os.system('cls')


clear()

x = input("Впишите вещественное число \n")
lenght_x = len(x)
x = float(x)*(10**lenght_x)
res = 0

while (x>0):
    res+=x%10
    x=int(x/10)

print(int(res))
