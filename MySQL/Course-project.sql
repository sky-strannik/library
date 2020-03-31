-- КУРСОВОЙ ПРОЕКТ: БД "db_ecommerce"
-- ЗАДАЧА: переделать текущий рабочий проект в новую БД с новой структурой


-- ОПИСАНИЕ ПРОЕКТА
-- Текущий рабочий проект представляет из себя БД с 4 таблицами: akks, akks_sendmails, company, task_sendmails
-- К текущей БД обращается внешнее приложение, которое осуществляет периодическую Email рассылку по клиентской базе компании
-- Принцип работы приложения следующий:
-- 1. Из общей базы аккаунтов менеджеров (таблица akks, выбираются несколько дежурных менеджеров и копируются в таблицу akks_sendmails)
-- 2. Персональные данные дежурных менеджеров из akks_sendmails периодически забираются приложением и подставляются в тексты писем
-- 3. Приложением, по заданным критериями, выбирается из таблицы company одна случайная компания и для нее готовится персональное КП
-- 4. В полученное КП подставляются контактные и прочие данные случайного дежурного менеджера, КП помещается в таблицу task_sendmails
-- 5. В таблице task_sendmails формируется очередь заданий на отправку писем с КП, которые и отправляются приложением

-- Проект имеет следующую структуру:
-- Таблицы: akks, akks_sendmails, company, task_sendmails

-- Поля akks: UID, UDate, UStatus, UType, ULogin, UEmail, UPass, UName, USurname, URegistr, USites, UPhoto, UNickName, UGender, UAge, UBornDay, UBornMonth, UBornYear, 
-- ULanguage, URePhone, UReEmail, URePass, UZipCode, UCountry, URegion, UTown, UInterests, USign, UComment

-- Поля akks_sendmails: UID, UDate, UStatus, UType, ULogin, UEmail, UPass, UName, USurname, URegistr, USites, UPhoto, UNickName, UGender, UAge, UBornDay, UBornMonth, UBornYear, 
-- ULanguage, URePhone, UReEmail, URePass, UZipCode, UCountry, URegion, UTown, UInterests, USign, UComment

-- Поля company: ID, `Date`, Status, Offer, `Search`, CategoryAll, Tags, Region, District, City, Company, Address, PhoneMobile, PhoneFree, PhoneCity, Emails, Site, 
-- TimeWork, YandexMap, Lat, `Long`, VK, FB, Insta, Twitter, OD, MyMir, YouTube

-- Поля task_sendmails: ID, `Date`, Offer, Company, Email, Subj, Sendtext


-- НОВЫЙ ПРОЕКТ ПО ОПТИМИЗАЦИИ БД
-- Общая идея оптимизации структуры БД состоит в том, чтобы вынести в отдельные таблицы редко используемые данные,
-- а также данные счетчиков (сколько, чего и кому было отправлено) и данные логирования (общие результаты успехов и неуспехов по дням)
-- модифицировать очередь отправки


-- ----------------------------------------------------


-- Создаем структуру нового проекта "ecommerce":


-- ----------------------------------------------------


-- Если потребуется удалить таблицы, то:
DROP TABLE cities, company, discounts, districts, logs, offers, orders, profiles, regions, socials, tasks, users;


-- ----------------------------------------------------


-- МЕНЕДЖЕРЫ (пользователи)
-- Вместо таблицы akks создаем 2 таблицы: users & profiles. При этом в users будут постоянно запрашиваемые данные с индексами, а в profiles редко используемые
-- Вместо таблицы akks_sendmails в таблицу users добавляем столбец статуса sentry, который будет выделять дежурных менеджеров

-- Создаем таблицу пользователей
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	updated DATETIME DEFAULT NOW() ON UPDATE NOW(),
	status CHAR(10),
	type_akk CHAR(10),
	sentry CHAR(10),
	login VARCHAR(100),
	pass VARCHAR(100),
	email VARCHAR(100),
	first_name VARCHAR(50),
	last_name VARCHAR(50)
);

