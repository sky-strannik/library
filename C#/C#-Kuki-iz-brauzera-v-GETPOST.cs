// Взять cookies из браузера и использовать в GET/POST
var site = project.Variables["Site"].Value; // Сайт вида test.ru
var cookies = instance.GetCookie(site, false);
return cookies;

// Прочитать куки из файла и использовать их в браузере
instance.LoadCookie(project.Variables["cookies_file"].Value);

// Чтобы получить все куки, а не для конкретного домена можно использовать GetCookie без параметров
instance.GetCookie();

