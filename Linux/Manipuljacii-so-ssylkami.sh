# Дать созданным файлам другие, произвольные имена. 
# Создать новую символическую ссылку. Переместить ссылки в другую директорию.

$ rm -f file4
$ mv -f file2 test2
$ mv -f file3 test3
$ ls
test2  test3

$ ln -s test2 tt2
$ ln -s test3 tt3
$ ls -lia
итого 16
1051232 drwxr-xr-x  2 vs vs 4096 янв 25 12:20 .
1050032 drwxr-xr-x 20 vs vs 4096 янв 25 11:26 ..
1050478 -rw-r--r--  1 vs vs   13 янв 25 11:53 test2
1050187 -rw-r--r--  1 vs vs   13 янв 25 11:52 test3
1051117 lrwxrwxrwx  1 vs vs    5 янв 25 12:19 tt2 -> test2
1051136 lrwxrwxrwx  1 vs vs    5 янв 25 12:20 tt3 -> test3

$ mkdir tt
$ ls
test2  test3  tt  tt2  tt3
$ mv tt2 /home/vs/test/tt
$ mv tt3 /home/vs/test/tt
$ ls
test2  test3  tt
$ cd tt
$ ls
tt2  tt3