-- Заполняем данными
TRUNCATE users;
INSERT INTO users VALUES
	(DEFAULT, DEFAULT, 'activity', 'manager', 'ok', 'alsorre', 'PIUW5PsybM', 'alsorre@mail.ru', 'Никита', 'Лобанов'),
	(DEFAULT, DEFAULT, 'activity', 'manager', 'no', 'ipcent', 'x8WhiGhiuf', 'umnetna@bk.ru', 'Иван', 'Панин'),
	(DEFAULT, DEFAULT, 'activity', 'manager', 'no', 'berniy', 'fg656yhdf', 'nonrero@mail.ru', 'Виктор', 'Архипов'),
	(DEFAULT, DEFAULT, 'activity', 'manager', 'no', 'tranelog', 'VU04AJlCYx', 'tranelog@list.ru', 'Максим', 'Фролов'),	
	(DEFAULT, DEFAULT, 'activity', 'manager', 'ok', 'ovberni', 'ElY0EOStsC', 'ovberni@inbox.ru', 'Галина', 'Новикова');

-- Создаем индексы
CREATE INDEX users_status_idx ON users(status);
CREATE INDEX users_type_akk_idx ON users(type_akk);
CREATE INDEX users_sentry_idx ON users(sentry);
CREATE INDEX users_login_idx ON users(login);


-- ---------------


-- ПРОФИЛИ

-- Создаем таблицу профилей
DROP TABLE IF EXISTS profiles;
CREATE TABLE profiles (
	user_id INT UNSIGNED NOT NULL,
	nickname VARCHAR(20),
	avatar INT(10), -- здесь нужен только id, т.к. аватар генерится приложением по id
	gender CHAR(10),
	birthday DATE,
	lang CHAR(10),
	site VARCHAR(255),
	zipcode INT(10),
	country VARCHAR(255),
	region VARCHAR(255),
	city VARCHAR(255),
	interests VARCHAR(255),
	sign VARCHAR(255),
	comment VARCHAR(255),
	rephone VARCHAR(100),
	reemail VARCHAR(100),
	repass VARCHAR(100),
	created DATETIME DEFAULT NOW(),
	updated DATETIME DEFAULT NOW() ON UPDATE NOW()
);

-- Заполняем данными
TRUNCATE profiles;
INSERT INTO profiles VALUES
	(1, 'alsorre', 12, 'm', '1971-01-12', 'ru', '', 195000, 'Russia', '', 'Москва', '', '', '', '79211234567', '', '', DEFAULT, DEFAULT),
	(2, 'ipcent', 34, 'm', '1975-02-09', 'ru', '', 197000, 'Russia', '', 'Москва', '', '', '', '79111234567', '', '', DEFAULT, DEFAULT),
	(3, 'berniy', 54, 'm', '1980-11-04', 'ru', '', 197055, 'Russia', '', 'Санкт-Петербург', '', '', '', '79811234567', '', '', DEFAULT, DEFAULT),
	(4, 'tranelog', 23, 'm', '1982-09-13', 'ru', '', 195744, 'Russia', '', 'Новосибирск', '', '', '', '79991234567', '', '', DEFAULT, DEFAULT),	
	(5, 'ovberni', 78, 'w', '1981-04-15', 'ru', '', 195325, 'Russia', '', 'Краснодар', '', '', '', '79311234567', '', '', DEFAULT, DEFAULT);

-- Добавляем внешние ключи
ALTER TABLE profiles
	ADD CONSTRAINT profiles_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id)
			ON UPDATE CASCADE
    		ON DELETE CASCADE;


-- ---------------


-- СПРАВОЧНИКИ

-- Создаем гео-таблицы
DROP TABLE IF EXISTS regions;
CREATE TABLE regions (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	region VARCHAR(255)
);

DROP TABLE IF EXISTS districts;
CREATE TABLE districts (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	district VARCHAR(255)
);

DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	city VARCHAR(255)
);

-- Заполняем данными
TRUNCATE regions;
INSERT INTO regions VALUES
	(DEFAULT, 'Россия, Санкт-петербург');

TRUNCATE districts;
INSERT INTO districts VALUES
	(DEFAULT, 'Санкт-петербург');

TRUNCATE cities;
INSERT INTO cities VALUES
	(DEFAULT, 'Санкт-петербург');


-- ---------------


-- ОФФЕРЫ

-- Создаем таблицу офферов
DROP TABLE IF EXISTS offers;
CREATE TABLE offers (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50),
	descr VARCHAR(255),
	created DATETIME DEFAULT NOW(),
	updated DATETIME DEFAULT NOW() ON UPDATE NOW()
);

-- Заполняем данными
TRUNCATE offers;
INSERT INTO offers VALUES
	(DEFAULT, 'bigpaket', 'Основной пакет услуг', DEFAULT, DEFAULT),
	(DEFAULT, 'dop', 'Дополнительные услуги', DEFAULT, DEFAULT);

-- Создаем индексы
CREATE INDEX offers_name_idx ON offers(name);


