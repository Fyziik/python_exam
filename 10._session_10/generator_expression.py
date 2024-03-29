# Expressions look like list comprehenssions, except with paranthesis instead of square brackets.
# Generator expressions generate one item at a time, where a list comprehension generates an entire list

#list comprehension
my_list = [x for x in [1, 2, 3, 4, 5]]

#Same list as a generator expression
my_gen_expression = (x for x in [1, 2, 3, 4, 5])

for item in my_gen_expression:
    print(f'Via gen exp: {item}')


class my_iterator:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.max:
            self.n += 1
            return self.n - 1
        else:
            raise StopIteration

numbers = my_iterator(5)

i = iter(numbers)

for num in i:
    print(f'Via for loop: {num}')  