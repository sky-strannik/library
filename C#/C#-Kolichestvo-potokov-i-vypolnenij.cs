// Изменить количество потоков или выполнений
// https://zennolab.com/discussion/threads/kak-dobavit-1-umenshit-1-kolichestvo-potokov-v-processe-vypolnenija.42614/#post-316376

string settings = "<LimitOfThreads>1</LimitOfThreads>" // Этот параметр устанавливает нужное число потоков
                + "<MaxAllowOfThreads>0</MaxAllowOfThreads>"
                + "<DoneSuccesfully>0</DoneSuccesfully>"
                + "<DoneAll>0</DoneAll>"
                + "<NumberOfTries>0</NumberOfTries>" // Это число выполнений
                + "<LastNumberOfTries>0</LastNumberOfTries>"
                + "<Priority>50</Priority>"
                + "<Proxy>{DoNotUseProxy, IfPossible, UseProxyWithoutRemove, UseProxy}</Proxy>"
                + "<Status>Newbie</Status>"
                + "<ProxyLabels></ProxyLabels>"
                + "<ShouldBeExecutedRandomly>{True, False}</ShouldBeExecutedRandomly>"
                + "<GroupLabels>Без метки</GroupLabels>"
                + "<GroupStates>Выполнены</GroupStates>"
                + "<MaxNumOfSuccesStop>-1</MaxNumOfSuccesStop>"
                + "<MaxNumOfFailStop>-1</MaxNumOfFailStop>"
                + "<NumOfFailStop>0</NumOfFailStop>";

ZennoPoster.SetExecutionSettings(Guid.Parse(project.TaskId), settings); // Применит настройки к текущему шаблону
ZennoPoster.SetExecutionSettings("НазваниеШаблона", settings); // Применит настройки к шаблону по имени

// Вариант 2.
// AddTries- это добавление нужного количества выполнений!
// SetTries - это установка нужного количества выполнений!

// Добавить 1 поток
var id = Guid.Parse(project.TaskId);
ZennoPoster.AddTries(id, 1);

// Установить 5 потоков исполнения
var id = Guid.Parse(project.TaskId);
ZennoPoster.SetTries(id, 5);

// Вариант 3.
int cnt = System.Convert.ToInt32(project.Variables["line"].Value);
var id = Guid.Parse(project.TaskId);
ZennoPoster.SetTries(id, cnt+1);

// Количество ПОТОКОВ! - не работает!
// Делаем через bat-файл в св-вах шаблона в ZP.
string status = string.Empty;
for(int a = 0; a < 10; a++)
	{
	var tpl = project.Variables["tpl"].Value;; // ИМЯ ШАБЛОНА
	var tasks = ZennoPoster.TasksList;
	foreach(var task in tasks)
		{
		var doc = new System.Xml.XmlDocument();
		doc.LoadXml("<Task>" + task + "</Task>");
		string name;
		var nameNode = doc.SelectSingleNode("Task/Name");
		if(nameNode != null && nameNode.InnerText.Equals(tpl))
			{
			name = nameNode.InnerXml;
			//ZennoPoster.AddTries(name, 1);
			if (Global.Variables.IsProjectMaker) if (!Global.Variables.IsDebugMode) break;
			// Количество 
			status = doc.SelectSingleNode("Task/ExecutionSettings/NumberOfTries").InnerText;
			//Complete
			return status;
			}
		}
	}