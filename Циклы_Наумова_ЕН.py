# Задание 1
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
    print(game) 

print("\n--- Спортивные игры ---")
for sport in sport_games:
    print(sport)

# Задание 2
promise = "I will not chew gum in class"
for i in range(5):
    print(promise)
print("\nС номерами итераций:")

# Задание 3
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    students_period_B.append(student)  
    print(f"Добавлен {student}")

print("Итоговый students_period_B:", students_period_B)

# Задание 4

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'poodle' 
print("Породы собак, доступные для усыновления:")
for breed in dog_breeds_available_for_adoption:
    print(breed)
    if breed == dog_breed_I_want:
        print("У них есть собака, которую я хочу!")
        break
if dog_breed_I_want not in dog_breeds_available_for_adoption:
    print(f"\nК сожалению, {dog_breed_I_want} нет в списке доступных пород.")

# Задание 5
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location_sales in sales_data:
    for scoops in location_sales:
        scoops_sold += scoops
print("Общее количество проданных сортов мороженого:", scoops_sold)
print("\nДетализация продаж:")
for i, location_sales in enumerate(sales_data, 1):
    location_total = sum(location_sales)
    print(f"Магазин {i}: {location_total} сортов")

# Задание 6
single_digits = list(range(10))
print("Цифры от 0 до 9:")
for digit in single_digits:
    print(digit)
squares = []
for digit in single_digits:
    squares.append(digit ** 2)
print("\nКвадраты чисел:")
print(squares)
cubes = [digit ** 3 for digit in single_digits]
print("\nКубы чисел:")
print(cubes)
print("\nТаблица чисел:")
print("Число | Квадрат | Куб")
print("-" * 25)
for i in range(10):
    print(f"{i:5} | {i**2:7} | {i**3:3}")
