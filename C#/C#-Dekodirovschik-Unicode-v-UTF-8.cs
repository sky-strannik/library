// Декодировщик Unicode в UTF-8
var str = @"\u0412\u0432\u0435\u0434";
str = Regex.Replace(str, @"\\u([\da-f]{4})", m => ((char)Convert.ToInt32(m.Groups[1].Value, 16)).ToString());
return str;

// Еще вариант
return System.Text.RegularExpressions.Regex.Unescape(project.Variables["Название_переменной"].Value);