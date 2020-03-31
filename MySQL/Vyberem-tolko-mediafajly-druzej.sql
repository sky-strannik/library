SELECT DISTINCT media.user_id, media.filename, media.created_at
  FROM media
    JOIN friendship
    JOIN users 
      ON (users.id = friendship.friend_id 
        OR users.id = friendship.user_id)
      AND (media.user_id = friendship.user_id 
        OR media.user_id = friendship.friend_id)   
  WHERE users.id = 8 AND media.user_id != 8;

-- Проверка
SELECT user_id, friend_id FROM friendship WHERE user_id = 8 OR friend_id = 8;