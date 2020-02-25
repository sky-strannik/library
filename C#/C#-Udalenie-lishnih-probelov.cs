// Удаление лишних пробелов
string input = project.Variables["text"].Value;
string pattern = "\\s+";
string replacement = " ";
string result = Regex.Replace(input, pattern, replacement);
return result;