# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# №9.48

print ("Введите слово")
word = str(input())
p = "+"
m = "-"
for i in range (3):
    p += "+"
for i in range (4):
    m += "-"
p = p + word + m
print(p)
