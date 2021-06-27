# Making a list of all uppercase letters in the alphabeat
my_alphabeat_list = []

for i in range(65, 91):
    my_alphabeat_list.append(chr(i))

print(f'List via for loop: {my_alphabeat_list}')


# How to declare a list comprehension
my_list_comprehension = [ chr(x) for x in range(65, 91)]
print(f'List via list comprehension: {my_list_comprehension}')

# As a oneliner
print(f'Oneliner: {[chr(x) for x in range(65, 91)]}')




# If condition with list comprehensions
my_even_list = [x for x in range(10) if x % 2 == 0]

# Multiple if statements
my_even_list_above_5 = [x for x in range(10) if x % 2 == 0 if x > 5]

#If else conditions with list comprehensions
my_result = [ f'{i} is even' if i % 2 == 0 else f'{i} is odd' for i in range(10)]

print(f'{my_even_list = }')
print(f'{my_even_list_above_5 = }')
print(f'{my_result = }')

