'''
Создать программно файл в текстовом формате, записать в него построчно данные, 
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''
with open('task_1_file.txt', 'w', encoding='utf-8') as f:
    while True:
        text = input('Введите построчно текст, в конце каждой строки '
					'нажимая "Enter" (для завершения ввода нажмите "Enter" без ввода текста): ')
        if text == '':
            break
        else:
            f.write(text + '\n')

# Вариант решения
while True:
    line = input("Enter - ").split()
    if not line:
        break
    with open("text.txt", "a") as my_file:
        for i in range(len(line)):
            print(line[i], file=my_file)
            #  my_file.write(line[i] + '\n')