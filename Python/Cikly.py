# Когда использовать for vs for range vs while
# for - перебор последовательности. Индекс не нужен
# for range - перебор последовательности. Нужен индекс
# for range - необходимо пропустить некоторые элементы или идти с конца в начало
# while - цикл связан с условием, но не с последовательностью

# Цикл while
i = 0
friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user') # кортеж - неизменяемый список
while i < len(friends): # если while True: - это бесконечный цикл с выходом по break
    print(i)
    i += 1 # Прибавляем 1
    # break # Выход из цикла независимо от выполнения/невыполнения условия
    # continue # Переход на следующую итерацию цикла (команды после continue не выполняются, т.е. сразу переходим в начало)
else: print('end') # (необязательный параметр) - else служит для проверки условия завершения цикла, т.к. внутри, например, может быть break

# Цикл for проходится по любому итерируемому объекту (например строке или списку), и во время каждого прохода выполняет тело цикла
for i in range(3): # ограничиваем цикл 3-мя итерациями
    print(f'Это Ваш друг {friends[i-1]}?')

for i in friends: # перебирает элементы по порядку без указания индекса. 'i' - это переменная в которую помещаются результаты в процессе перебора
    print(i, end=' ') # выводит данные в строку через пробел

for letter in friend_name:
    print(letter, end='- ')

for role in roles:
    print(role, end=';')

# Функция range
# Позволяет создавать последовательности целых чисел
# Чаще всего range используется с циклом for
numbers = range(10)
print(range)            # range(0, 10) - уже можно использовать в for
print(type(range))
print(list(numbers))    # [0, 1, ..., 9] - а это просто посмотреть что внутри

# Когда может помочь range
winners = ['Max', 'Leo', 'Kate']

# Простой перебор 
for winner in winners: 
	print(winner)
# или
for i in range(len(winners)):
    print(i)
    print(i+1, ')', winners[i])

# Параметры range
# range(start_or_stop, stop[, step])
# start_or_stop - начало или конец последовательности
# stop - конец
# step - шаг

# Вывести нечетные цифры от 1 до 5
numbers = [1, 3, 5]
for number in numbers:
	print(number)
# или
print(list(range(1, 10, 2)))
# или
for number in range(1, 10, 2):
	print(number)
