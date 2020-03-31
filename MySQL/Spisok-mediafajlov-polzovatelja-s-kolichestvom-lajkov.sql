SELECT likes.target_id,
  media.filename,
  target_types.name AS target_type,
  COUNT(DISTINCT(likes.id)) AS total_likes,
  CONCAT(first_name, ' ', last_name) AS owner
  FROM media
    LEFT JOIN likes
      ON media.id = likes.target_id
    LEFT JOIN target_types
      ON likes.target_type_id = target_types.id
    LEFT JOIN users
      ON users.id = media.user_id
  WHERE users.id = 8 AND target_types.name = 'media'
  GROUP BY media.id;

-- Проверка
SELECT id, user_id FROM media WHERE id = 22;