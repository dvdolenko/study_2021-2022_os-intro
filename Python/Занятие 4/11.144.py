# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# №11.144

from random import randrange
j = [randrange(1,999) for i in range(9)]
print ("Массив:", j)

q2 = j[2]
q5 = j[5]
j[2] = q5
j[5] = q2
print("a)", j)

m = int(input())
n = int(input())
qm = j[m]
qn = j[n]
j[m] = qn
j[n] = qm
print("б)", j)

q3 = j[3]
max = -1000000000
for i in range (9):
    if j[i] > max:
        max = j[i]
        maxi = i
j[3] = max
j[maxi] = q3
print("в)", j)

q1 = j[1]
min = 1000000000
for i in range (9):
    if j[i] <= min:
        min = j[i]
        mini = i
j[1] = min
j[mini] = q1
print("г)", j)
