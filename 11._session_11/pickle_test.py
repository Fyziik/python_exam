# When “pickel-ing” you convert a python object into bytecode and then you can save that to a file etc.
import pickle as p

my_list = ['Andreas', 'Findus', 'Ida', 'Anden person']

# Pickle Dump
with open('testfiles/pickle.json', 'wb') as f:
    p.dump(my_list, f)

# Pickle Load
with open('testfiles/pickle.json', 'rb') as f:
    print(f'Converted bytecode: {p.load(f)}')

