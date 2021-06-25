#Generator-function
def count(max):
    a = 0
    while a <= max:
        yield a
        a += 1

#Generator-object
counter = count(5)

#Manual looping
print(f'Manual looping count: {counter.__next__()}')
print(f'Manual looping count: {counter.__next__()}')

for i in counter:
    print(f'Remainder via automatic looping: {i}')
