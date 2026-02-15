#Задание 1
import random

name = input("Как вас зовут?")
question = input("Какой у вас вопрос?")
answer = ""
random_number = random.randint(1, 12)
# print(random_number)
if random_number == 1:
    answer = "Да, безусловно"
elif random_number == 2:
    answer = "Совершенно верно"
elif random_number == 3:
    answer = "Без сомнения"
elif random_number == 4:
    answer = "Ответ туманный, попробуйте еще раз"
elif random_number == 5:
    answer = "Спросите еще раз позже"
elif random_number == 6:
    answer = "Лучше не говорить вам сейчас"
elif random_number == 7:
    answer = 'Мои источники говорят "нет" '
elif random_number == 8:
    answer = "Прогноз не очень хороший"
elif random_number == 9:
    answer = "Очень сомнительно"
elif random_number==10:
    answer="Точно нет"
elif random_number==11:
    answer="Возможно частично"
elif random_number==12:
    answer="Все в ваших руках"
else:
    answer = "Ошибка"
if name=="":
    print("Вопрос:",question)
    print("Магический шар отвечает:",answer)
else:
    print(name,"спрашивает:",question)
    print("Магический шар отвечает:",answer)
    
# Задание 2
import random

max_number=random.randint(10,15)
average_number=random.randint(5,10)
standart_number=random.randint(1,15)
min_number=random.randint(1,5)
if min_number>=max_number or min_number>=average_number or average_number>=max_number:
    print("Данные неверны")
elif (standart_number>=3 and max_number-standart_number>average_number) or(standart_number>=3 and average_number-standart_number>min_number):
    print("В ваших данных имеются выбросы и требуют предобработки")
elif (standart_number>=5 and max_number-standart_number>average_number) or (standart_number>=5 and average_number-standart_number>min_number):
    print("В ваших данных имеются экстремальные значения и требуют предобработки")
elif (standart_number<=3 and max_number-standart_number>average_number) or (standart_number<=3 and average_number-standart_number>min_number):
    print("Ваши данные пригодны для анализа")
    
# Задание 3
age_of_user = input("Введите ваш возраст:")
age_limit = "13"
if age_of_user < age_limit:
    print("Приятного просмтора!")
else:
    print("Извините, ваш возраст не соответствует введенным возрастным ограничениям")
    
# Задание 4
import random

car_brand=random.randint(1,2)
driver_age=random.randint(20,34)
driver_experience=random.randint(2,15)
driver_reputation=random.randint(1,5)
road_traffic=random.randint(1,7)
travel_time=random.randint(1,120) # Время в минутах
rate_per_minute=0
if car_brand==1 and 27>=driver_age>=20 and 9>=driver_experience>=2 and 2>=driver_reputation>=1 and 3>=road_traffic>=1:
    rate_per_minute=8
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==1 and 27>=driver_age>=20 and 9>=driver_experience>=2 and 2>=driver_reputation>=1 and 7>=road_traffic>=4:
    rate_per_minute=8.5
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==1 and 27>=driver_age>=20 and 9>=driver_experience>=2 and 5>=driver_reputation>=3 and 3>=road_traffic>=1:
    rate_per_minute=7.5
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==1 and 27>=driver_age>=20 and 9>=driver_experience>=2 and 5>=driver_reputation>=3 and 7>=road_traffic>=4:
    rate_per_minute=7.4
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==1 and 34>=driver_age>=27 and 9>=driver_experience>=2 and 2>=driver_reputation>=1 and 3>=road_traffic>=1:
    rate_per_minute=7.2
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==1 and 34>=driver_age>=27 and 9>=driver_experience>=2 and 5>=driver_reputation>=3 and 3>=road_traffic>=1:
    rate_per_minute=7
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==1 and 34>=driver_age>=27 and 9>=driver_experience>=2 and 5>=driver_reputation>=3 and 7>=road_traffic>=4:
    rate_per_minute=7.2
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==1 and 34>=driver_age>=27 and 15>=driver_experience>=10 and 2>=driver_reputation>=1 and 3>=road_traffic>=1:
    rate_per_minute=6.9
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==1 and 34>=driver_age>=27 and 15>=driver_experience>=10 and 5>=driver_reputation>=3 and 7>=road_traffic>=4:
    rate_per_minute=6.6
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==1 and 34>=driver_age>=27 and 15>=driver_experience>=10 and 2>=driver_reputation>=1 and 7>=road_traffic>=4:
    rate_per_minute=6.7
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==2 and 27>=driver_age>=20 and 9>=driver_experience>=2 and 2>=driver_reputation>=1 and 3>=road_traffic>=1:
    rate_per_minute=12
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==2 and 27>=driver_age>=20 and 9>=driver_experience>=2 and 2>=driver_reputation>=1 and 7>=road_traffic>=4:
    rate_per_minute=12.5
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==2 and 27>=driver_age>=20 and 9>=driver_experience>=2 and 5>=driver_reputation>=3 and 3>=road_traffic>=1:
    rate_per_minute=11.6
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==2 and 27>=driver_age>=20 and 9>=driver_experience>=2 and 5>=driver_reputation>=3 and 7>=road_traffic>=4:
    rate_per_minute=11.3
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==2 and 34>=driver_age>=27 and 9>=driver_experience>=2 and 2>=driver_reputation>=1 and 3>=road_traffic>=1:
    rate_per_minute=11.4
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==2 and 34>=driver_age>=27 and 9>=driver_experience>=2 and 5>=driver_reputation>=3 and 3>=road_traffic>=1:
    rate_per_minute=11.7
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==2 and 34>=driver_age>=27 and 9>=driver_experience>=2 and 5>=driver_reputation>=3 and 7>=road_traffic>=4:
    rate_per_minute=11.9
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==2 and 34>=driver_age>=27 and 15>=driver_experience>=10 and 2>=driver_reputation>=1 and 3>=road_traffic>=1:
    rate_per_minute=10.8
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==2 and 34>=driver_age>=27 and 15>=driver_experience>=10 and 5>=driver_reputation>=3 and 7>=road_traffic>=4:
    rate_per_minute=10.9
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
elif car_brand==2 and 34>=driver_age>=27 and 15>=driver_experience>=10 and 2>=driver_reputation>=1 and 7>=road_traffic>=4:
    rate_per_minute=11
    print("Стоимость вашей поездки составляет:" ,travel_time*rate_per_minute)
    
