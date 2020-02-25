// Из буфера обмена
return System.Windows.Forms.Clipboard.GetText();

// Помещает значение переменной в буфер обмена и делает вставку нажатием ctrl+v
var descr = project.Variables["var1"].Value;
System.Windows.Forms.Clipboard.SetText(descr);
instance.ActiveTab.KeyEvent("v","press","ctrl");