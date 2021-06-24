mytuple = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]

def last_then_first(x):
    return (x[1], x[0])

print(f'Sorted tuple: { sorted(mytuple, key=last_then_first) }')