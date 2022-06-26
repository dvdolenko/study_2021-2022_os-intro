# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# Задание 2, №11

import math
a = float(input())
b = float(input())

a_ = math.fabs(a)
b_ = math.fabs(b)

Sum = a_ + b_
Def = a_ - b_
Prod = a_ * b_
Quot = a_ / b_

print("Сумма =" , Sum)
print("Разность =" , Def)
print("Произведение =" , Prod)
print("Частное =" , Quot)