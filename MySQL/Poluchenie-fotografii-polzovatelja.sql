SELECT filename FROM media
  WHERE user_id = 8
    AND media_type_id = (
      SELECT id FROM media_types WHERE name = 'photo'
    );