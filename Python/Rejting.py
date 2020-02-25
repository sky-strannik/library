'''
Реализовать структуру «Рейтинг», представляющую собой 
не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2. 
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, 
например, my_list = [7, 5, 3, 3, 2].
'''
my_list = [4, 3, 3, 2, 1]

while True:
    print(f"Current rating: {my_list}")
    number = input("Enter rating number or 111 to finish - ")
    if number.lstrip('-').isdigit() and number != "111":
        number = int(number)
        if my_list.count(number):
            my_list.insert(my_list.index(number) + my_list.count(number), number)
        else:
            param = 0
            n_param = 0
            for n, i in enumerate(my_list):
                if number > i:
                    if param < i:
                        param = i
                        n_param = n
                else:
                    n_param = n + 1
            my_list.insert(n_param, number)
    elif not number.isdigit():
        print("Enter number please")
    else:
        break

# вариант решения
# без отрицательных значений

my_list = [4, 3, 3, 2, 1, 0]

while True:
    print(f"Current rating: {my_list}")
    number = input("Enter rating number or 111 to finish - ")
    if number.isdigit() and number != "111":
        number = int(number)
        if my_list.count(number):
            my_list.insert(my_list.index(number) + my_list.count(number), float(number))
        else:
            param = 0
            n_param = 0
            for n, i in enumerate(my_list):
                if number > i:
                    my_list.insert(n, number)
                    break
                else:
                    my_list.append(number)
    elif not number.isdigit():
        print("Enter number please")
    else:
        break

# вариант решения

rating = [7, 5, 3, 3, 2]
print(f'\nRating: {rating}')
print('Enter some natural numbers. Press Enter to exit... ')

while True:
    n = input(' > ')
    if n == '':  # если нажата клавиша Enter - выход из цикла
        break
    try:
        n = int(n)
    except ValueError:
        print('Incorrect value.')
        continue
    if n < 0:
        print('Incorrect value.')
        continue
    for i, val in enumerate(rating):
        if n > val:
            rating.insert(i, n)
            break
    else:
        rating.append(n)
    print(f'{rating}')

# вариант решения

rating = [9, 8, 7, 7, 6, 5, 4, 3, 3, 3, 2, 1]
new = int(input('Enter some number'))

if new in rating:
    rating.reverse()
    index = rating.index(new)
    rating.insert(index, new)
    rating.reverse()
else:
    if min(rating) > new:
        rating.extend([new])
    else:
        for i in range(len(rating)):
            if rating[i] < new:
                rating.insert(i, new)
                break
print(rating)