# Задание 5
coffe_name = input("Введите название кофе:")
if coffe_name == "Капучино":
    print("Репцепт: 1. Сварите кофе. Можно сварить в турке (доведите до кипения 2-3 раза, чтобы напиток получился насыщеннее). Или заварить во френч-прессе. Обязательно процедите, налейте в подогретую кружку.\
        2. Подогрейте молоко. Старайтесь не перегревать его больше, чем 65 градусов. Оно не должно быть сильно горячим. \
            3. Взбейте с помощью блендера или миксера. Добивайтесь однородной пены, без крупных пузырьков. \
                4. Влейте взбитую массу в кофе." )
elif coffe_name=="Латте":
    print("Рецепт: 1. Кофе следует заварить, причем любым способом, который вам кажется удобнее.\
2. Главное, чтобы кофе был довольно крепким.\
3. Молоко нужно разогреть, но не кипятить: оптимальной будет температура в 50-60 градусов. Читайте ещё: вкусный рецепт приготовления кофе по турецки.\
4. После этого его нужно тщательно взбить с помощью блендера (либомиксера).\
    5. Процедура займет порядка 5 минут, пока не образуется воздушная пена.\
6. Следующий шаг – это переливание молока в заранее подготовленный высокий бокал (лучше всего для этого подходит так называемый айриш -бокал).\
7. Пена в итоге все равно останется сверху.\
8. Затем нужно влить в молоко кофе.\
9. Делать это нужно очень аккуратно, кофе должен литься тоненькой струйкой.\
10. Дело в том, что только таким образом может получиться правильный трехслойный напиток: молоко, кофе и пена сверху.\
11. Завершается приготовление классического латте добавлением корицы либо шоколада сверху.\
12. Впрочем, можно и вовсе не добавлять ничего.")
elif coffe_name==("Фрапучино"):
    print("Рецепт: 1. Варим и охлаждаем кофе. Для его приготовления можно использовать турку, кофемашину и любой другой прибор. Внимание! Для данного рецепта кофе можно заменить зеленым чаем. Объем тот же – 150 мл.\
2. Все компоненты помещаем в стационарный блендер. Ингредиенты взбиваем до тех пор, пока лед не превратиться в мелкую крошку.\
3. Взбиваем сливки. Их предварительно нужно охладить, подержав 1 -2 часа в холодильнике. При этом продукт нельзя замораживать, в противном случае он отслоится, и крем не получится. Сливки взбиваем миксером. Сначала устанавливаем минимальные обороты, постепенно увеличивая их количество. Продукт взбиваем до того момента, пока масса не будет сохранять форму.\
4. Кофе переливаем в бокал. Сверху украшаем сливками. Подаем холодным.")
elif coffe_name==("Эспрессо"):
    print("Рецепт: 1. В чашку с толстыми стенками насыпают растворимый кофе и сахарный песок в тех количествах, которые обычно используются для одной порции.\
2. Далее в чашку добавляют немного кипятка и интенсивно взбивают ложкой полученную смесь.\
3. После некоторого времени масса посветлеет и приобретет консистенцию сметаны.\
4. Во взбитую смесь аккуратно доливают оставшуюся воду, медленно помешивая до образования густой пены")

