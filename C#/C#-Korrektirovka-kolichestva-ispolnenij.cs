// Корректировка количества исполнений
var id = Guid.Parse(project.TaskId);

// Корректируем по таблице:
var sourceTable = project.Tables["base"];
int cnt = sourceTable.RowCount;
if ( cnt > 1 ) { ZennoPoster.SetTries(id, cnt+20); }
if ( cnt == 0 ) { ZennoPoster.SetTries(id, cnt+1); }

// или:

// Корректируем по списку:
var sourceList = project.Lists["pages"];
int cnt = sourceList.Count;
if ( cnt > 1 ) { ZennoPoster.SetTries(id, cnt+10); }
if ( cnt == 0 ) { ZennoPoster.SetTries(id, cnt+1); }