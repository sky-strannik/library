// Поиск в переменной по регулярке с сохранением результата
string text = project.Variables["config"].Value;
string pattern = @"(?<=<title>).*?(?=</title>)";
project.Variables["title"].Value = Convert.ToString(Regex.Match(text, pattern));
// или
project.Variables["title"].Value = Convert.ToString(Regex.Match(text, @"(?<=<title>).*?(?=</title>)"));