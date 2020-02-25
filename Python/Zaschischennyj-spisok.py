'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
name, surname, position (должность), income (доход). Последний атрибут 
должен быть защищенным и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, 
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''
class Worker:
    name = 'Ivan'
    surname = 'Kotov'
    position = 'Programmer'
    _income = {"wage": 50000, "bonus": 20000}

class Position(Worker):
    def get_full_name(self):
        if self.name != '' and self.surname != '':
            return self.name + ' ' + self.surname
        else:
            return 'Укажите Имя и Фамилию'

    def get_total_income(self):
        if self.position != '' and self._income != '':
            s = self._income['wage'] + self._income['bonus']
            return self.position + ' with income ' + str(s)
        else:
            return 'укажите должность, оклад и премию'

p = Position()
print(p.get_full_name(), p.get_total_income())


# Вариант решения
class Worker:
    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": profit, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"

meneger = Position("Dorian", "Grey", "СEO", 500000, 125000)
print(meneger.get_full_name())
print(meneger.position)
print(meneger.get_full_profit())