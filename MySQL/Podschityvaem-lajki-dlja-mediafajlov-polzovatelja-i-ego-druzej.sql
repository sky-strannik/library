SELECT target_id AS mediafile, COUNT(*) AS likes 
  FROM likes 
    WHERE target_id IN (
      SELECT id FROM media WHERE user_id = 3
        UNION
      (SELECT id FROM media WHERE user_id IN (
        SELECT friend_id 
          FROM friendship WHERE user_id = 8 AND status_id IN (
                SELECT id FROM friendship_statuses WHERE name = 'Confirmed'
              )))
        UNION
      (SELECT id FROM media WHERE user_id IN (
        SELECT user_id 
          FROM friendship WHERE friend_id = 8 AND status_id IN (
                SELECT id FROM friendship_statuses WHERE name = 'Confirmed'
              ))) 
    )
    AND target_type_id = (SELECT id FROM target_types WHERE name = 'media')
    GROUP BY target_id;