-- ---------------


-- КОМПАНИИ
-- Таблицу company разбиваем на несколько: company, region, district, city, socials
-- При этом категории, поисковые запросы и теги не выносим в отдельные таблицы, т.к. они имеют разнородную структуру записей и это затруднит идентификацию
-- Важно! Пользователи никак не связаны с компаниями, только через таски, где они указываются отправителями

-- Создаем таблицу компаний
DROP TABLE IF EXISTS company;
CREATE TABLE company (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	updated DATETIME DEFAULT NOW() ON UPDATE NOW(),
	status VARCHAR(20),
	offer_id INT UNSIGNED NOT NULL,
	searchweb VARCHAR(255),
	category VARCHAR(255),
	company VARCHAR(255),
	site VARCHAR(510),
	email VARCHAR(510),
	phone_mobile VARCHAR(510),
	phone_800 VARCHAR(510),
	phone_city VARCHAR(510),
	address VARCHAR(255),
	maps VARCHAR(255),
	region_id INT UNSIGNED NOT NULL,
	district_id INT UNSIGNED NOT NULL,
	city_id INT UNSIGNED NOT NULL,
	latitude CHAR(20),
	longitude CHAR(20),
	time_work VARCHAR(255),
	tags VARCHAR(255)
);

-- Заполняем данными
TRUNCATE company;
INSERT INTO company VALUES
	(DEFAULT, DEFAULT, '200', 1, 'системы безопасности и охраны', 'Студия веб-дизайна | системы безопасности и охраны', 'Эксклюзив Дизайн', 'http://exdesign.ru/', 'info@exdesign.ru', '', '', '7(812)335-40-55', 'Россия, Санкт-Петербург, площадь Конституции, 7', 'https://yandex.ru/maps/org/eksklyuziv_dizayn/1092778076/', 1, 1, 1, '59.850988', '30.308259', 'пн-пт 10:00–18:30', 'системы видеонаблюдения'),
	(DEFAULT, DEFAULT, '200', 1, 'магазин мебели', 'Магазин мебели', 'Ниагара', 'http://www.mk-niagara.ru/', 'mk-niagara@yandex.ru', '7(968)190-72-34,7(968)190-72-43', '', '7(812)610-07-41,7(812)640-09-89,7(812)988-20-31,7(812)610-17-41', 'Россия, Санкт-Петербург, улица Шостаковича, 8к1', 'https://yandex.ru/maps/org/niagara/1066947430/', 1, 1, 1, '60.05842', '30.331192', 'ежедневно, 11:00–21:00', ''),
	(DEFAULT, DEFAULT, '200', 2, 'кузовной ремонт', 'Автосервис, автотехцентр | кузовной ремонт | шиномонтаж', 'Автогуру', 'http://autoguru.spb.ru/', 'info@autoguru.spb.ru', '', '', '7(812)321-01-21', 'Россия, Санкт-Петербург, Парковая улица, 2', 'https://yandex.ru/maps/org/avtoguru/1276582632/', 1, 1, 1, '59.889887', '30.335926', 'ежедневно, 10:00–21:00', 'марка автомобиля: китайские, Iveco, корейские, японские, КАМАЗ, Rover, Lifan, Chevrolet, Ford, ГАЗ, FIAT, Maserati, УАЗ, Geely, Infiniti, Isuzu, DAF, ЗИЛ, МАЗ, Neoplan, Brilliance, Saab, отечественные, Daimler, Lexus, Acura, Land Rover, FAW, Great Wall'),
	(DEFAULT, DEFAULT, '200', 2, 'магазин одежды', 'Магазин одежды', 'Магазин мужской одежды Эгоист', 'http://egoiste.ru/', 'zakaz@egoiste.ru,egoistee@mtu-net.ru', '', '', '7(812)315-26-76,7(812)907-32-26', 'Россия, Санкт-Петербург, Спасский переулок, 7', 'https://yandex.ru/maps/org/magazin_muzhskoy_odezhdy_egoist/1061375394/', 1, 1, 1, '59.928647', '30.318085', 'пн-пт 11:00–20:00', 'виды одежды: мужская одежда, детская одежда'),
	(DEFAULT, DEFAULT, '200', 2, 'агентство недвижимости', 'Агентство недвижимости', 'Агентство недвижимости Ellitestate', 'http://ellitestate.ru/', 'info@ellitestate.ru,elitenedvigimost@gmail.com', '7(921)976-97-56', '', '7(812)242-86-28', 'Россия, Санкт-Петербург, Глиняная улица, 5, корп. 1', 'https://yandex.ru/maps/org/agentstvo_nedvizhimosti_ellitestate/1740268948/', 1, 1, 1, '59.916406', '30.392081', 'пн-пт 10:00–20:00; сб,вс 11:00–17:00', 'Элитная недвижимость'),
	(DEFAULT, DEFAULT, 'Send', 2, 'гостиница', 'Гостиница', 'Вояж', 'https://voyage-hotel.spb.ru/', 'info@voyage-hotel.spb.ru', '7(921)555-71-65', '8(800)500-21-86', '7(812)645-55-50,7(812)670-70-43,7(812)670-76-16,7(812)670-75-07,7(812)704-46-09', 'Россия, Санкт-Петербург, Пулковское шоссе, 107', 'https://yandex.ru/maps/org/voyazh/1035192908/', 1, 1, 1, '59.75039', '30.313798', 'ежедневно, круглосуточно', 'количество звезд: 3 звезды | Wi-Fi | парковка | кондиционер в номере | оплата картой | номеров: 98 | цена номера: от 2100 руб/ночь | тип гостиницы: гранд-отель, бизнес-отель, мотель, дизайн-отель | дата постройки: 2000 | веранда/терраса/патио | химчистка'),
	(DEFAULT, DEFAULT, '200', 2, 'магазин детской одежды', 'Шоу-рум | детский магазин | детские игрушки и игры', 'Интернет-Магазин ДобрыйПа-Па.рф', 'http://papad.ru/', 'info@papad.ru', '', '', '7(812)614-64-23', 'Россия, Санкт-Петербург, проспект Маршала Блюхера, 8, корп. 1', 'https://yandex.ru/maps/org/internet_magazin_dobryypa_pa_rf/172109359621/', 1, 1, 1, '59.984084', '30.370633', 'ежедневно, 9:00–21:00', 'оплата картой'),
	(DEFAULT, DEFAULT, '200', 2, 'лицензирование', 'Сертификация продукции и услуг | лицензирование | стандартизация и метрология', 'РосТехСтандарт', 'http://www.rostehstandart.ru/', 'info@rostehstandart.ru', '', '', '7(812)646-51-21', 'Россия, Санкт-Петербург, Лиговский проспект, 4А', 'https://yandex.ru/maps/org/rostekhstandart/1428159469/', 1, 1, 1, '59.937188', '30.366309', 'пн-пт 9:00–17:00', ''),
	(DEFAULT, DEFAULT, '200', 2, 'металлопрокат', 'Металлопрокат | цветные металлы | черная металлургия', 'Ауремо', 'http://auremo.org/', 'info@auremo.org,artem@auremo.org,stas@auremo.org', '', '8(800)100-44-70', '7(812)680-16-77', 'Россия, Санкт-Петербург, Лиговский проспект, 172', 'https://yandex.ru/maps/org/auremo/1146047621/', 1, 1, 1, '59.911313', '30.348648', 'пн-пт 8:00–17:00', ''),
	(DEFAULT, DEFAULT, '200', 2, 'студия автотюнинга', 'Студия автотюнинга | автосервис, автотехцентр', 'Parafara.ru', 'http://parafara.ru/', '9315859330@mail.ru', '7(931)585-93-30', '', '', 'Россия, Санкт-Петербург, проспект Пархоменко, 39', 'https://yandex.ru/maps/org/parafara_ru/195845559912/', 1, 1, 1, '59.99747', '30.354697', 'ежедневно, 10:00–20:00', 'марка автомобиля: легковые, импортные | Wi-Fi | автовинил');

