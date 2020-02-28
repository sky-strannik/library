# # import json
# from pymongo import MongoClient

# # соединяемся с сервером базы данных 
# # client = MongoClient()
# # client = MongoClient('localhost', 27017)
# client = MongoClient('192.168.0.107', 27017)
# # docs = client.python.test.find({"title": "Test Base"})

# # выбираем базу данных
# db = client.python
# # db = client['python']

# # выбираем коллекцию документов
# # docs = db.test.find({"title": "Test Base"})

# # for doc in docs:
# #     print(doc)


# # Примеры:

# # Осуществляем добавление документа в коллекцию,
# # который содержит поля name и surname - имя и фамилия
# doc = {"name":"Иван", "surname":"Иванов"}
# db.coll.save(doc)

# # Альтернативное добавление документа
# db.coll.save({"name":"Петр", "surname":"Петров"})
 
# # Выводим все документы из коллекции coll
# for men in db.coll.find():
#     print(men)
 
# # Выводим фамилии людей с именем Петр
# for men in db.coll.find({"name": "Петр"}):
#     print(men["surname"])
 
# # Подсчет количества людей с именем Петр
# print(db.coll.find({"name": "Петр"}).count())
 
# # Добавляем ко всем документам новое поле sex - пол
# db.coll.update({}, {"$set":{"sex": "мужской"}})
 
# # Всем Петрам делаем фамилию Новосельцев и возраст 25 лет
# db.coll.update({"name": "Петр"}, {"surname": "Новосельцев", "age": 25})
 
# # Увеличиваем всем Петрам возраст на 5 лет
# db.coll.update({"name": "Петр"}, {"$inc": {"age": 5}})



# Импортируем MongoClient:
import pymongo
from pymongo import MongoClient

# Подключение к БД MongoDB выполняется в формате:
# pymongo.MongoClient("mongodb://username:password@server_ip:port/")
client = pymongo.MongoClient("mongodb://root:1@192.168.0.107:27017/")

# Выбираем базу данных:
db = client.python

# выбираем коллекцию документов
docs = db.test.find({"title": "Test Base"})

for doc in docs:
    print(doc)
