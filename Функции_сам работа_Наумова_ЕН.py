#задача 1
def f_to_c(f_temp):
    c_temp=(f_temp -32)*5/9
    return f_to_c
print(f_to_c(100))
def c_to_f(c_temp):
    f_temp=c_temp*(9/5)+32
    return c_to_f
print(c_to_f(0))
#задача 2
train_mass=22680
train_acceleration=10
train_distance=100
def get_force(mass,acceleration):
    return mass*acceleration
    train_forse=get_force(train_mass,train_acceleration)
    print(f"поезд GE поставляет {train_forse} ньютовы силы")
def get_energy(mass, c=3*10**8):
    return mass*c**2
bomb_mass=1
bomb_energy=get_energy(bomb_mass)
print(f"1 кг бомбы составляет {bomb_energy} джоулей")
def get_work(mass,acceleration,distance):
    force=get_force(mass,acceleration)
    return mass*distance
train_work=get_work(train_mass,train_acceleration,train_distance)
print(f"Поезд выполняет {train_work} Джоулей за {train_distance} метров")
#Задание 3
clothes="домашняя одежда"
meal="каша"
def print_clothes_shedyle(clothes_item):
    print("у меня большой гардероб")
    print(f"Утром лучше всего подходит {clothes_item}")
    print(f"Для завтрака лучше всего подходит {clothes_item}")
    print(f"для обеда лучше всего подходит {clothes_item}")
    print(f"Для ужина лучше всего подходит {clothes_item}")
def print_meal_shedyle(meal_item):
    print("Мщи предпочтения в еде")
    print(f"Утром лучше всего подходит {meal_item}")
    print(f"Для завтрака лучше всего подходит {meal_item}")
    print(f"для обеда лучше всего подходит {meal_item}")
    print(f"Для ужина лучше всего подходит {meal_item}")
print_clothes_shedyle(clothes)
print_meal_shedyle(meal)
#Задание 4
user_name = input("Введите имя пользователя: ")
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
welcome_message = "Добро пожаловать"
if user_name == "Дмитрий":
    print(Dmitriy_check)
else:
    print(welcome_message)
employees = {"Дмитрий": 1,"Ангелина": 2,"Василий": 3,"Екатерина": 4}
user_name = input("Введите имя пользователя: ")
ARM = int(input("Введите номер АРМ: "))
if user_name in employees and employees[user_name] == ARM:
    print("Добро пожаловать!")
elif user_name == "Дмитрий" and ARM != employees["Дмитрий"]:
    print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
else:
    print("Логин или пароль не верный, попробуйте еще раз.")

#Задание 5
grade = float(input("Введите средний балл: "))
if grade >= 4.0:
    print("A")
elif grade >= 3.0:
    print("B")
elif grade >= 2.0:
    print("C")
elif grade >= 1.0:
    print("F")
else:
    print("Некорректный ввод")




































