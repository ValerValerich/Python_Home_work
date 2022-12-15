# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

import os
def clear(): return os.system('cls')


clear()

print("Введите координаты первой точки (через Enter)")
point1 = [float(input()), float(input())]

print("Введите координаты второй точки (через Enter)")
point2 = [float(input()), float(input())]

print(round(((point2[0]-point1[0])**2+(point2[1]-point1[1])**2)**0.5, 3))
