# Based on the Student class below, create a PythonStudents class that acts as a collection of students. 
# The class should implement the iterations functionality (iter() and next()) and be able to return an iter object.
# When iterated the Pythod_students object should return the name of each student in the list.

class PythonStudents:

    def __init__(self):
        student1 = Student("Test1", 11111)
        student2 = Student("Test2", 22222)
        student3 = Student("Test3", 33333)
        student4 = Student("Test4", 44444)
        student5 = Student("Test5", 55555)
        student6 = Student("Test6", 66666)
        self.students = []
        self.students.append(student1)
        self.students.append(student2)
        self.students.append(student3)
        self.students.append(student4)
        self.students.append(student5)
        self.students.append(student6)
    
    def __iter__(self):
        self.last = 0
        return self
    
    def __next__(self):
        if self.last > len(self.students) - 1:
            raise StopIteration()

        student = self.students[self.last]
        self.last += 1
        return student


class Student:

    def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

    @property
    def name(self):
            return self.__name

    @name.setter
    def name(self, name):
            self.__name = name.capitalize()

    def __add__(self, student):
            return Student('Anna the daugther', 1234)

    def __str__(self):
            return f'{self.name}, {self.cpr}'

    def __repr__(self):
            return f'{self.__dict__}'


python_students = PythonStudents()

psi = iter(python_students)

for i in psi:
    print(i)

psi_list_expression = [i for i in python_students]

print(psi_list_expression)