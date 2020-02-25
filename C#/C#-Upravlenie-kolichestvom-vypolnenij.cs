// Управление количеством выполнений
Добавить 1 выполнение:
var id = Guid.Parse(project.TaskId);
ZennoPoster.AddTries(id, 1);
Обнулить кол-во выполнений:
var id = Guid.Parse(project.TaskId);
ZennoPoster.SetTries(id, 0);
Установить 5 повторений:
var id = Guid.Parse(project.TaskId);
ZennoPoster.SetTries(id, 5);

