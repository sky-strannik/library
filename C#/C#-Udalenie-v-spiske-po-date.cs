// Удаление в списке по дате
var sourceList = project.Lists["cache2"];
int timeParsing = System.Convert.ToInt32(project.Variables["unixParsing"].Value);
var text = ""; int timeDate = 0;

// Регулярное выражение для поиска нужного значения. Двойные кавычки комментим двойными кавычками!
Regex parserRegex = new Regex(@"(?<=""date"":).*?(?=,)");

lock(SyncObjects.ListSyncer) {
    for(int i=0; i < sourceList.Count; i++) {
		if (parserRegex.IsMatch(sourceList[i])) {
			Match match = parserRegex.Match(sourceList[i]);
			text = Convert.ToString(match); // Конвертим найденный результат в строку
			timeDate = Convert.ToInt32(text); // Конвертим найденный результат в число
			if (timeDate < timeParsing) {
			sourceList.RemoveAt(i); i--;
			}
		}
    }
}