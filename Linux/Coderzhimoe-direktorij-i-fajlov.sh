# Просмотр содержимого директорий /etc, /home.

$ cd /etc
$ ls -l
итого 1088
drwxr-xr-x  3 root root    4096 авг  5 22:04 acpi
-rw-r--r--  1 root root    3028 авг  5 21:58 adduser.conf
drwxr-xr-x  2 root root    4096 янв 18 22:32 alternatives
...

$ cd /home
$ ls -l
итого 4
drwxr-xr-x 20 vs vs 4096 янв 21 21:56 vs

# Просмотр произвольных файлов в /etc.

$ cd /etc
$ cat apg.conf
#APG_PARM sets the defaults if apg is executed without any command arguments
#
#
#Examples:
#
#Pronounceable passwords with special characters:
#APG_PARM="-c /dev/urandom  -m 8 -x 14  -M SNCL  -t"
#
#Pronounceable passwords without special characters:
#APG_PARM="-c /dev/urandom  -m 8 -x 14  -M NCL  -t"
#
#Random passwords:
#APG_PARM="-c /dev/urandom  -m 20 -x 20  -a 1 -M SNCL"

APG_PARM="-c /dev/urandom  -m 8 -x 14  -M SNCL  -t"