class Deck:
    def __init__(self):
        self.__cards = ['A', 'K', 4, 7]


    def __getitem__(self, key):
        return self.__cards[key]

    def __len__(self):
        return len(self.__cards)

    def __add__(self, other):
        return f'{self} + {other}'

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return str(self.__cards)

    def __setitem__(self, key, val):
        self.__cards[key] = val


    def __delitem__(self, key):
        del(self.__cards[key])


"""
   implement the:
    __len__         method
    __add__         method
    __repr__        method
    __str__         method
    __setitem__     method
    __delitem__     method
"""