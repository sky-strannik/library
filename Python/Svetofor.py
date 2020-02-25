'''
Создать класс TrafficLight (светофор) и определить у него один атрибут
color (цвет) и метод running (запуск). Атрибут реализовать как приватный. 
В рамках метода реализовать переключение светофора в режимы: 
красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, 
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке 
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр 
и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, 
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
import time

class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый', 'желтый']

    def running(self):
        print('Для выхода нажмите Ctrl + C')
        while True:
            try:
                for i in TrafficLight._TrafficLight__color:
                    if i == 'красный':
                        print(i)
                        time.sleep(7)
                    elif i == 'зеленый':
                        print(i)
                        time.sleep(5)
                    else:
                        print(i)
                        time.sleep(2)
            except KeyboardInterrupt:
                break
            except:
                print('Ошибка в работе светофора!')
                break

start = TrafficLight()
start.running()


# Вариант решения
from time import sleep, perf_counter
from itertools import cycle

class TrafficLight:
    """ В private переменной color находится матрица, с цветом и временем переключения.
    В методе используется бесконечный цикл, который повторяет перебор элементов перемнной
    с необходимым ожиданием в секундах.
    """

    __color = [["red", 7], ["yellow", 2], ["green", 7], ["yellow", 2]]

    def running(self):
        for el in cycle(self.__color):
            for i, val in enumerate(self.__color):
                print(self.__color[i][0], perf_counter())
                sleep(self.__color[i][1])

light_1 = TrafficLight()
light_1.running()


# Вариант решения
from time import sleep

class TrafficLight:
    __color = "Черный"

    def running(self):
        while True:
            print("Trafficlight is red now")
            sleep(7)
            print("Trafficlight is yellow now")
            sleep(2)
            print("Trafficlight is green now")
            sleep(7)
            print("Trafficlight is yellow now")
            sleep(2)

trafficlight = TrafficLight()
trafficlight.running()


# Вариант решения
from time import *

class TrafficLight:
    __color = ['Зеленый', 'Желтый', 'Красный']
    stage = 1

    def running(self):
        i = 0
        while True:
            if TrafficLight.stage == 1:
                if i == 3: i = 0
                print('Светофор мигает')
                TrafficLight.stage = 2
                sleep(2)
            else:
                print(TrafficLight.__color[i])
                TrafficLight.stage = 1
                i += 1
                sleep(7)

t = TrafficLight()
t.running()


# Вариант решения
from time import sleep

class TrafficLight:
    __color = 0

    def running(self):
        # [красный, жёлтый, зелёный]
        lights = [
            {
                'name': 'красный',
                'color': '\x1b[41m',
                'delay': 7
            },
            {
                'name': 'жёлтый',
                'color': '\x1b[43m',
                'delay': 2
            },
            {
                'name': 'зелёный',
                'color': '\x1b[42m',
                'delay': 5
            }
        ]

        print('\nИмитация работы светофора:\n')

        while True:
            # формируем строку вывода (светофор)
            s = ''
            for i in range(3):
                if i == self.__color:
                    s += f'({lights[self.__color]["color"]}   \x1b[0m)'
                else:
                    s += '(   )'

            print(f'\r{s}', end='')
            # устанавливаем задержку
            sleep(lights[self.__color]["delay"])
            # меняем цвет
            self.__color = (self.__color + 1) % 3

lights = TrafficLight()
lights.running()