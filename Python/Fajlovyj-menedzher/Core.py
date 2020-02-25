import os
import shutil       # копирование
import datetime     # работа с датой и временем

# Функция для создания файла
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

# Функция для создания папки
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка уже существует')


# Функция выводит все файлы и папки
def get_list():
    print(os.listdir())

# Функция выводит только папки
def get_list2(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# Функция удаления файлов и папок
def delete_all(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


# Функция копирования файлов и папок
def copy_all(name, new_name):
    if os.path.isdir(name):
        try: # обрабатываем возможную ошибку
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Папка уже существует')
    else:
        shutil.copy(name, new_name)


# Функция сохранения информации в файл
def save_info(message):
    current_time = datetime.datetime.now() # текущая дата и время
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


# проверяем работу
if __name__ == "__main__":
    create_file('text.dat')
    create_file('text.dat', 'Text')
    create_folder('new_f')
    get_list()
    get_list2(True)
    # delete_all('new_f')
    # delete_all('text.dat')
    copy_all('new_f', 'new_test')
    copy_all('text.dat', 'text2.dat')
    save_info('Info')
