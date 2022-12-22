# Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.

import random
import os
def clear(): return os.system('cls')


clear()

x = int(input("Введите длину списка для перемешивания \n"))

lst = list(range(x))
print(* lst)
#x=len(lst)
lst2 = []
for i in range(len(lst)):
    temp = random.randrange(len(lst))
    lst2.append(lst.pop(temp))


print(* lst2)
