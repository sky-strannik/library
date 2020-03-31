SELECT 
    (SELECT CONCAT(first_name, ' ', last_name) 
      FROM users 
      WHERE id = user_id) AS friend, -- имя пользователя
    CASE (gender)                       
      WHEN 'm' THEN 'man'
      WHEN 'f' THEN 'women'
    END AS sex, -- пол
    TIMESTAMPDIFF(YEAR, birthday, NOW()) AS age -- возраст
  FROM profiles
  WHERE user_id IN (
    SELECT friend_id FROM friendship
      WHERE user_id = 8 
        AND confirmed_at IS NOT NULL
        AND status_id IN (
          SELECT id FROM friendship_statuses WHERE name = 'Confirmed'
          )
      UNION
      SELECT user_id 
      FROM friendship
      WHERE friend_id = 8
        AND confirmed_at IS NOT NULL
        AND status_id IN (
          SELECT id FROM friendship_statuses WHERE name = 'Confirmed'
          )
  );