// Поиск и замена в переменной из списка
var ListCache = project.Lists["colors"];
string descr = project.Variables["descr"].Value;
string result = "";

lock (SyncObjects.ListSyncer) {
	for (int i=0; i<ListCache.Count; i++) {
        result = Macros.TextProcessing.Replace(descr, @"(?i)" + ListCache[i], "", "Regex", "All");
	}
}