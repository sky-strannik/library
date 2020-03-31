-- Задача. Создайте SQL-запрос, который помещает в таблицу users миллион записей.

CREATE TABLE samples (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Покупатели';

INSERT INTO samples (name, birthday_at) VALUES
  ('Геннадий', '1990-10-05'),
  ('Наталья', '1984-11-12'),
  ('Александр', '1985-05-20'),
  ('Сергей', '1988-02-14'),
  ('Иван', '1998-01-12'),
  ('Мария', '1992-08-29'),
  ('Аркадий', '1994-03-17'),
  ('Ольга', '1981-07-10'),
  ('Владимир', '1988-06-12'),
  ('Екатерина', '1992-09-20');

SELECT
  COUNT(*)
FROM
  samples AS fst,
  samples AS snd,
  samples AS thd,
  samples AS fth,
  samples AS fif,
  samples AS sth;

SELECT COUNT(*) FROM users;

SELECT * FROM users LIMIT 10;