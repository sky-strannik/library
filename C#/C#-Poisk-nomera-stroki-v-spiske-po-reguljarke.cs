// Поиск номера строки в списке по регулярке
var ListCache = project.Lists["cache"];
string pattern = "~.*";
return ListCache.IndexOf(ListCache.First(e=>System.Text.RegularExpressions.Regex.IsMatch(e, pattern)));