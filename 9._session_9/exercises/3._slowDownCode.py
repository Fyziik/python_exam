import time 

def slowdown(func):
    def wrapper(n):
        time.sleep(1)
        return func(n) 
    return wrapper



@slowdown
def countdown(n):
    if not n:   # 0 is false, not false is true
        print('Liftoff!')
    else:
        print(n)
        return countdown(n-1) # call the same function with n as one less 


countdown(5)