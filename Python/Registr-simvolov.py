'''
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв 
и возвращающую его же, но с прописной первой буквой. 
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, 
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. 
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func().
'''
def int_func(words):
    # function takes words(split by space) and uppercase first letter in any words
    # verify that the all letters its lower latin script and spaces
    for i in words:
        if not ord(i) == 32 and not 97 <= ord(i) <= 122:
            print("Lower latin script and spaces between!\n")
            words = input("Enter words with a space(lower latin script):\n")
            break
    words_list = words.split()
    for i in range(len(words_list)):
        print(words_list[i][0].upper() + words_list[i][1:], end=" ")

int_func(input("Enter words with a space(lower latin script):\n"))

# вариант решения

def int_func(word):
    words, result = [], []
    if len(word) > 0:
        for i in word.split():
            words.append(i[0].upper() + i[1:])
        result = ' '.join(words)
    return result

print(int_func(input("Введите строку: ")))

# вариант решения

int_func = lambda sentence: print(sentence.title())

int_func(input("Please enter set of words. "))