'''
Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента. 
Использовать функцию type() для проверки типа. 
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''
my_list = [1, -2, False, 3.4, "Help", [1, 2, 3]]
p = dict()

for n in range(len(my_list)):
    p[n] = type(my_list[n])

print(p)

# вариант решения

my_list = [(-1 + 0j), 1, 2.2, True, None, 'String', [3, 4], (5, 6, 6.5), {7: 'seven', 8: 'eight'}, {9, 10}, frozenset(),
           range(11), (b'twelve'), bytearray(b'thirteen'), zip(*[(14, 15), (16, 17), ('a', 'b')]), TypeError]

for i, item in enumerate(my_list):
    print(f"{i}) {item} - {type(item)}")