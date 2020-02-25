// Столбец таблицы перенести в список

// получаем таблицу, в котором будем брать
var sourceTable = project.Tables["SourceTable"];
// получаем список, в которой будем копировать столбец из таблици
var sourceList = project.Tables["SourceList"];
 
lock(SyncObjects.TableSyncer)
{
    for(int i=0; i < sourceTable.RowCount; i++)
    {
        // читаем строку из таблицы (это будет массив ячеек)
        var cells = sourceTable.GetRow(i).ToArray();
       
        sourceList.Add(cells[1]);//В cells[1] вместо ОДИН вставляем номер столбца который будем копировать в список
           
    }
}