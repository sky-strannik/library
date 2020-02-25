var ListCache = project.Lists["delete"];
string result = project.Variables["descr"].Value.Trim();

// Удаляем данные из переменной по списку
for (int i=0; i<ListCache.Count; i++) {
	result = Macros.TextProcessing.Replace(result, ListPhones[i], "", "Regex", "All");
}