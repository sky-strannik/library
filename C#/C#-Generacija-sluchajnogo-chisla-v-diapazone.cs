// Генерация случайного числа в диапазоне
Random rnd=new Random();
int a = Convert.ToInt32(rnd.Next(10));
// или
return rnd.Next(10); // от 1 до 10
return rnd.Next(5,10); // от 5 до 10