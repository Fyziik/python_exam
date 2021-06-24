# Create a “clone” of the build in range() function, by doing an iterator class. 
# Besides implementing the protocol for beeing iterable, this class should also be callable in order for it to be used like this.

class My_iterator:

    def __init__(self, pos_1 = 1, pos_2 = 1, pos_3 = 1):
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.pos_3 = pos_3
        self.first = True


        if pos_1 != 1:
            self.pos_1 = pos_1

        if pos_2 != 1:
            self.pos_2 = pos_2

        if pos_3 != 1:
            self.pos_3 = pos_3

        if pos_2 == 1 and pos_3 == 1:
            self.pos_1 = 1
            self.pos_2 = pos_1


    def __iter__(self):
        self.last = self.pos_1
        return self

    def __next__(self):
        if self.last == self.pos_1 and self.first:
            self.first = False
            return self.pos_1

        self.last += self.pos_3
        if self.last > self.pos_2:
            raise StopIteration()

        return self.last

    def __gen__(self):
        start = self.pos_1
        end = self.pos_2
        toAdd = self.pos_3

        for i in range(end):
            if start > end:
                raise StopIteration()
            yield start
            start += toAdd

        
# Create iterator object
my_iterator = My_iterator(1, 10, 3)

test_iter = iter(my_iterator)

print("Via Iterator: ")
for i in test_iter:
    print(i)

# Now do the same, but use a generator function instead.

test_gen = (i for i in my_iterator.__gen__())

print('\n' + "Via Generator: ")
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))


