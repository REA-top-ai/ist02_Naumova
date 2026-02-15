correct_answer=(1,2,3,2,1,2,1,3,1,2,1,2,3,3,2,1,2,1,2,1)
print("Ведите 20 чисел через пробел от 1 до 3")
user_input=input().split()
user_answer=[int(x)for x in user_input]
if tuple(user_answer)==correct_answer:
    print("Экзамен сдан")
else:
    print("экзамен не сдан")
