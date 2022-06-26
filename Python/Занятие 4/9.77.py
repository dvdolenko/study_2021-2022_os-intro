# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# №9.77

print ("Введите слово")
word = str(input())
n = 0
for i in range (len(word)):
    if word[i] == "а":
        print (i)
        n += 1
        break
if n == 0:
    print ("Такой буквы нет")

