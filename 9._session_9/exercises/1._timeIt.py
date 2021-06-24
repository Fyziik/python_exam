import time, random

def timer(func):
    def wrapper_timer(*args, **kwargs):
        start = time.time()
        to_return = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return to_return
    return wrapper_timer

@timer
def sorter(x):
    time.sleep(0.5)
    return sorted(x)

@timer
def random_shuffle(x):
    time.sleep(1)
    return random.sample(x, len(x))


mylist = [chr(x) for x in range(65, 91)]

print(mylist)
print(random_shuffle(mylist))
print(sorter(mylist))