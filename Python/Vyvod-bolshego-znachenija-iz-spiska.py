'''
Представлен список чисел. Необходимо вывести элементы исходного списка, 
значения которых больше предыдущего элемента. Подсказка: элементы, 
удовлетворяющие условию, оформить в виде списка. Для формирования 
списка использовать генератор.
'''
a = [10, 30, 24, 17, 40]
b = []

for i in range(len(a)):
    if int(a[i]) > int(a[i-1]):
        b.append(int(a[i]))

print(a)
print(b)

# Вариант решения
my_list = [2, 4, 1, 6, 9, 33, 7]
more_then = [el for num, el in enumerate(my_list) if my_list[num] > my_list[num - 1]]
print(more_then)

# Вариант решения
my_list = [15, 16, 2, 3, 1, 7, 5, 4, 10]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)