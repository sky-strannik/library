# Скрипт будет с параметрами, поэтому импортируем
import sys
# Для удобства при импорте перечисляем все функции
from core import create_file, create_folder, get_list, get_list2, delete_all, copy_all, save_info

save_info('Начало работы')

# command = sys.argv[1]
try:
    command = sys.argv[1]
except IndexError:
    print('Отсутствуют параметры')

if command == 'list':
    get_list() # получаем список файлов и папок
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название папки')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла или папки')
    else:
        delete_all(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует первый параметр')
    try:
        name = sys.argv[3]
    except IndexError:
        print('Отсутствует второй параметр')
    # выдает ошибку при копировании :(
    try:
        copy_all(name, new_name)
    except Exception:
        print('Неизвестная ошибка')
    # name = sys.argv[2]
    # new_name = sys.argv[3]
    # copy_all(name, new_name)
elif command == 'help':
    print('list - Список файлов и папок')
    print('create_file - Создание файла')
    print('create_folder - Создание папки')
    print('delete - Удаление файла или папки')
    print('copy - Копирование файла или папки')

save_info('Завершение работы')
# После запуска можно посмотреть записи в log.txt
