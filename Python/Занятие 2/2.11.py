# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# Задание 2, №11

A = int(input())
B = int(input())
max = -10000000000
if A > max: max = A
if B > max: max = B
if A != B:
    A = max
    B = max
else:
    A = 0
    B = 0
print ("A =", A)
print ("B =", B)