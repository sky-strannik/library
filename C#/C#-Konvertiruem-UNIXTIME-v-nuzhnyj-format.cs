// Конвертируем UNIXTIME в нужный формат
int numVal = Int32.Parse(project.Variables["unixTimeAds"].Value);
double timestamp = numVal;
System.DateTime dateTm = new System.DateTime(1970, 1, 1, 0, 0, 0, 0);
dateTm = dateTm.AddSeconds(timestamp).ToLocalTime();
string nDate = dateTm.ToString("yyyy-MM-ddTHH:mm:ss+hh:mm");
return nDate;