# Задание 6
import random

column_1 = random.randint(1, 8)
column_2 = random.randint(1, 8)
column_3 = random.randint(1, 8)
column_4 = random.randint(1, 8)
column_5 = random.randint(1, 8)
phrase_1 = "Коллеги,"
phrase_2 = "В то же время,"
phrase_3 = "Однако,"
phrase_4 = "Тем не менее,"
phrase_5 = "Следовательно"
phrase_6 = "Соответственно,"
phrase_7 = "Вместе с тем,"
phrase_8 = "С другой стороны,"
phrase_9 = "парадигма цифровой экономики"
phrase_10 = "контекст цифровой трансформации"
phrase_11 = "диджитализация бизнес-процессов"
phrase_12 = "прагматичный подход к цифровым платформам"
phrase_13 = "совокупность сквозных технологий"
phrase_14 = "программа прорывных исследований"
phrase_15 = "ускорение блокчейн-транзакции"
phrase_16 = "экспоненциальный рост Big Data"
phrase_17 = "открывает новые возможности для"
phrase_18 = "выдвигает новые требования"
phrase_19 = "несет в себе риски"
phrase_20 = "расширяет горизонты"
phrase_21 = "заставляет искать варианты"
phrase_22 = "не оставляет шанса для"
phrase_23 = "повышает вероятность"
phrase_24 = "обостряет проблему"
phrase_25 = "дальнейшего углубления"
phrase_26 = "бюджетного финансирования"
phrase_27 = "синергетического эффекта"
phrase_28 = "компрометации конфиденциальных"
phrase_29 = "универсальной коммодитизации"
phrase_30 = "несанкционированной кастомизации"
phrase_31 = "нормативного регулирования"
phrase_32 = "практического применения"
phrase_33 = "знаний и компетенций."
phrase_34 = "непроверенных гипотез."
phrase_35 = "волатильных активов."
phrase_36 = "опасных экспериментов."
phrase_37 = "государственно-частных партнерств."
phrase_38 = "цифровых следов граждан."
phrase_39 = "нежелательных последствий."
phrase_40 = "внезапных открытий."
if column_1 == 1:
    print(phrase_1)
if column_1 == 2:
    print(phrase_2)
if column_1 == 3:
    print(phrase_3)
if column_1 == 4:
    print(phrase_4)
if column_1 == 5:
    print(phrase_5)
if column_1 == 6:
    print(phrase_6)
if column_1 == 7:
    print(phrase_7)
if column_1 == 8:
    print(phrase_8)
if column_2 == 1:
    print(phrase_9)
if column_2 == 2:
    print(phrase_10)
if column_2 == 3:
    print(phrase_11)
if column_2 == 4:
    print(phrase_12)
if column_2 == 5:
    print(phrase_13)
if column_2 == 6:
    print(phrase_14)
if column_2 == 7:
    print(phrase_15)
if column_2 == 8:
    print(phrase_16)
if column_3 == 1:
    print(phrase_17)
if column_3 == 2:
    print(phrase_18)
if column_3 == 3:
    print(phrase_19)
if column_3 == 4:
    print(phrase_20)
if column_3 == 5:
    print(phrase_21)
if column_3 == 6:
    print(phrase_22)
if column_3 == 7:
    print(phrase_23)
if column_3 == 8:
    print(phrase_24)
if column_4 == 1:
    print(phrase_25)
if column_4 == 2:
    print(phrase_26)
if column_4 == 3:
    print(phrase_27)
if column_4 == 4:
    print(phrase_28)
if column_4 == 5:
    print(phrase_29)
if column_4 == 6:
    print(phrase_30)
if column_4 == 7:
    print(phrase_31)
if column_4 == 8:
    print(phrase_32)
if column_5 == 1:
    print(phrase_33)
if column_5 == 2:
    print(phrase_34)
if column_5 == 3:
    print(phrase_35)
if column_5 == 4:
    print(phrase_36)
if column_5 == 5:
    print(phrase_37)
if column_5 == 6:
    print(phrase_38)
if column_5 == 7:
    print(phrase_39)
if column_5 == 8:
    print(phrase_40)
