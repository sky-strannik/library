# Конвертируем строку в дату
import pymongo, datetime
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://root:1@192.168.0.107:27017/")
db = client.vk

for item in db.users.find():
    if 'created_at' in item:
        item['created_at'] = datetime.datetime.strptime(item['created_at'], '%Y-%m-%d %H:%M:%S')
        db.users.replace_one({'_id': item['_id']}, item)