-- Добавляем внешние ключи
ALTER TABLE company
	ADD CONSTRAINT company_offer_id_fk
		FOREIGN KEY (offer_id) REFERENCES offers(id)
			ON UPDATE CASCADE,
	ADD CONSTRAINT company_region_id_fk
		FOREIGN KEY (region_id) REFERENCES regions(id)
			ON UPDATE CASCADE,
	ADD CONSTRAINT company_district_id_fk
		FOREIGN KEY (district_id) REFERENCES districts(id)
			ON UPDATE CASCADE,
	ADD CONSTRAINT company_city_id_fk
		FOREIGN KEY (city_id) REFERENCES cities(id)
			ON UPDATE CASCADE;
	
-- Создаем индексы
CREATE INDEX company_updated_idx ON company(updated);
CREATE INDEX company_status_idx ON company(status);
CREATE INDEX company_searchweb_idx ON company(searchweb);
CREATE INDEX company_category_idx ON company(category);
CREATE INDEX company_company_idx ON company(company);
CREATE INDEX company_site_idx ON company(site);
CREATE INDEX company_email_idx ON company(email);
CREATE INDEX company_phone_mobile_idx ON company(phone_mobile);
CREATE INDEX company_tags_idx ON company(tags);


-- ---------------


-- СОЦСЕТИ

