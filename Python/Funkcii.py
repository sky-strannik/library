# Полезные встроенные функции:
# abs - модуль числа (отбросить '-')
# min, max - минимальное, максимальное значение
# round - округление числа
# sum - сумма элементов последовательности
# enumerate - нумерация последовательности

# модуль числа (отбросить '-')
print(abs(-7))

# min, max - минимальное, максимальное значение
numbers = [5, 15, 7, 1, -9, 0]
print(max(numbers))
print(min(numbers))

# round - округление числа
print(round(10.9872, 2)) # '2' - это кол-во знаков после запятой

# sum - сумма элементов последовательности
print (sum(numbers))

# enumerate - нумерация последовательности
winners = ['Leo', 'Max', 'Kate'] 
for number, winner in enumerate(winners, 1): # '1' - это номер с которого начинать нумерацию, по умолчанию '0'
	print(number, winner)


# ПРИМЕРЫ:

# Пользователь вводит 3 числа
# Найти минимальное, максимальное и их сумму, результат вывести на экран
numbers = []
for i in range(3): # ограничиваем цикл 3-мя итерациями
    number = int(input('Введите число: '))
    numbers.append(number) # добавить результат в список
print(max(numbers))
print(min(numbers))
print(sum(numbers))


# Функция простой разделитель (с параметрами)
# Объявляем функцию:
def print_sep():
    print('-' * 100)
# Вызов (использование) функции:
print_sep()

# Меняем знак разделителя (используем один параметр):
def print_sep2(sep):        # один параметр
    print(sep * 100)
print_sep2('*')             # вызываем функцию
print_sep2('-')             # вызываем функцию

# Меняем знак и длину разделителя (используем два параметра):
def print_sep3(sep, sep_len): # два параметра
    print(sep * sep_len)
print_sep3('*', 100)        # вызываем функцию
print_sep3('-', 50)         # вызываем функцию

# Используем разделитель в тексте (функция с возвратом параметров)
def get_sep(sep, sep_len):  # два параметра
    return sep * sep_len    # возврат значения параметров
sep = get_sep('-', 10)
text = 'Hello {} Func {}'.format(sep, sep)
print(text)


# ПАРАМЕТРЫ ФУНКЦИИ
# def my_func(параметр 1, параметр 2, ...)
def hello():
    print('Hello', 'Max')
hello()

def hello2(who):
    print('Hello', who)
hello2('Leo')

# Передача параметров по порядку:
def hello3(who, say):
    print(say, who)
hello3('Leo', 'Hi')
hello3('Max', 'Hello')

# Передача параметров по имени:
def hello4(who, say):
    print(say, who)
hello4(say='Hi', who='Leo')

# Параметры значения по умолчанию:
def hello5(who, say='Hello'):
    print(say, who)
hello5('Leo')   # если 2-й параметр не задан, то say подставит по умолчанию Hello


# Передача любого кол-ва аргументов:
# def hello('Hello', 'Leo', 'Max', 'Kate', ...)
# *args - передача любого кол-ва по порядку
# **kwargs - передача любого кол-ва по имени
def greeting(say, *args): # общепринятый параметр '*args' позволяет передать любое кол-во параметров по порядку
    print(say, args)
greeting('Hello', 'Leo')
greeting('Hello', 'Leo', 'Max')
greeting('Hello', 'Leo', 'Max', 'Kate') # получаем кортеж

def get_person(**kwargs): # общепринятый параметр '**kwargs' позволяет передать любое кол-во параметров по имени
    for k, v in kwargs.items():
        print(k, v)
get_person(name='Leo', age=20, has_car=True) # получаем словарь


# Область видимости - это область программы в пределах которой доступнен идентификатор перемененной и т.п.
# Пример 1.
def my_f(my_var):
    my_var = 999
    print('Внутри функции: ', my_var)

ab = 1
my_f(ab)
print('После выполнения функции: ', ab)

# Пример 2.
def some_f():
    a = 999
    print('Внутри функции: ', a)

b = 1
some_f()
print('После выполнения функции: ', b)


# Глобальные переменные доступны за пределами функции во всем коде программы
# Пример.
global_var = 1 # если переменная задана до объявления функции, то она становится глобальной и доступна везде
def my_fu():
    # global global_var # расскомментить для теста global здесь и внизу функции global_var = 999
	# локальная переменная 
	local_var = 100
	# мы можем использовать локальную переменную внутри функции 
	print(local_var)
	# глобальная переменная, объявлена в модуле 
	print(global_var)
	# но глобальную переменную сейчас нельзя изменить:
	# global_var = 999
    # чтобы ее изменить, нужно указать что она глобальная: global my_var, но это чревато ошибками за пределами функции!

