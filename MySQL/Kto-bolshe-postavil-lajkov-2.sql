-- Задача. Определить кто больше поставил лайков (всего) - мужчины или женщины?

SELECT profiles.gender, 
  COUNT(likes.id) AS total_likes
  FROM likes
	JOIN profiles
	  ON likes.user_id = profiles.user_id
	GROUP BY profiles.gender
	ORDER BY total_likes DESC
	LIMIT 1;