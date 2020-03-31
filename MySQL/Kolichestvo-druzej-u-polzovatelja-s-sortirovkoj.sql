-- Выполним объединение и посмотрим на результат
SELECT users.id, first_name, last_name, requested_at
  FROM users
    LEFT JOIN friendship
      ON users.id = friendship.user_id
        OR users.id = friendship.friend_id
        ORDER BY users.id;

-- Затем подсчитаем
SELECT users.id, first_name, last_name, COUNT(requested_at) AS total_friends
  FROM users
    LEFT JOIN friendship
      ON users.id = friendship.user_id
        OR users.id = friendship.friend_id
  GROUP BY users.id
  ORDER BY total_friends DESC
  LIMIT 10;

-- Проверка
SELECT * FROM friendship WHERE user_id = 16 OR friend_id = 16;