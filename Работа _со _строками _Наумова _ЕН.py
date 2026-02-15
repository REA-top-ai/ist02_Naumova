# Задание 1
favour_word = "Хайп"
print(favour_word)

# Задание 2
first_name = "Виталий"
last_name = "Красилов"
new_account = last_name[:5]
temp_password = last_name[2:6]
print("Имя пользоватьеля:", new_account)
print("Пароль:", temp_password)

# Задание 3
first_name = "Виталий"
last_name = "Красилов"
account_generator = first_name[:3] + last_name[:3]
new_account = account_generator
print(new_account)

# Задание 4
first_name="Виталий"
last_name="Красилов"
length_1=len(first_name)
length_2=len(last_name)
password_generator=first_name[length_1-3:]+last_name[length_2-3:]
temp_password=password_generator
print(temp_password)

# Задание 5
company_motto="Мечты сбываются"
second_to_last=company_motto[-2]
final_word=company_motto[-4:]
print(second_to_last)
print(final_word)

# Задание 6
first_name="об"
# first_name[0]="Р"
letter="Р"
fixed_first_name=letter+first_name
print(fixed_first_name)

# Задание 7
# wrong_password="theycallme"crazy"91"
right_password="theycallme\"crazy\"91"
print(right_password)

# Задание 8
poem_title="spring storm"
poem_author="William Carlos Williams"
poem_title_fixed=poem_title.title()
print(poem_title)
print(poem_title_fixed)
