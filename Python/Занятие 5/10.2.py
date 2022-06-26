# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# Блок 1 №10.2

import math


def Y(n):
    result = (n + math.sin(n))/3
    return result

y = Y(1) + Y(5) + Y(3)
print("a)", y)


def Y(n, m):
    result = (n + math.sin(n))/(math.sin(m) + m)
    return result

y = Y(2, 5) + Y(6, 3) + Y(1, 4)
print("b)", y)


def Y(n, m):
    result = (n + math.sin(m))/(math.sin(n) + m)
    return result

y = Y(1, 4) + Y(7, 5) + Y(3, 2)
print("c)", y)


def Y(n1, n2, n3, n4, n5, n7):
    result1 = (n2 + math.sin(n3))/(math.sin(n2) + n3)
    result2 = (n1 + math.sin(n5))/(math.sin(n1) + n5)
    result3 = (n4 + math.sin(n7))/(math.sin(n3) + n7)
    result = result1 + result2 + result3
    return result

y = Y(1, 2, 3, 4, 5, 7)
print("d)", y)