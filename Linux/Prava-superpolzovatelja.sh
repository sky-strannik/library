# Создать пользователя, обладающего возможностью выполнять действия
# от имени суперпользователя.

$ sudo useradd -m -G sudo -s /bin/bash username
$ cat /etc/group
…
sudo:x:27:vs,username
…
username:x:1001:

# Пользователь добавлен в группу sudo