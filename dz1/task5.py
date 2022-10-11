# 5. Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
#  Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
import math

Xa = int(input('Ведите Хa ='))
Ya = int(input('Ведите Ya ='))
Xb = int(input('Ведите Хb ='))
Yb = int(input('Ведите Yb ='))
print("A ({0}, {1})".format(Xa, Ya))
print("B ({0}, {1})".format(Xb, Yb))
distance = round(math.sqrt((Xb - Xa) ** 2 + (Yb - Ya) ** 2), 2)
print("A ({0}, {1})".format(Xa, Ya), "B ({0}, {1})".format(Xb, Yb), distance, sep='\t')
