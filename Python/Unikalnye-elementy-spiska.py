'''
Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать итоговый массив чисел, соответствующих требованию. 
Элементы вывести в порядке их следования в исходном списке. 
Для выполнения задания обязательно использовать генератор. 
'''
result = [el for el in list(range(3, 9)) if list(range(3, 9)).count(el) == 1]
print(result)

# Вариант решения
from random import randint

my_list = [randint(-10, 10) for i in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Source list\n{my_list}\nNo repetition list\n{uniq_list}")

# Вариант решения
my_list = [2, 4, 6, 6, 7, 7, 8, 8, 2, 3, 1]
new_list = [el for el in dict.fromkeys(my_list)]
print(f"Исходный список: {my_list} ")
print(f"Новый список: {new_list} ")