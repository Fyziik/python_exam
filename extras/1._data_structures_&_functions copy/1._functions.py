# Functions

# How to define a function
def my_function():
    # The body of the function
    print('I am the function!')
    
my_function()

# How to return a value via a function
def my_return_function():
    return 'I am the return value'

print(my_return_function())

# How to pass an arguement as a parameter to a function
def my_parameterized_function(name):
    return f'Hello there {name}'

print(my_parameterized_function('Andreas'))

# How to allow an undefined amount of parameters for a function
def my_args_function(*args, **kwargs):
    print(args)
    print(args[0])
    print(kwargs)
    print(kwargs['key'])

my_args_function(['list', 'values'], 5, 'Hi!', key = 'value', anotherKey = 'Another Value')


# Inner functions
def my_outer_function(*args):
    if not args:
        return 'No name given'
    return my_inner_function(args[0], args[1])

def my_inner_function(text_1, text_2):
    return f'Your first name is {text_1}, and I bet your last name is {text_2}'

print(my_outer_function())
print(my_outer_function('Andreas', 'Laursen'))