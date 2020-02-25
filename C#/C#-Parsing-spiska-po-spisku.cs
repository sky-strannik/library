// Парсинг списка по списку

//кладем в переменную то что будет парсится
string body = project.Variables["body"].Value;
//составляем регулярку
Regex regularka = new Regex(project.Variables["regularka"].Value);
//определяем список в который парсим
var link = project.Lists["link"];
//парсим
regularka.Matches(body).Cast<Match>().ToList().ForEach(m=>link.Add(m.Value));