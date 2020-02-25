// Кодировщик из ANSI в UTF-8
// Создаем объекты кодировок
var inAsciiEncoding = System.Text.Encoding.GetEncoding("windows-1251");
var outUTF8Encoding = System.Text.Encoding.UTF8;
// Читаем оригинальный файл по байтам
var inAsciiBytes = System.IO.File.ReadAllBytes(project.Variables["pathToWin1251File"].Value);
// Конвертируем байты в нужную кодировку
var outUTF8Bytes = System.Text.Encoding.Convert(inAsciiEncoding, outUTF8Encoding, inAsciiBytes);
// Записываем переконвертированные байты в файл
using (var stream = new System.IO.FileStream(project.Variables["pathToUTF8File"].Value, System.IO.FileMode.Create))
{
    using (var writer = new System.IO.BinaryWriter(stream, outUTF8Encoding))
    {
        writer.Write(outUTF8Encoding.GetPreamble());
        writer.Write(outUTF8Bytes);
    }
}