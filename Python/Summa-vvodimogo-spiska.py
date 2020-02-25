'''
Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, 
разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, то вначале нужно добавить 
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''
def summary():
    ex = False
    fResult = 0
    while ex == False:
        lNumbers = input('Input numbers divided by whitespaces or q to quit: ').split()
        result = 0
        for i in range(len(lNumbers)):
            if lNumbers[i] == 'q':
                ex = True
                break
            else:
                result = result + int(lNumbers[i])
        fResult = fResult + result
        print(f"Current sum is {fResult}")
    print(f"You've quited! Final sum is {fResult}")

summary()

# вариант решения

def my_func():
    # function takes numbers lines (split by space) and sum all elements
    # verify that the numbers are entered correctly
    while True:
        try:
            inp = input("Enter your numbers with a space('q' in any position to exit after sum):\n")
            num_line = inp.split()
            # check the "q" button for exit the program
            if "q" in num_line:
                try:
                    global summ
                    num_line = list(map(float, num_line[:num_line.index("q")]))
                    summ += sum(num_line)
                    print(f"Total sum = {summ}   End of program")
                    break
                except ValueError:
                    print("Enter the numbers!\n")
            num_line = list(map(float, num_line))
            summ += sum(num_line)
            print(f"Total sum = {summ}\n")
        except ValueError:
            print("Enter the numbers!\n")

summ = 0
my_func()

# вариант решения

def sum_fun():
    all_sum = 0
    while True:
        sum_ = 0
        args = input("Enter numbers with a space - ").split()
        try:
            for n, i in enumerate(args):
                if i != "?":
                    sum_ += int(args[n])
                else:
                    all_sum += sum_
                    return f"The all sum - {all_sum}"
            print(sum_)
            all_sum += sum_
            answer = input("Enter more numbers? y/n - ")
            if answer == "y":
                continue
            else:
                break
        except ValueError:
            return f"Enter only numbers, the all sum - {all_sum}"
    return f"The all sum - {all_sum}"

print(sum_fun())

# вариант решения

num = 0
try:
    while num != '#':
        for i in map(int, input("Для выхода наберите '#'\nВведите числа, используя пробел.\n").split()):
            num += i
        print(num)
except ValueError:
    print(num)