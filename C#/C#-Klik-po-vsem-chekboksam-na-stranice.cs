// Клик по всем чекбоксам на странице
HtmlElementCollection hecol = instance.ActiveTab.FindElementsByAttribute("input:checkbox", "fulltagname", "input:checkbox", "regexp");
    for(int i = 0; i< hecol.Count; i++)
    {
        hecol.Elements[i].Click();
    }