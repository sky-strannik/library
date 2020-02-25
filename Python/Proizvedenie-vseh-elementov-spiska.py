'''
Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''
from functools import reduce

def my_func(prev_el, el):
    return prev_el + el

print(reduce(my_func, list(range(100, 1001, 2))))

# Вариант решения
from functools import reduce

def sum_list(el_1, el_2):
    return el_1 * el_2

uniq_list = [el for el in range(100, 1001, 2)]
print(f"List\n{uniq_list}\nMultiplication of numbers\n{reduce(sum_list, uniq_list)}")

# Вариант решения
from functools import reduce

list = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(lambda a, b: a * b, list))