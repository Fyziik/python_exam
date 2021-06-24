def sort_cons(x):
    for i in ['a', 'e', 'i', 'o', 'u', 'y', ' ']:
        x = x.lower().replace(i, '')

    return sorted(x)

print(sort_cons('Hello World'))