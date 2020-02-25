// Сортировка списка по списку
var listA = project.Lists["cache1"]; 	// Исходный список
var listB = project.Lists["cache2"]; 	// Стоп-слова
var Result = project.Lists["Result"]; 	// Результат сортировки

lock (SyncObjects.ListSyncer) {
	for (int i=0; i<listB.Count; i++) {
		var parserRegex = new Regex("(?i)"+listB[i]);
		for (int t=0; t<listA.Count; t++) {
			if (parserRegex.IsMatch(listA[t])) {
				Result.Add(listA[t]);
				listA.RemoveAt(t);
				t--;
			}
		}
	}
}
------------
// Сортировка списка по списку 2
IZennoList for_claster = project.Lists["for_claster"];
IZennoList clastered = project.Lists["clastered"];
IZennoList readyClatered = project.Lists["readyClatered"];
 
foreach (var cl in clastered){
	foreach (var for_cl in for_claster){
		if (for_cl.Contains(cl)){
		readyClatered.Add(for_cl);
		}
	}
}
