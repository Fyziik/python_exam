#Decorators makes it possible to make powerful functions in Python, by making wrappers for these decorators, we can transform the way functions operate in runtime

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        uppercase(func(*args, **kwargs))
        uppercase(func(*args, **kwargs))
    return wrapper_do_twice

@do_twice
def greet(*args, **kwargs):
    return f'Hello {args}!'

def uppercase(text):
    print(text.upper())


greet('Andreas', 'Emil')

