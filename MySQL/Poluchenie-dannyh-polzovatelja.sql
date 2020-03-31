SELECT * FROM users WHERE id = 8;

SELECT first_name, last_name, 'main_photo', 'city' FROM users WHERE id = 8;

SELECT
  first_name,
  last_name,
  (SELECT filename FROM media WHERE id = 
    (SELECT photo_id FROM profiles WHERE user_id = users.id)
  ) AS filename,
  (SELECT city FROM profiles WHERE user_id = users.id) AS city
  FROM users
    WHERE id = 8;