# Strings in Python are considered arrays of chars, therefore we can get the char of a string via indexing

word = "ThisIsATesString"
tenth_letter = word[9]
fifth_letter = word[4]
last_letter = word[-1]

print(f'{tenth_letter = }')
print(f'{fifth_letter = }')
print(f'{last_letter = }')

# Not only can we get specific letters of a string, we can also get substrings of the string via index slicing
# [ start : finish ]

fifth_to_eleventh = word[4 : 10]
sevent_to_last = word[6 : -1]

print(f'{fifth_to_eleventh = }')
print(f'{sevent_to_last = }')



# And index slicing also allows a third parameter, this is the "step" parameter, basically meaning how many indexes to skip
# [ start : finish : step ]

every_second_letter = word[::2]
every_second_letter_2nd_letter_start = word[1::2]
reverse_word = word[::-1]

print(f'{every_second_letter = }')
print(f'{every_second_letter_2nd_letter_start = }')
print(f'{reverse_word = }')