# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

import os
def clear(): return os.system('cls')


clear()

a, b= int(input("Введите первой число \n")), int(input("Введите второе число \n"))
n=int(input("Введите N \n"))

lst=[]
for i in range(-n, n+1):
    lst.append(i)

if a<len(lst) and b<len(lst):
    print(lst[a-1]*lst[b-1])
else:
    print("There are no values for these indexes!")