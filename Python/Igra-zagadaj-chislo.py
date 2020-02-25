# Игра - Загадай число
# В этой игре человек загадывает число, а компьютер пытается его угадать
import random   # вызываем встроенную функцию получения рандомного числа

min_num = 1
max_num = 100
result = None # Объявляем заранее переменную, чтобы зайти в цикл
while result != '=':
    number = random.randint(min_num, max_num)
    print(number)
    result = input(' = > (загаданное число больше) < ')
    if result == '>':
        min_num = number + 1
    elif result == '<':
        max_num = number - 1
print('Победа!')