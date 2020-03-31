-- Задача. Выведите список товаров products и разделов catalogs, который соответствует товару.

SELECT
  p.id,
  p.name,
  p.price,
  c.name AS catalog
FROM
  products AS p
LEFT JOIN
  catalogs AS c
ON
  p.catalog_id = c.id;