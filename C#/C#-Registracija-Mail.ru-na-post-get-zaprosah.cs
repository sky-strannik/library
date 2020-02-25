// Регистрация Mail.ru на post get запросах
// http://zennolab.com/discussion/threads/mail-ru-post-get.31814/page-5

//Get запрос, получаем куки
var resultGet = ZennoPoster.HttpGet(
    url:"https://e.mail.ru/signup?from=main_noc",
    proxy:project.Variables["Proxy"].Value, // Если регаем без прокси, то строку в коде комментим!!!
    Encoding:"utf-8",
    respType:InterfacesLibrary.Enums.Http.ResponceType.HeaderAndBody,
    Timeout:30000,
       Cookies:"",
    UserAgent:project.Profile.UserAgent,
    UseRedirect:true,
    MaxRedirectCount:5,
    AdditionalHeaders: new [] {
                                "Host: e.mail.ru",
                                "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                                "Accept-Language: uk,ru;q=0.8,en-US;q=0.5,en;q=0.3 ", //+project.Profile.AcceptLanguage,
                                "Accept-Encoding: gzip, deflate, br" ,//+project.Profile.AcceptEncoding,
                                "Referer: https://e.mail.ru/signup?from=main_noc",
                                "Connection: keep-alive"
                                }
);
//Проверяем на бан по IP
if (Regex.Match(resultGet, "noPhoneLink.*?").Value == "noPhoneLink")//Ip чист
    {  
                               
        // Парсим регулярками переменные
        var cookie = Regex.Match(resultGet, "(?<=Set-Cookie: ).*?(?=;)").Value;
        var id = Regex.Match(resultGet, "(?<=<input\\ type=\"hidden\" name=\"ID\" value=\").*(?=\"/>)").Value;
        var x_reg_id = Regex.Match(resultGet, "(?<='x_reg_id':\\ ').*(?=')").Value;
        var name = Regex.Match(resultGet, "(?<=:first',\\ 'firstName':\\ 'input\\[name=\\\\').*?(?=\\\\']:)").Value;
        var surname = Regex.Match(resultGet, "(?<=:first',\\ 'lastName':\\ 'input\\[name=\\\\').*?(?=\\\\']:)").Value;
        var year = Regex.Match(resultGet, "(?<='x_reg_id', ').*?(?=', 'BirthMonth', ')").Value;
        var sex = Regex.Match(resultGet, "(?<=<input type=\"radio\" class=\"vtm\" name=\").*?(?=\" value=\"1\" id=\"man1\">)").Value;
        var email = Regex.Match(resultGet, "(?<=\\{'login':\\ 'input\\[name=\\\\').*?(?=\\\\'])").Value;
        
		var password1 = Regex.Match(resultGet, "(?<=name=\").*(?=\"\\ autocomplete=\"new-password\")").Value;
        var password2 = Regex.Match(resultGet, "(?<=name=\").*?(?=\"\\ value=\"\"\\ type=\"password\"\\ class=\"inPut\"\\ maxlength=\"40\"/>)", RegexOptions.RightToLeft).Value;
		// Если не работает password1 и password2, то:
		//var password1 = Regex.Match(resultGet, "(?<=name=\").*(?=\"\\ autocomplete=\"new-password\")").Value;
		//var password2 = Regex.Match(resultGet, "(?<=name=\").*?(?=\"\\ value=\"\"\\ type=\"password\"\\ class=\"inPut\"\\ maxlength=\"40\"/>)", RegexOptions.RightToLeft).Value;
 
        var catpcha = Regex.Match(resultGet, "(?<=<input id=\"captchaCode\" class=\"inPut form__captcha-old__input\" type=\"text\" name=\").*?(?=\" value=\")").Value;
        var cpat = Regex.Match(resultGet, "(?<=2\\?r=).*?(?=\"\\ )").Value;
        var day = Regex.Match(resultGet, "(?<=BirthMonth',\\ ').*?(?=\')").Value;
                //Get на каптчу
                var captcha__get = ZennoPoster.HttpGet(
                                                        url:"http://c.mail.ru/c/2?r=" + cpat,
                                                           proxy:project.Variables["Proxy"].Value,
                                                        Encoding:"utf-8",
                                                        respType:InterfacesLibrary.Enums.Http.ResponceType.File,
                                                        Timeout:5000,
                                                           Cookies:cookie,
                                                        UserAgent:project.Profile.UserAgent,
                                                        UseRedirect:true,
                                                        MaxRedirectCount:5,
                                                         AdditionalHeaders: new []     {
                                                                                    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                                                                                    "Accept-Language: uk,ru;q=0.8,en-US;q=0.5,en;q=0.3 ", //+project.Profile.AcceptLanguage,
                                                                                    "Accept-Encoding: gzip, deflate, br" ,//+project.Profile.AcceptEncoding,
                                                                                    "Referer: https://e.mail.ru/signup?from=main_noc",
                                                                                    "Connection: keep-alive"
                                                                                    }
                                                    );
        //Обрабатываем каптчу
        var image = System.Drawing.Image.FromFile(@captcha__get);
        string base64String = String.Empty;
        using (System.IO.MemoryStream ms = new System.IO.MemoryStream())
            {
                image.Save(ms, System.Drawing.Imaging.ImageFormat.Png);
                byte[] imageBytes = ms.ToArray();
                base64String = Convert.ToBase64String(imageBytes);
            }
        var result = ZennoPoster.CaptchaRecognition("RuCaptcha.dll", base64String,"" ); // Указываем модуль распознавания CapMonsterModule=ZennoLab.MailRu
        var tmp = result.Split(new [] {"-|-"}, StringSplitOptions.None);
        if (tmp.Length <= 1) return null;
   
            //Post отправка данных регистрации на сервер
            var post = ZennoPoster.HttpPost(
                                            url:"https://e.mail.ru/reg?from=main_noc",
                                            content:"signup_b=1&sms=1&no_mobile=1&ID=" + id + "&Count=1&back=&browserData=NoJS&Mrim.Country=24&Mrim.Region=226&x_reg_id=" + x_reg_id +  "&security_image_id=&geo_countryId=24&geo_cityId=226&geo_regionId=999998&geo_country=&geo_place=&lang=ru_RU&" + name + "=" + project.Profile.Name + "&" + surname + "=" + project.Profile.Surname + "&" + day + "=" + project.Profile.BornDay +    "&BirthMonth=3&" + year + "=" + project.Profile.BornYear +  "&your_town=Санкт-Петербург, Россия&" + sex + "=2&" +email + "=" + project.Profile.Login +  "&RegistrationDomain=mail.ru&" + password1 + "=" + project.Profile.Password +    "&" + password2 +  "=" + project.Profile.Password + "&RemindPhoneCode=7&RemindPhone=&Password_Question=Custom&" + catpcha + "=" + tmp[0] + "&new_captcha=1",
                                            contentPostingType:"application/x-www-form-urlencoded",
                                            proxy:project.Variables["Proxy"].Value,
                                            Encoding:"utf-8",
                                            respType:ZennoLab.InterfacesLibrary.Enums.Http.ResponceType.HeaderAndBody,
                                            Timeout:30000,
                                            Cookies:cookie,
                                            UserAgent:project.Profile.UserAgent,
                                            UseRedirect:true,
                                            MaxRedirectCount:5,
                                            AdditionalHeaders: new [] {
                                                                        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                                                                        "Accept-Language: uk,ru;q=0.8,en-US;q=0.5,en;q=0.3 ", //+project.Profile.AcceptLanguage,
                                                                        "Accept-Encoding: gzip, deflate, br" ,//+project.Profile.AcceptEncoding,
                                                                        "Referer: https://e.mail.ru/signup?from=main_noc",
                                                                        "Connection: keep-alive"
                                                                        }
                                            );
            //Проверка
            string path = project.Directory + "\\";
   
                if (Regex.Match(post, "__log.v2_js").Value == "__log.v2_js")
                        {
                            FileSystem.FileAppendString(path + "Mail.ru_good_accs.txt", project.Profile.Login + "@mail.ru:" + project.Profile.Password , true);
                            project.SendInfoToLog("", "Регистрация успешна! Аккаунт  записан в " + path + "Mail.ru_good_accs.txt",true);
                       
                        }
                        else
                        {
                                   
                                if (Regex.Match(post, "2\\?r.*?").Value == "2?r")//Неверная каптча
                                        {
                                            throw new System.Exception("Не удалось зарегистрироваться, каптча разгадана неверно");
                                        }
                           
                                else
                                        {
                                            throw new System.Exception("Не удалось зарегистрироваться");
                                        }
                        }      
        }
                   
       
else    throw new System.Exception("Превышен лимит регистраций с 1 Ip");

