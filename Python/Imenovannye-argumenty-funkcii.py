'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
'''
def personal_info(**kwargs):
    return kwargs

print(personal_info(name=input("Enter your name: "), surname=input("Enter your surname: "),
      birthday=input("Enter your birthday: "), city=input("Enter your city: "), email=input("Enter your email: "),
      phone_number=input("Enter your phone number: ")))

# вариант решения

def person_inf(name, surname, birthday, city, email, phone):
    return f"Name - {name}; Surname - {surname}; birthday - {birthday}; city - {city};" \
           f" email - {email}; phone - {phone}"


print(person_inf(name="Alice", surname="Selezneva", birthday="21.09.67", city="Moscow",
                 email="alice.selezneva@mail.ru", phone="143-91-19 "))