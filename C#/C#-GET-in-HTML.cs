// Полученный html из get установить в активную вкладку
var x = project.Variables["get"].Value; // переменная x с html кодом после гет запроса
instance.ActiveTab.MainDocument.Body.SetAttribute("innerHtml", x);