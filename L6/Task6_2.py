# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21.

import os
def clear(): return os.system('cls')


clear()


def only_special(num):
    return [i for i in range(20, num+1) if (i % 20 == 0 or i % 21 == 0)]


print(*only_special(int(input("Введите число от 20 и выше\n"))))
