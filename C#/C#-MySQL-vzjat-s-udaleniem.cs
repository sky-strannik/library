// C# MySQL взять с удалением
string zapros = @"LOCK TABLES nametable WRITE;
         SELECT * FROM nametable LIMIT 1;
         DELETE FROM nametable LIMIT 1;
         UNLOCK TABLES;";
string rezult = ZennoPoster.Db.ExecuteQuery(zapros, null, ZennoLab.InterfacesLibrary.Enums.Db.DbProvider.MySqlClient, "server=localhost;user id=root;database=base", " ", "");
return rezult;

// Вариант 2. Получение свободного ID в многопотоке
string query = "start transaction; set @free_id=-1; SELECT id from `table` where used = 0  ORDER BY RAND() limit 1 into @free_id for update; UPDATE `table` SET used = 1 WHERE used = 0 and id=@free_id; select @free_id; commit;";
string result = ZennoPoster.Db.ExecuteScalar(query,null,ZennoLab.InterfacesLibrary.Enums.Db.DbProvider.MySqlClient, project.Variables["connect"].Value);
