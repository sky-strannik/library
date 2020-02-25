// Разбиваем строку по разделителю
string acc_full = project.Variables["account_source"].Value;
var account = acc_full.Split('|').ToList();
project.Variables["login"].Value = account[0];
project.Variables["pass"].Value = account[1];
project.Variables["hz"].Value = account[2];
