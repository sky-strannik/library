// Количество символов
return project.Variables["имя_переменной"].Value.Length;

// Количество символов без пробелов
return project.Variables["var1"].Value.Replace(" ", "").Length;

// Количество символов без знаков (!,") ?
string str = project.Variables["var"].Value;
str = Regex.Replace(str, "[(!,\")]", "");
return str.Length;