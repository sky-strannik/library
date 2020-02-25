# Модулем в Python называется любой файл с программой
# Модули нужны для:
# повторного использования кода
# управления пространством имен (одинаковые переменные в разных модулях)
# деления проекта на мелкие части
# Разновидности модулей:
# встроенные (math, random, ...)
# стронние (diango, PyQt5, ...)
# свои (любой .py файл)
# между своими и сторонними нет разницы, кроме автора
# Варианты подключения модулей:
# модуль целиком import math
# псевдоним для модуля import math as mt
# импорт всего содержимого from math import * (не рекомендуется)
# импорт конкретных функций, классов, ... из модуля from math import sin, cos

import math
print(math.pi)
print(math.sin(38))

import random as rd # импорт модуля с присваиванием ему псевдонима
print(rd.randint(1, 10))

# from math import * # импорт всего содержимого модуля, он не рекомендуется, т.к. могут быть совпадения по именам
# print(pi)
# print(sin(30))

from random import randint, randrange # классов может быть сколько угодно, но обычно берем только те, что нужны
print(randint(1, 10))


# Основные функции библиотеки math
# factorial - факториал числа
# exp - экспонента
# log, log2, log10 - логарифмы
# sqrt - квадратный корень
# sin, cos, asin, acos, ... - функции для работы с углами

# Задачи.
import math
r = 100
# 1. Найти длину окружности с определенным радиусом
print(2*r*math.pi)
# 2. Найти площадь окружности с определенным радиусом
print((r**2)*math.pi)
print((math.pow(r, 2))*math.pi)
# 3. По коориднатам 2-ух точек определить расстояние между ними
x1 = 10
y1 = 10
x2 = 50
y2 = 100
l = math.sqrt((x1-x2)**2+(y1-y2)**2)
print(l)
# 4. Найти факториал числа 9
print(math.factorial(9))


# Основные функции библиотеки random:
# Генерация случайных чисел, букв, элементов помледовательности
# randint - целое случайное число от А до В
# choice - случайный элемент последовательности
# shuffle - перемешивает последовательность
# random - случайное число от 0 до 1
# sample - список длинной k из последовательности

# Задачи.
from random import randint, choice, sample, shuffle
# 1. Загадать случайное число от 0 до 100
print(randint(0, 100))
# 2. Выбрать победителя лотереи из списка players
players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(choice(players))
# 3. Выбрать 3 победителей лотереи из списка players
print(sample(players, 3))
# 4. Перемешать карты в стопке (списке) cards
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
print(cards)
shuffle(cards)
print(cards)


# Модуль OS
# Функции для работы с операционной системой
# Не зависит от конкретной ОС
# Функции и переменный модуля OS
# name - имя операционной системы
# chdir - смена текущей директории
# getcwd() - текущая рабочая директория
# mkdir() - создание директории (папки)
# os.path - модуль для работы с путями
# и многие другие
import os
# имя операционной системы
print(os.name)
# текущая рабочая директория
print(os.getcwd())
# создаем новый путь
new_path = os.path.join(os.getcwd(), 'new_f')
# создаем папку по новому пути
# os.mkdir(new_path)


# Модуль SYS - обеспечивает взаимодействие с Python
# Функции и переменные SYS
# executable - путь к интерпретатору python
# exit() - выход из python
# platform - информация об ОС
# path - список путей поиска модулей
# argv - список аргументов командной строки
# и многие другие
# import sys
# sys.argv и sys.path рассмотрим подробнее далее
# Путь до интерпретатора
# print(sys.executable)
# Информация о платформе
# print(sys.platform)
# выход из python
# sys.exit()
# print('Этот код мы уже не выполним')


# sys.path
# очень важная переменная
# она хранит пути по которым python ищет модули
# она имеет изменяемый тип данных list
# таким образом мы можем изменять эту переменную
# мы можем импортировать
# import math
# но не можем импортировать наш модуль например на диске С:
# import mymodule
# как питон находит модули?
# import sys
# print(sys.path)
# print(type(sys.path))
# for p in sys.path:
#     print(p)
# sys.path.append('D:/')
# import mymodule


# Пример.
# в папке с модулем создать 5 подпапок названия которых состоят
# из платформы на которой запушен интерпретатор и порядкового номера начиная с 1: 
# win32_l, win_32_2, ... Платформа может быть другой.
# import sys, os
# name = sys.platform
# for i in range(1, 6):
#     new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
#     os.mkdir(new_path)


# sys.argv
# Список аргументов командной строки при запуске скрипта python
# sys.argv[0] - путь до скрипта
# Остальные параметры передаются при вызове скрипта через пробел
# python my_script.py par1 par2 parЗ ...
# import sys
# for arg in sys.argv:
#     print(arg)
#     print(type(arg))

# Пример.
# В зависимости от параметра вызывать различные функции скрипта
# Параметр ping -> функция выводит pong
# 2 параметра name <Имя> -> функция приветствия пользователя
# параметр list показать содержимое текущей директории
import sys, os
def ping():
    print('pong')

def hello(name):
    print('Hello', name)

def get_info():
    print(os.listdir()) # выводит список всех папок и файлов директории

command = sys.argv[1]

if command == 'ping':
    ping()
elif command == 'list':
    get_info()
elif command == 'name':
    name = sys.argv[2]
    hello(name)

# заходим в ту же папку через терминал и запускаем параметры по очереди:
# python Модули.py ping
# python Модули.py list
# python Модули.py name Max

