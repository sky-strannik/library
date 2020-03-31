(SELECT friend_id FROM friendship WHERE user_id = 8)
UNION
(SELECT user_id FROM friendship WHERE friend_id = 8);