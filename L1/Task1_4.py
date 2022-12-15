# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)

import os
def clear(): return os.system('cls')


clear()

quarter = int(input("Введите номер четверти "))

if 1 <= quarter <= 4:
    if quarter == 1:
        print("x>0 и y>0")
    elif quarter == 2:
        print("x<0 и y>0")
    elif quarter == 3:
        print("x<0 и y<0")
    else:
        print("x>0 и y<0")
else:
    print("Нет такой четверти")
