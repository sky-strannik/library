'''
Реализовать функцию, принимающую два числа (позиционные аргументы) 
и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "Division by zero forbidden!!!"
    return div_num

print(div(input("Enter first number - "), input("Enter second - ")))