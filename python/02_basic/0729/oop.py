class Person:
    pass

class Professor(Person):
    pass

class Student(Person):
    pass

class No:
    pass

print(issubclass(Student, (Person, No)))