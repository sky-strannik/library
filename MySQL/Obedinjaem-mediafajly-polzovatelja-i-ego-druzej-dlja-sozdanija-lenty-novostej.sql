SELECT filename, user_id, created_at FROM media WHERE user_id = 8
UNION
SELECT filename, user_id, created_at FROM media WHERE user_id IN (
  (SELECT friend_id 
  FROM friendship 
    WHERE user_id = 8 AND status_id IN (
      SELECT id FROM friendship_statuses WHERE name = 'Confirmed'
    )
  )
  UNION
  (SELECT user_id 
    FROM friendship 
    WHERE friend_id = 8 AND status_id IN (
      SELECT id FROM friendship_statuses WHERE name = 'Confirmed'
    )
  )
);