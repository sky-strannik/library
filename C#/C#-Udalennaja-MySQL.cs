// C# Удаленная MySQL

// результат выполнения
string result = String.Empty;
 
// команда для MySql
var command = new MySql.Data.MySqlClient.MySqlCommand();
// строка подключения
string connectionString = "Data source=localhost;UserId=user;Password=qwerty;database=MyDatabaseName;";
// текст команды (Ну то есть забрать всё из Data)
command.CommandText = "SELECT * FROM Data;";
 
// пытаемся подключиться
try
{
    // создаём подключение
    command.Connection = new MySql.Data.MySqlClient.MySqlConnection(connectionString);
}
catch(Exception e)
{
    // не получилось
    result = "MySql connect failed";
}
// подключение не возможно -> выходим
 if (result != String.Empty) return result;
 
// ловим исключение
try
{
    // откроем соединение
    command.Connection.Open();
    // выполним команду
    var reader = command.ExecuteReader();
    // запишим данные сюда
    StringBuilder sb = new StringBuilder();
    int i = 0;
    // до тех пор пока есть что читать
    while (reader.Read())
    {
        i++;
        // пусть в таблице 3 записи id|firstname|lastname
        sb.AppendLine(String.Format("№{0}: id = {1} | first name = {2} | last name = {3}", i,
                                    reader["id"], reader["firstname"], reader["lastname"]));
    }
    // это и вернём
    result = sb.ToString();
    // закроем
    reader.Close();
}
catch (MySql.Data.MySqlClient.MySqlException e)
{
    // словили
    result = String.Format("MySql reader exception: {0}", e.Message);
}
finally
{
    // что бы не произошло закроем соединение
    command.Connection.Close();
}
 
// вернём результат
return result;