-- Задача. Создать функцию, где должны выводиться:

-- Направленность дружбы
-- Кол-во приглашений в друзья к пользователю
-- /
-- Кол-во приглашений в друзья от пользователя

-- Чем больше - популярность выше
-- Если значение меньше единицы - пользователь инициатор связей.

DROP FUNCTION IF EXISTS friendship_direction;

DELIMITER -
CREATE FUNCTION friendship_direction(check_user_id INT)
RETURNS FLOAT READS SQL DATA

  BEGIN
	
	DECLARE requests_to_user INT;
	DECLARE requests_from_user INT;
	
	SET requests_to_user = 
	  (SELECT COUNT(*) 
		FROM friendship
		  WHERE friend_id = check_user_id);
	
	SET requests_from_user = 
	  (SELECT COUNT(*) 
		FROM friendship
		  WHERE user_id = check_user_id);
	
	RETURN requests_to_user / requests_from_user;
  END-
  
DELIMITER ;

-- Пример использования для пользователя с id 8
SELECT TRUNCATE(friendship_direction(8), 2) AS friendship_direction;