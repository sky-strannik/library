import redis
r = redis.Redis(host='192.168.0.107', port=6379, db=0)

# Создадим счетчик global_user_id для пользователей:
r.set('global_user_id', 1)
user_id = int(r.get('global_user_id'))

# Создадим тестовых пользователей:
r.set('user:%d:name' % user_id, 'John')
r.set('user:%d:age' % user_id, 25)

user_id = int(r.incr('global_user_id'))

r.set('user:%d:name' % user_id, 'Jane')
r.set('user:%d:age' % user_id, 21)

# Назначим каждому из пользователей фильмы, которые ему нравятся. 
# Для наглядности конечного вывода, пересечения двух множеств, 
# фильмы хранятся как их полные названия, а не их id.

r.sadd('user:1:films', 'The Expendables')
r.sadd('user:1:films', 'Iron Man 2')
r.sadd('user:1:films', 'Prince of Persia')

r.sadd('user:2:films', 'State of Play')
r.sadd('user:2:films', 'Iron Man 2')
r.sadd('user:2:films', 'The Expendables')

# Посмотрим какие фильмы нравятся обоим пользователям:
email = r.sinter(['user:1:films', 'user:2:films'])

print(email)