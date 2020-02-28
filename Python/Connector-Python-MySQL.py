# Данный тип подключения возращает данные в виде словаря
# import pymysql.cursors

# connection = pymysql.connect(host='192.168.0.107',
#     port=3306,
#     user='root',
#     password='1',                             
#     db='vk',
#     charset='utf8mb4',
#     cursorclass=pymysql.cursors.DictCursor)

# cursor = connection.cursor()

# cursor.execute('SELECT * FROM users LIMIT 10')
# for row in cursor:
#     print(row)

# cursor.close()
# connection.close()



# Данный метод возвращает данные в виде словаря
# а также сразу автоматически закрывает соединение
from contextlib import closing
import pymysql.cursors

connection = pymysql.connect(host='192.168.0.107',
    port=3306,
    user='root',
    password='1',                             
    db='vk',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

with closing(connection) as connection:
	with connection.cursor() as cursor:
		query = """SELECT * FROM users LIMIT 10"""
		cursor.execute(query)
		for row in cursor:
			print(row)
