# Задание 1
class Facade:
    pass


# Задание 2
facade_1 = Facade()

# Задание 3
facade_1_type = type(facade_1)
print(facade_1_type)


# Задание 4
class Grade:
    minimum_passing = 65


# Задание 5
class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."


# Задание 6
class Circle:
    pi = 3.14

    def area(self, radius):
        return self.pi * radius ** 2

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        # Задание 9 (стр. 6) - Выводите сообщение при создании круга
        print(f"New circle with diameter: {diameter}")


# Задание 7
teaching_table = Circle(36)

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2
        print(f"New circle with diameter: {diameter}")

    def area(self, radius):
        return self.pi * radius ** 2

    def circumference(self):
        return 2 * self.pi * self.radius


# Задание 8
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)


print(f"Medium pizza circumference: {medium_pizza.circumference()}")
print(f"Teaching table circumference: {teaching_table.circumference()}")
print(f"Round room circumference: {round_room.circumference()}")


print(dir(5))


def this_function_is_an_object():
    pass


print(dir(this_function_is_an_object))


class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2
        print(f"New circle with diameter: {diameter}")

    def area(self, radius):
        return self.pi * radius ** 2

    def circumference(self):
        return 2 * self.pi * self.radius

    def __repr__(self):
        return f"Circle with radius {self.radius}"


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)