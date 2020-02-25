// Преобразование телефона
long NumberPhone = Convert.ToInt64(project.Variables["phone"].Value);
string Format = "0(000)000-00-00";
return NumberPhone.ToString(Format);