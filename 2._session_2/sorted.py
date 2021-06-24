# sorted(list) return an array of the given elements sorted in alphabetical order by default

mylist = ['A', 'H', 'C', 'K', 'M', 'B', 'Y', 'U']

print(f'Unsorted list: {mylist}')
print(f'Sorted list: {sorted(mylist)}')

# sorted has a parameter called reverse, which can be set to true if we wanna reverse the returned array

print(f'Sorted and reversed list: {sorted(mylist, reverse = True)}')

# sorted allows for custom sorting with a third parameter 'key=', which takes in a pre-defined function for sorting

vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']

def sort_by_vowels(x):
    if x in vowels:
        return -1
    return 0
    

print(f'Sorted list via vowels & consonants: {sorted(mylist, key=sort_by_vowels)}')
