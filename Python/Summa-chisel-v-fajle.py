'''
Создать (программно) текстовый файл, записать в него программно набор чисел, 
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле 
и выводить ее на экран.
'''
from random import randrange

with open('task_5_file.txt', 'w') as f:
    for i in range(10):
        f.write(str(randrange(1, 20)) + ' ')

with open('task_5_file.txt', 'r') as f:
    line = f.readline().split()
    s = sum([int(el) for el in line])
    print(f'Сумма чисел: {s}')

# Вариант решения
from random import randint

sum_el = 0
with open("text.txt", "w") as my_file:
    for i in range(100):
        el = randint(1, 100)
        sum_el += el
        my_file.write(str(el) + " ")

print(f"Sum of elements - {sum_el}")