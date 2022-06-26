# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# Блок 2 №6

import math

def SUM(j):
    j6 = j % 10
    j5 = (j // 10) % 10
    j4 = (j // 100) % 10
    j3 = (j // 1000) % 10
    j2 = (j // 10000) % 10
    j1 = (j // 100000) % 10
    if j1+j2+j3 == j4+j5+j6:
        result = "HAPPY"
    else: result = " "
    return result

for i in range (100000, 1000000):
    if SUM(i) == "HAPPY":
        print (i)
