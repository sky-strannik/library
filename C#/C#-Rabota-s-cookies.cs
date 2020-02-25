// Работа с cookies http://zennolab.com/discussion/threads/rabota-s-cookies-kukami-vzjat-iz-brauzera-i-ispolzovat-v-get-post-don-shampinon.33469/
var cookies = instance.GetCookie("site.com", false);
cookies += instance.GetCookie("another-site.com", false);
return cookies;

// Вариант 2.
// save cookie
string CookiesFile = project.Directory + @"\cookies-temp.txt";
instance.SaveCookie(CookiesFile);
string text = System.IO.File.ReadAllText(CookiesFile);
Macros.TextProcessing.ToList(text, "\r\n", "Text", project, project.Lists["cookies"]);
System.IO.File.Delete(CookiesFile);