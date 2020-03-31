-- Задача. Создать процедуру, где выполняется:

-- Рассылка приглашений вида "Возможно, вам будет интересно пообщаться с ..."
-- Варианты:
-- из одного города
-- состоят в одной группе
-- друзья друзей
-- Из выборки показывать 5 человек в случайной комбинации.

DROP PROCEDURE IF EXISTS friendship_offers;

DELIMITER -

CREATE PROCEDURE friendship_offers (IN for_user_id INT)

  BEGIN 
	(
	  SELECT pr2.user_id
		FROM profiles pr1
		  JOIN profiles pr2
			ON pr1.city = pr2.city
		WHERE pr1.user_id = for_user_id
	  
	  UNION
	  
	  SELECT cu2.user_id
		FROM communities_users cu1
		  JOIN communities_users cu2
			ON cu1.community_id = cu2.community_id
		WHERE cu1.user_id = for_user_id
	  
	  UNION
			
	  SELECT DISTINCT fr2.user_id
		FROM friendship fr1
		  JOIN friendship fr2
			ON fr1.user_id = fr2.user_id 
			  OR fr1.friend_id = fr2.friend_id
			  OR fr1.friend_id = fr2.user_id 
			  OR fr1.user_id = fr2.friend_id
			WHERE fr1.user_id = for_user_id 
			  OR fr1.friend_id = for_user_id 
			
	  UNION
			
	  SELECT DISTINCT fr2.friend_id
		FROM friendship fr1
		  JOIN friendship fr2
			ON fr1.user_id = fr2.user_id 
			  OR fr1.friend_id = fr2.friend_id
			  OR fr1.friend_id = fr2.user_id 
			  OR fr1.user_id = fr2.friend_id
			WHERE fr1.user_id = for_user_id 
			  OR fr1.friend_id = for_user_id 
		  
	)
		
	ORDER BY RAND()
	LIMIT 5;
	 
END-
  
DELIMITER ;

CALL friendship_offers(8);