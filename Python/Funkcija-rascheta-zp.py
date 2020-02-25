'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной 
платы сотрудника. В расчете необходимо использовать формулу: 
(выработка в часах*ставка в час) + премия. 
Для выполнения расчета для конкретных значений 
необходимо запускать скрипт с параметрами. 
'''
from sys import argv

script_name, param_1, param_2, param_3 = argv

def salary(par_1, par_2, par_3):
    try:
        return float(par_1) * float(par_2) + float(par_3)
    except ValueError:
        return 'Ошибочный ввод значений'

print("Зарплата сотрудника составляет: ", salary(param_1, param_2, param_3))

# Вариант решения
from sys import argv

def salary():
    try:
        time, stavka, premia = map(int, argv[1:])
        print(f"Salary - {time * stavka + premia}")
    except ValueError:
        print("Enter all 3 numbers. Not string or empty character.")

salary()