# Python supports the usage of logical conditions from mathematics
# Equals: a == b
# Not Equals: a != b
# Less Then: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = input('Insert first number to compare to: ')
b = input('Insert second number to compare to: ')


def checkFormat(num_1, num_2):
    return num_1.isdigit() and num_2.isdigit()

def calculate(num_1, num_2):
    if num_1 > num_2 and correctFormat:
        return f'{num_1} is greater than {num_2}'

    elif num_1 == num_2 and correctFormat:
        return f'{num_1} is equal to {num_2}'

    elif num_1 < num_2 and correctFormat:
        return f'{num_1} is smaller than {num_2}'

    else:
        return f'Something went wrong'


correctFormat = checkFormat(a, b)

print(calculate(a, b))