# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

import os
def clear(): return os.system('cls')


clear()


# честно загуглил. Сам реализовать не смог
def get_collection_prime_factors(x):
    i = 2
    result_list = []
    while i * i <= x:
        while x % i == 0:
            result_list.append(i)
            x /= i
        i += 1
    if x > 1:
        result_list.append(int(x))
    print(*result_list)
    return result_list


n_from_user = int(input("Введите число\n"))
some_list = get_collection_prime_factors(n_from_user)
