class Person:

    def __init__(self, name, age, public = "public"):
        self.public = public #Public attribute
        self.__age = age #Private attribute
        self.__name = name #Private attribute

    #A property
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 3:
            self.__name = name
        else:
            self.__name = 'Unnamed'

    def __str__(self) -> str:
        return f'Name: {self.name} \nAge: {self.__age}'


example = Person('Andreas', 25)

example.name = 'Jesper'

print(example)
print(example.public)
print(example.name)
#print(example.__age) #This line wont work beacuse age is private, so we cant directly retrieve the value without a getter

