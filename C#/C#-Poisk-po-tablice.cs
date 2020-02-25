// Поиск по таблице
var textContains = project.Variables["email"].Value;
// Получаем таблицу, в которой будем искать
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