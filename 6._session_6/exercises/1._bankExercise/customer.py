class Customer:

    def __init__(self, *args):

        if len(args) == 1:
            self.name = args[0]
            self.age = None

        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
