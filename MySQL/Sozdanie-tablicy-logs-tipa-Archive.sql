-- Задача. Создайте таблицу logs типа Archive. Пусть при каждом создании записи 
-- в таблицах users, catalogs и products в таблицу logs помещается время и дата 
-- создания записи, название таблицы, идентификатор первичного ключа и содержимое поля name.

CREATE TABLE Logs (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	created_at datetime DEFAULT CURRENT_TIMESTAMP,
	table_name varchar(50) NOT NULL,
	row_id INT UNSIGNED NOT NULL,
	row_name varchar(255)
) ENGINE = Archive;

CREATE TRIGGER products_insert AFTER INSERT ON products
FOR EACH ROW
BEGIN
	INSERT INTO Logs VALUES (NULL, DEFAULT, "products", NEW.id, NEW.name);
END;

CREATE TRIGGER users_insert AFTER INSERT ON users
FOR EACH ROW
BEGIN
	INSERT INTO Logs VALUES (NULL, DEFAULT, "users", NEW.id, NEW.name);
END;

CREATE TRIGGER catalogs_insert AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN
	INSERT INTO Logs VALUES (NULL, DEFAULT, "catalogs", NEW.id, NEW.name);
END;