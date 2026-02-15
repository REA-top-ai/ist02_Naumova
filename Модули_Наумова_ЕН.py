#Задание 1
import datetime
current_time=datetime.datetime.now()
print (current_time)
#Задание 2
import random
random_list=[]
random_list = [random.randint(1, 100) for _ in range(101)]
random_number = random.choice(random_list)
print(f"Длина списка: {len(random_list)}")
print(f"Первые 10 элементов списка: {random_list[:10]}")
print(f"Случайное число из списка: {random_number}")
#Задание 3

#Задание 4
from datetime import datetime, date
employees = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000]]
def programmer_bonus(employee):
    position = employee[1].lower()
    salary = employee[3]
    if "программист" in position:
        bonus = salary * 0.03
        return bonus
    else:
        return 0
def holiday_bonus(employee):
    name = employee[0]
    last_name = name.split()[0]
    
    if last_name.endswith(('а', 'я')):
        return 2000
    else:
        return 2000
def salary_indexation(employee, current_date=date.today()):
    hire_date = datetime.strptime(employee[2], "%d.%m.%Y").date()
    years_worked = (current_date - hire_date).days / 365.25
    salary = employee[3]
    
    if years_worked > 10:
        indexation = salary * 0.07
    else:
        indexation = salary * 0.05
    
    return indexation
def employees_for_vacation(employees, current_date=date.today()):
    vacation_list = []
    for employee in employees:
        hire_date = datetime.strptime(employee[2], "%d.%m.%Y").date()
        months_worked = (current_date - hire_date).days / 30.44  
        
        if months_worked > 6:
            vacation_list.append(employee[0]) 
    
    return vacation_list

print("Расчет премий ко дню программиста:")
for employee in employees:
    bonus = programmer_bonus(employee)
    if bonus > 0:
        print(f"{employee[0]} ({employee[1]}): премия {bonus:.2f} руб.")

print("\nРасчет премий к праздникам (8 марта/23 февраля):")
for employee in employees:
    bonus = holiday_bonus(employee)
    print(f"{employee[0]}: премия {bonus} руб.")

print("\nРасчет индексации зарплаты:")
for employee in employees:
    indexation = salary_indexation(employee)
    new_salary = employee[3] + indexation
    print(f"{employee[0]}: индексация {indexation:.2f} руб., новая зарплата {new_salary:.2f} руб.")

print("\nСотрудники для графика отпусков (отработали > 6 месяцев):")
vacation_employees = employees_for_vacation(employees)
for name in vacation_employees:
    print(name)
#Задание 5
import random

def calculate_digit_sum(number):
    """Вычисляет сумму цифр числа"""
    return sum(int(digit) for digit in str(number))

def lottery_draw():
    admin_number = random.randint(1, 9)
    print(f"Загаданное администрацией число: {admin_number}")
    participants = list(range(1, 101))
    random.shuffle(participants)
    
    winners = []
    
    print("\nПоиск выигрышных номеров...")
    
    for participant in participants:
        digit_sum = calculate_digit_sum(participant)
        if digit_sum % admin_number == 0:
            winners.append(participant)
            print(f"Выигрышный номер: {participant} (сумма цифр: {digit_sum})")
        
            if len(winners) >= 5:
                print(f"\nРозыгрыш завершен! Найдено {len(winners)} победителей.")
                break
    
    if len(winners) < 5:
        print(f"\nРозыгрыш завершен! Найдено всего {len(winners)} победителей.")
    
    return winners
if name == "__main__":
    winners = lottery_draw()
    print(f"\nИтоговый список победителей: {winners}")

#Задание 6    
import random

def coin_toss():
    attempts = int(input("Введите количество бросков монеты: "))
    
    print("\nРезультаты бросков:")
    for i in range(attempts):
        result = random.choice(["Орел", "Решка"])
        print(f"Бросок {i+1}: {result}")
coin_toss()

#Задание 7   
import random

def dice_roll():
    
    attempts = int(input("Введите количество бросков кубика: "))
    
    print("\nРезультаты бросков:")
    for i in range(attempts):
        
        result = random.randint(1, 6)
        print(f"Бросок {i+1}: {result}")
dice_roll()

#Задание 8   
import random

def generate_password():
   
    length = int(input("Введите желаемую длину пароля: "))
    
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    password = ""
    for i in range(length):
        
        password += random.choice(characters)
    
    print(f"\nСгенерированный пароль: {password}")

generate_password()















