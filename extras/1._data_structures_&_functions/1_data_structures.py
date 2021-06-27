# How to declare a list
my_list = ['apple', 2]
my_second_list = ['Even more lists within my list']

# Adding the values within my_second_list to the already existing my_list list
my_new_list = my_list + my_second_list

# Pushing a list within a list
my_list.append(my_second_list)

print(f'{my_list = }')
print(f'{my_new_list = }')


#--------------------------#

# How to declare a tuple
my_tuple = ('apple', 57)
my_second_tuple = (55, 'Something')

my_new_tuple = my_tuple + my_second_tuple

# This line will result in an error, because lists and tuples cannot be concenated
#my_combined_list_tuple = my_list + my_tuple

print(f'{my_tuple = }')
print(f'{my_new_tuple = }')
#print(f'{my_combined_list_tuple = }')


#--------------------------#

# How to declare a set
# Sets dont allow dupes, so the second occurance of apple will be omitted
my_set = {'apple', 5, 'a car', 'apple'}
print(f'Instantiated: {my_set = }')

my_set.add('A new value')
print(f'Added new value: {my_set = }')
my_set.add(10)
print(f'Added new value: {my_set = }')
my_set.add(5)
print(f'Added value that was omitted: {my_set = }')


#--------------------------#

# How to declare a dict
# Because dict dont allow dupes, age will be assigned to the latest given value, aka age = 25
my_dictionary = {
    'name': 'Andreas',
    'age': 24,
    'age': 25,
    'education': 'IT'
}

print(f'Dict original: {my_dictionary = }')

# Change value in dict
my_dictionary['age'] = 24

# A list of dictionaries
my_list_of_dicts = [
    {
        'name': 'Andreas',
        'age': 25,
        'education': 'IT'
    },
    {
        'name': 'Findus',
        'age': 2,
        'education': 'Cat'
    }
]

print(f'Dict changed: {my_dictionary = }')
print(f'{my_list_of_dicts = }')


