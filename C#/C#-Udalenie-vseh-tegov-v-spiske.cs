// Удаление всех тегов в списке
var sourceList = project.Lists["cache2"];
var text = "";

// Регулярное выражение для поиска нужного значения. Двойные кавычки комментим двойными кавычками!
Regex parserRegex = new Regex(@"<[\w\W]*?>");

lock(SyncObjects.ListSyncer) {
    for(int i=0; i < sourceList.Count; i++) {
		for(int t=0; t < 10; t++) {
			if (parserRegex.IsMatch(sourceList[i])) {
			Match match = parserRegex.Match(sourceList[i]);
			text = Convert.ToString(match); // Конвертим найденный результат в строку
			sourceList[i] = sourceList[i].Replace(text,""); // Заменяем
			} else break;
		}
    }
}