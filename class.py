class SchoolMember(object):
    """docstring for SchoolMember."""
    def __init__(self,name,age):
        self.age = age
        self.name = name
        print('Initialized SchoolMember: "{}"'.format(self.name))

    def tell(self):
        print('Name: "{}", age: "{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{}"'.format(self.salary))

class Student(SchoolMember):
    """docstring for Student."""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{}"'.format(self.marks))

a = Student("Joksi",22,120)
b = Teacher("Puki",22,700)

members=[a,b]

for member in members:
    member.tell()
