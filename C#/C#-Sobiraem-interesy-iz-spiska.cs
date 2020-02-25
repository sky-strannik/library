// Собираем интересы из списка
var List = project.Lists["cache"];
string akks_type = project.Variables["akks_type"].Value;
string sex = project.Profile.Sex.ToString(); // Преобразуем в строку
var UInterests = project.Variables["UInterests"].Value;
var interes = "";
Random rnd = new Random();
int a = Convert.ToInt32(rnd.Next(3,7));
//If ( UInterests == "" )
	lock (SyncObjects.ListSyncer) {
		for (int i=1; i < a; i++) {
			var M = new Regex(@"^.*м(?==)");
			var J = new Regex(@"^.*ж(?==)");
			var O = new Regex(@"^.*о(?==)");
			var Postfix = new Regex(@".*?=");
			Random S = new Random();
			int b = Convert.ToInt32(S.Next(0,List.Count)); // Случайная строка из списка
			if ( M.IsMatch(List[b]) && sex == "Male" ) interes = Postfix.Replace(List[b],"");
			if ( J.IsMatch(List[b]) && sex == "Female" ) interes = Postfix.Replace(List[b],"");
			if ( O.IsMatch(List[b]) ) interes = Postfix.Replace(List[b],"");
			if ( UInterests != "" && interes != "" ) UInterests = UInterests + ", " + interes;
			if ( UInterests == "" && interes != "" ) UInterests = interes; 
			List.RemoveAt(b); // Удаление строки в списке
			if ( interes == "" ) i--; else interes = "";
		}
	}
return UInterests;



string akks_type = project.Variables["akks_type"].Value;
string sex = project.Profile.Sex.ToString(); // Преобразуем в строку

if ( akks_type == "Все типы" ) return sex;
else {
	if ( akks_type == "Мужчины" &&  sex == "Male" ) return sex; else sex = "NoGender";
	if ( akks_type == "Женщины" &&  sex == "Female" ) return sex; else sex = "NoGender";
	return sex;
}