# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# Раздел 1, №5.28

print ("а)")
n = 8
P = 1
while n <=15:
    P *= n
    n += 1
print (P)


print ("б)")
a = int(input())
while a < 1 or a > 20:
    a = int(input())
P = 1
while a <=20:
    P *= a
    a += 1
print (P)


print ("в)")
b = int(input())
while b < 1 or b > 20:
    b = int(input())
m = 1
P = 1
while m <= b:
    P *= m
    m += 1
print (P)


print ("г)")
a = int(input())
b = int(input())
while b < a:
    b = int(input())
P = 1
while a <= b:
    P *= a
    a += 1
print (P)