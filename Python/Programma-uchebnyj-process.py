'''
Необходимо создать (не программно) текстовый файл, где каждая строка 
описывает учебный предмет и наличие лекционных, практических 
и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество 
занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) - 10(лаб)
Физкультура: - 30(пр) -
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
dict_ = {}

with open('task_6_file.txt', 'r', encoding='utf-8') as f:
    for i in f:
        name, hours = i.split(':')
        hours_sum = sum(map(int, "".join([i for i in hours if i == ' ' or  (i >= '0' and i <= '9')]).split()))
        dict_[name] = hours_sum

print(dict_)


# Вариант решения
plan = {}
hours = []
with open("text_6.txt") as lesson5_6:
    for subject in lesson5_6:
        subject_split = subject.split()
        subject_name = subject_split[0]
        all_hours = subject_split[1:]
        plan[subject_name] = 0
        for types in all_hours:
            try:
                plan[subject_name] += int(types[:types.find("(")])
            except ValueError:
                pass

print(plan)


# Вариант решения через регулярные выражения
from re import findall

d = dict()
with open('text_6.txt', 'r') as f:
    for line in f:
        key = findall('\w*', line)[0]
        values = [int(i) for i in findall('\d+', line)]
        s = 0
        for v in values:
            s += v
        d[key] = s

print(d)