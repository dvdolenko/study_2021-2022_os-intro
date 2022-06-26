# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# Раздел 2, №18

A = float(input())
N = int(input())
i = 0
sum = 0
while i <= N:
    sum += A**i
    i += 1
    A *= -1
print (sum)
