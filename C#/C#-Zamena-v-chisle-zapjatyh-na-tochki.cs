// Замена в числе запятых на точки
System.Globalization.CultureInfo culture = new System.Globalization.CultureInfo("en-US");
double a = double.Parse(project.Variables["go"].Value.Replace(",", "."), culture);
return Convert.ToString(a / 100, culture);