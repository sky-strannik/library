// Звуки
Console.Beep(800, 500); // частота сигнала и длительность, мс
System.Threading.Thread.Sleep(125);

// Проигрывает любой .wav файл
System.Media.SoundPlayer player = new System.Media.SoundPlayer(@"путь к файлу");
player.Play();
 
// Еще вариант
System.Media.SystemSounds.Exclamation.Play();