-- Создаем таблицу для ссылок на социальные сети
DROP TABLE IF EXISTS socials;
CREATE TABLE socials (
	company_id INT UNSIGNED NOT NULL,
	vk VARCHAR(255),
	fb VARCHAR(255),
	insta VARCHAR(255),
	twitter VARCHAR(255),
	od VARCHAR(255),
	mymir VARCHAR(255),
	youtube VARCHAR(255),
	updated DATETIME DEFAULT NOW() ON UPDATE NOW()
);

-- Заполняем данными
TRUNCATE socials;
INSERT INTO socials VALUES
	(1, '', '', '', '', '', '', '', DEFAULT),
	(2, 'https://vk.com/mk_niagara', '', '', '', '', '', '', DEFAULT),
	(3, 'https://vk.com/autoguruspb', '', '', '', '', '', '', DEFAULT),
	(4, '', '', 'http://instagram.com/iegoist1', '', '', '', '', DEFAULT),
	(5, '', '', 'http://www.instagram.com/ellitestate.ru/', '', '', '', 'http://www.youtube.com/channel/UCTqjALOPcrYe_Hv7ClMQ9_Q', DEFAULT),
	(6, 'https://vk.com/voyzh', '', 'https://www.instagram.com/hotel_voyage', '', '', '', '', DEFAULT),
	(7, 'http://vk.com/tdvektor', '', '', '', '', '', '', DEFAULT),
	(8, '', '', '', '', '', '', '', DEFAULT),
	(9, '', '', '', '', '', '', '', DEFAULT),
	(10, '', '', 'http://instagram.com/parafaracenter', '', '', '', '', DEFAULT);

-- Добавляем внешние ключи
ALTER TABLE socials
	ADD CONSTRAINT socials_company_id_fk
		FOREIGN KEY (company_id) REFERENCES company(id)
			ON UPDATE CASCADE;
		
		
-- ---------------		


-- АКЦИИ
		
-- Создаем таблицу акций
DROP TABLE IF EXISTS discounts;
CREATE TABLE discounts (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	offer_id INT UNSIGNED NOT NULL,
	name VARCHAR(100),
	descr VARCHAR(255),
	discont DECIMAL,
	started DATETIME,
	finished DATETIME,
	created DATETIME DEFAULT NOW(),
	updated DATETIME DEFAULT NOW() ON UPDATE NOW()
);

-- Заполняем данными
TRUNCATE discounts;
INSERT INTO discounts VALUES
	(DEFAULT, 1, '5%', '5% скидка при первой покупке', 0.05, '2020-03-30 10:00:00', '2020-04-15 20:00:00', DEFAULT, DEFAULT);

-- Добавляем внешние ключи
ALTER TABLE discounts
	ADD CONSTRAINT discounts_offer_id_fk
		FOREIGN KEY (offer_id) REFERENCES offers(id)
			ON UPDATE CASCADE;


-- ---------------		

		
-- ЗАКАЗЫ
	
-- Создаем таблицу заказов
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	company_id INT UNSIGNED NOT NULL,
	offer_id INT UNSIGNED,
	discount_id INT UNSIGNED,
	price DECIMAL,
	comment VARCHAR(255),
	created DATETIME DEFAULT NOW(),
	updated DATETIME DEFAULT NOW() ON UPDATE NOW()
);

-- Заполняем данными
TRUNCATE orders;
INSERT INTO orders VALUES
	(DEFAULT, 2, 1, NULL, 75000, 'Нет скидки', DEFAULT, DEFAULT),
	(DEFAULT, 5, 1, 1, 150000, '50% предоплата + скидка 5%', DEFAULT, DEFAULT);

-- Добавляем внешние ключи
ALTER TABLE orders
	ADD CONSTRAINT orders_company_id_fk
		FOREIGN KEY (company_id) REFERENCES company(id)
			ON UPDATE CASCADE,
	ADD CONSTRAINT orders_offer_id_fk
		FOREIGN KEY (offer_id) REFERENCES offers(id)
			ON UPDATE CASCADE,
	ADD CONSTRAINT orders_discount_id_fk
		FOREIGN KEY (discount_id) REFERENCES discounts(id)
			ON UPDATE CASCADE;
		

