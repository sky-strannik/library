Ресурсы:
https://zennolab.com/wiki/ru:json_xml
https://zennolab.com/discussion/threads/obrabotka-rezultatov-v-json.27622/
https://www.it-swarm.dev/ru/c#/kak-konvertirovat-json-v-xml-ili-xml-v-json/957971965/
https://www.newtonsoft.com/json/help/html/ConvertingJSONandXML.htm

Библиотека https://www.nuget.org/packages/Newtonsoft.Json/
Чтобы скачать его с nuget.org, надо перейти по ссылке
https://www.nuget.org/api/v2/package/Newtonsoft.Json/12.0.3
Полученный файл newtonsoft.json.12.0.3.nupkg - это zip-архив. Например, в Windows Explorer его можно переименовать, заменить .nupkg на .zip, и открыть.
В \lib находятся \net20, \net35, и т.д.
Если для вашего проекта требуется сборка для .NET 4.5, то в \net45 находится соответствующий файл Newtonsoft.Json.dll
