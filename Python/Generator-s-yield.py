'''
Реализовать генератор с помощью функции с ключевым словом yield, 
создающим очередное значение. При вызове функции должен создаваться объект-генератор. 
Функция должна вызываться следующим образом: for el in fibo_gen(). 
Функция отвечает за получение факториала числа, а в цикле необходимо 
выводить только первые 15 чисел. Подсказка: факториал числа n — 
произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24. 
'''
from functools import reduce

def fibo_gen():
    for el in list(range(1, 30)):
        yield el

print(fibo_gen())

for el in fibo_gen():
    if el < 16:
        a = list(range(1, el+1))
        print(f'# {el} -', reduce(lambda x, y: x*y, a))
    else:
        break


# Вариант решения
from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

generator = fibo_gen()
x = 0
for i in generator:
    if x == 15:
        break
    else:
        x += 1
        print(f"Factorial {x} = {i}")
    

# Вариант решения
def fibo_gen(n):
    m = 1
    for i in range(1, n):
        if i > 15:
            break
        m *= i
        yield m

for i in fibo_gen(26):
    print(i)