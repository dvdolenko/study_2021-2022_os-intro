# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# Блок 3 №10.41

import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input())
print(factorial(n))