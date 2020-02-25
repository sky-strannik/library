// Замена в переменной
var text = project.Variables["text"].Value;
text = text.Replace("-"," "); // Заменяем "-" на " "

// Еще вариант
string result = project.Variables["productName"].Value.Trim();
return Macros.TextProcessing.Replace(result, "\t", "", "Regex", "All");