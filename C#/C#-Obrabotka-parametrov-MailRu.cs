// Обработка параметров MailRu

string resultGet = project.Variables["resultGet"].Value; // переменная с результатом GET запроса
 
project.Variables["cookie"].Value = Regex.Match(resultGet, "(?<=Set-Cookie: ).*?(?=;)").Value;
project.Variables["id"].Value = Regex.Match(resultGet, "(?<=<input\ type=\"hidden\" name=\"ID\" value=\").*(?=\"/>)").Value;
project.Variables["x_reg_id"].Value = Regex.Match(resultGet, "(?<='x_reg_id': ').*(?=')").Value;
project.Variables["name"].Value = Regex.Match(resultGet, "(?<=:first', 'firstName': 'input\[name=\\').*?(?=\\'\]:-)").Value;
project.Variables["family"].Value = Regex.Match(resultGet, "(?<=:first', 'lastName': 'input\[name=\\').*?(?=\\'\]:-)").Value; // исправил название переменной
project.Variables["god"].Value = Regex.Match(resultGet, "(?<='x_reg_id', ').*?(?=', 'BirthMonth', ')").Value;
project.Variables["pol"].Value = Regex.Match(resultGet, "(?<=<input type=\"radio\" class=\"vtm\" name=\").*?(?=\" value=\"1\" id=\"man1\">)").Value;
project.Variables["name_mail"].Value = Regex.Match(resultGet, "(?<=\{'login': 'input\[name=\\').*?(?=\\'\])").Value; // исправил название переменной
project.Variables["password1"].Value = Regex.Match(resultGet, "(?<=name=\").*?(?=\" value=\"\" type=\"password\")").Value;
project.Variables["password2"].Value = Regex.Match(resultGet, "(?<=name=\").*?(?=\" value=\"\" type=\"password\")", RegexOptions.RightToLeft).Value;
project.Variables["secret_vopros"].Value = Regex.Match(resultGet, "(?<=<label for=\").*?(?=\" class=\"sig1\">Свой вопрос</label>)").Value;
project.Variables["otvet"].Value = Regex.Match(resultGet, "(?<=<label for=\").*?(?=\" class=\"sig1\">Ответ</label>)").Value;
project.Variables["dop_mail"].Value = Regex.Match(resultGet, "(?<=<label for=\").*?(?=\" class=\"sig1\">Дополнительный e-mail</label>)").Value;
project.Variables["captha1"].Value = Regex.Match(resultGet, "(?<=<input id=\"captchaCode\" class=\"inPut form__captcha-old__input\" type=\"text\" name=\").*?(?=\" value=\")").Value;
project.Variables["cpat"].Value = Regex.Match(resultGet, "(?<=<img src=\"//c\.mail\.ru/c/).*?(?=\")").Value;