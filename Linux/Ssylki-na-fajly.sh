# Создать файл file1 и наполнить его произвольным содержимым. 
# Скопировать его в file2. Создать символическую ссылку file3 на file1. 
# Создать жесткую ссылку file4 на file1. Посмотреть, какие айноды у файлов. 
# Удалить file1. Что стало с остальными созданными файлами? 
# Попробовать вывести их на экран.

$ cat > file1
Hello world!
$ cat file1
Hello world!

$ cp file1 file2
$ ls
file1  file2
$ cat file2
Hello world!
$ ls -ail
итого 16
1051232 drwxr-xr-x  2 vs vs 4096 янв 25 11:53 .
1050032 drwxr-xr-x 20 vs vs 4096 янв 25 11:26 ..
1050187 -rw-r--r--  1 vs vs   13 янв 25 11:52 file1
1050478 -rw-r--r--  1 vs vs   13 янв 25 11:53 file2

$ ln file1 file3
$ ls -ail
итого 20
1051232 drwxr-xr-x  2 vs vs 4096 янв 25 12:01 .
1050032 drwxr-xr-x 20 vs vs 4096 янв 25 11:26 ..
1050187 -rw-r--r--  2 vs vs   13 янв 25 11:52 file1
1050478 -rw-r--r--  1 vs vs   13 янв 25 11:53 file2
1050187 -rw-r--r--  2 vs vs   13 янв 25 11:52 file3

$ ln -s file1 file4
$ ls -ail
итого 20
1051232 drwxr-xr-x  2 vs vs 4096 янв 25 12:05 .
1050032 drwxr-xr-x 20 vs vs 4096 янв 25 11:26 ..
1050187 -rw-r--r--  2 vs vs   13 янв 25 11:52 file1
1050478 -rw-r--r--  1 vs vs   13 янв 25 11:53 file2
1050187 -rw-r--r--  2 vs vs   13 янв 25 11:52 file3
1051136 lrwxrwxrwx  1 vs vs    5 янв 25 12:05 file4 -> file1

$ rm -f file1
$ cat file2 file3 file4
Hello world!
Hello world!
cat: file4: Нет такого файла или каталога

# Жесткие ссылки по-прежнему сохраняют доступ к файлу, 
# а символьная ссылка file4 работать перестала.