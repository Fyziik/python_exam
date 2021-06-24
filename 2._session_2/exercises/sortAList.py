mylist = ['Claus', 'Ib', 'Per', 'Andreas', 'Ida']

print(sorted(mylist))

print(f'Reversed: {sorted(mylist, reverse=True)}')

print(f'Sorted by length of names: {sorted(mylist, key=len)}')

def sort_by_last_letter(x):
    return x[-1]

print(f'Sorted by last letter in name: {sorted(mylist, key=sort_by_last_letter)}')

def sort_by_first_letter(x):
    if 'a' in x[0].lower():
        return -1
    return 1

print(f'Sorted by first letter: {sorted(mylist, key=sort_by_first_letter)}')
