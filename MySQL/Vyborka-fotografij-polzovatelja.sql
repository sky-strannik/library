SELECT users.first_name, users.last_name, media.user_id, media.filename, media.created_at
  FROM media
    JOIN users
      ON media.user_id = users.id
    JOIN media_types
      ON media.media_type_id = media_types.id     
  WHERE media.user_id = 8 AND media_types.name = 'photo';