
# How to make a custom decorator
def my_decorator(func):
    def wrapper_my_decorator(*args, **kwargs):
        print('\n This is before running the func')
        if len(args) == 0:
            result = func(())
        else:
            result = func(args)
        print('And this is after')
        return result
    return wrapper_my_decorator

@my_decorator
def greet(args):
    if len(args) == 0:
        return 'No people to greet'
    elif len(args) == 1:
        return f'Hello {args[0]}'
    else:
        people = ''
        for person in args:
            people += f'{person} '

        return f'Hello {people}'

print(greet())
print(greet('Andreas'))
print(greet('Andreas', 'Findus'))
