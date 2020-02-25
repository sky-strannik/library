# В ОС Linux скрытыми файлами считаются те, имена которых начинаются с символа “.”
# Сколько скрытых файлов в вашем домашнем каталоге? 
# (Использовать конвейер, а для подсчета количества строк использовать wc).

$ pwd
/home/vs
$ ls -ap | grep '^\.' | grep -v '\/$' | wc
     11      11     204