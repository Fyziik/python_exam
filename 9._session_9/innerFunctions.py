# In python we dont have to return a specific value for a function, we can also have a function return a function

def calculate(a, b, method):
    
    if method == 1:
        def add(a, b):
           return int(a) + int(b)

        return add(a, b) 

    elif method == 2:
        def subtract(a, b):
            return int(a) - int(b)

        return subtract(a, b)


a = input('First number: ')
b = input('Second number: ')
toDo = input('1. to add, 2. to subtract: ')

result = calculate(a, b, int(toDo))
print(result)