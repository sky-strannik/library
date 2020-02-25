// Скачать почту, каждое письмо в отдельную строку списка
// http://help.zennolab.com/en/v5/zennoposter/5.0.0/ZennoLab.CommandCenter~ZennoLab.CommandCenter.ZennoPoster~BulkMailDownload.html


var mail_login = project.Variables["login"].Value;
var mail_pass = project.Variables["pass"].Value;
Tuple<string, string, string, string>[] allMails;
allMails = ZennoPoster.BulkMailDownload(mail_login, mail_pass, "imap.gmail.com", 993, true, ZennoLab.InterfacesLibrary.Enums.Email.EmailProtocol.IMAP, 24*100, 100, false);
var list = project.Lists["cache"];
 
foreach(Tuple<string, string, string, string> tuple in allMails) {
    // tuple.Item1 - sibject, tuple.Item2 - from, tuple.Item3 - html message, tuple.Item4 - text message
    //list.Add(tuple.Item1+";"+tuple.Item2+";"+tuple.Item3+";"+tuple.Item4);
    list.Add(tuple.Item3+";"+tuple.Item4); // заносим в список
}
/*
После выполнения этого кода просто берёте построчно данные из списка и обрабатываете их. Или же Операции над списком - Объединить в переменную. И дальше работаете с переменной.
*/
ZennoPoster.BulkMailDownload - расшифровка параметров:
"name@gmail.com", 											// Логин
"ххххххх", 													// Пароль
"imap.gmail.com",											// Сервер
993, 														// Порт
true, 														// Шифрование SSL
ZennoLab.InterfacesLibrary.Enums.Email.EmailProtocol.IMAP,	// Протокол POP или IMAP
24*100, 													// За период: слева часы, справа дни
20, 														// Сколько максимум скачивать писем
false);														// True - удалять письма, False - оставлять
