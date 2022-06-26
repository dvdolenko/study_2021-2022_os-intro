# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# №9.91

print ("Введите предложение")
sent = str(input())
sent2 = "Результат: "
for i in range (len(sent)):
    if sent[i] == " ":
        sent2 += "_"
    else:
        sent2 += sent[i]
print (sent2)

