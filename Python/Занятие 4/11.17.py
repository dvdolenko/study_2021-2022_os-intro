# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# №11.17

j = [1, 5, -6, 88, -485, -544, 77]
print ("Введите два номера элемента")
s = int(input())
k = int(input())

if j[s-1] > 0:
    print("a) Yes")
else:
    print("a) No")

if j[k-1] % 2 == 0:
    print("b) Yes")
else:
    print("b) No")

if j[k-1] > j[s-1]:
    print("c) k -", k, "-й")
else:
    print("c) s -", s, "-й")