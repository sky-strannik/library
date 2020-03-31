SELECT user_id, filename, size 
  FROM media 
  ORDER BY size DESC
  LIMIT 10;

-- Улучшим запрос, используем алиасы для имён таблиц:
SELECT 
  (SELECT CONCAT(first_name, ' ', last_name) 
    FROM users u WHERE u.id = m.user_id) AS owner,
  filename, 
  size 
    FROM media m
    ORDER BY size DESC
    LIMIT 10;