// Config файл
// http://zennolab.com/discussion/threads/chtenie-parametrov-v-avtosozdavaemye-peremennye-iz-ini-fajla-odnim-snippetom.41824/

// Содержимое ini
[Optoins] // Блок переменных
x=1024
y=768

[Panels]
Closed=0

и т.д.

////////////////////////////

// Код снипета в самом начале проекта:

//Берем имя проекта и заменяем расширение на ini
string config_file = project.Name.Replace("xmlz","ini");
//если несколько проектов юзают один и тот же конфиг
//string config_file = "Config.ini";
string config_path = Path.Combine(project.Directory,config_file);
 
//проверяем существование конфига
if (File.Exists(config_path)){
    project.SendInfoToLog("Ќачинаем загрузку конфигурации из файла:"+config_file);  
    var vFile = File.ReadAllLines(config_path);
    var vList = new List<string>(vFile);
 
    string CurrentSection = String.Empty;
 
    foreach( string str in vList){              
        //чистим лишние пробелы и табуляции с начала и конца строки
        string cstr = str.Trim();
        //если пустышка - дальше
        if (cstr==String.Empty) continue;
        //если первый символ комментарий - дальше
        if (cstr[0]=='#'||cstr[0]==';') continue;
        //если строка соответствет секции сохраняем ею имя
        Match m = Regex.Match(cstr,@"(?<=\[).*(?=])",RegexOptions.None);
        if (m.Success){
            CurrentSection = m.Value;
            project.SendInfoToLog("Ќашли секцию " + CurrentSection);
            continue;
        }
     
        //ловим параметр и значение
        string ParamName = String.Empty;
        Match pn = Regex.Match(cstr,@".*?(?==)",RegexOptions.None);      
        Match pv = Regex.Match(cstr,@"(?<==).*",RegexOptions.None);      
     
        if (pn.Success&&pv.Success){
            project.SendInfoToLog("наши параметр "+pn.Value);            
         
            string vParamValue = pv.Value;
            string vParamName = String.Empty;
            if (CurrentSection==String.Empty){
                vParamName = "cfg_"+pn.Value;
            } else {
                vParamName = "cfg_"+CurrentSection+"_"+pn.Value;
            }
                //проверяем существование переменной, если нет то создаем новую
                if (project.Variables.Keys.Contains(vParamName)){
                    project.SendInfoToLog("ЏеременнаЯ "+vParamName+" уже существует - присваиваем ей значение");                  
                    project.Variables[vParamName].Value = vParamValue;
                } else {
                    project.SendInfoToLog("‘оздаем переменную "+vParamName+" и присваиваем ей значение");
                    object obj = project.Variables;
                    obj.GetType().GetMethod("QuickCreateVariable").Invoke(obj,new Object[]{vParamName});
                    project.Variables[vParamName].Value = vParamValue;
                }
        }
    }  
} else {
   project.SendInfoToLog("Ћтсутствует файл конфигурации: "+config_path);  
}