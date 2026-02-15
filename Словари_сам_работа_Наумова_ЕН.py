
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 
          4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter: point for letter, point in zip(letters, points)}


letter_to_points[""] = 0

def score_word(word):
    """Подсчитывает количество очков за слово в игре Скрабл"""
    point_total = 0
    for letter in word.upper():  
        point_total += letter_to_points.get(letter, 0) 
    return point_total


print("Тестирование функции score_word:")
print(f"Слово 'BLUE': {score_word('BLUE')} очков")
print(f"Слово 'EARTH': {score_word('EARTH')} очков")
print(f"Слово 'ZAP': {score_word('ZAP')} очков")
print()

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"],"wordNerd": ["EARTH", "EYES", "MACHINE"],"Lexi Con": ["ERASER", "BELLY", "HUSKY"],"Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

print("Текущее положение в игре:")
print("-" * 40)
for player, points in player_to_points.items():
    print(f"{player:12}: {points:3} очков")

print("\nСлова, составленные игроками:")
print("-" * 40)
for player, words in player_to_words.items():
    print(f"{player:12}: {', '.join(words)}")

def update_point_totals(player_to_words, player_to_points):
    """Обновляет очки игроков на основе их слов"""
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

print("\n--- Добавляем слово 'PYTHON' игроку player1 ---")
player_to_words["player1"].append("PYTHON")
update_point_totals(player_to_words, player_to_points)

print("Обновленное положение в игре:")
print("-" * 40)
for player, points in player_to_points.items():
    print(f"{player:12}: {points:3} очков")
