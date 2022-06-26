# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# Задание 4, №4

import math
print ("Введите координаты через Enter, сначала X, затем Y")
x = float(input())
y = float(input())
if x >= 0 and x <= 1:
    if math.fabs(y) <= x:
        print ("Yes")
    else:
        print ("No")
else:
    print ("No")


