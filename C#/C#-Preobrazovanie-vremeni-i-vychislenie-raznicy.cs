// Преобразование времени и вычисление разницы
string timePrice = project.Variables["timePrice"].Value;
string timeNow = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
string format = "yyyy-MM-dd HH:mm:ss";
if (timePrice != "")
{
DateTime itemPrice = DateTime.ParseExact(timePrice, format, CultureInfo.InvariantCulture);
TimeSpan span1 = itemPrice.Subtract(new DateTime(1970,1,1,0,0,0));
int Time1 = span1.TotalSeconds;
DateTime itemNow = DateTime.ParseExact(timeNow, format, CultureInfo.InvariantCulture);
TimeSpan span2 = itemNow.Subtract(new DateTime(1970,1,1,0,0,0));
int Time2 = span2.TotalSeconds;
return Time2-Time1;
}
else return "0";