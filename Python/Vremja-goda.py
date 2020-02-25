'''
Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict. 
'''
seasons_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                "November", "December"]
season = int(input("Enter the month number - "))

for i in range(len(seasons_list)):
    if season == i + 1:
        if 3 <= season <= 5:
            print(f"This is Spring, month - {seasons_list[i]}")
        elif 6 <= season <= 8:
            print(f"This is Summer, month - {seasons_list[i]}")
        elif 9 <= season <= 11:
            print(f"This is Autumn, month - {seasons_list[i]}")
        else:
            print(f"This is Winter, month - {seasons_list[i]}")

# вариант решения

seasons_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                9: "September", 10: "October", 11: "November", 12: "December"}
season = int(input("Enter the month number - "))

for i in range(len(seasons_dict)):
    if season == i + 1:
        if 3 <= season <= 5:
            print(f"This is Spring, month - {seasons_dict.get(i + 1)}")
        elif 6 <= season <= 8:
            print(f"This is Summer, month - {seasons_dict.get(i + 1)}")
        elif 9 <= season <= 11:
            print(f"This is Autumn, month - {seasons_dict.get(i + 1)}")
        else:
            print(f"This is Winter, month - {seasons_dict.get(i + 1)}")

# вариант решения

# variant with dictionary
print("Variant with dictionary")
seasons = ["winter", "winter", "spring", "spring", "spring", "summer",
           "summer", "summer", "autumn", "autumn", "autumn", "winter"]
list_12 = (x for x in range(1, 13))
months = dict(zip(list_12, seasons))
user_month_number = input("Please enter a month's number:\n")
try:
    user_season = months.get(int(user_month_number))
except ValueError:
    print("you entered not a digit!")
    user_season = None
if user_season:
    print(f"It's {user_season}")
else:
    print("This month doesn't exist!")

# variant with list
print("Variant with list")
try:
    if int(user_month_number) < 1:
        print("This month doesn't exist!")
        exit(0)
    try:
        print(f"It's {seasons[int(user_month_number) - 1]}")
    except IndexError:
        print("This month doesn't exist!")
except ValueError:
    print("you entered not a digit!")