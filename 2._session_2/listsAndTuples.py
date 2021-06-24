# Declartion of a list
mylist = ['Apple', 'Banana', 'Cherry']

# ---------------------List Characteristics ----------------------------
# Ordered list, all elements will remain at the same spots
# Changeable, items within the list can be added, removed or changed
# Duplicates, multiple of the same value in a list is allowed
# Any data type, everything within the list can be of any data type
# -----------------------------------------------------------------------



# Declartion of a tuple
mytuple = ('Apple', 'Banana', 'Cherry')

# ---------------------Tuple Characteristics ----------------------------
# Ordered list, all elements will remain at the same spots
# Immutable, items within the tuple cant be added, removed or changed
# Duplicates, multiple of the same value in a tuple is allowed
# Any data type, everything within the tuple can be of any data type
# -----------------------------------------------------------------------



# Looping over lists
# For loop / Foreach loop
print('With a for loop')
for item in mylist:
    print(item)

print('\n')

#While loop
print('With a while loop')
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1