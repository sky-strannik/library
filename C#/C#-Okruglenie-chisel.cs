// https://zennolab.com/discussion/threads/okruglenie-v-bolshuju-storonu-c.34754/
// Округление чисел
var a = project.Variables["price"].Value;
decimal b = Math.Floor(decimal.Parse(a, System.Globalization.CultureInfo.InvariantCulture));
decimal result = Math.Ceiling(b/10);	// Делим на 10 и округляем до целого числа
//decimal result = Math.Floor(b/10+1);	// Округление в меньшую сторону: +1 или +0.5
//decimal result = Math.Round(b/10+1); 	// Округление в большую сторону: +1 или +0.5
result=result*10; // Умножаем на 10 или 5 соответственно
return result;