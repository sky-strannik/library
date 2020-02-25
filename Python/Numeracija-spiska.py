'''
Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове. 
'''
string = (input("Enter the numbers with space - ")).split()
print(string)

for i in range(len(string)):
    if len(string[i]) <= 10:
        print(i, string[i])
    else:
        print(i, (string[i])[:10])

# вариант решения

string = (input("Enter the numbers with space - ")).split()

for n, i in enumerate(string):
    print(n + 1, i) if len(i) <= 10 else print(n, (i[:10]))

# вариант решения

my_string = input('Введите строку из нескольких слов, разделенных пробелами: ').split()

for i, word in enumerate(my_string, 1):
    print(f'{i} {word[:10]}')