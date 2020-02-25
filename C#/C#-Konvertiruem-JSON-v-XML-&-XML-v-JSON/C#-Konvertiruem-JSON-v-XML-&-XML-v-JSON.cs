var ListJson = project.Lists["json"];
// string timeXML = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
string json = string.Join("\n", ListJson);    // Список в переменную
json = Macros.TextProcessing.Replace(json, @"\n", ",", "Regex", "All");
// json = "{\"?xml\":{\"@version\":\"1.0\",\"@encoding\":\"UTF-8\",\"@date=\":\"" + timeXML + "\"},\"catalog\":{\"offer\":[" + json + "]}}";
json = "{\"?xml\":{\"@version\":\"1.0\",\"@encoding\":\"UTF-8\"},\"catalog\":{\"offer\":[" + json + "]}}";
project.Variables["json"].Value = json;
XmlDocument doc = JsonConvert.DeserializeXmlNode(json);
return doc.OuterXml;