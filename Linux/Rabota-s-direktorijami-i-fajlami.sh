# Создайте несколько файлов. Создайте директорию, переместите файл туда.
# Удалите все созданные в этом и предыдущем задании директории и файлы.

$ ls
111  222  444
$ touch 555 777
$ ls
111  222  444  555  777

$ mkdir /home/vs/test2
$ mv 777 /home/vs/test2
$ cd ~/test2
$ ls
777

$ cd ~
$ ls
	examples.desktop   snap   test   test2   Видео   Документы   Загрузки   
	Изображения   Музыка   Общедоступные  'Рабочий стол'   Шаблоны
$ rm -Rfv test test2
удалён 'test/555'
удалён 'test/222'
удалён 'test/444'
удалён 'test/111'
удален каталог 'test'
удалён 'test2/777'
удален каталог 'test2'
$ ls
	examples.desktop   snap   Видео   Документы   Загрузки   Изображения   
	Музыка   Общедоступные  'Рабочий стол'   Шаблоны