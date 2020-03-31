-- Задача. Определить кто больше поставил лайков (всего) - мужчины или женщины?

SELECT 
  (CASE(gender)
		WHEN 'm' THEN 'man'
		WHEN 'f' THEN 'woman'
	END) AS gender, 
	COUNT(*) as likes_count 
	  FROM (
		SELECT 
		  user_id as user, 
			(SELECT gender FROM profiles 
			  WHERE profiles.user_id = likes.user_id) as gender 
		  FROM likes) dummy_table 
  GROUP BY gender
  ORDER BY likes_count DESC
  LIMIT 2;