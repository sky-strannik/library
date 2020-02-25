'''
Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
'''
with open('task_2_file.txt', 'w', encoding='utf-8') as f:
    my_list = ['Я помню чудное мгновенье:', 'Передо мной явилась ты,', 'Как мимолетное виденье,', 'Как гений чистой красоты.']
    for i in my_list:
        f.write(i + '\n')

f = open('task_2_file.txt')

my_list = []
for i in f: 
    my_list.append(len([len(i) for x in i.split()]))
print('Кол-во строк:', len(my_list))

for i in range(len(my_list)):
    print(f'{i+1} строка: {my_list[i]} слова')

f.close()

# Вариант решения
counter = 0
with open("text_2.txt", "r") as f_obj:
    for line in f_obj:
        counter += 1
        line_words = line.split(' ')
        print(line, 'Длина строки: ', len(line_words))
    print('Всего строк: ', counter)

# Вариант решения
with open("text_2.txt") as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line):
        number_of_words = len(value.split())
        print('Строка {} содержит {} слов'.format(index + 1, number_of_words))