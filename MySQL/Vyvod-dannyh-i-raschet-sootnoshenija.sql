-- Задача. Построить запрос, который будет выводить следующие столбцы:
-- имя группы
-- среднее количество пользователей в группах
-- самый молодой пользователь в группе
-- самый пожилой пользователь в группе
-- общее количество пользователей в группе
-- всего пользователей в системе
-- отношение в процентах
-- (общее количество пользователей в группе / всего пользователей в системе) * 100

SELECT DISTINCT 
  communities.name AS group_name,
  COUNT(communities_users.user_id) OVER() 
	/ (SELECT COUNT(*) FROM communities) AS avg_users_in_groups,
  FIRST_VALUE(users.first_name) 
	OVER birthday_desc AS youngest_first_name,
  FIRST_VALUE(users.last_name) 
	OVER birthday_desc AS youngest_last_name,
  FIRST_VALUE(users.first_name) 
	OVER birthday_asc AS oldest_first_name,
  FIRST_VALUE(users.last_name) 
	OVER birthday_asc AS oldest_last_name,
  COUNT(communities_users.user_id) 
	OVER(PARTITION BY communities.id) AS users_in_groups,
  (SELECT COUNT(*) FROM users) AS users_total,
  COUNT(communities_users.user_id) OVER(PARTITION BY communities.id) 
	/ (SELECT COUNT(*) FROM users) *100 AS '%%'
	FROM communities
	  LEFT JOIN communities_users 
		ON communities_users.community_id = communities.id
	  LEFT JOIN users 
		ON communities_users.user_id = users.id
	  LEFT JOIN profiles 
		ON profiles.user_id = users.id
	  WINDOW birthday_desc AS (PARTITION BY communities.id ORDER BY profiles.birthday DESC),
			 birthday_asc AS (PARTITION BY communities.id ORDER BY profiles.birthday);