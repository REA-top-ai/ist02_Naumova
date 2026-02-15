# Задание 1
print((6 * 6) - 1 == 8 + 1)
print(13 - 7 != (3 * 2) + 1)
print(3 * (2 - 1) == 4 - 1)
# Задание 2
print((6 * 6) - 1 >= 8 + 1)
print(13 - 7 <= (3 * 2) + 1)
print(3 * (2 - 1) > 4 - 1)
# Задание 3
bool_variable = "True"
print(bool_variable)
type(bool_variable)
print(type(bool_variable))
bool_variable_2 = True
type(bool_variable_2)
print(type(bool_variable_2))
# Задание 4
user_name = input("Введите имя")
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
if user_name == "Дмитрий":
    print(Dmitriy_check)
if user_name == "Ангелина":
    print("Добро пожаловать!")
# Задание 5
enter_number = 0
if enter_number < 3:
    print("Попробуйте еще раз. У вас осталось", (3 - enter_number), "попыток")
else:
    print(
        "Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки"
    )
# Задание 6
statement_one = (2 + 2 + 2) >= 6 and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
print(statement_one)
print(statement_two)
# Задание 7
user_name = input("Введите имя: ")
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
Dmitriy_APM = "1"
Angelina_APM = "2"
Vasiliy_APM = "3"
Ekaterina_APM = "4"
ARM = input("Введите номер APM: ")
if ARM == Angelina_APM and user_name == "Ангелина":
    print("Добро пожаловать!")
if ARM == Vasiliy_APM and user_name == "Василий":
    print("Добро пожаловать!")
if ARM == Ekaterina_APM and user_name == "Екатерина":
    print("Добро пожаловать!")
if ARM != Dmitriy_APM and user_name != "Дмитрий":
    print("Логин или пароль не верный, попробуйте еще раз")
if ARM != Angelina_APM and user_name != "Дмитрий":
    print("Логин или пароль не верный, попробуйте еще раз")
if ARM != Vasiliy_APM and user_name != "Дмитрий":
    print("Логин или пароль не верный, попробуйте еще раз")
if ARM != Ekaterina_APM and user_name != "Дмитрий":
    print("Логин или пароль не верный, попробуйте еще раз")
if ARM != Dmitriy_APM and user_name == "Дмитриий":
    print(Dmitriy_check)
if ARM != Angelina_APM and user_name == "Дмитрий":
    print(Dmitriy_check)
if ARM != Vasiliy_APM and user_name == "Дмитрий":
    print(Dmitriy_check)
if ARM != Ekaterina_APM and user_name == "Дмитрий":
    print(Dmitriy_check)

# Задание 8
print((2 - 1 > 3) or (-5 * 2 == -10))
print((9 + 5 <= 15) or (7 != 4 + 3))

# Задание 9
user_name = input("Введите имя: ")
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
Dmitriy_APM = "1"
Angelina_APM = "2"
Vasiliy_APM = "3"
Ekaterina_APM = "4"
ARM = input("Введите номер APM: ")
if ARM == Angelina_APM and user_name == "Ангелина":
    print("Добро пожаловать!")
else:
    print("Логин или пароль не верный, попробуйте еще раз")
if ARM == Vasiliy_APM and user_name == "Василий":
    print("Добро пожаловать!")
else:
    print("Логин или пароль не верный, попробуйте еще раз")
if ARM == Ekaterina_APM and user_name == "Екатерина":
    print("Добро пожаловать!")
else:
    print("Логин или пароль не верный, попробуйте еще раз")
if user_name == "Дмитрий":
    print(Dmitriy_check)

# Задание 10
grade = input("Введите вашу оценку:")
if grade >= "4.0" and grade < "5.0":
    print("Верните оценку A")
elif grade >= "3.0" and grade < "4.0":
    print("Верните оценку B")
elif grade >= "2.0" and grade < "3.0":
    print("Верните оценку C")
elif grade >= "1.0" and grade < "2.0":
    print("Верните оценку D")
elif grade >= "0.0" and grade < "1.0":
    print("Верните оценку F")
