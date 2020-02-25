// Unixtime с учетом часового пояса
int unixTime = (int)(DateTime.Now - new DateTime(1970,1,1)).TotalSeconds;
return unixTime;

// Дата и Время
return DateTime.Now.ToString("yyyy-MM-dd");
return DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss-fff");
project.Variables["date1"].Value = DateTime.Now.ToString("yyyy-MM-dd");
project.Variables["date2"].Value = DateTime.Now.ToString("yyyyMMdd");
project.Variables["date3"].Value = DateTime.Now.ToString("dd.MM.yyyy");
project.Variables["time"].Value = DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss-fff");

// Дата в пути
{-Project.Directory-}{-Variable.cat-}[{-TimeNow.Datedd-MM-yy-}].csv

// Пример 1
var date = DateTime.Now.ToString("yyyyMMdd");
var date1 = DateTime.Now.AddDays(-1).ToString("yyyyMMdd");
var date2 = DateTime.Now.AddDays(-2).ToString("yyyyMMdd");
var date3 = DateTime.Now.AddDays(-3).ToString("yyyyMMdd");
string result = "^" + date + "|^" + date1 + "|^" + date2 + "|^" + date3;
return result;

// Пример 2
int week = 2;
int unixTime = (int)(DateTime.Now - new DateTime(1970,1,1)).TotalSeconds;
week = week * 604800; 	// Умножаем на количество секунд в неделю
week = unixTime - week;	// Вычитаем количество прошедших недель
DateTime pDate = (new DateTime(1970, 1, 1, 0, 0, 0, 0)).AddSeconds(week);
string nDate = pDate.ToString();
var dataSA = DateTime.Parse(nDate).ToString("yyMMdd");
return dataSA;

// Пример 3. Меняем формат
string format = "dd MM yyyy HH:mm";
string orderTime = project.Variables["orderTime"].Value.Trim();
DateTime itemdate = DateTime.ParseExact(orderTime, format, CultureInfo.InvariantCulture);
TimeSpan span = itemdate.Subtract(new DateTime(1970,1,1,0,0,0));
int unixTime = System.Convert.ToInt32(span.TotalSeconds);
DateTime pDate = (new DateTime(1970, 1, 1, 0, 0, 0, 0)).AddSeconds(unixTime);
string nDate = pDate.ToString();
var dataNEW = DateTime.Parse(nDate).ToString("dd.MM.yyyy HH:mm:ss");
return dataNEW;