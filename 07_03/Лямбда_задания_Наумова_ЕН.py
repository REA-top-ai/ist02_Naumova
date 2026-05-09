contins_a = lambda my_input: 'a' in my_input
print(contins_a(input()))

long_string = lambda my_input: len(my_input)>12
print(long_string(input()))

end_in_a = lambda my_input: my_input[-1] == 'a'
print(end_in_a(input()))

even_or_odd = lambda num: 'четное' if num%2 == 0 else 'нечетное'
print(even_or_odd(int(input())))

multiple_of_three = lambda num: 'кратное трем' if num%3 == 0 else 'не кратное'
print(multiple_of_three(int(input())))

rate_movie = lambda rating: 'Мне понравился этот фильм' if rating > 8.5 else 'Этот фильм был не очень хорошим'
print(rate_movie(float(input())))