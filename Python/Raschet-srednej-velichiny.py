'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников 
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''
f = open('task_3_file.txt', encoding='utf-8')

my_list = f.readlines()
salary = 0

for i in my_list:
    ls = i.split()
    if salary == 0:
        salary = int(ls[1])
    else:
        salary = salary + int(ls[1])
    if int(ls[1]) < 20000:
        print(f'{ls[0]} имеет оклад меньше 20000')

print('Средний доход сотрудников составляет:', salary/len(my_list))

f.close()


# Вариант решения
with open("text_3.txt", "r") as my_file:
    s_sum = []
    less = []
    line = my_file.read().split("\n")
    for i in line:
        i = i.split()
        if int(i[1]) < 20000:
            less.append(i[0])
        s_sum.append(i[1])

print(f"Salary less 20 000 {less}. Average salary - {sum(map(int, s_sum)) / len(s_sum)}")


# Вариант решения
def task_3():
    wages = {}
    try:
        with open('task_3.txt', 'r', encoding='utf-8') as file:
            for line in file:
                wages[line.split()[0]] = float(line.split()[1])
        print('Меньше 20000 получают:')
        for name, wage in wages.items():
            if wage < 20000:
                print(name)
        print(f'Средняя зарплата равна {sum(wages.values()) / len(wages)}')
    except IOError:
        print('Бухгалтер сбежал с ведомостью. Зарплаты не будет')
    except:
        print('Что-то пошло не так')

task_3()
print('Итого как всегда меньше всех работал и больше всех получает )))')