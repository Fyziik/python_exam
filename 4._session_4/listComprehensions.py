# Regular list comprehension
# [ (valid item) for (item) in (data structure) ]

regular_comprehension = [ x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
print(regular_comprehension)


# List comprehension with if statement
# [ (valid item) for (item) in (data structure) if (condition) ]

if_comprehension = [ x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x % 2 == 0 ] #Here only elements that are even will be returned
print(if_comprehension)


# List comprehension with if else statement
# [ (valid item) if (condition) else (statement) for (item) in (data structure) ]

if_else_comprehension = [ x if x % 2 == 0 else 'Not an even number' for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] ] #Here we return equal numbers, else we return a string with 'not an even number'
print(if_else_comprehension)