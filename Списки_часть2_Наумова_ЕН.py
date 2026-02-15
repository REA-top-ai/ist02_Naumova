# Задание 1. 
list1 = range(2, 20, 2)
list1_len = len(list1)
print("Длина list1:", list1_len)
print("Элементы list1:", list(list1))
list1 = range(2, 20, 3)
list1_len = len(list1)

print("\nПосле изменения:")
print("Длина list1:", list1_len)
print("Элементы list1:", list(list1))
print("Как это изменит list1_len? - Длина уменьшится с 9 до 6")
# Задание 2
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
print("Длина shopping_list:", len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print("element5:", element5)
print("last_element:", last_element)
print("Равны ли element5 и last_element?", element5 == last_element)

# Задание 3
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase[0:2]
print("beginning:", beginning)
print("Количество элементов в beginning:", len(beginning))
beginning = suitcase[0:4]
print("\nИзмененный beginning (первые 4 элемента):", beginning)
middle = suitcase[2:4]
print("middle (два средних элемента):", middle)
print("\nПолный список чемодана:", suitcase)
print("Количество элементов в чемодане:", len(suitcase))

# Задание 4
suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги']
start = suitcase[0:3]
print("suitcase:", suitcase)
print("start (первые 3 элемента):", start)

# Задание 5
from collections import Counter
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Laurie', 
         'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 
         'Jake', 'Jake', 'Cassie', 'Jake']
vote_count = Counter(votes)
jake_votes = vote_count['Jake']
print("Количество голосов за Jake:", jake_votes)
print("\nВсе результаты голосования:")
for name, count in vote_count.items():
    print(f"{name}: {count} голосов")
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Laurie', 
         'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 
         'Jake', 'Jake', 'Cassie', 'Jake']

jake_votes = votes.count('Jake')
print("Количество голосов за Jake:", jake_votes)

# Задание 6
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', 
             '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
print("Исходный список адресов:")
print(addresses)
print()
addresses.sort()
print("Отсортированный список адресов:")
print(addresses)
addresses_original = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', 
                     '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
sorted_addresses = sorted(addresses_original)

print("\nАльтернативный вариант с sorted():")
print("Исходный (не изменился):", addresses_original)
print("Новый отсортированный список:", sorted_addresses)

# Задани 7
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print("Исходный список games:")
print(games)
print()

print("Отсортированный список games_sorted:")
print(games_sorted)
print("\nПроверка: исходный список остался без изменений:")
print("games:", games)
print("games_sorted:", games_sorted)

# Задание 8
inventory = ['двухспальная кровать', 'двухспальная кровать', 'изголовье', 'двухспальная кровать',
    'двухспальная кровать', 'комод', 'комод', 'стол', 'стол', 'тумбочка', 'тумбочка', 
    'королевская кровать', 'двухспальная кровать', 'две односпальные кровати', 'две односпальные кровати',
    'простыни', 'простыни', 'подушка', 'подушка']
inventory_len = len(inventory)
print("1. Количество товаров на складе:", inventory_len)
first = inventory[0]
print("2. Первый элемент:", first)
last = inventory[-1]
print("3. Последний элемент:", last)
inventory_2_6 = inventory[2:6]
print("4. Предметы с индекса 2 до 6:", inventory_2_6)
first_3 = inventory[:3]
print("5. Первые 3 предмета:", first_3)
twin_beds = inventory.count('две односпальные кровати')
print("6. Количество односпальных кроватей:", twin_beds)
print("\n7. Сортировка инвентаря:")
print("До сортировки:", inventory)
inventory.sort()
print("После сортировки:", inventory)
