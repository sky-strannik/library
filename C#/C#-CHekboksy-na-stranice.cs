// Чекбоксы на странице
// Ставим значение 0 всем чекбоксам на странице
HtmlElementCollection hecol = instance.ActiveTab.FindElementsByAttribute("input:checkbox", "fulltagname", "input:checkbox", "regexp");
for(int i = 0; i< hecol.Count; i++)
{
    hecol.Elements[i].SetValue("0", instance.EmulationLevel, false);
}

// Делаем клик по всем чекбоксам на странице
HtmlElementCollection hecol = instance.ActiveTab.FindElementsByAttribute("input:checkbox", "fulltagname", "input:checkbox", "regexp");
    for(int i = 0; i< hecol.Count; i++)
    {
        hecol.Elements[i].Click();
    }
