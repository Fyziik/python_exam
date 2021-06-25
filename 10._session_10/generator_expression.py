# Expressions look like list comprehenssions, except with paranthesis instead of square brackets.
# Generator expressions generate one item at a time, where a list comprehension generates an entire list

#list comprehension
my_list = [x for x in [1, 2, 3, 4, 5]]

#Same list as a generator expression
my_gen_expression = (x for x in [1, 2, 3, 4, 5])

print(my_list)
print(my_gen_expression)

print(f'Via next(): {next(my_gen_expression)}')
print(f'Via next(): {next(my_gen_expression)}')

for item in my_gen_expression:
    print(item)