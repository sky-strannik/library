'''
Реализовать два небольших скрипта: 
а) бесконечный итератор, генерирующий целые числа, начиная с указанного, 
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. 
'''
from itertools import count, cycle

num = input('Введите два положительных целых числа через пробел, где второе больше первого: ').split()
for el in count(int(num[0])):
    try:
        if el > int(num[1]):
            break
        else:
            print(el)
    except:
        print('Ошибка ввода')
        break

my_list = ['one', 'two', 'tree', 'four', 'five']
iter = cycle(my_list)

for i in my_list:
    print(next(iter))


# Вариант решения
from itertools import count, cycle

print('Программа генерирует целые числа, начиная с указанного.'
			' Для генерации следующего числа необходимо нажать Enter,'
      ' для выхода из программы - "q"')
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print(
    'Программа повторяет элементы списка. Для генерации следующего'
		' повторения необходимо нажать Enter, для выхода'
    ' из программы - "q"')
u_list = input('Введите список, разделяя элементы пробелом: ').split()
iter = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter), end='')
    quit = input()


# Вариант решения
from itertools import islice, cycle, count

def unexpected(start_el, stop_el, num_str):
    try:
        start_el, stop_el, num_str = int(start_el), int(stop_el), int(num_str)
        my_list = [el for el in islice(count(start_el), 1, stop_el + 1)]
        #  repeat_list = [next(cycle(my_list)) for el in range(num_str)]
        r_list = iter(el for el in cycle(my_list))
        repeat_list = [next(r_list) for _ in range(num_str)]
        print(my_list)
        return repeat_list
    except ValueError:
        return "Value Error"
    except TypeError:
        return "TypeError"

print(unexpected(input("List starting at - "), input("from to - "), input("Number of repetition - ")))


# Вариант решения
import itertools as it

# integers iterator with checking for integer
try:
    integers = iter(i for i in it.count(int(input("Enter starting integer: "))))
    print(f"first numbers in the 'integers' iterator: {next(integers)} {next(integers)} {next(integers)}\n")
except:
    print("Error, only integers!")
# cycle iterator
my_list = ['go', 1, 2, "hello"]
print(f"List - {my_list}")
cycle_iter = iter(i for i in it.cycle(my_list))
print(f"first elements in the 'cycle' iterator: {next(cycle_iter)} {next(cycle_iter)} "
      f"{next(cycle_iter)} {next(cycle_iter)} {next(cycle_iter)} {next(cycle_iter)}\n")