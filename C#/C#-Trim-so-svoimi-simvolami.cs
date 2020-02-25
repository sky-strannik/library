// Trim со своими символами И заменяем по регулярке на "+"
string Test = project.Variables["var_filter_names"].Value.Trim();
string regexTest = System.Text.RegularExpressions.Regex.Replace(Test, @"[ .?!)(,:]", "+");
return regexTest;