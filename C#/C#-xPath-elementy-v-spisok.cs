// Полученный html из get установить в активную вкладку
var x = project.Variables["get"].Value; // переменная x с html кодом после гет запроса
instance.ActiveTab.MainDocument.Body.SetAttribute("innerHtml", x);

// Находим через xPath элементы и кладем их в список
Tab tab = instance.ActiveTab;
if (tab.IsVoid || tab.IsNull) return -1;
// Получаем атрибут "href" всех элементов, соответствующих пути //*[@id='supermenu']/ul[1]/li[@class='tlli mkids']/a[@class='tll']
var attributes = ZennoPoster.Parser.ParseByXpath(tab, ZennoLab.InterfacesLibrary.Enums.Parser.SourceType.Dom, "//*[@id='supermenu']/ul[1]/li[@class='tlli mkids']/a[@class='tll']", "href", true).ToList();
// Фильтруем элементы
attributes.Filter(ZennoLab.InterfacesLibrary.Enums.Parser.FilterType.None, "");
// Выбираем элементы из диапазона "all"
attributes.Range("all");

project.Lists["cache"].AddRange(attributes);
