# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

from os import system
from itertools import groupby
from os import path
def clear(): return system('cls')


clear()


def coder(address):  # text.txt
    if path.exists(address):

        f = open(address, 'r')
        text = f.readline()
        print(text)
        f.close()
        lst = [''.join(j) for i, j in groupby(text)]
        strng = ''
        for i in lst:
            strng += str(len(i))+i[0]
        return strng

    else:
        return "Такого файла не существует"


def decode(data):
    decode = ''
    counter = ''
    for i in data:
        if i.isdigit():
            counter += i
        else:
            decode += i * int(counter)
            counter = ''
    return decode


file_location = input("Введите название файла\n")

first_q = coder(file_location)
print(first_q)

second_q = decode(first_q)
print(second_q)
