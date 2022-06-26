# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# №11.2

print ("variant 1")
m = str(input())
n = m
for i in range (9):
    m = str(input())
    n += m
print (n)

print ("variant 2")
j = []
for i in range(10):
    u = int(input())
    j.append(u)
print(j)
