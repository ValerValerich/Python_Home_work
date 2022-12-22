# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

import os
def clear(): return os.system('cls')


clear()

n=int(input("Введите число \n"))

lst=[]
for i in range(1, n+1):
    lst.append(round((1 + 1/i) ** i, 3))

print(*lst)

sum_lst=sum(lst)

print(sum_lst)