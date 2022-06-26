# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# Задание 1, №20

ABC = int(input())
C = ABC % 10
nnn = ABC // 10
B = nnn % 10
A = nnn // 10
if A != B and A != C and B != C:
    print ("True")
else:
    print ("False")