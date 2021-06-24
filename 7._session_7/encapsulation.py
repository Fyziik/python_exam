class Person:

    def __init__(self, name, age):
        self.name = name #Public attribute
        self.__age = age #Private attribute

    #A property
    @property
    def name(self):
        return self.__name

    #name makes use of this function when its set, so the value of name is set depending on the length of the name parameter
    @name.setter
    def name(self, name):
        if len(name) > 3:
            self.__name = name
        else:
            self.__name = 'Unnamed'

    def __str__(self) -> str:
        return f'Name: {self.name} \nAge: {self.__age}'


example = Person('Andreas', 25)

print(example)

print(example.name)
#print(example.age) This line wont work beacuse age is private, so we cant directly retrieve the value without a getter

