'''
Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса 
Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов метод должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод 
для каждого экземпляра. 
'''
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')
        print(self.title)

class Pen(Stationery):
    def draw(self):
        print(f'{self.title} пишет')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} рисует')

class Handle(Stationery):
    def draw(self):
        print(f'{self.title} выделяет')

s = Stationery('Канцелярская принадлежность')
s.draw()

p = Pen('Ручка')
p.draw()

pl = Pencil('Карандаш')
pl.draw()

h = Handle('Маркер')
h.draw()


# Вариант решения
class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}))")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start drawing with {self.title} pen!")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start drawing with {self.title} pencil!")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start drawing with {self.title} handle!")

stat = Stationery()
stat.draw()
pen = Pen("Parker")
pen.draw()
pencil = Pencil("Faber-Castell")
pencil.draw()
handle = Handle("COPIC")
handle.draw()