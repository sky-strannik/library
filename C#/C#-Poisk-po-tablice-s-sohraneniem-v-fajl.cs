// Получаем таблицу, с которой будем работать
var sourceTable = project.Tables["base"];
// Ищем в каждой строчке в таблице
lock(SyncObjects.TableSyncer)
	{
    for(int i=0; i < sourceTable.RowCount; i++)
		{
        // Читаем строку из таблицы (это будет массив ячеек)
        var cells = sourceTable.GetRow(i).ToArray();
        // Пройдем в цикле по всем ячейкам
        for (int j=0; j < cells.Length; j++)
			{
            // Проверяем содержание текста в ячейке, если есть совпадение, то:
            if (cells[j].Contains(textContains))
				return "yes"; // Если нашли возвращаем "yes"
			}
		}
	}
return "no"; // Если ничего не нашли возвращаем "no"


// Получаем таблицу, с которой будем работать
IZennoTable table = project.Tables["cs_cart"];
IZennoTable cache = project.Tables["cache"];
string row;

lock(SyncObjects.TableSyncer) { 
	for (int i = 0; i < table.RowCount; i++) {
		row = string.Concat(table.GetRow(i));
		// cache.Add(row);
		if ( i < 1000 ) { 
			cache.Rows.Add(row);
		}
		else {
		//сохранить в файл
		cache.Clear();
		}

	}
}


// Сохранение в файл
StreamWriter sw = new StreamWriter(pathGo + "\\test.csv", false, Encoding.UTF8);
for (int i=0;i<mmv.RowCount;i++){
    string row = String.Join(";", mmv.GetRow(i));
        sw.Write(row);
}
sw.Close();