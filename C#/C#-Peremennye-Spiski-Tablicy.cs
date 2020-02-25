// Берем переменные из проекта
string work = project.Variables["work"].Value; // Берем переменную из проекта
string work = project.Variables["work"].Value.Trim();
int cnt = int.Parse(project.Variables["cnt"].Value);
int cnt = System.Convert.ToInt32(project.Variables["cnt"].Value);
string num = num.ToString(); // Преобразуем в строку

// Меняем тип переменной, для работы внутри методов C#
// Переводим переменную проекта mailDays типа стринг, в тип инт
int mailDaysC = int.Parse(project.Variables["mailDays"].Value);
//Переводим переменную проекта useSSL типа стринг, в тип bool
bool mailDaysC = bool.Parse(project.Variables["useSSL"].Value);

// Декодирование запросов
return System.Net.WebUtility.HtmlDecode(project.Variables["get"].Value);

// Очищаем все переменные
var regex = ".*";
project.Variables.Keys
.Where(key=>Regex.IsMatch(key, regex))
.ToList()
.ForEach(key=>project.Variables[key].Value = "");

// Выборочная очистка переменных
project.Variables["var1"].Value = "";
project.Variables["var2"].Value = ""; 

// Передаем переменные в проект
project.Variables["work"].Value = work;
project.Variables["cnt"].Value = Convert.ToString(cnt);

// Берем в переменную через разделитель
// 01:00:00, 02:00:00, 9:00:00, 11:00:00
var time = project.Variables["time"].Value;
string[] hours = time.Split(',');

// Trim
string city = cityList[b].Trim();
string text = Macros.TextProcessing.Trim(text, ".,", "Full");

// Списки
var ListCache = project.Lists["cache"]; // Берем список из проекта
var ListCount = project.Lists["cache"].Count.ToString(); // Кол-во строк в списке
ListCache.Add(ListCache[i]); // Добавляем результат обработки в список
ListCache.RemoveAt(i); // Удаляем результат обработки из списка
List<string> t1 = new List<string>(); // Удаляем дубли из списка
ListCache.Distinct().ToList(); // Удаляем дубли из списка
ListCache.Clear(); // Очистка списка

// Удаление дублей из списка. Вариант
string path = project.Variables["puth"].Value;
var lines = System.IO.File.ReadAllLines(path).ToList().Distinct().ToList();;
System.IO.File.WriteAllText(path, string.Join(Environment.NewLine, lines));
return 0;

// Удаление дублей из списка. Вариант
IZennoList list1 = project.Lists["List 1"]; // Вычитаем из первого. Второй остаётся нетронутым
IZennoList list2 = project.Lists["List 2"];
List<string> tmpList = new List<string>();
tmpList = list1.Except(list2).ToList();
list1.Clear();
list1.AddRange(tmpList);

// Таблицы
var SourceTable = project.Tables["base"]; // Берем таблицу из проекта
SourceTable.AddRow(result); // Добавляем результат обработки в таблицу
sourceTable.DeleteRow(i); // Удаляет строку таблицы

// Строка в таблицу
IZennoTable table = project.Tables["base"];
// table.ColSeparator = ";";
lock(SyncObjects.ListSyncer)
{
    table.AddRow("one;two;three;four");
}

// Перезапись строки заголовков, если не стоит галка "Первая строка - заголовки"
string str = "000:111:222"; // строка которую добавляем
string separator = ":"; // разделитель
string[] col_name = {"A","B","C","D","E","F","G","H"}; // тут аналогичным образом нужно прописать до конца алфавита (ну или сколько макс. столбцов у вас)
// int[] col_name = new int[1000];
// for (int t = 0; t < col_name.Length; t++) col_name[t] = t+1;             
project.Tables["mytable"].ColSeparator = separator; // назначаем разделитель для таблицы
var data = str.Split(new string[]{separator},StringSplitOptions.None).ToList();
for(int i=0; i<data.Count; i++){
    project.Tables["mytable"].SetCell(col_name[i],0,data[i]);
}