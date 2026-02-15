# 1. Определение функции с одним аргументом title
def create_spreadsheet(title):
    print("Создание электронной таблицы с именем " + title)

# 2. Вызов функции с значением title «Загрузки»
create_spreadsheet("Загрузки")

# 3. Добавление параметра row_count со значением по умолчанию 1000
# 4. Изменение оператора print для включения row_count
def create_spreadsheet(title, row_count=1000):
    print("Создание электронной таблицы с названием " + title + " with " + str(row_count) + " lines")

# 5. Вызов функции с названием «Приложения» и row_count = 10
create_spreadsheet("Приложения", 10)

# Дополнительный вызов с значением по умолчанию
create_spreadsheet("Документы")  # row_count будет 1000 по умолчанию
