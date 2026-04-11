# def add_data(func):
#     def wrapper():
#         return '<data>'+func()+'</data>'
#     return wrapper
#
# def add_name(func):
#     def wrapper():
#         return '<name>'+func()+'</name>'
#     return wrapper
#
# @add_data
# @add_name
# def app_name():
#     return 'Calc'
#
# print(app_name())
# '<data><name>Calc</name></data>'

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'Trace called for {func.__name__}()'
              f'with {args}, {kwargs}')
        original = func(*args, **kwargs)
        modified = original.upper()
        print(f'returned {modified}')
        return modified
    return wrapper

@trace
def say_greet(name, greeting='hello'):
    print(f' {name}, {greeting}')

print(say_greet('Jane'))






