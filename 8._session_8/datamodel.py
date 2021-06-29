# __init__()
# When you initialize an object

from os import device_encoding


class initialize:

    def __init__(self):
        self.x = 5

initialize = initialize()

print(f'{initialize.x = }') #f{var=} string for attribute name and value

class represent:

    def __init__(self):
        self.y = 10

    #repr is used for intern debugging, basically meant for programmers
    def __repr__(self):
        return f'{self.__dict__}'

    #str is meant for outside use, for instance showing for client, for easy understandability
    def __str__(self):
        return f'Y: {self.y}'

represent = represent()

print(represent.__repr__())
print(represent.__str__())

class adding:

    def __init__(self, name):
        self.name = name

    def __add__(self, other_name):
        return adding(f'{self.name} {other_name}')

    def __str__(self):
        return f'Name: {self.name}'

first_person = adding('Andreas')
second_person = adding('Findus')

added = first_person + second_person.name

print(added)

class Card:

    def __init__(self):
        self.cards = ['A', 'K', '4', '7']

    def __getitem__(self, key):
        return self.cards[key]

    def __add__(self, element):
        self.cards.append(element)

    def __str__(self):
        return f'{self.cards}'




deck = Card()
print(deck[2])

deck + 2
print(deck)