# How to use built-in .sorted()
import shuffled

my_list = list(shuffled.Shuffled(10))

print(f'Unsorted list: {my_list}')

my_list = sorted(my_list)
print(f'Sorted list: {my_list}')

#Reversing a list
my_list = sorted(my_list, reverse=True)
print(f'Reversed list: {my_list}')

#Custom sort by even
def sort_by_a(x):
    if x % 2 == 0:
        return -1
    return 0

my_list = sorted(my_list, key=sort_by_a)
print(f'My custom sort: {my_list}')