// Поиск и замена в списке
var ListPhones = project.Lists["phones"];
string Format = "0(000)000-00-00";

lock (SyncObjects.ListSyncer) {
	for (int i=0; i<ListPhones.Count; i++) {
		// Определяем "маску" для форматирования телефона:
		var Prefix = new Regex(@"^.*?\(");
		var Postfix = new Regex(@"\).*?$");
		var CodeCity = Prefix.Replace(ListPhones[i],"");
		CodeCity = Postfix.Replace(CodeCity,"");
		int Symbols = CodeCity.Length; // Количество символов
		if ( Symbols > 3 && Symbols < 6 ) {
			if ( Symbols == 4 ) Format = "0(0000)00-00-00";
			if ( Symbols == 5 ) Format = "0(00000)0-00-00";
		}
		// Очищаем телефон и делаем нужные замены:
		var Clear = new Regex(@"\D");
		var Country = new Regex(@"^8");
		ListPhones[i] = Clear.Replace(ListPhones[i],""); // Очистка мусора
		Symbols = ListPhones[i].Length; // Количество символов
		if (Symbols == 11 || Symbols == 10) {
			if ( Country.IsMatch(ListPhones[i]) && Symbols == 11 ) 
				ListPhones[i] = Country.Replace(ListPhones[i],"7");
			if ( Symbols == 10 )
				ListPhones[i] = "7" + ListPhones[i];
			if ( Format != "" ) {
				// Преобразование телефона:
				long NumberPhone = Convert.ToInt64(ListPhones[i]);
				string NewPhone = NumberPhone.ToString(Format);
				ListPhones[i] = "+" + NewPhone;
			}
		} else { ListPhones.RemoveAt(i); i--; }
	}
}

// Вариант 2.
// Поиск и замена в списке
var List = project.Lists["cache"];
var Name = project.Variables["UName"].Value;
var reg = new Regex(@"^"+Name+"(?=($|\r|\n))");
lock (SyncObjects.ListSyncer) {
	for (int i=0; i<List.Count; i++) {
		if ( reg.IsMatch(List[i]) ) project.Variables["UGender"].Value = "Male";
	}
}