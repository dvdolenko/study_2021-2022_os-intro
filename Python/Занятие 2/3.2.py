# Доленко Дарья, РУДН, НБИбд-01-21, 25.06.22
# Задание 3, №2

K = int(input())
if K >= 1 and K <=5:
    match K:
        case 1:
            print("плохо")
        case 2:
            print("неудовлетворительно")
        case 3:
            print("удовлетворительно")
        case 4:
            print("хорошо")
        case 5:
            print("отлично")
else:
    print ("ошибка")


