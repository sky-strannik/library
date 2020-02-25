// Конвертирование переменных: https://msdn.microsoft.com/ru-ru/library/system.convert.aspx

int a = Convert.ToInt32(project.Variables["var"].Value);
// обратный перевод:
int a = 3;
// так
project.Variables["var"].Value = Convert.ToString(a);
// или так
project.Variables["var"].Value = a.ToString();

// Конвертирование строки в число
string s = "5";
int i = Int32.Parse(s);

// Конвертирование с проверкой
string stringValue = "10";
int integerValue = 0;
if (!int.TryParse(stringValue, out integerValue))
{
    MessageBox.Show("Не удалось преобразовать \""+stringValue+\" в int!");
}