-- ---------------			
		
		
-- ЗАДАЧИ
-- Таблицу task_sendmails переформатируем с оптимизацией в таблицу tasks
-- Финальные данные для таблицы генерируются приложением, поэтому в ней должны быть указаны окончательные значения, а не ссылки на другие таблицы
-- Важно! После отработки задачи таска удаляется

-- Создаем таблицу задач
DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
	company_id INT UNSIGNED NOT NULL,
	created DATETIME DEFAULT NOW(),
	offer VARCHAR(50),
	company VARCHAR(255),
	email VARCHAR(255),
	subject VARCHAR(255),
	sendtext TEXT
);

-- Заполняем данными
TRUNCATE tasks;
INSERT INTO tasks VALUES
	(1, DEFAULT, 'bigpaket', 'Эксклюзив Дизайн', 'info@exdesign.ru', 'Новый тариф', 'Добрый день! С Уважением...'),
	(3, DEFAULT, 'dop', 'Автогуру', 'info@autoguru.spb.ru', 'Новый тариф', 'Добрый день! С Уважением...');

-- Добавляем внешние ключи
ALTER TABLE tasks DROP FOREIGN KEY tasks_company_id_fk;
ALTER TABLE tasks
	ADD CONSTRAINT tasks_company_id_fk
		FOREIGN KEY (company_id) REFERENCES company(id)
			ON UPDATE CASCADE;


-- ---------------		
		
		
-- ЛОГГИРОВАНИЕ

-- Создаем таблицу логов
DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	company_id INT(10) NOT NULL,
	offer VARCHAR(50),
	created DATETIME DEFAULT NOW()
);

TRUNCATE logs;

-- Заполняем данными автоматически через триггеры



-- ----------------------------------------------------


-- Создаем выборки, представления, процедуры, триггеры:


-- ----------------------------------------------------


-- Создаем запись в таблице логов

DELIMITER //

DROP TRIGGER IF EXISTS tasks_ok_insert;
CREATE TRIGGER tasks_ok_insert AFTER INSERT ON tasks
FOR EACH ROW BEGIN
	INSERT INTO logs VALUES (DEFAULT, NEW.company_id, NEW.offer, DEFAULT);
END;

DELIMITER ;


-- Создаем процедуру подсчета кол-ва отправок офферов за сегодня

DELIMITER //

DROP PROCEDURE IF EXISTS send_offers;
CREATE PROCEDURE send_offers()
BEGIN
	SELECT DATE_FORMAT(DATE(CONCAT_WS('-', YEAR(NOW()), MONTH(NOW()), DAY(NOW()))), 'Cегодня отправлено:') AS today, COUNT(*) AS total FROM logs GROUP BY today ORDER BY total DESC;
END;

DELIMITER ;

CALL send_offers();


-- Создаем представление - Dashboard, выводящее данные по компаниям только за сегодня

DROP VIEW IF EXISTS dashboard;
CREATE OR REPLACE VIEW dashboard
	AS SELECT id, updated, status, offer_id FROM company WHERE updated >= CURDATE();

SELECT * FROM dashboard;


-- Создаем представление - кому и какие офферы отправлены за сегодня

DROP VIEW IF EXISTS daylogs;
CREATE OR REPLACE VIEW daylogs
	AS SELECT company_id, offer FROM logs WHERE created >= CURDATE();

SELECT * FROM daylogs;


-- Делаем запрос на проверку наличия заказов

SELECT 
	(SELECT id FROM company WHERE id = company_id) AS ID,
	(SELECT company FROM company WHERE id = company_id) AS company,
	(SELECT name FROM offers WHERE id = offer_id) AS offer,
	(SELECT name FROM discounts WHERE id = discount_id) AS discount,
	price, comment, created
FROM orders
WHERE created >= CURDATE()
GROUP BY ID 
ORDER BY price DESC;
	

-- Менеджеры с наибольшей активностью

SELECT users.id, COUNT(DISTINCT users.sentry) + COUNT(DISTINCT users.status) + COUNT(DISTINCT profiles.interests) AS activity 
	FROM users
    	LEFT JOIN profiles
      		ON users.id = profiles.user_id AND interests NOT LIKE ''
  	WHERE users.sentry = 'ok' AND status LIKE 'activity'
  	GROUP BY users.id
  	ORDER BY activity DESC;
 



