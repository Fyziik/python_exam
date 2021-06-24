# In python, functions are treated just like ints and lists etc.
# This means that we can use functions as variables, even store them inside lists and such as "values"

def add(a, b):
    return int(a) + int(b)

def subtract(a, b):
    return int(a) - int(b)

a = input('First number: ')
b = input('Second number: ')
toDo = input('1 for add, 2 for subtract: ')

methods = [add(a, b), subtract(a, b)]

result = methods[int(toDo) - 1]

print(result)