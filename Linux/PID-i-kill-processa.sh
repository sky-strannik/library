# Запустить в одном терминале программу, в другом терминале посмотреть PID процесса 
# и остановить с помощью kill, посылая разные типы сигналов. Что происходит?

# Первый терминал:
$ ping ya.ru
# PING ya.ru (87.250.250.242) 56(84) bytes of data.
# 64 bytes from ya.ru (87.250.250.242): icmp_seq=1 ttl=249 time=18.4 ms
# 64 bytes from ya.ru (87.250.250.242): icmp_seq=2 ttl=249 time=21.6 ms
# 64 bytes from ya.ru (87.250.250.242): icmp_seq=3 ttl=249 time=22.0 ms
# …

# Второй терминал:
$ pidof ping
2850
$ kill -s 9 2850

# Первый терминал:
# …
# 64 bytes from ya.ru (87.250.250.242): icmp_seq=76 ttl=249 time=19.1 ms
# 64 bytes from ya.ru (87.250.250.242): icmp_seq=77 ttl=249 time=19.9 ms
# Убито