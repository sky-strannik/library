// Количество файлов в папке
{-Project.Directory-}/{-Variable.folder-}/1
return System.IO.Directory.GetFiles(project.Directory + project.Variables["folder"].Value + "\\1").Length;