my_fu()
print(global_var)
# а тут недоступна локальная перменная:
# print (local_var)


# Вложенные друг в друга функции
# Тогда мы рассматриваем область видимости относительно какой-либо функции
# def(a):
#      def(b):
#           def(c):
m = 'Меня видно везде'
def a():
    ma = 'Меня видно в Ь() и в а()'

    def Ь():
        print(m)
        print(ma)
        mb = 'Меня видно в c() и в Ь() но не видно в а'

        def c():
            print(m)
            print(ma)
            print(mb)
            mc = 'Меня видно только в с'
            print (mc) 
        c()
    Ь()
a()


# Передача функции параметром в другие функции
def smm():
    return 10

result = smm() # сохраняем функцию как объект в переменную
print(result)

a = smm # переменная становится функцией
print(a)

print(type(a))  # смотрим тип функции
print(a())      # выводим функцию уже с другим именем


def f():
    print('Hello')

def to(f_param):
    # параметром будет функция
    # поэтому в теле функции to мы ее вызовем
    f_param()

# проверим
to(f)

# Применение
# возможность не только входных данных, но и входных функций
# внутри функции переменными являются:
# алгоритм
# последовательность действий
# сами действия

# Пример.
def my_filter(numbers): 
	result = []
	for number in numbers: 
		if number % 2 == 0:
			result.append(number)
	return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(my_filter(numbers))

# модернизируем функцию, чтобы не плодить новые
def my_filter2(numbers2, function): 
	result = []
	for number in numbers2: 
		if function(number): # если вернет True, то записываем в функцию это число
			result.append(number)
	return result

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8]

# снова получаем четные числа
def is_even(number):
    return number % 2 == 0
print(my_filter2(numbers2, is_even))

# если нужны нечетные числа
def is_not_even(number):
    return number % 2 != 0
print(my_filter2(numbers2, is_not_even))

# если нужны числа > 4
def big_4(number):
    return number > 4
print(my_filter2(numbers2, big_4))


# lambda-функции
# применяются для создания анонимных функций по месту их использования
# lambda входные параметры: результат
def my_filter3(numbers3, function): 
	result = []
	for number in numbers3: 
		if function(number): # если вернет True, то записываем в функцию это число
			result.append(number)
	return result

numbers3 = [1, 2, 3, 4, 5, 6, 7, 8]

# если больше применять не будем, то вместо функции is_even, используем lambda-функцию
# def is_even(number):
#    return number % 2 == 0
print(my_filter3(numbers3, lambda number: number % 2 == 0))
print(my_filter3(numbers3, lambda number: number % 2 != 0))
print(my_filter3(numbers3, lambda number: number > 4))


# Функции sorted, filter, map

# sorted
# сортировка последовательности
# sorted(iterable, *, кеу=Nоne, reverse=False)
# аргументы: последовательность, ключ для сортировки, порядок

# набор чисел
numbers = [1, 5, 3, 5, 9, 7, 11]
# сортировка по возрастанию 
print(sorted(numbers))
# сортировка по убыванию
print(sorted(numbers, reverse=True))

# набор строк
names = ['Max', 'Alex', 'Kate']
# сортировка по алфавиту
print(sorted(names))

# города и численность населения (цифры не настоящие)
cities = [('Москва', 1000), ('Лас-Вегас', 500), ('Антверпен', 2000)]
# такая сортировка сработает по алфавиту
print(sorted(cities))

# как отсортировать по численности населения?
def by_count(city):
    return city[1]
print(sorted(cities, key=by_count)) # передаем функцию в переменную без параметров
# или вместо def by_count используем lambda-функцию
print(sorted(cities, key=lambda city: city[1]))


# filter
# Фильтрация последовательности
# filter(function, iterable)
# Аргументы: функция фильтрации, последовательность

# набор чисел
numbers = (1, 2, 3, 4, 5, 6, 7, 8)

# получить только четные числа
def is_even5(number):
	return number % 2 == 0 # только для четных чисел

result = filter(is_even5, numbers)
print(result)
result = list(result)
print(result)

# набор строк
names = ['Max', 'Leo', 'Kate']

# получить строки больше 3-х символов
# print(filter(names, ))
print(list(filter(lambda x: len(x)>3, names)))


# map
# применение функции к каждому элементу последовательности
# map(func, iterable, ...)
# аргументы: функция, последовательность

# набор чисел
numbers = [5, 3, 4, 7, 8]
# получить список квадратов чисел
print(list(map(lambda x: x**2, numbers)))
# привести числа к строке
print(list(map(lambda x: str(x), numbers)))
