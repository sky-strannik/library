# Словари diсt - это неупорядоченные коллекции произвольных объектов с доступом по ключу
# my_dict = {key1: val1, key2: val2, ...}
# dog = {'name': 'Rocky', age: 3}
# Пример простого словаря:
friend = {
    'name': 'Max',
    'age': 23
}
print(friend)
print(type(friend))

# Основные действия со словарем:
# получение элемента по ключу friend['name']
# добавление значения friend['has_car'] = True
# изменение значения friend['has_car'] = False
# удаление значения remove friend['age']
# оператор in 'age' in friend

print(friend['age'])        # получение элемента по ключу

friend['has_car'] = True    # добавление значения
print(friend)

friend['has_car'] = False   # изменение значения
print(friend)

del friend['age']           # удаление значения
print(friend)

if 'has_car' in friend:     # оператор in
    print('Есть ключ has_car!')

# Варианты перебора словаря:
# по ключам
# по значениям
# по парам ключ, значение
friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}

# по ключам (ключ/значение)
for key in friend.keys():
    print(key)
    print(friend[key])
# или (ключи/значения)
for key in friend:
    print(key)
    print(friend[key])

# по значениям (только значения)
for val in friend.values():
    print(val)

# пары ключ / значение в виде кортежа
for item in friend.items():
    print(item)

# пары ключ / значение сразу раскладываем по переменным key, val
for key, val in friend.items():
    print(key)
    print(val)
