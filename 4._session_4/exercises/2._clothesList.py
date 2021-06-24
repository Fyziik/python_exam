colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
sold_out = [('Black', 'm'), ('White', 's')]

paired = [ (color, size) for color in colors for size in sizes ]

print(paired)

paired_2 = [ (color, size) for color in colors for size in sizes if (color, size) not in sold_out]

print(paired_2)
