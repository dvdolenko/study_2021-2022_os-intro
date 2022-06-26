# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# №11.109

from random import randrange
j = [randrange(1000000,100000000) for i in range(50)]
print (j)

price = 0
for i in range (50):
    if j[i] > price:
        price = j[i]
print (price)

