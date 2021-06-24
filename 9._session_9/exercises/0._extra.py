from datetime import datetime

def logger(func):
    def wrapper_logger(*args, **kwargs):
        result = func(*args, **kwargs)
        date = timestamp()
        return [result, date]
    return wrapper_logger

def timestamp():
    return datetime.now()

@logger
def add(*args):
    sum = 0
    for i in args:
         sum += i
    return sum

#Logger does work on printer, but messes up the functionality of the logger method itself, or what is expected to be returned, but it would in theory work, yes
@logger
def printer(text):
    return text


result = add(2, 5, 99, 100)
print(printer('Test'))
print(result)



file = open('log.txt', 'w')
file.write(f'Calculated result: {result[0]}   -   Date: {result[1].date()} at {result[1].time()}')