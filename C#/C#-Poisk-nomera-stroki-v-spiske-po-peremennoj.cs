// Поиск номера строки из переменной
var ListCache = project.Lists["categories"];
string category = project.Variables["category"].Value.Trim();
category = Macros.TextProcessing.PrepToJavaScriptEval(category);
return ListCache.IndexOf(ListCache.First(e=>System.Text.RegularExpressions.Regex.IsMatch(e, category)));