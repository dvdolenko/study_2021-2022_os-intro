# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# №11.55

j = [1, 50, -60, 88, -485, -544, 77]

print("a)")
m = 0
for i in range (7):
    if j[i] % 2 == 1:
        m += j[i]
print (m)


print("b)")
m = 0
z = int(input())
for i in range (7):
    if j[i] % z == 0:
        m += j[i]
print (m)

print("c)")
m = 0
z = int(input())
w = int(input())
for i in range (7):
    if j[i] % z == 0 or j[i] % w == 0:
        m += j[i]
print (m)