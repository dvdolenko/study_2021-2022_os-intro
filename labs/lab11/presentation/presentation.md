---
## Front matter
lang: ru-RU
title: Программирование в командном процессоре ОС UNIX. Ветвления и циклы
author: |
	  Доленко Дарья Васильевна НБИбд-01-21\inst{1}

institute: |
	\inst{1}Российский Университет Дружбы Народов

date: 28 мая, 2022, Москва, Россия

## Formatting
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true

---

# Цели и задачи работы

## Цель лабораторной работы

Изучить основы программирования в оболочке ОС UNIX. Научится писать более сложные командные файлы с использованиемлогических управляющих конструкций и циклов.

# Процесс выполнения лабораторной работы

(../report/image/1.jpg){#fig:001 width=70%}

## Используя команды getopts grep, написала командный файл, который анализирует командную строку с ключами: -iinputfile; -ooutputfile; -pшаблон; -C; -n, затем ищет в указанном файле нужные строки,определяемые ключом -p. (рис. [-@fig:001] [-@fig:002] [-@fig:003])

![Пример работы программы](../report/image/1.jpg){#fig:001 width=70%}

##

![Содержание текстового файла](../report/image/2.jpg){#fig:002 width=70%}

##

![Текст программы](../report/image/3.jpg){#fig:003 width=70%}

## Написала на языке Си программу, которая вводитчисло и определяет, являетсяли оно больше нуля, меньше нуля или равно нулю. Затем программа завершается с помощью функции exit(n), передавая информацию в о коде завершения в оболочку. Командный файл должен вызывать эту программу и, проанализировав с помощью команды $?,выдать сообщение отом, какое число было введено. (рис. [-@fig:004] [-@fig:005] [-@fig:006])

![Пример работы программы](../report/image/4.jpg){#fig:004 width=70%}

##

![Файл sh](../report/image/5.jpg){#fig:005 width=70%}

##

![Файл С](../report/image/6.jpg){#fig:006 width=70%}

## Написала командный файл, создающий указанное число файлов, пронумерованных последовательно от 1 до 𝑁 (например 1.tmp, 2.tmp, 3.tmp, 4.tmp и т.д.). Число файлов, которые необходимо создать,передаётся в аргументы командной строки.Этот же командный файл должен уметь удалять все созданные им файлы (если они существуют). (рис. [-@fig:007] [-@fig:008] [-@fig:009])

![Пример работы программы (состояние до применения)](../report/image/7.jpg){#fig:007 width=70%}

##

![Пример работы программы (после применения)](../report/image/8.jpg){#fig:008 width=70%}

##

![Текст программы](../report/image/9.jpg){#fig:009 width=70%}

## Написала командный файл,который с помощью команды tar запаковываетв архив все файлы в указанной директории. Модифицировала его так, чтобы запаковывались только те файлы, которые были изменены менее недели тому назад (использовать команду find). (рис. [-@fig:010] [-@fig:011] [-@fig:012] [-@fig:013])

![До применения программы](../report/image/10.jpg){#fig:010 width=70%}

##

![После применения программы](../report/image/11.jpg){#fig:011 width=70%}

##

![Текст программы](../report/image/12.jpg){#fig:012 width=70%}

##

![Команды архивации](../report/image/13.jpg){#fig:013 width=70%}

# Выводы по проделанной работе

## Вывод

В ходе данной лабораторной работы я изучила основы программирования в оболочке ОС UNIX, научилась писать более сложные командные файлы с использованиемлогических управляющих конструкций и циклов.
