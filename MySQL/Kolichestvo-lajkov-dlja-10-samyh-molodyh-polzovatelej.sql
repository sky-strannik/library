-- Задача. Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей.

SELECT SUM(got_likes) AS total_likes_for_youngest
  FROM (   
	SELECT COUNT(DISTINCT likes.id) AS got_likes 
	  FROM profiles
		LEFT JOIN likes
		  ON likes.target_id = profiles.user_id
			AND target_type_id = 2
	  GROUP BY profiles.user_id
	  ORDER BY profiles.birthday DESC
	  LIMIT 10
) AS youngest;

-- или
SELECT count(*) 
  FROM likes
	JOIN target_types ON target_types.id = likes.target_type_id 
	JOIN (SELECT user_id FROM profiles ORDER BY birthday DESC limit 10) AS youngest 
	  ON youngest.user_id = likes.target_id 
  WHERE target_types.name = 'users';