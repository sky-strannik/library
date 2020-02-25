// Поиск по списку из переменной
var ListCache = project.Lists["colors"];
string descr = project.Variables["descr"].Value;

lock (SyncObjects.ListSyncer) {
	for (int i=0; i<ListCache.Count; i++) {
		if (descr.Contains(ListCache[i])) return ListCache[i];
	}
}