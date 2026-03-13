class Person( object ):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

class Employee( Person ):
    def __init__(self, name, idnumber, post, salary):
        self.salary = salary
        self.post = post

        super().__init__(name,idnumber)

obj1 = Employee("Clark", 209877, 'Manager', 20000000)

obj1.display()