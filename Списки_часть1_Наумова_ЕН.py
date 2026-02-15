# Задание 1. 
cake = ['торт', 1]
print("1. Список с тортом:", cake)

# Задание 2
household_chemicals = [['стиральный порошок', 1],['средство для мытья посуды', 1]]
print("2. Бытовая химия:", household_chemicals)

# Задание 3
Names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']
names_and_dogs_names = zip(Names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

# Задание 4
orders = ['маргаритки', 'васильки']
print("4.1 Исходные заказы:", orders)

orders.append('тюльпаны')
orders.append('розы')
print("4.2 Заказы после добавления:", orders)

# Задание 5
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень', 'ирис']
print("5. Новые заказы:", new_orders)
broken_prices = [5, 3, 4, 5, 4] + [4]  
print("6. Исправленный broken_prices:", broken_prices)

# Задание 6
list1 = range(0, 9)  
print("7. list1 как range(0,9):", list(list1))

# Задание 7
list1 = range(5, 16, 3)  
print("9. list1 с шагом 3 от 5 до 15:", list(list1))
list2 = range(0, 40, 5)  
print("10. list2 с шагом 5 от 0 до 35:", list(list2))

# Задани 8
first_names = ["Эйнсли", "Бен", "Чани", "Депак"]
age = []
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = zip(first_names, all_ages)
ids = range(4)
print("first_names:", first_names)
print("age:", age)
print("all_ages:", all_ages)
print("name_and_age:", list(name_and_age))
print("ids:", list(ids))
