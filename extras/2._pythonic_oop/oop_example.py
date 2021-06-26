class Person:
    
    def __init__(self, social_number, name, age, height):
        self.social_number = social_number
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'Social Number: {self.social_number} \nName: {self.name} \nAge: {self.age} \nHeight: {self.height} \n'

    def get_name(self) -> str:
        return self.name

class School:

    def __init__(self, subjects):
        self.subjects = subjects

#This Student class inherits from the Person class and the School class
class Student(Person, School):

    def __init__(self, person, school, graduation_year):
        super().__init__(person.social_number, person.name, person.age, person.height)
        self.graduation_year = graduation_year
        self.subjects = school.subjects

    def __str__(self):
        return f'Social Number: {self.social_number} \nName: {self.name} \nAge: {self.age} \nHeight: {self.height} \nSubjects at school: {self.subjects} \nGrad year: {self.graduation_year} \n'


person = Person('1111', 'Andreas', 25, 174)
school = School(['AP Science', 'Mathematics', 'English'])
student = Student(person, school, 2020)


print(person)
print(student)

print(f'Student name: {student.get_name()}')