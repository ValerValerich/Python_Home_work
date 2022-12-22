# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка

import os
def clear(): return os.system('cls')


clear()

x=int(input("Введите число \n"))
lst=[]
for i in range(1, x+1):
    temp=1
    for j in range(1, i+1):
        temp*=j
    lst.append(temp)

print(lst)