# Создать два произвольных файла. Первому присвоить права на чтение, 
# запись для владельца и группы, только на чтение для всех.  
# Второму присвоить права на чтение, запись только для владельца. 
# Сделать это в численном и символьном виде.

$ touch file1 file2
$ ls -l
итого 0
-rw-r--r-- 1 vs vs 0 янв 25 12:26 file1
-rw-r--r-- 1 vs vs 0 янв 25 12:26 file2

$ chmod -R u=rw,g=rw,o=r file1
$ chmod -R u+rw,g-r,o-r file2
$ ls -l
итого 0
-rw-rw-r-- 1 vs vs 0 янв 25 12:26 file1
-rw------- 1 vs vs 0 янв 25 12:26 file2

$ chmod -R 777 file1
$ chmod -R 777 file2
$ ls -l
итого 0
-rwxrwxrwx 1 vs vs 0 янв 25 12:26 file1
-rwxrwxrwx 1 vs vs 0 янв 25 12:26 file2

$ chmod -R 664 file1
$ chmod -R 600 file2
$ ls -l
итого 0
-rw-rw-r-- 1 vs vs 0 янв 25 12:26 file1
-rw------- 1 vs vs 0 янв 25 12:26 file2