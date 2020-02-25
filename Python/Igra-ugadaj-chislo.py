# Игра - Угадай число
# Шаг 1. Задаем случайное число
import random   # вызываем встроенную функцию получения рандомного числа
number = random.randint(1, 100)
print(number)   # для тестирования выводим загаданное число

# Вариант 1.
# while True:
#     # Шаг 2. Предложить ввести число
#     user_number = int(input('Введите число: '))
#     # Шаг 3. Сравнение чисел и вывод результата
#     if number == user_number:
#         print('Победа!')
#         break
#     elif number < user_number:
#         print('Ваше число больше загаданного!')
#     else:
#         print('Ваше число меньше загаданного!')


# Вариант 2. Меняем условие, улучшаем код
# user_number = None
# while number != user_number:
#     # Шаг 2. Предложить ввести число
#     user_number = int(input('Введите число: '))
#     # Шаг 3. Сравнение чисел и вывод результата
#     if number < user_number:
#         print('Ваше число больше загаданного!')
#     elif number > user_number:
#         print('Ваше число меньше загаданного!')
# print('Победа!')


# Вариант 3. Добавляем кол-во максимальных попыток
# user_number = None
# count = 0
# max_count = 3
# while number != user_number:
#     count += 1
#     if count > max_count:
#         print('Вы проиграли!')
#         break
#     print(f'Попытка № {count}')
#     # Шаг 2. Предложить ввести число
#     user_number = int(input('Введите число: '))
#     # Шаг 3. Сравнение чисел и вывод результата
#     if number < user_number:
#         print('Ваше число больше загаданного!')
#     elif number > user_number:
#         print('Ваше число меньше загаданного!')
# else:
#     print('Победа!')


# Вариант 4. Добавляем уровни сложности
# user_number = None
# count = 0
# levels = {1:10, 2:5, 3:3} # Кол-во попыток кладем в словарь
# level = int(input('Выберите уровень сложности (1,2,3): '))
# max_count = levels[level]
# while number != user_number:
#     count += 1
#     if count > max_count:
#         print('Вы проиграли!')
#         break
#     print(f'Попытка № {count}')
#     # Шаг 2. Предложить ввести число
#     user_number = int(input('Введите число: '))
#     # Шаг 3. Сравнение чисел и вывод результата
#     if number < user_number:
#         print('Ваше число больше загаданного!')
#     elif number > user_number:
#         print('Ваше число меньше загаданного!')
# else:
#     print('Победа!')


# Вариант 5. Делаем игру многопользовательской
user_number = None
count = 0
levels = {1:10, 2:5, 3:3} # Кол-во попыток кладем в словарь

level = int(input('Выберите уровень сложности (1,2,3): '))
max_count = levels[level]

user_count = int(input('Введите кол-во игроков: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i+1}: ')
    users.append(user_name)
print(users)

is_winner = False
winner_name = None
while not is_winner:
    count += 1
    if count > max_count:
        print('Все игроки проиграли!')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        # Шаг 2. Предложить ввести число
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        # Шаг 3. Сравнение чисел и вывод результата
        elif number < user_number:
            print('Ваше число больше загаданного!')
        else:
            print('Ваше число меньше загаданного!')
else:
    print(f'Победитель {winner_name}!')
