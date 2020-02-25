// Импорт или экспорт входных настроек с заменой данных

// Примеры: http://zennolab.com/discussion/threads/import-nastroek-cherez-bat-fajl.25611/
// bat файл для импорта в проект в ZP
"C:\Program Files (x86)\ZennoLab\ZennoPoster Pro\Progs\TasksRunner.exe" -o ImportInputSettings C:\Bots\eManagerVK\Gatchina\settings.xml -names "EManagerVK-L-2.2"
// Вместо -names можно ID, а получить его в контекстном меню ZP Создать bat файл.


///////////////////


// Примеры: http://zennolab.com/discussion/threads/inputsettings-nastrojki-s-koda.23962/

// Вариант 1.
string path = @"D:\settings.xml";    //Путь экспорта
File.WriteAllText(path, ZennoPoster.ExportInputSettings(new Guid(project.TaskId)));
// (!) Экспорт предназначен для запуска в ZennoPoster, не в ProjectMaker (в PM сохраняет пустой файл).

// Вариант 2.
// Экспорт настроек и замена
var id = Guid.Parse(project.TaskId);
var exportSettings = ZennoPoster.ExportInputSettings(id);
exportSettings = Regex.Replace(exportSettings, @"C:", @"D:");
// Импорт новых настроек
ZennoPoster.ImportInputSettings(id, exportSettings);


// Вариант 3.
var guid = Guid.NewGuid();
 
var task =
"<Id>"+guid+"</Id>"+
"<Name>"+project.Variables["name"].Value+"</Name>"+
"<CreateTime>01/01/0001 00:00:00</CreateTime>"+
"<ExecutionSettings>    "+
"    <LimitOfThreads>1</LimitOfThreads>"+
"    <MaxAllowOfThreads>0</MaxAllowOfThreads>"+
"    <DoneSuccesfully>0</DoneSuccesfully>"+
"    <DoneAll>0</DoneAll>"+
"    <NumberOfTries>1</NumberOfTries>"+
"    <LastNumberOfTries>0</LastNumberOfTries>"+
"    <Priority>50</Priority>"+
"    <Proxy>DoNotUseProxy</Proxy>"+
"    <Status>Newbie</Status>"+
"    <ProxyLabels></ProxyLabels>"+
"    <ShouldBeExecutedRandomly>False</ShouldBeExecutedRandomly>"+
"    <GroupLabels>"+project.Variables["label"].Value+"</GroupLabels>"+
"    <GroupStates>Выполнены</GroupStates>"+
"    <MaxNumOfSuccesStop>-1</MaxNumOfSuccesStop>"+
"    <MaxNumOfFailStop>-1</MaxNumOfFailStop>"+
"    <NumOfFailStop>0</NumOfFailStop>"+
"</ExecutionSettings>"+
"<SchedulerSettings>"+
"    <StartDate>01/01/0001 00:00:00</StartDate>"+
"    <EndDate>01/01/0001 00:00:00</EndDate>"+
"    <RepetitionCount>1</RepetitionCount>"+
"    <ScheduleType>EveryMinutes</ScheduleType>"+
"    <RepeatType>FinishAfter</RepeatType>"+
"    <ActivateTime>01/01/0001 00:00:00</ActivateTime>"+
"    <ActivateWorkTime>01/01/0001 00:00:00</ActivateWorkTime>"+
"    <IsActive>False</IsActive>"+
"    <NumberOfTries>0</NumberOfTries>"+
"    <Minutes>1</Minutes>"+
"    <Days>1</Days>"+
"    <LastScheduleDate>01/01/0001 00:00:00</LastScheduleDate>"+
"    <IsClearSucces>False</IsClearSucces>"+
"</SchedulerSettings>"+
"<Project>"+
"    <ProjectFileLocation>"+project.Variables["patch"].Value+"</ProjectFileLocation>"+
"    <ProjectType>Assembly</ProjectType>"+
"</Project>";
 
ZennoPoster.AddTask(task);

var exportSettings = ZennoPoster.ExportInputSettings(guid);
exportSettings = Regex.Replace(exportSettings, @"projectname", project.Variables["name"].Value);
ZennoPoster.ImportInputSettings(guid, exportSettings);


