# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# Раздел 2, №10 (while)

N = int(input())
while N < 1:
    N = int(input())
K = 0
while 3**K < N:
    K += 1
print (K-1)
