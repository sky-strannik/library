-- Задача. Найти сколько занимают места медиафайлы в разрезе типов в процентном соотношении.

-- Реализация использует агрегатные функции как оконные:
SELECT DISTINCT media_types.name, 
  SUM(media.size) OVER(PARTITION BY media.media_type_id) AS total_by_type,
  SUM(media.size) OVER() AS total,
  SUM(media.size) OVER(PARTITION BY media.media_type_id) / SUM(media.size) OVER() * 100 AS "%%"
	FROM media
	  JOIN media_types
		ON media.media_type_id = media_types.id;

-- Расширяем вывод:
SELECT DISTINCT media_types.name,
  AVG(media.size) OVER(PARTITION BY media.media_type_id) AS average,
  MIN(media.size) OVER(PARTITION BY media.media_type_id) AS min,
  MAX(media.size) OVER(PARTITION BY media.media_type_id) AS max,
  SUM(media.size) OVER(PARTITION BY media.media_type_id) AS total_by_type,
  SUM(media.size) OVER() AS total,
  SUM(media.size) OVER(PARTITION BY media.media_type_id) / SUM(media.size) OVER() * 100 AS "%%"
	FROM media
	  JOIN media_types
		ON media.media_type_id = media_types.id;

-- Выносим окно отдельно.
-- Оконные функции не сворачивают вывод, убираем DISTINCT:
SELECT media_types.name,
  AVG(media.size) OVER w AS average,
  MIN(media.size) OVER w AS min,
  MAX(media.size) OVER w AS max,
  SUM(media.size) OVER w AS total_by_type,
  SUM(media.size) OVER() AS total,
  SUM(media.size) OVER w / SUM(media.size) OVER() * 100 AS "%%"
	FROM (media
	  JOIN media_types
		ON media.media_type_id = media_types.id)
		WINDOW w AS (PARTITION BY media.media_type_id);