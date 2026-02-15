# Задание 1. 
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors["кладовая"] = 22
print("Обновленный словарь sensors:", sensors)
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
print("Словарь num_cameras:", num_cameras)

# Задание 2
elvish_translations = {"mountain": "orod","bread": "bass","friend": "mellon","horse": "roch"}
print("Переводы с английского на синдарин:")
for english, sindarin in elvish_translations.items():
    print(f"{english} -> {sindarin}")
print(f"\nПеревод слова 'friend': {elvish_translations['friend']}")
print(f"Перевод слова 'mountain': {elvish_translations['mountain']}")

# Задание 3
animals_in_zoo = {}
animals_in_zoo["зебры"] = 8
animals_in_zoo["обезьяны"] = 12
animals_in_zoo["динозавров"] = 0
print(animals_in_zoo)

# Задание 4
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids["theLooper"] = 138475
user_ids["stringQueen"] = 85739
print(user_ids)

# Задание 5
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

# Задание 6
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {drink: caffeine_mg for drink, caffeine_mg in zipped_drinks}
print(drinks_to_caffeine)

# Задание 7
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {song: playcount for song, playcount in zip(songs, playcounts)}
print("После создания:")
print(plays)
plays["Purple Haze"] = 1
plays["Respect"] += 5
print("\nПосле добавления Purple Haze и увеличения Respect:")
print(plays)
library = {"The Best Songs": plays, "Sunday Feelings": {} }
print("\nИтоговый словарь library:")
print(library)

