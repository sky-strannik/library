# Написать регулярное выражение, которое проверяет, является ли указанный файл
# нужного типа (на выбор .com,.exe или .jpg,.png,.gif и т.д.). 
# Написать регулярное выражение для проверки, ведет ли ссылка URL на некоторый файл, 
# и это действительно ссылка на картинку (например, http://site.com/folder/1.png), 
# а не на любой файл.

# Регулярка:
# (?i)(?<=/)[^/]+\.(jpg|png|gif)(?=($|\r|\n))

# Ищем по списку:
https://i.ytimg.com/vi/lkQ0LDx9jHs/maxresdefault.jpg
https://i.ytimg.com/vi/mK72EwuxZAU/hqdefault.png
https://ru.wikipedia.org/wiki/book.pdf
https://habr.com/ru/post/55766.docx

# Получаем:
maxresdefault.jpg
hqdefault.png