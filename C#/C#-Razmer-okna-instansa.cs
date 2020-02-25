// Задаем размер окна инстанса
var www = Convert.ToInt32(project.Variables["wwinst"].Value);
var hhh = Convert.ToInt32(project.Variables["hhinst"].Value);
instance.SetWindowSize(www,hhh);