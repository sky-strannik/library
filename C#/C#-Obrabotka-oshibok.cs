// Обработка ошибок
// Всплывающие
Global.SpecialForms.AlertNotificator.Instance.DisplayAlert("Заголовок", "Текст оповещения");
Global.SpecialForms.AlertNotificator.Instance.DisplayAlert("Заголовок", "Текст оповещения", null, 5000);
// Только в логе
project.SendInfoToLog("Текст оповещения");
project.SendErrorToLog("Текст оповещения", "Текст перед оповещением");
project.SendWarningToLog("Текст оповещения", "Текст перед оповещением", true);
// true - выводить в лог ZennoPoster'a (по умолчанию не выводится, однако в ProjectMaker выводится всегда вне зависимости от true/false)

/*
оповещение: SendInfoToLog
предупреждение: SendWarningToLog
ошибка: SendErrorToLog
*/

//Получить ошибку из-за которой выполнение шаблона остановилось
var error = project.GetLastError();
if(error != null)
project.Variables["errors"].Value = string.Format("ActionComment: {0}.\r\nActionGroupId: {1}.\r\nActionId: {2}", error.ActionComment, error.ActionGroupId, error.ActionId);


// Отлов ошибок с оповещением в телеграм:
// -----------------------------------------
// Получить ошибку из-за которой выполнение шаблона остановилось
var error = project.GetLastError();
var action_errors = "";
if(error != null)
    action_errors = string.Format("ActionComment: {0}.\r\nActionGroupId: {1}.\r\nActionId: {2}\r\n--------------------------------------------------------", error.ActionComment, error.ActionGroupId, error.ActionId);
 
project.Variables["action_errors"].Value = action_errors;
 
// Присваиваем переменной путь к файлу
string strFilePath = project.Directory + @"\actions_errors.txt";
// В файле на этот момент находится текст. Чтобы текст дописывался с новой строки - используем Environment.NewLine
File.AppendAllText(strFilePath,
        project.Variables["login"].Value + Environment.NewLine +
        DateTime.Now.ToString("yyyy-dd-MM-hh-mm-ss") + Environment.NewLine +
        action_errors + Environment.NewLine);
 
// Сохраняем скриншот 1й вариант
string recognition = ZennoPoster.CaptchaRecognition("CaptchaSaver.dll",
        instance.ActiveTab.FindElementByAttribute("body", "tagname", "body", "regexp", 0).DrawToBitmap(false).DrawToBitmap(false),
        project.Path + "error\\" + project.Variables["login"].Value + DateTime.Now.ToString("-yyddMM-hhmmss") + ".jpg");
 
// Сохраняем скриншот 2й вариант закомментируйте или раскоментируйте вариант сохранения скриншота
//File.WriteAllBytes(project.Path + "error\\" + project.Variables["login"].Value + ".jpg", Convert.FromBase64String(instance.ActiveTab.FindElementByTag("html", 0).DrawToBitmap(false)));
 
// Постим в телегу сообщение
string resultGet = ZennoPoster.HttpGet(
        "https://api.telegram.org/bot373546537:AAGKerfDFHFGHFGGDGERWERTWERGWERGER/sendMessage?chat_id=@RGRGRGHRHRHRGHRGHRHG&text=тут ваш текст",
        "", "UTF-8", ZennoLab.InterfacesLibrary.Enums.Http.ResponceType.BodyOnly);
// -----------------------------------------
