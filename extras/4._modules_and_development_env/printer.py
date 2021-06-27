def printer(*args, **kwargs):
    people = ''
    for person in args:
        people += f'{person}, '
    print(f'Hello there {people[:-2]}!')



        