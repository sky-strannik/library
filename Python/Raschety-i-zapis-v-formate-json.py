'''
Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки. 
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
а также среднюю прибыль. Если фирма получила убытки, в расчет средней 
прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами 
и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков). 
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''
import json

cnt = 0
average_profit = 0
f_dict = {}

with open('task_7_file.txt', 'r', encoding='utf-8') as f:
    for i in f:
        ls = i.split()
        ls.pop(1)
        firm = ls[0]
        ls.pop(0)

        # Считаем и записываем прибыль
        res = int(ls[0]) - int(ls[1])
        if res > 0:
            if average_profit == 0:
                average_profit = res
            else:
                average_profit = average_profit + res
            cnt += 1

        # Упаковываем в словарь
        f_str = {firm: res for c in ls}
        f_dict.update(f_str)

# Получаем среднюю прибыль
average_profit = average_profit / cnt
# Приводим к нужному формату
to_json = [f_dict, {'average_profit': average_profit}]

# Записываем JSON в файл
with open('task_7_2_file.json', 'w', encoding='utf-8') as f:
    json.dump(to_json, f, indent=2, ensure_ascii=False)


# Вариант решения
import json

with open('07listFirm.txt', 'r', encoding='utf-8') as fIn:
    allProfit = []
    allFirms = []
    dallFirmProfit = {}
    for sLine in fIn:
        sline = sLine[:-1]
        lLine = sLine.split()
        try:
            lLine[2] = int(lLine[2])
            lLine[3] = int(lLine[3])
        except ValueError:
            print('Некоректные данные в исходном файле')
            exit()
        profit = lLine[2] - lLine[3]
        lLine.append(profit)
        dallFirmProfit[f'{lLine[1]} \'{lLine[0]}\''] = profit
        if profit > 0:
            # Прибыль
            allProfit.append(profit)

averageProfit = sum(allProfit) / len(allProfit)
dAverageProfit = {}
dAverageProfit['average_profit'] = averageProfit
result = [dallFirmProfit, dAverageProfit]

with open("my_file.json", 'w', encoding='utf-8') as fOut:
    json.dump(result, fOut)


# Вариант решения
import json
import codecs

with codecs.open("text_77.json", "w", encoding='utf-8') as j_file:
    with open('text_7.txt', encoding='utf-8') as my_file:
        subjects = {}
        middle = {}
        k, o = 0, 0
        line = my_file.read().split("\n")
        for i in line:
            i = i.split()
            profit = int(i[2]) - int(i[3])
            subjects[i[0]] = profit
            if profit > 0:
                k += profit
                o += 1
            middle["average_profit"] = k/o
        all_list = [subjects, middle]
        json.dump(all_list, j_file, ensure_ascii=False, indent=4)

print(f"All information on firms:\n{line}\n\nTotal list:\n{all_list}")