// Блокировка для многопотока
lock (SyncObjects.ListSyncer){
    //Добавляем в список "Список 1" элемент со значением "строка"
    project.Lists["Список 1"].Add("строка");
}

//SyncObjects.ListSyncer - для списков
//SyncObjects.TableSyncer - для таблиц
//SyncObjects.InputSyncer - для буфера обмена