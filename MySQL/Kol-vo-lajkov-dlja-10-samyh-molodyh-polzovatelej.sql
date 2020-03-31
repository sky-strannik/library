-- Задача. Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей.

-- Суммируем для всех пользователей:
SELECT SUM(likes_per_user) AS likes_total FROM ( 
  SELECT COUNT(*) AS likes_per_user 
	FROM likes 
	  WHERE target_type_id = 2
		AND target_id IN (
		  SELECT * FROM (
			SELECT user_id FROM profiles ORDER BY birthday DESC LIMIT 10
		  ) AS sorted_profiles 
		) 
	  GROUP BY target_id
) AS counted_likes;

-- На самом деле можно упростить до:
SELECT COUNT(*) FROM likes 
  WHERE target_type_id = 2
	AND target_id IN (SELECT * FROM (
	  SELECT user_id FROM profiles ORDER BY birthday DESC LIMIT 10
	) AS sorted_profiles ) 
;

-- Либо другой вариант:
SELECT 
  (SELECT COUNT(*) FROM likes WHERE target_id = profiles.user_id AND target_type_id = 2) AS likes_total  
  FROM profiles 
  ORDER BY birthday 
  DESC LIMIT 10;

SELECT SUM(likes_total) FROM  
  (SELECT 
	(SELECT COUNT(*) FROM likes WHERE target_id = profiles.user_id AND target_type_id = 2) AS likes_total  
	FROM profiles 
	ORDER BY birthday 
	DESC LIMIT 10) AS user_likes
;