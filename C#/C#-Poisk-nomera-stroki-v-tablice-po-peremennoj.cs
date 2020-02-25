// Поиск номера строки в таблице по переменной
var SourceTable = project.Tables["update"];
string search = project.Variables["productCode"].Value.Trim();
string columnTable = "1"; // Номер столбца для поиска
int cnt = int.Parse(columnTable);

for (int i = 0; i<SourceTable.RowCount; i++) {
	if (SourceTable.GetCell(columnTable, i).Contains(search)) {
		// Читаем строку из таблицы (это будет массив ячеек)
		var cells = SourceTable.GetRow(i).ToArray();
		if (cells[cnt] == search) return i.ToString();
	}
}
return "";