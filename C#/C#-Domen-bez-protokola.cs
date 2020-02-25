// Домен без протокола
var Url = project.Variables["domen"].Value;
return new Uri(Url).Host;